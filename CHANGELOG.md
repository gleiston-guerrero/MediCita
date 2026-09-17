# Historial de cambios

Todos los cambios relevantes del proyecto se documentan en este archivo.
El formato se basa en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/)
y el proyecto utiliza [versionado semántico](https://semver.org/lang/es/).

## [4.3.2] - 2026-09-17 — Documenta correcciones de datos, manuscrito y retrospectiva omitidas en [4.3.0]/[4.3.1]

### Corregido
- `10_Autoria/exif_inventario.csv`: se agregaron/actualizaron filas del inventario EXIF (commits `8e99d71`, `a47b450`) — *Jamileth Gamarra Zárate*, *Mayummy Trujillo Vega*.
- `07_Publicacion/manuscrito_final.tex`: cálculo de potencia movido a Metodología y tabla de cobertura RF Must incorporada (commit `7e25c92`) — *Paul Tigasi Sampedro*.
- `10_Autoria/retrospectiva_equipo.md`: revisión de fecha y detalle de aportes (commits `51ee739`, `9fb9957`) — *Jamileth Gamarra Zárate*.
- `10_Autoria/notas_campo/notas_campo.md` y `10_Autoria/correspondencia/evidencia_entrevista/Readme.md`: aclaraciones adicionales (commits `6ad4abe`, `efe60d0`) — *Paul Tigasi Sampedro*.

## [4.3.1] - 2026-09-17 — Declara línea base vigente y corrige V09/manifiesto de datos

Segundo ajuste el mismo día, tras una segunda verificación estricta post-`[4.3.0]`.

### Corregido
- `10_Autoria/notas_campo/notas_campo.md`: la fila V09 — Psicología atribuía
  la nota a Paul Tigasi Sampedro; el escaneo tiene el campo de responsable
  vacío y `bitacora_sesiones.csv` declara "no consta" — corregido a
  "No consta" para eliminar la contradicción.
- `07_Datos/checksums_datos.sha256`: quedó desactualizado tras corregir el
  docstring de `run_all.py`; regenerado (23 entradas, verificado limpio).
- `07_Datos/scripts/run_all.py`: `cobertura_RF_Must_final.csv` seguía
  listado en `RESULTADOS_GENERADOS_POR_PIPELINE`, contradiciendo su propio
  docstring; movido a `RESULTADOS_ESTATICOS_ESPERADOS`.

### Línea base
Esta entrada se publica bajo la etiqueta anotada de cierre
`cierre-examen-suspenso-20260917`, que reemplaza a
`cierre-examen-suspenso-20260916` como línea base vigente.


## [4.3.0] - 2026-09-17 — Corrección de atribuciones falsas señaladas en el informe del examen suspenso (5,68/10)

Responde al `Informe de evaluación del examen suspenso` del docente (17/09/2026,
00:40, nota 5,68/10 sobre `cierre-examen-suspenso-20260916`), que detectó
atribuciones incorrectas introducidas en `[4.2.0]` al intentar cerrar
`[4.1.0]`.

### Corregido

- §2 de `[4.2.0]` atribuía a *Steven Díaz Pontón* la subida de las notas de
  campo V01–V10 citando el commit `8e0f8165`. Verificado con
  `git show --stat 8e0f8165`: ese commit solo modifica `CHANGELOG.md`. Las
  10 notas V01–V10 las subió *Jamileth Gamarra Zárate* (usuario `Jami1405`)
  el 15/09/2026 entre las 14:53 y las 14:57, en 10 commits independientes
  (`6935a33` a `69f125e`); las 8 notas P01–P08 también las subió ella, el
  05/09/2026 entre las 20:22 y las 20:25, en 8 commits independientes.
- §2 de `[4.2.0]` atribuía a *Paul Tigasi Sampedro* la corrección de rutas
  del script de resultados citando el commit `3b3cace`. Verificado con
  `git show --stat 3b3cace`: ese commit solo modifica
  `resultados_estadisticos.json` y los manifiestos de checksums. La
  corrección real de `generar_resultados.py` es de *Jamileth Gamarra
  Zárate*, commit `0688bac`.
- Enlaces a etiquetas `v1.0.0`–`v4.0.0` al pie de este archivo, que no
  existen en el repositorio remoto, retirados.
- "34 fotografías reales" (README y este archivo) corregido a "34
  fotografías del expediente, de las cuales 5 son capturas de pantalla de
  Google Forms sin EXIF de cámara", para no implicar que las 34 son tomas
  de cámara.

## [4.2.0] - 2026-09-16 — Cierre final tras revisión del docente (7,12/10)

Publicado bajo la etiqueta anotada `cierre-examen-suspenso-20260916`, sobre
el último commit de esta serie de correcciones. Responde punto por punto al
`Informe de evaluación del examen suspenso` del docente (16/09/2026, 19:30,
nota 7,12/10 sobre la entrega `[4.1.0]`), que dejó §2, §3 y §15 en "Por
modificar". Reemplaza a `[4.1.0]` como línea base vigente; esa etiqueta y
`vFinal` se conservan como referencia histórica de los dos intentos de
cierre anteriores.

### Corregido (respuesta al informe del 16/09)

- §2 CHANGELOG: la entrada de `[4.1.0]` ya indicaba quién hizo cada cambio,
  ya no estaba bajo "[No publicado]" y `vFinal` ya tenía su propia entrada
  (`[4.0.1]`) — los tres puntos que el informe marcó como pendientes en esa
  revisión. — *Mayummy Trujillo Vega* (`a3478c9`).
- §3 Etiqueta de línea base: `evidencia-restringida-v1` se convirtió de
  etiqueta ligera a anotada, sobre el mismo commit (`b320145`), tal como
  pedía el informe. — *Paul Tigasi Sampedro* (recreación de la etiqueta,
  verificada con `git cat-file -t evidencia-restringida-v1` → `tag`).
- §15 Notas de campo: se agregó a `10_Autoria/notas_campo/notas_campo.md`
  la declaración por escrito de cuándo se redactó cada nota V01–V10 y dónde
  está el original en papel, incluyendo la aclaración específica sobre por
  qué el campo "duración" coincide con la grabación (se verificó ese dato
  puntual contra la grabación después de la sesión; el contenido de la nota
  se escribió a mano el mismo día). — *Jamileth Gamarra Zárate* (`74684b6`,
  `84ce5de`, `848582e`), aclaración final de *Paul Tigasi Sampedro*
  (`b180e5b`).
- §15 Inventario EXIF: se añadieron a `10_Autoria/exif_inventario.csv` las
  5 filas faltantes de `10_Autoria/correspondencia/evidencia_entrevista/`,
  completando 34 de 34 elementos fotográficos del expediente (29 fotografías de cámara y 5 capturas de pantalla de Google Forms).
  — *Jamileth Gamarra Zárate* (`a01b93f`).
- Recompilación del PDF de `01_ERS/ERS_SRS_2B_V2.0.pdf` con XeLaTeX+BibTeX
  (el depositado antes se había generado por error con pdfTeX, que no
  soporta el paquete `fontspec` que usa la fuente). — *Thais Herrera Ramos*
  (`dd0fad0`).
- Corrección de tres README desactualizados detectados en auditoría
  posterior al informe (no señalados explícitamente por el docente, pero
  inconsistentes con el resto del repositorio): `01_ERS/Readme.md` (117→120
  páginas, 19→21 RNF activos), `10_Autoria/Readme.md` (29→34 fotos en el
  inventario EXIF) y `04_Trazabilidad/Readme.md` (72→75 filas de la
  matriz). — *Mayummy Trujillo Vega* (`86f4148`), *Thais Herrera Ramos*
  (`da4febe`), *Paul Tigasi Sampedro* (`3ae8324`).
- Manifiesto raíz `checksums.sha256` regenerado con `generar_checksums.sh`
  para reflejar los 7 archivos corregidos en este cierre.

## [4.1.0] - 2026-09-16 — Cierre del examen suspenso (versión final)

Publicado bajo la etiqueta anotada `cierre-examen-suspenso-20260915`, sobre el
commit `d0a0195`. Reemplaza a `vFinal` (ver la entrada `[4.0.1]` más abajo):
agrega la corrección de reproducibilidad cross-OS (§12) y la recompilación
correcta del manuscrito final (§16) que `vFinal` todavía no tenía. `vFinal`
se conserva en el repositorio únicamente como referencia histórica del primer
intento de cierre, hecho el mismo día pero antes de completar esos dos puntos.

### Añadido

- 10 notas de campo manuscritas escaneadas de las sesiones de validación
  por walkthrough (`V01` a `V10`, 2026-08-28/30), depositadas en
  `10_Autoria/notas_campo/`. **Nota:** las 18 sesiones de campo (8 de
  elicitación + 10 de validación) están completas y ahora enlazadas
  1 a 1 desde `10_Autoria/bitacora_sesiones.csv` (columnas `tipo` y
  `ruta_nota_campo`, agregadas hoy), junto a las 28 filas de trabajo
  interno del equipo ya existentes — 46 filas en total.
  — *Steven Díaz Pontón* (`8e0f8165`), con aportes de *Jamileth Gamarra
  Zárate* (`1582c816`) y *Mayummy Trujillo Vega* (`83890702`).
- Cobertura técnica de RF Must (20 de 22, 90,91 %) incorporada como
  resultado explícito en el manuscrito (`07_Publicacion/manuscrito_final.tex`).
  — *Steven Díaz Pontón* (`8e0f8165`).
- Retrospectiva del equipo (`10_Autoria/retrospectiva_equipo.md`).
  — *Steven Díaz Pontón* (`8e0f8165`).

### Corregido

- Reproducibilidad byte a byte del paquete de datos: `resumen_descriptivo.csv`
  (en `07_Datos/datos_procesados/` y `07_Publicacion/dataset_zenodo/`) se
  regeneró con la orden única (`python 07_Datos/scripts/run_all.py`)
  para que coincida con la salida real del script; `checksums_datos.sha256`
  actualizado en consecuencia. `sha256sum -c checksums_datos.sha256 --quiet`
  ya no reporta discrepancias.
  — *Steven Díaz Pontón* (`8e0f8165`), con una corrección de *Jamileth
  Gamarra Zárate* (`1582c816`). La causa raíz (rutas con separador de
  Windows en `generar_resultados.py`) fue corregida por *Paul Tigasi
  Sampedro* en el commit `3b3cace` ("Fix reproducibilidad cross-OS: rutas
  POSIX en resultados_estadisticos.json"), posterior a esta entrada.

### Resuelto

- Requisito de "asignación o recomendación automática de cita" (Sección 5.2 de
  la Guía de Desarrollo): en vez de dejarlo solo como párrafo justificativo,
  se documenta como ficha formal de determinación de aplicabilidad (FDA-01),
  con el mismo nivel de detalle exigido a RNF-18 a RNF-22 (evidencia técnica,
  responsable, fecha). Fila 75 añadida a `matriz_trazabilidad_ACTUALIZADA.csv`
  y a su tabla equivalente en el ERS/SRS; conteo de filas actualizado de 74 a
  75 en el ERS y en el README; tabla de RNF del componente inteligente en el
  README actualizada para incluir FDA-01 junto a RNF-18 a RNF-22.
  — *Mayummy Trujillo Vega* (`14e04d59`).
- `10_Autoria/correspondencia/` (ítem A8): depositados los 4 documentos reales
  de correspondencia institucional (solicitud del 28/05/2026, aval
  institucional del 22/07/2026, aval del establecimiento del 20/08/2026 y
  oficio de respaldo del 04/09/2026), antes solo referenciados desde otras
  carpetas y ausentes del propio directorio de autoría.
- Evidencia fotográfica fechada de 5 de las 7 sesiones de la ronda de
  elicitación (Nutrición, Psicología, Coordinación/Odontología, Recepción,
  Enfermería), recuperada de los dispositivos del equipo y depositada en
  `10_Autoria/correspondencia/evidencia_entrevista/`, con el rostro de cada
  persona entrevistada pixelado y el del integrante del equipo visible.
- Desviación declarada explícitamente en `07_Datos/desviaciones.md`: la
  coordinación puntual de horario de cada sesión de campo se realizó de
  forma verbal/telefónica sin registro escrito; las 2 sesiones sin
  evidencia fotográfica recuperable (Fisioterapia, Medicina General) se
  declaran como pérdida por limpieza de espacio, sin reconstruirse.
- Corrección de rutas rotas en `07_Datos/desviaciones.md` (carpeta
  `evidencia_entrevistas` mal escrita, debía ser `evidencia_entrevista`; un
  nombre de archivo con letra faltante).
  — *(los 4 puntos anteriores)* *Thais Herrera Ramos* (`002808ff`).
- Fragmento roto de evidencia audiovisual (`VIDEOS_Validacion.7z.206`, 2 bytes)
  reparado y republicado en el Release `evidencia-restringida-v1` con su
  tamaño e integridad correctos.
- Nueva sección "Alcance del componente de IA y requisitos que no aplican" en
  el ERS/SRS: se deja constancia expresa de que RF-02 y RF-13 no son un
  componente de IA (son consultas deterministas), y que el requisito de
  "asignación/recomendación automática de cita" no aplica a este sistema.
- RNF-21 (supervisión humana) y RNF-22 (clasificación del nivel de riesgo)
  añadidos al ERS/SRS, con métrica, umbral, responsable y frecuencia
  definidos; catálogo de RNF activos actualizado de 19 a 21.
- RNF-19 (equidad) reescrito: estaba incorrectamente asociado a RF-02/RF-13;
  ahora se define sobre el único componente de IA real del sistema (RF-16).
- Corrección de un `\begin{quote}` sin cerrar en `ERS_SRS_2B_V2.0.tex` que
  impedía la recompilación limpia del documento (afectaba directamente la
  reproducibilidad documental).
- Matriz de trazabilidad (`matriz_trazabilidad_ACTUALIZADA.csv` y su tabla
  equivalente dentro del ERS): fila 71 corregida para reflejar RF-16 en vez
  de RF-02/RF-13; filas 73 y 74 añadidas para RNF-21 y RNF-22.
- Finalidad del tratamiento y plazo de conservación añadidos a
  `CategoriaA_A4_Referencia_LOPDP.pdf`, completando los cuatro elementos que
  exige el ítem de ética de la guía de cierre.
- Columna de duración por sesión añadida a `ficha_observacion.csv`, cruzada
  contra el inventario técnico ya verificado con hash SHA-256.
- Perfil agregado de los participantes de validación
  (`07_Datos/datos_procesados/perfil_agregado_participantes.csv`), con su
  sección correspondiente en `README_datos.md`.
- Doble observación independiente sobre el 25% de las sesiones de validación
  (VAL-MG, VAL-ENF): kappa de Cohen = -0,07 (sin acuerdo, por desbalance de
  categorías), documentado en `10_Autoria/doble_observacion_sesiones/` junto
  con las dos hojas de observación y el script de cálculo.
- Corrección de dos fragmentos de código incompletos en `05_MVP/script.js`
  (una función sin cerrar y una llamada `later()` sin cerrar) que impedían
  que la demostración interactiva del MVP respondiera al hacer clic.
- Guion de defensa, presentación PPTX y folleto de una hoja actualizados
  para reflejar los 21 RNF, los tres controles de confiabilidad (incluido el
  kappa de doble observación), y el reparto real de diapositivas (Paul
  9–12, Mayummy 13–18, con traspaso a Thais en la diapositiva 16).
- `checksums_datos.sha256` y `diccionario_datos.csv` regenerados para
  reflejar los archivos nuevos y modificados de `07_Datos/`.
- Declaración de uso de IA y aporte individual actualizados y refirmados
  por los 5 integrantes con fecha 12/09/2026.
- Script de análisis (`06_Experimento/scripts_analisis/run_all.py`) dividido
  en tres etapas independientes (`leer_datos.py`, `procesar_datos.py`,
  `generar_resultados.py`) más un orquestador, tal como exige el ítem A4;
  salida verificada como idéntica byte por byte a la versión anterior de un
  solo archivo.
- Doce archivos de 1 byte que anunciaban evidencia o documentación sin
  contenerla (`scripts_analisis_.md`, `prompts_LLm_.md`, y nueve `README.md`
  de subcarpetas de `03_Modelado/Diagramas_UML_Corregidos/` y
  `Mockups_Prototipo_Final/`) completados con su descripción real o
  eliminados, para eliminar el riesgo de cero directo por el criterio de
  piso P3.
  — *(los 12 puntos anteriores, desde "Fragmento roto de evidencia
  audiovisual" hasta este)* *Thais Herrera Ramos* (`48dd7e60`).
- Repositorio espejo (`MediCita_ISR401-archive`) archivado en Software
  Heritage; SWHID real (`swh:1:dir:6fbdc09760140cb9d176d33621b1262e1b9de2c2`)
  incorporado en `CITATION.cff` (09/09/2026).
  — *Mayummy Trujillo Vega* (`4d87c346`).

### Nota sobre firmas del expediente ético

`A13_Participantes_Externos_MediCita.pdf`, `Adenda_Segunda_Ronda.pdf` y
`Adenda_Validacion_Walkthrough_corregida.pdf` permanecen sin firma del
docente responsable por decisión explícita de este, comunicada al equipo:
sirven como constancia del proceso realizado, ya que los documentos
originales firmados se conservan en el comité de ética. No se trata de un
pendiente.
— *Mayummy Trujillo Vega* (`8541d631`).

### Atribución — cierre final (2026-09-15/16, posterior a esta entrada)

Los siguientes cambios se hicieron después del contenido anterior (que ya
estaba en `vFinal`) para llegar de `vFinal` a `cierre-examen-suspenso-20260915`:

- Corrección de reproducibilidad cross-OS en `generar_resultados.py` (rutas
  POSIX) y regeneración de `resumen_descriptivo.csv` y de
  `checksums_datos.sha256` — *Paul Tigasi Sampedro* (`3b3cace`, `2988519`,
  `81de1c0`, y las correcciones de formato previas en `d1a09e0`, `d039a2e`).
- Subida de archivos y regeneración del manifiesto raíz `checksums.sha256`
  tras las correcciones — *Jamileth Gamarra Zárate* (`a5fb14d`, `0688bac`,
  `529670d`, `12276e4`).
- Corrección del conteo de consentimientos y de páginas del ERS/SRS 2B en el
  README, y ajuste de la referencia de la etiqueta en este CHANGELOG —
  *Mayummy Trujillo Vega* (`908670b`, `0d694c1`, `f3769e1`).
- Subida de archivos del cierre (incluido el manuscrito final recompilado) —
  *Thais Herrera Ramos* (`bda5ccf`, `bd89422`, `87a0e1d`, `6c012fe`).
- Creación y corrección de la etiqueta anotada final, y subida de archivos de
  cierre — *Paul Tigasi Sampedro* (`d0a0195`).

## [4.0.1] - 2026-09-15 — vFinal (cierre incompleto, superado por 4.1.0)

Publicado bajo la etiqueta anotada `vFinal`, sobre el commit `8389070`.
Primer intento de cierre del examen suspenso: incluye todo el contenido de
`[4.1.0]` **excepto** la corrección de reproducibilidad cross-OS (§12,
corregida después en el commit `3b3cace`) y la recompilación correcta del
manuscrito final (§16, resuelta después en los commits de subida de
*Thais Herrera Ramos* del 2026-09-15 22:27–22:53). Se conserva en el
repositorio únicamente como referencia histórica; no representa el estado
final evaluado. Ver `[4.1.0]` para el cierre completo.

## [4.0.0] - 2026-09-07 — Entrega 4 (2B) / Defensa Final
### Añadido

- RNF-19 (equidad en el acceso a la cita) y RNF-20 (monitoreo posterior al
  despliegue del componente de IA) en el ERS/SRS, con métrica, umbral y
  responsable definidos.
- Paquete de datos reproducible completo en `07_Datos/` (datos crudos,
  procesados, resultados, diccionario de datos, licencia CC BY 4.0, script
  orquestador `run_all.py`).
- Evidencia de autoría completa en `10_Autoria/`: bitácora de sesiones (19
  días, historial completo del repositorio), capturas de pantalla de los 5
  integrantes, grabaciones de sesión de equipo, notas de campo manuscritas
  de las 8 entrevistas de elicitación, fotos del equipo en la organización
  (con EXIF verificado), doble codificación con cálculo de Cohen's Kappa
  (0,6997, acuerdo sustancial), declaración de uso de IA firmada por los 5
  integrantes, aporte individual con conteo real de commits, `.mailmap`.
- Sesión de member checking (04/09/2026) con 3 participantes previos del
  estudio, documentada en `02_Evidencias/Member_Checking/` (guion, resumen,
  registro estructurado por bloque y acta de conformidad).
- Despliegue reproducible del MVP mediante Docker y Docker Compose
  (`05_MVP/Dockerfile`, `docker-compose.yml`).
- Workflow de GitHub Actions para publicación automática del MVP en GitHub
  Pages (`.github/workflows/pages.yml`).
- Migración de la evidencia audiovisual restringida a un GitHub Release
  (`evidencia-restringida-v1`), para reducir el peso de clonado del
  repositorio.

### Cambiado

- Manuscrito final actualizado: se incorporaron los resultados del acuerdo
  intercodificador y de la sesión de member checking (antes reportados como
  trabajo futuro), y se corrigieron las secciones de "Amenazas a la validez"
  y "Conclusiones y trabajo futuro" en consecuencia.
- Los 8 commits históricos de la identidad genérica `MediCita Team` fueron
  atribuidos a Thais Melanie Herrera Ramos mediante `.mailmap`.
- Catálogo de requisitos no funcionales activos: de 17 a 19.
- Script de generación de checksums renombrado de `GENERA_CHEDKSUMS.sh` a
  `generar_checksums.sh`.
- Corrección de la referencia cruzada de número de oficio institucional
  (DGDS-069-2026) en `CategoriaA_A3_Aval_Establecimiento.pdf`, y actualización
  de los avales institucionales para reflejar a los 5 integrantes del equipo.

### Eliminado

- Carpeta de práctica independiente de Unidad V
  (`PE5_U5_PFC_DIAZ_GAMARRA_HERRERA_TIGASI_TRUJILLO/`), ajena a la estructura
  obligatoria del PFC.
- Matriz de trazabilidad duplicada (`matriz_trazabilidad.csv`), quedando
  `matriz_trazabilidad_ACTUALIZADA.csv` como única versión vigente.

## [3.0.0] - 2026-08-02 — Entrega 3 / corte actual

### Añadido

- Interfaces y mockups para los roles de paciente, recepción, enfermería,
  odontología, psicología y nutrición.
- Diagramas de casos de uso en PlantUML y sus exportaciones PNG.
- Diagrama general, diagramas de datos y diagramas complementarios del sistema.
- Archivos raíz para citación, licenciamiento y control de integridad.

### Cambiado

- Ampliación de la cobertura funcional del MVP y de los módulos clínicos.
- Normalización de nombres de mockups y organización del modelado UML.
- Actualización de los metadatos de citación a la versión 3.0.0.

### Corregido

- Relaciones, actores y distribución visual de los casos de uso.
- Correspondencia entre roles, módulos, requisitos e interfaces.

## [2.0.0] - 2026-07-28 — Entrega 2

### Añadido

- Evidencias del entorno del centro médico y registros de recolección.
- Transcripciones anonimizadas de participantes y áreas clínicas.
- Codificación inicial y categorías temáticas de la investigación.
- Diagramas UML, datos de trazabilidad y priorización de requisitos.
- Documentación ética, consentimientos y documentos organizacionales.

### Cambiado

- Reorganización de evidencias por tipo y nivel de acceso.
- Separación del material restringido en `02_Evidencias/00_Restringido/`.

### Corregido

- Nombres y ubicación de archivos de evidencias y modelado.
- Contenido de la codificación temática y de las transcripciones.

## [1.0.0] - 2026-07-21 — Entrega 1A

### Añadido

- Estructura inicial del repositorio.
- Especificación de Requisitos de Software.
- Directorios de evidencias, modelado, trazabilidad, MVP, experimento,
  publicación y ética.
- Archivos README iniciales para documentar el contenido de cada sección.

[4.2.0]: https://github.com/gleiston-guerrero/MediCita_ISR401/releases/tag/cierre-examen-suspenso-20260916
[4.1.0]: https://github.com/gleiston-guerrero/MediCita_ISR401/releases/tag/cierre-examen-suspenso-20260915
[4.0.1]: https://github.com/gleiston-guerrero/MediCita_ISR401/releases/tag/vFinal
