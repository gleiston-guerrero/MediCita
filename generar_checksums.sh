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
git ls-files -z -- . ':!:checksums.sha256' \
  | sort -z \
  | xargs -0 sha256sum > checksums.sha256

printf '%s\n' 'checksums.sha256 generado correctamente.'
printf '%s\n' 'Verificación: sha256sum --check checksums.sha256'
