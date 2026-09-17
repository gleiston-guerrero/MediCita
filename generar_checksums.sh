#!/usr/bin/env sh
set -eu

# Ejecutar desde la raíz del repositorio, con el working tree limpio
# (git status sin cambios pendientes) y con core.autocrlf=false.
#
# Usa "git ls-files" en vez de "find ." para que el manifiesto cubra
# EXACTAMENTE lo que Git rastrea -- ni un archivo más, ni uno menos --
# sin importar qué basura local haya en el disco de quien lo genera
# (cachés de Python __pycache__/*.pyc, entornos virtuales, archivos de
# build, etc.). Así el manifiesto es igual sin importar la máquina o el
# sistema operativo desde el que se genere.
#
# Excepción deliberada: las dos figuras PNG que genera
# 06_Experimento/scripts_analisis/generar_resultados.py
# (07_Publicacion/figuras/estado_tareas_validacion.png y
# cobertura_rf_must.png) se excluyen del manifiesto. Son renders de
# matplotlib a partir de los mismos datos ya verificados en
# resultados_estadisticos.json y power_calculation.csv (esos sí están en
# el manifiesto y sí son reproducibles byte a byte); el PNG en sí no lo es
# entre versiones/entornos de matplotlib distintos, aunque los datos que
# grafica no cambien. Verificado el 17/09/2026: al regenerar con la orden
# única (python 07_Datos/scripts/run_all.py) desde una copia limpia y
# correr después sha256sum -c checksums.sha256 --quiet, estas dos figuras
# quedaban FAILED de forma reproducible mientras el resto del manifiesto
# coincidía. Se excluyen para que el manifiesto no prometa una garantía
# bit a bit que el pipeline no puede cumplir de forma estable.
git ls-files -z -- . \
    ':!:checksums.sha256' \
    ':!:07_Publicacion/figuras/estado_tareas_validacion.png' \
    ':!:07_Publicacion/figuras/cobertura_rf_must.png' \
  | sort -z \
  | xargs -0 sha256sum > checksums.sha256

printf '%s\n' 'checksums.sha256 generado correctamente.'
printf '%s\n' 'Verificación: sha256sum --check checksums.sha256'
