<div align="center">

# 🤖 A9 — Declaración de Uso de IA

### Proyecto MediCita (SICM) — ISR-401

![Estado](https://img.shields.io/badge/Estado-Completado-Green?style=for-the-badge)
![Herramientas](https://img.shields.io/badge/Herramientas-GPT--5.6_Sol_%2B_Claude_Sonnet_5-6e56cf?style=for-the-badge)
![Actualizado](https://img.shields.io/badge/Actualizado-13/09/2026-informational?style=for-the-badge)

</div>

---

## 📌 Cómo leer esta tabla

- **Herramienta:** nombre y modelo exacto usado.
- **Para qué:** tarea concreta realizada.
- **Quién verificó:** integrante humano responsable de revisar el resultado antes de aceptarlo.
- **Método de verificación:** cómo se confirmó que el resultado era correcto antes de incorporarlo.

> ✅ **Nota de confirmación:** la ejecución de los 12 usos de ChatGPT registrados en `registro_uso_llm.csv` fue confirmada directamente por Paul Alexander Tigasi Sampedro como propia, dado que comparten la misma marca de tiempo (`2026-08-29T19:44:50+00:00`) correspondiente a su sesión de corrección documental de esa fecha.

---

## 1️⃣ Revisión documental asistida por IA — ChatGPT / GPT-5.6 Sol 

Fuente: [`06_Experimento/prompst_LLm/registro_uso_llm.csv`](../06_Experimento/prompst_LLm/registro_uso_llm.csv) (registro completo con prompt, respuesta y hash SHA-256 por cada uso).

| Sección/artefacto revisado | Para qué se usó | Quién verificó | Método de verificación |
|---|---|---|---|
| ERS/SRS 2B — identificadores RF/RNF | Detectar contradicciones internas de conteos y definiciones | Paul Alexander Tigasi Sampedro | Revisión manual de los identificadores señalados antes de aceptar el cambio |
| Matriz de trazabilidad | Contrastar relaciones RF/RNF contra el catálogo vigente | Paul Alexander Tigasi Sampedro | Revisión manual de las filas corregidas |
| Ficha de observación → trazado a requisitos | Relacionar observaciones con RF/RNF sin inventar datos | Paul Alexander Tigasi Sampedro | Contraste contra las transcripciones originales |
| Control de integridad de métricas (SUS, IA) | Verificar que umbrales no se presenten como resultados medidos | Paul Alexander Tigasi Sampedro | Revisión cruzada contra el protocolo registrado |
| Control metodológico de SUS | Verificar si SUS fue realmente aplicado | Paul Alexander Tigasi Sampedro | Revisión de la ficha de observación disponible |
| Separación de líneas base 2B y PE5 | Evitar fusión silenciosa de líneas base distintas | Paul Alexander Tigasi Sampedro | Revisión manual de ambas líneas base |
| Revisión de requisitos de IA (equidad, monitoreo, explicabilidad) | Distinguir especificación de evidencia experimental real | Paul Alexander Tigasi Sampedro | Revisión manual de cada RNF de IA |
| Supervisión humana de IA | Identificar controles a verificar cuando exista implementación | Paul Alexander Tigasi Sampedro | Revisión manual del listado de controles |
| Control de procedencia de evidencia | Evitar mezclar elicitación (ELI-\*) con validación (OBS-\*) | Paul Alexander Tigasi Sampedro | Revisión cruzada contra el manifiesto de evidencia |
| Control de sesiones pendientes | Evitar completar observaciones sin evidencia real | Paul Alexander Tigasi Sampedro | Revisión contra el manifiesto de transcripciones |
| Rol de la IA en el experimento | Definir si la revisión cuenta como participante/entrevista | Paul Alexander Tigasi Sampedro | Decisión documentada: no cuenta como participante ni minutos humanos |
| Integridad de archivos LLM | Generar SHA-256 de los registros de uso de IA | Paul Alexander Tigasi Sampedro | Verificación de que los hashes coinciden con los archivos actuales |

> Ninguno de estos 12 usos cuenta como participante, entrevista o minutos humanos — son revisión documental de consistencia, no generación de datos de campo ni de resultados experimentales (declarado así en el registro original).

---

## 2️⃣ Redacción de documentos y análisis de datos recolectados — uso combinado GPT-5.6 Sol + Claude Sonnet 5

| Actividad | Herramientas usadas | Quién participó / verificó | Método de verificación |
|---|---|---|---|
| Redacción y elaboración de documentos | ChatGPT (GPT-5.6 Sol) y Claude Sonnet 5 (Anthropic) | Los 5 integrantes del equipo (Paul Alexander Tigasi Sampedro, Steven Santiago Díaz Pontón, Jamileth Estefanía Gamarra Zárate, Thais Melanie Herrera Ramos, Mayummy Jailly Trujillo Vega) | No aplica (actividad de redacción, no de verificación) |
| Verificación y análisis de coherencia de los datos generados | ChatGPT (GPT-5.6 Sol) y Claude Sonnet 5 (Anthropic) | Steven Santiago Díaz Pontón (principal) y Paul Alexander Tigasi Sampedro | Se revisó lo que ya se tenía contra lo que generaba cada herramienta, verificando si existía coherencia o relación exacta con los datos originales. Adicionalmente, se contrastó cruzando la respuesta de una herramienta contra la opinión de la otra (de ChatGPT a Claude y viceversa) antes de aceptar cualquier contenido. |

---

## 3️⃣ Asistencia de IA en la corrección final del repositorio — Claude Sonnet 5 (Anthropic), agosto-septiembre 2026

> **Sobre la columna "Quién verificó":** la interacción directa con la IA la realizó Paul Alexander Tigasi Sampedro. Sin embargo, los cambios propuestos no se aceptaron de forma unilateral: cada integrante revisaba el repositorio en sus propios días, se discutían los cambios en conjunto y se comparaban criterios entre todos antes de darlos por definitivos. Por eso cada fila indica ambos niveles: quién interactuó directamente con la IA, y que la validación final fue colectiva.

| Tarea | Para qué se usó | Quién verificó | Método de verificación |
|---|---|---|---|
| Auditoría del repositorio contra la Guía de Desarrollo | Contrastar el estado real del repositorio contra la guía y el informe del docente | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Verificación directa sobre el repositorio clonado (conteos, hashes, compilación real del LaTeX) |
| Redacción de RNF-19 (equidad) y RNF-20 (monitoreo) | Especificar dos requisitos no funcionales exigidos por la guía, no declarados previamente | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Revisión de que la métrica y el umbral fueran razonables para el dominio del proyecto; compilación real del documento sin errores |
| Corrección de rutas en `run_all.py` | Reparar el pipeline tras mover archivos de `06_Experimento` a `07_Datos` | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Ejecución real del script, confirmando que reproduce las mismas cifras ya publicadas en el manuscrito |
| Migración de evidencia audiovisual a GitHub Release | Reducir el peso de clonado del repositorio sin eliminar evidencia | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Verificación de que los hashes SHA-256 del Release coinciden con `fichas_tecnicas.csv` |
| Redacción de plantillas de `10_Autoria/` (A8, A9, A10) | Generar el formato exigido por la guía, con datos reales del historial de Git y de los documentos de correspondencia | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Contraste de las cifras (commits, fechas) contra `git log` y contra los PDF originales directamente |
| Redacción de oficios corregidos (Oficio de Respaldo, Aval CategoriaA_A3) | Actualizar los 5 integrantes del equipo y corregir la inconsistencia de nombre de firmante | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Contraste línea por línea contra el texto original antes de aceptar cada cambio |

---

## 4️⃣ Secciones/artefactos donde NO se usó ninguna herramienta de IA

| Actividad | Responsable(s) |
|---|---|
| Recolección de datos en campo (entrevistas, observación del walkthrough) | Equipo completo, en persona |
| Firma de consentimientos y trámites institucionales (solicitudes, avales) | Paul Alexander Tigasi Sampedro,  Steven Santiago Díaz Pontón ,Thais Melanie Herrera Ramos |

---

## 5️⃣ Corrección final del repositorio tras la revisión de cierre — Claude Sonnet 5 (Anthropic), 09-12/09/2026

> **Sobre la columna "Quién verificó":** igual que en la sección 3️⃣, la interacción directa con la IA la realizó Paul Alexander Tigasi Sampedro; los cambios se discutieron y validaron en conjunto con el equipo antes de aceptarlos como definitivos.

| Tarea | Para qué se usó | Quién verificó | Método de verificación |
|---|---|---|---|
| Redacción de la sección "Alcance del componente de IA y requisitos que no aplican" | Declarar explícitamente que RF-02/RF-13 no son un componente de IA y que el requisito de "asignación/recomendación automática de cita" no aplica al sistema | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Revisión línea por línea de RF-02 y RF-13 contra la especificación real, sin modelo ni métrica de acierto |
| Redacción de RNF-21 (supervisión humana) y RNF-22 (clasificación del nivel de riesgo) | Completar los seis requisitos del componente inteligente exigidos por la guía de cierre | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Revisión de que la métrica y el umbral fueran razonables para el dominio; compilación real del documento sin errores (xelatex + bibtex, 3 pasadas) |
| Reescritura de RNF-19 (equidad), re-enfocado de RF-02/RF-13 a RF-16 | Corregir la referencia errónea a un componente que no es de IA | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Contraste contra el único componente de IA real del sistema (RF-16) |
| Corrección de un `\begin{quote}` sin cerrar en `ERS_SRS_2B_V2.0.tex` | Reparar una falla de compilación que afectaba la reproducibilidad documental (P2) | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Recompilación real del documento, confirmando 0 errores |
| Corrección de las filas 71, 73 y 74 de `matriz_trazabilidad_ACTUALIZADA.csv` | Sincronizar la matriz con la corrección de RNF-19 y agregar RNF-21/RNF-22 | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Contraste manual contra la tabla equivalente ya corregida dentro del ERS |
| Redacción de finalidad y plazo de conservación en `CategoriaA_A4_Referencia_LOPDP.pdf` | Completar los cuatro elementos exigidos por el ítem B6 (base de licitud, finalidad, plazo, responsable) | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Revisión de que el plazo declarado (6 meses tras la defensa) fuera razonable para el equipo |
| Diseño de las plantillas y el script de la doble observación independiente (`10_Autoria/doble_observacion_sesiones/`) | Cubrir el ítem B4 (kappa entre dos observadores independientes sobre el 20% de las sesiones de validación) | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | El script se probó verificando que se niega a calcular el Kappa si falta algún juicio del segundo observador |
| Cálculo de la tabla de duración por sesión en `ficha_observacion.csv` y del perfil agregado de participantes (`perfil_agregado_participantes.csv`) | Completar los datos de duración y el perfil agregado exigidos por B3, cruzando `fuente_evidencia` contra `fichas_tecnicas.csv` ya verificado | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Cruce por nombre de archivo contra el inventario técnico ya verificado con hash SHA-256; dos asignaciones de menor certeza (VAL-COORD, VAL-PAC) quedaron marcadas para confirmación del equipo |
| Corrección de dos fragmentos de código incompletos en `05_MVP/script.js` | Reparar la demostración interactiva del MVP, que no respondía al hacer clic | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Prueba real en navegador (Playwright): el botón responde y la animación avanza tras el arreglo |
| División de `06_Experimento/scripts_analisis/run_all.py` en `leer_datos.py`, `procesar_datos.py` y `generar_resultados.py` | Cumplir el ítem A4 (separar lectura, procesamiento y generación en etapas, dejando `run_all.py` como coordinador) | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Ejecución de ambas versiones (original y dividida) con comparación byte por byte de las salidas: JSON, CSV y hash de las figuras PNG, todos idénticos |
| Redacción del contenido de 12 archivos de 1 byte (`scripts_analisis_.md`, `prompts_LLm_.md`, y 9 `README.md` de `03_Modelado`) | Eliminar el riesgo de cero directo por el criterio de piso P3 (evidencia vacía) | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Contraste de cada descripción contra el conteo real de archivos de su carpeta, o contra `registro_uso_llm.csv` ya existente; ningún dato inventado |
| Construcción de `generar_procesados.py` y ajuste de `leer_datos.py` para que la cadena de análisis arranque desde `ficha_observacion.csv` (crudo) en vez de datos "procesados estáticos" | Cumplir el ítem B1/A4 (que el paquete de datos sea reproducible desde el crudo real, sin tocar nada a mano) | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Comparación campo por campo de la salida generada contra los archivos oficiales ya publicados: `observacion_requisito_long.csv` salió idéntico byte por byte (72 filas); se documentó una inconsistencia heredada (RNF-04 en 5 filas) sin resolverla unilateralmente |
| Identificación y adición de 16 filas reales faltantes en `ficha_observacion.csv` (sesiones VAL-PSI y VAL-PAC02) | El crudo estaba incompleto: le faltaban dos sesiones de validación que sí formaban parte de los "46 observaciones" ya publicados | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Verificación de que la evidencia de esas sesiones existe (transcripciones, consentimientos, notas de campo) antes de copiar el contenido ya redactado por el equipo; ningún juicio observacional nuevo fue generado por IA |
| Corrección de `power_calculation_justificacion.md` | El archivo atribuía el cálculo de potencia al prerregistro OSF; esa afirmación no está respaldada por el contenido real de `osf_registration.pdf` | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Lectura completa del PDF del prerregistro: no aparece ninguna mención de Cohen's d, alfa, potencia, ni n=64/128 |
| Depósito de correspondencia real en `10_Autoria/correspondencia/` (ítem A8) y redacción de la desviación sobre confirmaciones de horario en `07_Datos/desviaciones.md` | Cerrar el ítem A8, que estaba a medias porque la carpeta solo tenía un índice sin comunicaciones fechadas depositadas | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Confirmación de que los 4 documentos ya existían, reales y firmados, en otras carpetas del repositorio antes de copiarlos aquí; ninguna comunicación nueva fue generada o simulada |
| Detección automática y pixelado del rostro de la persona entrevistada en 5 fotografías aportadas por el equipo (`10_Autoria/correspondencia/evidencia_entrevista/`) | Anonimizar al personal del centro médico en la evidencia fotográfica de las entrevistas, siguiendo el mismo criterio ya aplicado a los consentimientos | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Cada detección se verificó visualmente antes de aplicar el pixelado, marcando la posición sobre la imagen para confirmar que correspondía a la persona correcta (entrevistado, no al integrante del equipo); la fecha, hora y contenido de cada fotografía fueron aportados directamente por el equipo, no generados por IA |

> **Nota importante:** el contenido observacional en sí (qué se completó, qué incidente se registró en cada tarea del walkthrough, el juicio del segundo observador) fue producido por integrantes del equipo viendo directamente los videos de validación — la IA no generó, sugirió ni completó ningún juicio de observación de campo.

---

## 6️⃣ Repaso exhaustivo de cierre — categorías adicionales no listadas en las secciones anteriores

> Esta sección se agrega tras un repaso sistemático completo de todas las sesiones de trabajo con Claude Sonnet 5 a lo largo de todo el proyecto (agosto-septiembre 2026), para asegurar cobertura total conforme al criterio P9 de la rúbrica de cierre. **Sobre la columna "Quién verificó":** igual que en las secciones 3️⃣ y 5️⃣, la interacción directa con la IA la realizó Paul Alexander Tigasi Sampedro; los cambios se discutieron y validaron en conjunto con el equipo antes de aceptarlos como definitivos.

| Tarea | Para qué se usó | Quién verificó | Método de verificación |
|---|---|---|---|
| Diseño del script `calcular_kappa.py` y cálculo del acuerdo intercodificador (A7, `10_Autoria/doble_codificacion/`) | Cumplir el ítem A7 de la Guía de Desarrollo: coeficiente de acuerdo entre dos codificadores independientes, con intervalo de confianza, generado por script | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | El script se ejecutó realmente sobre las hojas de ambos codificadores; el resultado (κ=0,6997) se contrastó contra un cálculo manual de verificación de la fórmula de Cohen |
| Redacción del guion, resumen narrativo y acta formal de la sesión de Member Checking (`02_Evidencias/Member_Checking/`) | Documentar la sesión de miembro-verificación exigida por el ítem C4 de la rúbrica, con los 7 bloques temáticos reales trabajados por el equipo | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Contraste de cada bloque y resultado contra lo que el equipo reportó verbalmente haber ocurrido en la sesión real; ningún hallazgo ni cita fue generado por IA |
| Incorporación al manuscrito de los resultados de Kappa (A7) y de la sesión de Member Checking, y del intervalo de confianza bootstrap para la V de Cramér | Corregir que el manuscrito reportaba estos dos controles como "trabajo futuro" cuando ya se habían ejecutado; agregar el IC faltante en el análisis estadístico principal | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Recompilación real del manuscrito (xelatex+bibtex×2), confirmando 15 páginas sin errores; el IC se generó ejecutando la función de bootstrap agregada a `run_all.py`, no calculado a mano |
| Reestructuración del guion de defensa oral, la presentación (PPTX) y el folleto de una hoja para incorporar los resultados de Kappa, Member Checking y el estado real de Software Heritage | Actualizar los 3 materiales de defensa (`09_Defensa/`), que estaban desactualizados respecto al estado final del repositorio | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Verificación de que cada cifra citada en los 3 materiales coincidiera exactamente con los archivos fuente (`resultado_kappa.md`, `resultados_estadisticos.json`); reparto de tiempo de exposición revisado para quedar parejo entre los 5 integrantes |
| Elaboración del documento `verificacion_previa.docx/pdf` (Sección 11 de la Guía de Desarrollo) y verificación técnica de sus 12 puntos | La carpeta `10_Autoria` no tenía este documento, exigido explícitamente antes del cierre | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo; firma final de conformidad por Jamileth Estefanía Gamarra Zárate | Cada uno de los 12 puntos se verificó contra evidencia real del repositorio (fecha de commits, existencia de archivos, compilación) antes de marcarlo como cumplido |
| Redacción de `Fe_de_Erratas_Adenda_Walkthrough.md` y de la aclaración sobre la composición real de participantes (16 externos distintos) en `07_Datos/desviaciones.md` y `06_Experimento/osf_deviations.tex` | Corregir una discrepancia real entre lo declarado en la adenda y lo que muestran las transcripciones de las sesiones 07 y 10 de validación | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Lectura directa de ambas transcripciones para confirmar quién habla en cada una, antes de redactar la corrección |
| Corrección de `CHANGELOG.md` (registro de versiones) y activación del identificador real de Software Heritage en `CITATION.cff` | Mantener el historial de cambios sincronizado con el estado real, e incorporar el SWHID obtenido tras el archivado del repositorio espejo | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | El SWHID se copió textualmente de la página de Software Heritage tras confirmar el estado "succeeded" del archivado; se validó que el YAML de `CITATION.cff` siguiera siendo válido tras el cambio |
| Reformateo de decenas de archivos `README.md`/`Readme.md` de subcarpetas de todo el repositorio al formato visual estándar (insignias y tablas) adoptado por el equipo | Unificar la presentación de toda la documentación del repositorio | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | En cada caso, el contenido factual ya existente se conservó sin alterarlo; solo se le aplicó el formato visual ya usado en el resto del repositorio |
| Actualización recurrente de `10_Autoria/bitacora_sesiones.csv` y `10_Autoria/aporte_individual.md` conforme avanzaba el proyecto (conteo de commits, días de participación, detalle cualitativo por integrante) | Mantener estos 2 documentos (A1 y A10) reflejando el estado real del historial de Git en cada etapa del cierre | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Cada actualización se generó ejecutando `git shortlog`/`git log` directamente sobre un clon completo del repositorio, nunca estimado ni copiado de una versión anterior sin verificar |
| Redacción de la nota de transparencia sobre el campo de cédula (CI) sin completar en 2 consentimientos (`02_Evidencias/Consentimientos/Readme.md`) | Documentar honestamente una omisión real del firmante, en vez de dejarla sin explicar o completarla sin respaldo | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Verificación visual directa de los 2 documentos PDF para confirmar que el campo seguía vacío antes de redactar la nota |
| Actualización de `07_Datos/registro_deposito.md` con el detalle verificado del origen de la evidencia audiovisual (19 videos, 18 audios, por ronda) y confirmación de que ningún archivo de audio/video está referenciado en los 3 depósitos abiertos | Responder con precisión a una consulta directa del equipo sobre cuántos videos existen y de dónde salen | Paul Alexander Tigasi Sampedro (interacción directa) — validado en conjunto con el equipo | Conteo directo sobre `fichas_tecnicas.csv` con Python; búsqueda de texto directa en los 3 paquetes de depósito para confirmar la ausencia de referencias |

> **Nota:** en ninguna de las tareas anteriores la IA generó un juicio de campo, una cifra experimental, una cita textual de un participante, ni una decisión ética o de contenido — su función fue exclusivamente de redacción de formato, verificación cruzada de consistencia entre documentos ya existentes, y ejecución de scripts sobre datos ya reales y verificados por el equipo.

---

## ✍️ Firma de los integrantes

⚠️ **Esta declaración se amplió el 13/09/2026 (Sección 6️⃣) respecto a la versión firmada el 12/09/2026.** Se recomienda que los 5 integrantes revisen la sección nueva y vuelvan a firmar para que la fecha de firma respalde el contenido completo y actual del documento.

| Integrante - Firma | Fecha |
|------|---|
| Paul Alexander Tigasi Sampedro | 13/09/2026 18:42 |
| Steven Santiago Díaz Pontón | | |
| Jamileth Estefanía Gamarra Zárate | 13/09/2026 18:42 |
| Thais Melanie Herrera Ramos | 13/09/2026  18:40 |
| Mayummy Jailly Trujillo Vega | 13/09/2026 18:41 |
