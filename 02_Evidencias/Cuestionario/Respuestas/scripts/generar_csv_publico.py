#!/usr/bin/env python3
"""Genera el CSV público del cuestionario a partir del crudo restringido.

Por qué existe este script (G1, plan de mejora de datos, 19/09/2026):
el CSV que antes vivía en este repositorio público
(`Resultado_Cuestionario_IR_SGICM.csv`) traía la edad exacta y el
servicio usado (incluida psicología) de 66 personas — eso identifica a
encuestados individuales al cruzarlo con la edad. El dato crudo con la
edad exacta salió del repositorio público y ahora vive únicamente en el
contenedor restringido cifrado del equipo
(`02_Evidencias/00_Restringido/Resultado_Cuestionario_IR_SGICM_restringido.7z`).

Este script NO edita el crudo. Lee el crudo restringido (ruta fuera del
repo, indicada por --crudo o por la variable de entorno
CUESTIONARIO_CRUDO_PATH) y escribe el CSV público con:
  - Edad -> rango de edad (14-17, 18-24, 25-34, 35-44, 45+).
  - Servicio usado -> agrupado en solo dos categorías ("Medicina
    General" / "Otro servicio o combinación"), porque al cruzar el
    rango de edad con el detalle del servicio original quedaban
    combinaciones de una sola persona (p. ej. 45+ x Odontología). El
    criterio del plan es explícito: "si el rango de edad junto con el
    servicio deja grupos de una sola persona, agrupen también esos
    servicios" — por eso el servicio se agrupa, no solo la edad.
  - El resto de columnas se copia sin cambios.

Antes de escribir, el script verifica que ninguna combinación
(rango_edad, servicio_agrupado) tenga un solo caso; si la encontrara,
se detiene en vez de publicar un CSV que no cumple el criterio (por
ejemplo, si se agregan nuevas respuestas más adelante).

Uso (desde la raíz del repositorio):
    python 02_Evidencias/Cuestionario/Respuestas/scripts/generar_csv_publico.py \
        --crudo /ruta/al/crudo/restringido/Resultado_Cuestionario_IR_SGICM_crudo.csv

o exportando la variable de entorno:
    export CUESTIONARIO_CRUDO_PATH=/ruta/al/crudo/restringido/...csv
    python 02_Evidencias/Cuestionario/Respuestas/scripts/generar_csv_publico.py
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SALIDA = ROOT / "02_Evidencias" / "Cuestionario" / "Respuestas" / "Resultado_Cuestionario_IR_SGICM.csv"

COLUMNA_EDAD = "Edad"
# Nombre exacto de la columna de servicio en el crudo (con los espacios
# dobles que trae la exportación original de Google Forms/Excel):
COLUMNA_SERVICIO = "  ¿Qué servicio utiliza con mayor frecuencia?  "


def parse_edad(valor: str) -> int:
    """Extrae el número de edad aunque venga con texto (p. ej. '19 años')."""
    m = re.search(r"\d+", valor)
    if not m:
        raise ValueError(f"No se pudo interpretar la edad: {valor!r}")
    return int(m.group())


def rango_edad(edad: int) -> str:
    if edad <= 17:
        return "14-17"
    if edad <= 24:
        return "18-24"
    if edad <= 34:
        return "25-34"
    if edad <= 44:
        return "35-44"
    return "45+"


def servicio_agrupado(valor: str) -> str:
    return "Medicina General" if valor.strip() == "Medicina General" else "Otro servicio o combinación"


def generar(crudo_path: Path) -> None:
    with crudo_path.open(encoding="utf-8") as f:
        lector = csv.DictReader(f, delimiter=";")
        filas = list(lector)
        columnas = list(lector.fieldnames or [])

    if COLUMNA_EDAD not in columnas:
        raise SystemExit(f"La columna {COLUMNA_EDAD!r} no está en el crudo.")
    if COLUMNA_SERVICIO not in columnas:
        raise SystemExit(f"La columna {COLUMNA_SERVICIO!r} no está en el crudo.")

    filas_publicas = []
    cruce: Counter[tuple[str, str]] = Counter()
    for fila in filas:
        edad = parse_edad(fila[COLUMNA_EDAD])
        rango = rango_edad(edad)
        servicio = servicio_agrupado(fila[COLUMNA_SERVICIO])
        cruce[(rango, servicio)] += 1

        fila_publica = dict(fila)
        fila_publica[COLUMNA_EDAD] = rango
        fila_publica[COLUMNA_SERVICIO] = servicio
        filas_publicas.append(fila_publica)

    singulares = [combinacion for combinacion, n in cruce.items() if n == 1]
    if singulares:
        raise SystemExit(
            "No se publica: quedan combinaciones (rango_edad, servicio) de una "
            f"sola persona: {singulares}. Agrupe más las categorías de servicio "
            "antes de volver a correr este script."
        )

    with SALIDA.open("w", encoding="utf-8", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=columnas, delimiter=";")
        escritor.writeheader()
        escritor.writerows(filas_publicas)

    print(f"CSV público regenerado: {SALIDA.relative_to(ROOT)} ({len(filas_publicas)} filas).")
    print("Distribución rango_edad x servicio (todas las celdas >= 2):")
    for combinacion in sorted(cruce):
        print(f"  {combinacion}: {cruce[combinacion]}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--crudo",
        type=Path,
        default=Path(os.environ.get("CUESTIONARIO_CRUDO_PATH", "")),
        help=(
            "Ruta al CSV crudo (con edad exacta) fuera del repositorio, "
            "extraído del contenedor restringido cifrado. También se puede "
            "definir con la variable de entorno CUESTIONARIO_CRUDO_PATH."
        ),
    )
    args = parser.parse_args()

    if not args.crudo or not str(args.crudo):
        sys.exit(
            "Falta la ruta del crudo restringido: use --crudo <ruta> o la "
            "variable de entorno CUESTIONARIO_CRUDO_PATH. El crudo con la edad "
            "exacta NO vive en este repositorio (ver 07_Datos/registro_correcciones.md)."
        )
    if not args.crudo.exists():
        sys.exit(f"No existe el archivo crudo indicado: {args.crudo}")

    generar(args.crudo)


if __name__ == "__main__":
    main()
