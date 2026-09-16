#!/usr/bin/env sh
set -eu

# Ejecutar desde la raíz del repositorio después de descargar todos los archivos.
# Cubre TODO el árbol versionado (código, datos, documentación y binarios),
# igual que el manifiesto checksums.sha256 realmente commiteado.
find . -type f \
  ! -path './.git/*' \
  ! -name 'checksums.sha256' \
  -print0 | sort -z | xargs -0 sha256sum > checksums.sha256

printf '%s\n' 'checksums.sha256 generado correctamente.'
printf '%s\n' 'Verificación: sha256sum --check checksums.sha256'
