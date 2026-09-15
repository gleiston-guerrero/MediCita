# Historial de cambios

Todos los cambios relevantes del proyecto se documentan en este archivo.
El formato se basa en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/)
y el proyecto utiliza [versionado semántico](https://semver.org/lang/es/).

## [No publicado]

### Cierre del examen suspenso — 2026-09-15

### Añadido

- 10 notas de campo manuscritas escaneadas de las sesiones de validación
  por walkthrough (`V01` a `V10`, 2026-08-28/30), depositadas en
  `10_Autoria/notas_campo/`. **Nota:** las 18 sesiones de campo (8 de
  elicitación + 10 de validación) están completas; las 28 filas de
  `10_Autoria/bitacora_sesiones.csv` son sesiones internas de trabajo del
  equipo (commits) y no representan sesiones de campo — no se comparan
  entre sí.
- Cobertura técnica de RF Must (20 de 22, 90,91 %) incorporada como
  resultado explícito en el manuscrito (`07_Publicacion/manuscrito_final.tex`).
- Retrospectiva del equipo (`10_Autoria/retrospectiva_equipo.md`).

### Corregido

- Reproducibilidad byte a byte del paquete de datos: `resumen_descriptivo.csv`
  (en `07_Datos/datos_procesados/` y `07_Publicacion/dataset_zenodo/`) se
  regeneró con la orden única (`python 07_Datos/scripts/run_all.py`)
  para que coincida con la salida real del script; `checksums_datos.sha256`
  actualizado en consecuencia. `sha256sum -c checksums_datos.sha256 --quiet`
  ya no reporta discrepancias.

### Resuelto

- Requisito de "asignación o recomendación automática de cita" (Sección 5.2 de
  la Guía de Desarrollo): en vez de dejarlo solo como párrafo justificativo,
  se documenta como ficha formal de determinación de aplicabilidad (FDA-01),
  con el mismo nivel de detalle exigido a RNF-18 a RNF-22 (evidencia técnica,
  responsable, fecha). Fila 75 añadida a `matriz_trazabilidad_ACTUALIZADA.csv`
  y a su tabla equivalente en el ERS/SRS; conteo de filas actualizado de 74 a
  75 en el ERS y en el README; tabla de RNF del componente inteligente en el
  README actualizada para incluir FDA-01 junto a RNF-18 a RNF-22.
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
- Repositorio espejo (`MediCita_ISR401-archive`) archivado en Software
  Heritage; SWHID real (`swh:1:dir:6fbdc09760140cb9d176d33621b1262e1b9de2c2`)
  incorporado en `CITATION.cff` (09/09/2026).

### Nota sobre firmas del expediente ético

`A13_Participantes_Externos_MediCita.pdf`, `Adenda_Segunda_Ronda.pdf` y
`Adenda_Validacion_Walkthrough_corregida.pdf` permanecen sin firma del
docente responsable por decisión explícita de este, comunicada al equipo:
sirven como constancia del proceso realizado, ya que los documentos
originales firmados se conservan en el comité de ética. No se trata de un
pendiente.

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

[No publicado]: https://github.com/gleiston-guerrero/MediCita_ISR401/compare/v4.0.0...HEAD
[4.0.0]: https://github.com/gleiston-guerrero/MediCita_ISR401/releases/tag/v4.0.0
[3.0.0]: https://github.com/gleiston-guerrero/MediCita_ISR401/releases/tag/v3.0.0
[2.0.0]: https://github.com/gleiston-guerrero/MediCita_ISR401/releases/tag/v2.0.0
[1.0.0]: https://github.com/gleiston-guerrero/MediCita_ISR401/releases/tag/v1.0.0
