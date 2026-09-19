"""
07_Datos/scripts/calcular_metricas_prerregistradas.py

Calcula las métricas que el prerregistro OSF (10.17605/OSF.IO/DTYNC) declaró
para RQ1/RQ2: tasa de finalización de tareas global, por sesión y por
requisito relacionado. Se agrega como paso propio de run_all.py — no
reemplaza a generar_resultados.py (que calcula el chi-cuadrado/permutación,
ahora marcado como exploratorio, ver Readme.md).

Uso: python calcular_metricas_prerregistradas.py
Lee:   07_Datos/datos_procesados/observaciones_validacion_procesadas.csv
Escribe: 07_Datos/resultados/metricas_prerregistradas.json
"""
from __future__ import annotations
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "07_Datos" / "datos_procesados" / "observaciones_validacion_procesadas.csv"
DST = ROOT / "07_Datos" / "resultados" / "metricas_prerregistradas.json"

ESTADOS_COMPLETADO = {"COMPLETADA", "COMPLETADA_CON_OBSERVACION"}


def tasa(counter: Counter) -> float | None:
    total = sum(counter.values())
    if not total:
        return None
    completadas = sum(counter[e] for e in ESTADOS_COMPLETADO if e in counter)
    return round(100 * completadas / total, 1)


def main() -> None:
    with SRC.open(encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f, delimiter=";"))

    estado_global = Counter(r["estado_tarea"] for r in rows)
    total = sum(estado_global.values())
    completadas = sum(estado_global[e] for e in ESTADOS_COMPLETADO if e in estado_global)

    por_sesion: dict[str, Counter] = defaultdict(Counter)
    por_requisito: dict[str, Counter] = defaultdict(Counter)
    for r in rows:
        por_sesion[r["codigo_sesion"]][r["estado_tarea"]] += 1
        for req in (x.strip() for x in r["requisito_relacionado"].split(";")):
            if req:
                por_requisito[req][r["estado_tarea"]] += 1

    result = {
        "metrica_prerregistrada": (
            "Tasa de finalizacion de tareas (global, por sesion, por requisito) "
            "- RQ1/RQ2 del prerregistro OSF DTYNC"
        ),
        "tasa_global": {
            "completadas": completadas,
            "total": total,
            "porcentaje": round(100 * completadas / total, 1) if total else None,
        },
        "por_sesion": {
            s: {
                "completadas": sum(c[e] for e in ESTADOS_COMPLETADO if e in c),
                "total": sum(c.values()),
                "porcentaje": tasa(c),
                "detalle": dict(c),
            }
            for s, c in sorted(por_sesion.items())
        },
        "por_requisito": {
            r: {
                "menciones": sum(c.values()),
                "porcentaje_completado": tasa(c),
                "detalle": dict(c),
            }
            for r, c in sorted(por_requisito.items())
        },
        "nota": (
            "El chi-cuadrado y la prueba de permutacion (ver resultados_estadisticos.json) "
            "no formaban parte del analisis prerregistrado en OSF y se presentan aparte, "
            "como exploratorios, no como resultado principal de RQ1/RQ2."
        ),
    }
    DST.parent.mkdir(parents=True, exist_ok=True)
    DST.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["tasa_global"], ensure_ascii=False))


if __name__ == "__main__":
    main()
