<div align="center">

# 🏥 SICM — Sistema de Gestión Inteligente para un Centro Médico

### MediCita_ISR401

**Proyecto Fin de Curso (PFC) – Ingeniería de Requerimientos (ISR-401)**

<br>

![Universidad](https://img.shields.io/badge/Universidad-UTEQ-003366?style=for-the-badge)
![Carrera](https://img.shields.io/badge/Carrera-Ingeniería_de_Software-00509d?style=for-the-badge)
![Norma](https://img.shields.io/badge/ISO-29148:2018-orange?style=for-the-badge)
![Licencia](https://img.shields.io/badge/Licencia-MIT_%2B_CC_BY_4.0-2e7d32?style=for-the-badge)
![Entrega](https://img.shields.io/badge/Entrega_Final_Defensa_Final-success?style=for-the-badge)

</div>

---

## 📌 Entrega vigente y alcance de la evaluación

Este repositorio corresponde a la **Entrega 4 (2B / Defensa Final)** del Proyecto Fin de Curso de la asignatura **Ingeniería de Requerimientos (ISR-401)** de la Universidad Técnica Estatal de Quevedo (UTEQ).

**Etiqueta de línea base vigente:** `cierre-examen-suspenso-20260917f`, anotada sobre el commit que corrige la reproducibilidad real de `07_Datos/resultados/resultados_estadisticos.json` (CHANGELOG `[4.3.8]`, 17/09/2026) y sincroniza este README, el CHANGELOG y la retrospectiva (`10_Autoria/retrospectiva_equipo.md`) para que los tres declaren la misma etiqueta como línea base. `cierre-examen-suspenso-20260917d`, `cierre-examen-suspenso-20260917c`, `cierre-examen-suspenso-20260917`, `cierre-examen-suspenso-20260916`, `cierre-examen-suspenso-20260915` y `vFinal` se conservan como referencia histórica de los intentos de cierre anteriores, **verificadas con `git ls-remote --tags` contra el repositorio remoto** — `cierre-examen-suspenso-20260917e` se planeó en el CHANGELOG `[4.3.7]` pero nunca se publicó (no existe en el remoto) y no debe citarse como línea base histórica; las demás etiquetas (`evidencia-restringida-v1`, etc.) corresponden a releases de evidencia distintos y tampoco son la línea base.

**Sobre las notas de campo y la bitácora:** `10_Autoria/bitacora_sesiones.csv` tiene 46 filas — 28 de trabajo interno del equipo y 18 de sesiones de campo con participante externo (8 entrevistas + 10 validaciones por walkthrough), estas últimas con columna `tipo` y con enlace directo en `ruta_nota_campo` a su nota manuscrita en `10_Autoria/notas_campo/` (que tiene, en efecto, sus 18 notas completas).

La evaluación de esta entrega debe considerar los artefactos organizados en las carpetas `01_ERS/` a `10_Autoria/`, junto con los archivos de documentación, integridad y reproducibilidad ubicados en la raíz del repositorio.

El repositorio integra la línea base final del proyecto **SICM / MediCita**, incluyendo:

- ERS/SRS (40 RF, 21 RNF activos).
- Evidencias de elicitación y validación.
- Modelado UML.
- Trazabilidad.
- MVP funcional.
- Componente empírico reproducible.
- Paquete de datos abierto y reproducible (`07_Datos/`).
- Documentación de publicación.
- Documentación ética.
- Evidencia de autoría y trabajo propio (`10_Autoria/`).
- Materiales de defensa final.

> **Importante:** para la evaluación de la Entrega 4 (2B) debe prevalecer la documentación final y vigente del PFC.

---


## 🗃️ Historial de repositorios del proyecto

**Repositorio histórico — Avances 1A y 1B:**
https://github.com/ptigasis-Alexander/PFC_IR_AVANCES_TIGASI_GAMARRA-ZARATE_DIAZ_THAIS_TRUJILLO

**Repositorio vigente — desde 2A hasta Entrega 4 (2B):**
https://github.com/gleiston-guerrero/MediCita_ISR401

Para la **Entrega Final** prevalece el contenido vigente de este repositorio.

---

## ⚙️ Clonar el repositorio

⚠️ **El repositorio pesa varios gigabytes en su historial completo**, debido a evidencia audiovisual que estuvo versionada directamente en Git. Esa evidencia **ya no forma parte del árbol actual** — se movió a un GitHub Release — pero el historial de commits todavía la conserva.

### Clonación recomendada (rápida y liviana, ~370 MB)

```bash
git clone --depth 1 https://github.com/gleiston-guerrero/MediCita_ISR401.git
cd MediCita_ISR401
```

Esto trae **todo el contenido actual del proyecto**, en todas sus carpetas, sin descargar el historial completo de versiones.

### Clonación completa (incluye todo el historial, mucho más pesada)

```bash
git clone https://github.com/gleiston-guerrero/MediCita_ISR401.git
cd MediCita_ISR401
```

Use esta opción únicamente si necesita auditar el historial completo de commits.

### 🎬 Evidencia audiovisual restringida (videos y audios)

Los archivos `.7z` de video/audio de `02_Evidencias/00_Restringido/` se publican como assets de GitHub Release, para no inflar el peso del repositorio:

**https://github.com/gleiston-guerrero/MediCita_ISR401/releases/tag/evidencia-restringida-v1**

Los hashes SHA-256 de cada archivo, declarados en `fichas_tecnicas.csv`, corresponden exactamente a los archivos publicados en ese Release — el traslado no modificó ningún contenido.

---

## ✅ Estado de la Entrega 4 (2B)

| Sección / artefacto | Contenido principal | Estado |
|---|---|:---:|
| `01_ERS/` | ERS/SRS (40 RF, 21 RNF activos), fuentes LaTeX, bibliografía y figuras | 🟢 Completo |
| `02_Evidencias/` | Entrevistas, consentimientos, transcripciones, codificación temática, cuestionario, walkthrough y evidencia restringida | 🟢 Completo |
| `03_Modelado/` | Diagramas UML y mockups/interfaces finales | 🟢 Completo |
| `04_Trazabilidad/` | Matrices de trazabilidad y priorización de requisitos | 🟢 Completo |
| `05_MVP/` | Prototipo funcional y demo mediante GitHub Pages | 🟢 Completo |
| `06_Experimento/` | Protocolo, OSF, instrumentos, prompts LLM y desviaciones | 🟢 Completo |
| `07_Datos/` | Paquete de datos crudos, procesados, resultados y script orquestador reproducible | 🟢 Completo |
| `07_Publicacion/` | Manuscrito, bibliografía, figuras, tablas y paquete de publicación | 🟢 Completo |
| `08_Etica/` | Documentación ética y anexos | 🟢 Completo  |
| `09_Defensa/` | Presentación, guion, folleto y video de defensa final | 🟢 Completo |
| `10_Autoria/` | Bitácora de sesiones, `.mailmap`, declaración de uso de IA, aporte individual, correspondencia | 🟢 Completo |
| Registro OSF | DOI `10.17605/OSF.IO/DTYNC` | 🟢 Público |
| Depósito Zenodo | DOI `10.5281/zenodo.22236373` | 🟢 Publicado |
| Software Heritage | SWHID `swh:1:dir:6fbdc0976...` | 🟢 Obtenido |
| Integridad SHA-256 | Comprobación de integridad de archivos | 🟢 Obtenido |
| Autoevaluación FAIR | Evaluación de principios FAIR (F-UJI, 88%) | 🟢 Confirmado (v1.0.0, 01/09/2026) |


> **Nota — `02_Evidencias/`:**  los 9 consentimientos originales están pixelados para mantener la privacidad de datos sensibles como los nombres y firmas.

---

# 📖 Descripción del proyecto

**SICM — Sistema de Gestión Inteligente para un Centro Médico**, denominado también **MediCita**, es una propuesta de sistema orientada a centralizar y apoyar los principales procesos clínicos y administrativos de un centro médico ambulatorio.

El proyecto fue desarrollado a partir de evidencia de campo obtenida durante el proceso de Ingeniería de Requisitos, en colaboración con el Centro Médico Municipal de la Dirección de Gestión de Desarrollo Social (DGDS) del GAD Municipal de Quevedo.

Las áreas consideradas incluyen: Medicina General, Enfermería, Odontología, Psicología, Nutrición, Terapia Física, Recepción y Recaudación, Coordinación, y Paciente.

El sistema contempla procesos de: registro de pacientes, gestión de citas, agenda profesional, historia clínica, signos vitales, atención por especialidad, recetas médicas, entrega de medicamentos, derivaciones, pagos y comprobantes, inventario, notificaciones, gestión de personal, reportes, auditoría, y control de acceso basado en roles.

---

# 👥 Equipo

| Integrante | Rol | Correo institucional | ORCID |
|---|---|---|:---:|
| Paul Alexander Tigasi Sampedro | Líder | ptigasis@uteq.edu.ec | [0009-0005-1812-7100](https://orcid.org/0009-0005-1812-7100) |
| Steven Santiago Díaz Pontón | Técnico | sdiazp3@uteq.edu.ec | [0009-0000-6558-4930](https://orcid.org/0009-0000-6558-4930) |
| Jamileth Estefanía Gamarra Zárate | Secretaria | jgamarraz@uteq.edu.ec | [0009-0002-8916-6578](https://orcid.org/0009-0002-8916-6578) |
| Thais Melanie Herrera Ramos | Técnica | therrerar@uteq.edu.ec | [0009-0005-2666-6921](https://orcid.org/0009-0005-2666-6921) |
| Mayummy Jailly Trujillo Vega | Técnica | mtrujillov@uteq.edu.ec | [0009-0009-5157-290X](https://orcid.org/0009-0009-5157-290X) |

**Docente:** Ing. Gleiston Cicerón Guerrero Ulloa
**Asignatura:** Ingeniería de Requerimientos (ISR-401)
**Facultad:** Ciencias de la Computación
**Universidad:** Universidad Técnica Estatal de Quevedo (UTEQ)

---

# 🔗 Enlaces principales

| Recurso | Enlace | Estado |
|---|---|:---:|
| 📄 ERS/SRS 2A | [`01_ERS/ERS_SRS_2A_V1.0.pdf`](01_ERS/ERS_SRS_2A_V1.0.pdf) | 🟢 |
| 📄 ERS/SRS 2B final (120 pág., 40 RF, 21 RNF) | [`01_ERS/ERS_SRS_2B_V2.0.pdf`](01_ERS/ERS_SRS_2B_V2.0.pdf) | 🟢 |
| 📝 Fuente LaTeX ERS 2B | [`01_ERS/ERS_SRS_2B_V2.0.tex`](01_ERS/ERS_SRS_2B_V2.0.tex) | 🟢 |
| 💻 MVP funcional | [GitHub Pages](https://gleiston-guerrero.github.io/MediCita_ISR401/) | 🟢 |
| 📦 Paquete de datos reproducible | [`07_Datos/README_datos.md`](07_Datos/README_datos.md) | 🟢 |
| 📝 Registro OSF | [10.17605/OSF.IO/DTYNC](https://doi.org/10.17605/OSF.IO/DTYNC) | 🟢 |
| 📑 Manuscrito final | [`07_Publicacion/manuscrito_final.pdf`](07_Publicacion/manuscrito_final.pdf) | 🟢 |
| 📦 Dataset Zenodo | [10.5281/zenodo.22236373](https://doi.org/10.5281/zenodo.22236373) | 🟢 |
| 🎬 Evidencia audiovisual restringida | [GitHub Release](https://github.com/gleiston-guerrero/MediCita_ISR401/releases/tag/evidencia-restringida-v1) | 🟢 |
| 🧾 Evidencia de autoría | [`10_Autoria/Readme.md`](10_Autoria/Readme.md) | 🟢 |
| 🎓 Defensa final | [`09_Defensa/`](09_Defensa/) | 🟢 |
| 📜 Citación | [`CITATION.cff`](CITATION.cff) | 🟢 |
| ⚖️ Licencia | [`LICENSE`](LICENSE) | 🟢 |

---

# 📊 Evidencia y resultados principales

## Primera ronda — elicitación (8 entrevistas)

Medicina General · Enfermería · Nutrición · Odontología/Coordinación · Terapia Física · Psicología · Recepción · Paciente simulado.

## Segunda ronda — validación del prototipo (10 sesiones con transcripción)

| Indicador | Resultado |
|---|---:|
| Entrevistas de elicitación | **8** |
| Sesiones de validación procesadas | **10** |
| Observaciones procesadas | **46** |
| Completadas con observación de mejora | **39** |
| No completadas | **5** |
| Completadas sin observación | **2** |
| Relaciones observación–requisito | **72** |

---

# 🧪 Cobertura técnica del MVP

Verificación técnica reproducible de los RF Must: **20 de 22 (90,91 %)**, sobre un umbral académico de **≥ 80 %**.

Requisitos sin cierre técnico: **RF-09**, **RF-18**.

### ⚠️ Interpretación correcta del 90,91 %

No representa SUS, satisfacción de participantes, precisión de IA, ni una segunda revalidación humana. Es únicamente verificación técnica reproducible del MVP tras los ajustes derivados del walkthrough.

---

# 🤖 Componente inteligente — requisitos no funcionales

El único componente de IA identificado en el sistema es **RF-16 — Asistente virtual con IA (chat box)**. RF-02 y RF-13 (agendar cita, consultar disponibilidad) son consultas deterministas y no forman parte de este componente. Sobre RF-16 se definieron 5 requisitos no funcionales específicos, cada uno con métrica, umbral y método de verificación propios. El sexto requisito que exige la guía de cierre para todo componente de IA —asignación o recomendación automática— no aplica a RF-02/RF-13 por ser deterministas; esa determinación queda documentada formalmente como ficha FDA-01 (ver `01_ERS/ERS_SRS_2B_V2.0.pdf`, Sección 3.4.1, y fila 75 de `04_Trazabilidad/matriz_trazabilidad_ACTUALIZADA.csv`):

| RNF / Ficha | Característica | Estado de validación |
|---|---|:---:|
| RNF-18 | Explicabilidad | 🟡 Base normativa definida; validación de campo pendiente |
| RNF-19 | Equidad en la resolución de consultas del asistente | 🟡 Requisito y métrica definidos; medición pendiente de datos en producción |
| RNF-20 | Monitoreo posterior al despliegue | 🟡 Requisito e indicadores definidos; monitoreo pendiente de despliegue |
| RNF-21 | Supervisión humana | 🟡 Mecanismo de anulación definido; medición pendiente de datos en producción |
| RNF-22 | Clasificación del nivel de riesgo | 🟡 Niveles y método de verificación definidos; conjunto de prueba etiquetado pendiente |
| FDA-01 | Determinación de no aplicabilidad — asignación/recomendación automática de cita | 🟢 Determinación completa, con evidencia técnica y responsable |

---

# 🔗 Trazabilidad

```text
Fuente / necesidad → Requisito → Caso de uso / historia → Modelo UML
→ Interfaz / MVP → Observación de validación → Verificación
```

Archivos en `04_Trazabilidad/` — matriz vigente: `matriz_trazabilidad_ACTUALIZADA.csv` (75 filas: 74 de RF/RNF más la fila FDA-01 de determinación de no aplicabilidad).

---

# 🗂️ Organización del repositorio

```text
MediCita_ISR401/
│
├── 01_ERS/
├── 02_Evidencias/
├── 03_Modelado/
├── 04_Trazabilidad/
├── 05_MVP/
├── 06_Experimento/
├── 07_Datos/
├── 07_Publicacion/
├── 08_Etica/
├── 09_Defensa/
├── 10_Autoria/
│
├── .mailmap
├── README.md
├── LICENSE
├── CITATION.cff
├── CHANGELOG.md
├── checksums.sha256
├── generar_checksums.sh
└── fair_assessment.pdf
```

> **Nota sobre numeración:** `07_Datos/` coexiste con `07_Publicacion/`. El prefijo "07" de `07_Datos` corresponde a la numeración exigida por la Guía de Desarrollo del 02/09/2026 (Sección 7), independiente de la numeración secuencial de las entregas del PFC.

---

## 📁 `01_ERS/`
Especificación de Requisitos de Software: 40 RF, 21 RNF activos, reglas de negocio, priorización, historias de usuario, casos de uso, referencias, figuras, fuentes LaTeX y PDF.

## 📁 `02_Evidencias/`
Consentimientos, transcripciones, codificación temática, cuestionario, fotografías de entorno, validación walkthrough y evidencia restringida. Los archivos con información sensible permanecen en el área restringida o se publican anonimizados.

## 📁 `03_Modelado/`
Diagramas UML y mockups/interfaces relacionados con los requisitos del proyecto.

## 📁 `04_Trazabilidad/`
Matrices que relacionan requisitos, fuentes, modelos, evidencias, interfaces y elementos de verificación.

## 📁 `05_MVP/`
Prototipo funcional. Versión pública: https://gleiston-guerrero.github.io/MediCita_ISR401/

## 📁 `06_Experimento/`
Protocolo, registro OSF, desviaciones, instrumentos, prompts LLM y scripts de análisis (`run_all.py`).

## 📁 `07_Datos/`
Paquete de datos reproducible: `datos_crudos/`, `datos_procesados/`, `resultados/`, diccionario de datos, licencia de datos (CC BY 4.0, distinta de la licencia del código), checksums propios, registro de desviaciones y de depósito. Ver `07_Datos/README_datos.md` para el procedimiento de reproducción con una sola orden.

## 📁 `07_Publicacion/`
Manuscrito científico, fuente LaTeX, bibliografía, figuras, tablas y materiales del depósito en Zenodo.

## 📁 `08_Etica/`
Documentación ética y anexos. Los materiales con datos identificables deben tratarse según su nivel de acceso y no incorporarse a datasets públicos sin anonimización.

## 📁 `09_Defensa/`
Presentación, guion de exposición, folleto de apoyo y video de la Defensa Final.

## 📁 `10_Autoria/`
Evidencia de autoría y trabajo propio: bitácora de sesiones (generada a partir del historial real de Git), `.mailmap`, declaración de uso de IA por sección, aporte individual, correspondencia con la organización, y demás elementos A1–A12 exigidos por la Guía de Desarrollo. Ver `10_Autoria/Readme.md` para el estado detallado de cada elemento.

---

# 🔬 Reproducibilidad

## Requisitos básicos

```bash
sudo apt install texlive-xetex texlive-lang-spanish
pip install scipy matplotlib
```

## 📄 Compilar ERS/SRS 2B

```bash
cd 01_ERS
xelatex -interaction=nonstopmode ERS_SRS_2B_V2.0.tex
bibtex ERS_SRS_2B_V2.0
xelatex -interaction=nonstopmode ERS_SRS_2B_V2.0.tex
xelatex -interaction=nonstopmode ERS_SRS_2B_V2.0.tex
```

## 📑 Compilar el manuscrito

```bash
cd 07_Publicacion
pdflatex -interaction=nonstopmode manuscrito_final.tex
bibtex manuscrito_final
pdflatex -interaction=nonstopmode manuscrito_final.tex
pdflatex -interaction=nonstopmode manuscrito_final.tex
```

## 📊 Reproducir el análisis y el paquete de datos

```bash
python 07_Datos/scripts/run_all.py
```

Este script ejecuta el pipeline real (`06_Experimento/scripts_analisis/run_all.py`) y sincroniza sus salidas hacia `07_Datos/datos_procesados/` y `07_Datos/resultados/`, para que ambas copias provengan siempre del mismo código.

---

# 🔐 Evidencias restringidas

Evidencia restringida en `02_Evidencias/00_Restringido/`. Los archivos `.7z` de video/audio se publican como assets del GitHub Release (ver sección de clonación); esa carpeta conserva únicamente `fichas_tecnicas.csv` con los hashes SHA-256 de verificación.

Los datasets públicos no contienen identificadores directos (nombres, cédulas, firmas, rostros, voces, teléfonos, correos personales, direcciones).

---

# 🔎 Integridad mediante SHA-256

```bash
sh generar_checksums.sh
sha256sum --check checksums.sha256
```

> **Importante:** `checksums.sha256` debe regenerarse después del último cambio realizado en la entrega.

---

# ♻️ Autoevaluación FAIR

Documentada en `fair_assessment.pdf`. Mecanismo distinto del archivado en Software Heritage y de los hashes SHA-256 de integridad.

---

# 🌐 Identificadores persistentes

| Servicio | Identificador | Estado |
|---|---|:---:|
| OSF | `10.17605/OSF.IO/DTYNC` | 🟢 Obtenido |
| Zenodo | `10.5281/zenodo.22236373` | 🟢 Obtenido |
| Software Heritage | SWHID | 🟢 Obtenido|

---

# 🗄️ Software Heritage

El repositorio principal excede el límite de 4 GiB de Software Heritage debido a la evidencia audiovisual que permaneció versionada en su historial. Para resolverlo, se archivó un **repositorio espejo** (`MediCita_ISR401-archive`), idéntico al contenido de este repositorio pero sin `02_Evidencias/00_Restringido/*.7z*`.

**Identificador obtenido:** `swh:1:dir:6fbdc09760140cb9d176d33621b1262e1b9de2c2` (09/09/2026), ya incorporado en `CITATION.cff`.

---

# ⚠️ Integridad académica

Los resultados reportados corresponden únicamente a evidencia disponible y a procedimientos efectivamente realizados.

- No se reporta SUS si no fue aplicado.
- No se convierten criterios de aceptación en resultados experimentales.
- No se atribuyen pruebas técnicas posteriores a los participantes.
- No se presentan las correcciones del prototipo como una nueva validación humana.
- No se inventan DOI, SWHID, observaciones, participantes ni resultados.
- La validación humana y la verificación técnica del MVP se reportan de forma separada.

---

# 📚 Cómo citar el proyecto

Ver `CITATION.cff`. Identificadores persistentes: OSF `10.17605/OSF.IO/DTYNC` · Zenodo `10.5281/zenodo.22236373`.

---

# 🎓 Defensa Final

Materiales en `09_Defensa/`. Estructura de la exposición: problema y contribuciones → sistema y stakeholders → metodología del componente empírico → resultados → discusión y amenazas a la validez → conclusiones y trabajo futuro → demostración del prototipo.

Los resultados utilizados durante la defensa deben coincidir con los datos procesados en `07_Datos/` y con el manuscrito final.

---

<div align="center">

## Universidad Técnica Estatal de Quevedo

### Facultad de Ciencias de la Computación
### Carrera de Ingeniería de Software

**Proyecto Fin de Curso — Ingeniería de Requerimientos (ISR-401)**

# SICM / MediCita

⭐ Repositorio elaborado con fines académicos.

</div>
