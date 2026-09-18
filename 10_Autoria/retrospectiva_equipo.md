<div align="center">

# 🔁 retrospectiva_equipo.md — Cierre del Examen Suspenso

### Proyecto MediCita (SICM) — ISR-401



![Estado](https://img.shields.io/badge/Estado-Completo-success?style=for-the-badge)




![Fuente](https://img.shields.io/badge/Fuente-git_log_%2B_commits_reales-informational?style=for-the-badge)




![Actualizado](https://img.shields.io/badge/Actualizado-17/09/2026-blue?style=for-the-badge)



</div>

---

## 📌 Sobre este documento

Cubre el trabajo realizado desde el lunes 2026-09-14 hasta el cierre del
examen suspenso, en respuesta directa a la Guía de cierre y rúbrica del
examen suspenso, con línea base vigente en la etiqueta anotada
`cierre-examen-suspenso-20260917g` (ver la sección final de este documento). El detalle por integrante se
construyó cruzando el historial real de commits (`git log`) con los
cambios efectivamente aplicados al repositorio.

---

## 👥 Qué hicimos, por integrante

| Integrante | Usuario | Qué hizo |
|---|---|---|
| **Mayummy Jailly Trujillo Vega** | `mtrujillov-sys` | Reforzó la descripción del método de la V de Cramér en los resultados y en el JSON de salida; documentó el proceso de anonimización en el README; actualizó los enlaces del repositorio tras el cambio de cuenta de GitHub; actualizó la bitácora de sesiones y las estadísticas de participación. |
| **Steven Santiago Díaz Pontón** | `DIAZ PONTON STEVEN` | Creó el README de `fuentes_editables/`; aclaró la visibilidad de los integrantes del equipo en las fotografías de evaluación; corrigió enlaces del repositorio en `CHANGELOG.md` y en varios README. |
| **Thais Melanie Herrera Ramos** | `Melanie-G23` | Revisó la entrada A3 del README con detalles de fuente actualizados; implementó `detectar_rostros.py` y la sección de verificación objetiva por detección de rostros sobre las fotos del equipo; agregó el intervalo de confianza a `resumen_descriptivo.csv`. |
| **Jamileth Estefanía Gamarra Zárate** | `Jami1405` | Depositó las 10 notas de campo manuscritas escaneadas de las sesiones de validación por walkthrough (`V01` a `V10`, 2026-08-28/30) en `10_Autoria/notas_campo/`; actualizó `checksums_datos.sha256`; retiró la versión obsoleta del ERS (`ERS_SRS_2A_v1.0.pdf`). |
| **Paul Alexander Tigasis Sampedro** (líder de equipo) | `ptigasis-Alexander` | Corrigió las rutas del manifiesto `checksums_datos.sha256`; actualizó los enlaces de la demo y del prototipo público en el README; coordinó el cierre de los pendientes de la guía del examen suspenso: reproducibilidad del paquete de datos (§12). |
| **Jamileth Estefanía Gamarra Zárate** (edición adicional) | `Jami1405` | Además de lo indicado arriba: editó y actualizó esta retrospectiva (creada originalmente por Steven Díaz Pontón). |

---

## 🛠️ Qué corregimos puntualmente en el cierre

**Reproducibilidad del paquete de datos (§12).** `resumen_descriptivo.csv` había sido reformateado a mano (de punto y coma con BOM, la salida real del script, a comas sin BOM) el 2026-09-15 a las 00:21, lo que rompía la verificación `sha256sum -c checksums_datos.sha256 --quiet` aunque los valores numéricos fueran correctos. Se regeneró el archivo ejecutando la orden única (`python 07_Datos/scripts/run_all.py`) y se actualizó el manifiesto para que coincida con la salida real del pipeline.

**Cobertura de RF Must y cálculo de potencia (§16).** Se incorporó al manuscrito el cálculo de potencia a priori (Cohen's *d* = 0,5, α = 0,05, potencia = 0,80, *n* = 128) como referencia de diseño frente a las diez sesiones de validación disponibles, y se reforzó la sección de amenazas a la validez con esa comparación explícita. El párrafo del cálculo de potencia a priori (Cohen's *d* = 0,5, α = 0,05, potencia = 0,80, *n* = 128) fue redactado por Mayummy Jailly Trujillo Vega y ubicado en la sección de Metodología del manuscrito, no en Resultados. El manuscrito se recompiló desde el `.tex` versionado.

**Consistencia de la línea base y evidencia de fecha (§2, §3, §15) — última ronda.** El README, el CHANGELOG y esta misma retrospectiva declaraban etiquetas de cierre distintas entre sí en momentos distintos del día; se sincronizaron los tres para declarar `cierre-examen-suspenso-20260917d` como línea base vigente. En `10_Autoria/exif_inventario.csv`, las notas sobre `2026-07-17_recepcion.png` y `2026-07-17_enfermeria.png` afirmaban que eran una revisita fotográfica posterior a las entrevistas P07/P06, sin citar de dónde salía esa fecha; se agregó la referencia explícita a la nota de campo manuscrita de cada sesión (escrita el mismo día) como la evidencia que confirma el 07/07/2026. Se recontaron los commits por última vez (`git shortlog -sne HEAD` sobre clon completo, `.mailmap` aplicado): 1.804 commits totales, en `10_Autoria/aporte_individual.md` y `10_Autoria/Readme.md`. `checksums.sha256` se regeneró después de cada uno de estos cambios, como último paso.

---

## 💡 Qué aprendimos

- Un archivo puede tener el valor correcto y aun así fallar la verificación de integridad: reformatear a mano una salida generada por script (aunque sea solo el separador o la codificación) rompe la reproducibilidad byte a byte que el propio repositorio declara. La lección para el resto del proyecto es no tocar a mano ningún archivo bajo `resultados/` o `datos_procesados/`: si el formato necesita cambiar, el cambio va en el script generador, no en la salida.
- Reportar un resultado (como la cobertura de RF Must) no basta si el cálculo que lo acompaña —en este caso, la potencia estadística— se queda solo en el archivo de datos y no llega al manuscrito: el evaluador lee el informe, no el JSON.
- Cerrar entregables de a uno, verificando con el comando exacto de la guía antes de pasar al siguiente, evitó reabrir trabajo ya dado por terminado.
- Verificar en la propia máquina de desarrollo no basta cuando la evaluación se hace en otro sistema operativo: una ruta con `\` en vez de `/` es invisible al ojo pero rompe un hash. La lección es regenerar el manifiesto raíz como el último paso, después de cualquier otro cambio de contenido — no antes.
- Declarar la etiqueta de línea base "vigente" en tres archivos distintos (README, CHANGELOG y esta retrospectiva) hizo que, dos veces seguidas, se corrigiera uno y se olvidaran los otros dos al crear la siguiente etiqueta. La lección es la misma que con los archivos de `resultados/`: la etiqueta debe ser siempre el último paso, después de confirmar que los tres documentos ya dicen lo mismo — no algo que se cree primero y se documente después.

---

## Correcciones finales — 2026-09-15 (noche)

Después del primer cierre bajo `vFinal`, se detectó que `checksums_datos.sha256`
no coincidía con la salida real de `resumen_descriptivo.csv`. Se corrigió el
formato de varios CSV, se regeneró `resumen_descriptivo.csv` y sus derivados
desde el pipeline real (`07_Datos/scripts/run_all.py`), se corrigieron rutas
no compatibles entre sistemas operativos en `resultados_estadisticos.json`
(el script guardaba las rutas de origen con `str(Path(...))`, que produce `\`
en Windows y `/` en Linux; se corrigió con `.as_posix()`, estable en cualquier
sistema operativo), y se recompiló `07_Publicacion/manuscrito_final.pdf` para
que su commit quedara posterior a esta última regeneración de resultados.

Se actualizó también la etiqueta de línea base declarada en el README para
que apunte al commit final real de este segundo cierre (`cierre-examen-suspenso-20260915`),
dejando `vFinal` como referencia histórica del primer intento. Se corrigió
`generar_checksums.sh`, que solo cubría imágenes, video, audio, PDF y `.7z`
y dejaba fuera del manifiesto raíz cerca de 290 archivos de código y datos
(`.py`, `.md`, `.csv`, `.drawio`, `.tex`, entre otros) presentes en
`checksums.sha256`. Se corrigieron además dos datos desactualizados en el
README (páginas del ERS y número de consentimientos pixelados).

## Fe de erratas post-etiqueta y nueva línea base — 2026-09-17 (`[4.3.7]`)

Tras crear la etiqueta `cierre-examen-suspenso-20260917d`, se detectaron dos afirmaciones
falsas hechas en la ronda anterior (`[4.3.6]`): el recuento de "1.804 commits, recuento final"
ya estaba desactualizado en 8 commits para el momento del propio tag (el recuento correcto sobre
el commit real del tag, `a0fcc55`, es 1.812), y la exclusión de las dos figuras no reproducibles
de matplotlib (`estado_tareas_validacion.png`, `cobertura_rf_must.png`) nunca llegó a aplicarse
realmente a `generar_checksums.sh`, pese a haberse documentado antes de crear el tag. Se
corrigieron ambos datos en `10_Autoria/aporte_individual.md`, `10_Autoria/Readme.md` y
`generar_checksums.sh`/`checksums.sha256`. Como este archivo (§16), el CHANGELOG (§2) y el
README deben declarar la misma etiqueta que el commit vigente (§3), y ese commit avanzó un paso
más allá de `cierre-examen-suspenso-20260917d`, se planeó crear una nueva etiqueta anotada,
`cierre-examen-suspenso-20260917e`, sobre este commit de fe de erratas. **Corrección (agregada
al cerrar `[4.3.8]`):** esa etiqueta se documentó como creada pero nunca se ejecutó el
`git push origin cierre-examen-suspenso-20260917e` — verificado con `git ls-remote --tags`
directo contra el repositorio remoto, no existe. La línea base pasó de `d` directamente a `f`
(ver la sección siguiente), sin `e` intermedia.

## Reproducibilidad real de los resultados y nueva línea base — 2026-09-17 (`[4.3.8]`)

`resultados_estadisticos.json` fallaba de forma reproducible en `sha256sum -c
checksums_datos.sha256 --quiet` al regenerarse en Linux, porque se escribía sin fijar el
separador de línea y el archivo depositado se había generado en Windows. Se corrigió
`generar_resultados.py` para fijar `newline="\n"` explícitamente y se protegió el archivo en
`.gitattributes`, igual que ya se hacía con los `.csv` de `07_Datos/`. Verificado corriendo la
orden única dos veces seguidas desde una copia limpia: ambas veces el manifiesto de `07_Datos/`
queda en silencio total. También se revisaron las 14 imágenes del repositorio que no están en
`exif_inventario.csv` (documentado en el CHANGELOG `[4.3.8]`): 5 son artefactos derivados o
ejemplos ilustrativos, correctamente fuera; 9 son consentimientos pixelados de la validación por
walkthrough, evidencia real que queda fuera solo por el alcance que el propio equipo declaró —
no se agregaron al inventario en esta ronda para no introducir EXIF sin verificar, pero queda
documentado como pendiente abierto, no como omisión silenciosa. Se creó la etiqueta anotada
`cierre-examen-suspenso-20260917f` sobre este commit y se actualizó el README para declararla
como línea base vigente.

## Corrección de la etiqueta `e` falsa y nueva línea base — 2026-09-17 (`[4.3.9]`)

Después de crear `cierre-examen-suspenso-20260917f`, se detectó (verificando con `git ls-remote
--tags` directo contra el repositorio remoto) que `cierre-examen-suspenso-20260917e` —que este
mismo README, el CHANGELOG y este documento citaban como creada y preservada de referencia
histórica— **nunca se publicó**. El `git push origin cierre-examen-suspenso-20260917e` planeado
en `[4.3.7]` no se ejecutó, o se ejecutó solo en un repositorio local sin llegar al remoto. Se
corrigieron los tres documentos para retirar esa afirmación falsa. Esta corrección en sí misma
avanzó el commit vigente 2 pasos más allá de `cierre-examen-suspenso-20260917f`, dejando a esa
etiqueta apuntando a un commit ya superado — el mismo defecto de etiqueta desincronizada
señalado y corregido varias veces antes (`[4.3.1]`–`[4.3.7]`). Por eso se crea una nueva etiqueta
anotada, `cierre-examen-suspenso-20260917g`, sobre el commit de esta entrada, que reemplaza a
`cierre-examen-suspenso-20260917f` como línea base vigente. `cierre-examen-suspenso-20260917f` se
conserva sin modificar como referencia histórica.
