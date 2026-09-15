#!/usr/bin/env python3
"""Orquestador único de 07_Datos/.

Este script NO reimplementa el análisis: ejecuta el pipeline real que ya
existe en 06_Experimento/scripts_analisis/run_all.py. Ese pipeline lee y
escribe directamente sobre 07_Datos/datos_procesados/ y
07_Datos/resultados/ (ver las constantes DATA y RESULTS al inicio de
run_all.py) — no hay ninguna copia intermedia que sincronizar desde
06_Experimento/.

Qué hace este script, en orden:
  1. Verifica que los archivos crudos (el punto de partida fijo del
     estudio) estén presentes en 07_Datos/datos_crudos/.
  2. Verifica que los resultados estáticos de resultados/ que se
     documentan a mano y no se recalculan (como power_calculation_
     justificacion.md) estén presentes.
  3. Ejecuta el pipeline real (run_all.py), que ahora arranca desde
     datos_crudos/ficha_observacion.csv, regenera
     observaciones_validacion_procesadas.csv y
     observacion_requisito_long.csv (antes eran estáticos, ver
     generar_procesados.py), y sobrescribe en su propio destino final
     (07_Datos/) los demás archivos que calcula: resumen_descriptivo.csv,
     cobertura_RF_Must_final.csv, resultados_estadisticos.json y
     power_calculation.csv.
  4. Verifica que todo lo esperado haya quedado en su lugar.

Si algún archivo falta, el script se detiene con un mensaje claro en
lugar de fallar a mitad de camino con un traceback de Python.

Uso (desde la raíz del repositorio):
    python 07_Datos/scripts/generar_paquete_datos.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PIPELINE_REAL = ROOT / "06_Experimento" / "scripts_analisis" / "run_all.py"

DATOS_CRUDOS = ROOT / "07_Datos" / "datos_crudos"
DATOS_PROCESADOS = ROOT / "07_Datos" / "datos_procesados"
RESULTADOS = ROOT / "07_Datos" / "resultados"

# Crudos: punto de partida fijo del estudio, versionado directamente en
# su destino final. El pipeline los LEE desde aquí; nunca se copian ni
# se regeneran.
ARCHIVOS_CRUDOS_ESPERADOS = [
    "ficha_observacion.csv",
    "manifest_transcripciones_validacion.csv",
]

# Procesado que run_all.py sí escribe (línea `DATA / "resumen_descriptivo.csv"`):
PROCESADOS_GENERADOS_POR_PIPELINE = [
    "resumen_descriptivo.csv",
    "observaciones_validacion_procesadas.csv",
    "observacion_requisito_long.csv",
]

# Resultados que run_all.py sí calcula y escribe en RESULTS:
RESULTADOS_GENERADOS_POR_PIPELINE = [
    "cobertura_RF_Must_final.csv",
    "resultados_estadisticos.json",
    "power_calculation.csv",
]

# Resultados estáticos: verificación técnica y documentación de
# respaldo que no se recalculan en cada corrida (verificar_rf_must.js
# se ejecuta y se documenta aparte; power_calculation_justificacion.md
# es texto redactado, no una salida de script):
RESULTADOS_ESTATICOS_ESPERADOS = [
    "run_all_output.json",
    "verificacion_tecnica_RF_Must.json",
    "trazabilidad_observacion_correccion.csv",
    "power_calculation_justificacion.md",
]


def _verificar(carpeta: Path, nombres: list[str], etiqueta: str) -> None:
    faltantes = [nombre for nombre in nombres if not (carpeta / nombre).exists()]
    if faltantes:
        raise SystemExit(
            f"Faltan archivos {etiqueta} en {carpeta.relative_to(ROOT)}: "
            f"{', '.join(faltantes)}."
        )
    for nombre in nombres:
        print(f"  {etiqueta}: {nombre}")


def ejecutar_pipeline_real() -> None:
    print(f"Ejecutando pipeline real: {PIPELINE_REAL.relative_to(ROOT)}")
    resultado = subprocess.run([sys.executable, str(PIPELINE_REAL)], cwd=ROOT)
    if resultado.returncode != 0:
        raise SystemExit(
            "El pipeline real (06_Experimento/scripts_analisis/run_all.py) "
            "falló. Corríjalo antes de regenerar 07_Datos/."
        )


def main() -> None:
    print("Verificando entradas fijas...")
    _verificar(DATOS_CRUDOS, ARCHIVOS_CRUDOS_ESPERADOS, "crudo")
    _verificar(RESULTADOS, RESULTADOS_ESTATICOS_ESPERADOS, "resultado estático")

    ejecutar_pipeline_real()

    print("Verificando salidas del pipeline...")
    _verificar(DATOS_PROCESADOS, PROCESADOS_GENERADOS_POR_PIPELINE, "procesado generado")
    _verificar(RESULTADOS, RESULTADOS_GENERADOS_POR_PIPELINE, "resultado generado")

    print("\n07_Datos/ verificado y regenerado correctamente en su destino final.")


if __name__ == "__main__":
    main()
