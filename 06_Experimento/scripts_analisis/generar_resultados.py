#!/usr/bin/env python3
"""Etapa 3 de 3 — Generación de resultados finales.

Recibe los valores ya calculados por procesar_datos.py y escribe todos los
artefactos publicables: el JSON de resultados estadísticos, los CSV de
resumen y potencia, y las dos figuras PNG del walkthrough y de RF Must.

No calcula nada nuevo — solo da formato y escribe a disco lo que ya viene
calculado.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "07_Datos" / "datos_procesados"
RESULTS = ROOT / "07_Datos" / "resultados"
FIGURES = ROOT / "07_Publicacion" / "figuras"
TABLES = ROOT / "07_Publicacion" / "tablas"
ZENODO = ROOT / "07_Publicacion" / "dataset_zenodo"


def write_csv(path: Path, rows: list[list[object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        csv.writer(stream, delimiter=";").writerows(rows)


def generar(procesado: dict[str, object]) -> dict[str, object]:
    """Escribe el JSON, los CSV y las figuras a partir de lo ya calculado.

    Devuelve el diccionario de resultados que se escribió en
    resultados_estadisticos.json, por si quien orquesta quiere imprimirlo
    o inspeccionarlo.
    """
    observations = procesado["observations"]
    relations = procesado["relations"]
    states = procesado["states"]
    p_value = procesado["p_value"]
    cramer_v = procesado["cramer_v"]
    passed = procesado["passed"]
    total = procesado["total"]
    coverage_percent = procesado["coverage_percent"]
    power_n = procesado["power_n"]

    result = {
        "fuente_observaciones": (DATA / "observaciones_validacion_procesadas.csv").relative_to(ROOT).as_posix(),
        "fuente_relaciones": (DATA / "observacion_requisito_long.csv").relative_to(ROOT).as_posix(),
        "observaciones": len(observations),
        "relaciones_observacion_requisito": len(relations),
        "estados_observacion": dict(states),
        "grupos_tabla_3x2": procesado["group_order"],
        "tabla_sin_hallazgo_con_hallazgo": procesado["contingency"],
        "chi_cuadrado": round(procesado["statistic"], 6),
        "frecuencia_esperada_minima": round(procesado["expected_min"], 6),
        "replicas_monte_carlo": 100_000,
        "semilla": 42,
        "p_permutacion": round(p_value, 6),
        "v_cramer": round(cramer_v, 6),
        "v_cramer_ic95_inferior": round(procesado["cramer_v_ic_inf"], 6),
        "v_cramer_ic95_superior": round(procesado["cramer_v_ic_sup"], 6),
        "v_cramer_ic95_metodo": "bootstrap no paramétrico, 10000 réplicas, semilla 42, percentiles 2.5/97.5. Nota: V de Cramér está acotada en [0,1] y este intervalo nunca incluye el cero por construcción; no se usa para inferir significancia, solo describe la precisión de la estimación. La prueba de significancia es la de permutación (p_permutacion).",
        "rf_must_aprobados": passed,
        "rf_must_total": total,
        "cobertura_rf_must_porcentaje": round(coverage_percent, 2),
        "power_calculation": {
            "prueba": "t bilateral de dos muestras independientes, grupos iguales",
            "cohen_d": 0.5,
            "alpha": 0.05,
            "potencia": 0.80,
            "n_requerido_por_grupo": power_n,
            "n_total_requerido": 2 * power_n,
            "nota": "Cálculo de referencia; no convierte las sesiones disponibles en una muestra suficiente.",
        },
    }
    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "resultados_estadisticos.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    summary_rows = [
        ["metrica", "valor"],
        ["sesiones_validacion_con_transcripcion", len({row["codigo_sesion"] for row in observations})],
        ["observaciones_totales", len(observations)],
        ["completada_con_observacion", states["COMPLETADA_CON_OBSERVACION"]],
        ["no_completada", states["NO_COMPLETADA"]],
        ["completada", states["COMPLETADA"]],
        ["relaciones_observacion_requisito", len(relations)],
        ["p_permutacion_monte_carlo", f"{p_value:.6f}"],
        ["v_cramer", f"{cramer_v:.6f}"],
        ["v_cramer_ic95", f"[{procesado['cramer_v_ic_inf']:.6f}, {procesado['cramer_v_ic_sup']:.6f}]"],
        ["rf_must_verificacion_tecnica_aprobados", passed],
        ["rf_must_total", total],
        ["cobertura_rf_must_porcentaje", f"{coverage_percent:.2f}"],
    ]
    for destination in [DATA / "resumen_descriptivo.csv", ZENODO / "resumen_descriptivo.csv"]:
        write_csv(destination, summary_rows)

    write_csv(
        TABLES / "resumen_validacion.csv",
        [["estado", "conteo"], ["Completada", states["COMPLETADA"]],
         ["Completada con observación", states["COMPLETADA_CON_OBSERVACION"]],
         ["No completada", states["NO_COMPLETADA"]]],
    )
    write_csv(
        RESULTS / "power_calculation.csv",
        [["cohen_d", "alpha", "potencia", "n_por_grupo", "n_total"],
         ["0.5", "0.05", "0.80", power_n, 2 * power_n]],
    )

    FIGURES.mkdir(parents=True, exist_ok=True)
    labels = ["Completada", "Con observación", "No completada"]
    values = [states["COMPLETADA"], states["COMPLETADA_CON_OBSERVACION"], states["NO_COMPLETADA"]]
    plt.figure(figsize=(7.2, 4.2))
    bars = plt.bar(labels, values, color=["#2e7d32", "#f9a825", "#c62828"])
    plt.ylabel("Observaciones")
    plt.title("Estado de las tareas del walkthrough (N=46)")
    plt.bar_label(bars)
    plt.tight_layout()
    plt.savefig(FIGURES / "estado_tareas_validacion.png", dpi=200)
    plt.close()

    plt.figure(figsize=(6.4, 4.0))
    bars = plt.bar(["RF Must cubiertos", "RF Must no cubiertos"], [passed, total - passed],
                   color=["#1565c0", "#b0bec5"])
    plt.ylabel("Requisitos")
    plt.title(f"Cobertura técnica: {passed}/{total} ({coverage_percent:.2f} %)")
    plt.bar_label(bars)
    plt.tight_layout()
    plt.savefig(FIGURES / "cobertura_rf_must.png", dpi=200)
    plt.close()

    return result


if __name__ == "__main__":
    import leer_datos
    import procesar_datos

    datos = leer_datos.cargar_datos()
    procesado = procesar_datos.procesar(datos)
    resultado = generar(procesado)
    print(json.dumps(resultado, ensure_ascii=False, indent=2))
