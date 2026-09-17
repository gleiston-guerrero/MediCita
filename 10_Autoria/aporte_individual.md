<div align="center">

# 👤 A10 — Aporte Individual por Integrante

### Proyecto MediCita (SICM) — ISR-401

![Estado](https://img.shields.io/badge/Estado-Completo-success?style=for-the-badge)
![Fuente](https://img.shields.io/badge/Fuente-git_log_%2B_bitácora_A1-informational?style=for-the-badge)
![Actualizado](https://img.shields.io/badge/Actualizado-17/09/2026_(cierre_definitivo)-blue?style=for-the-badge)

</div>

---

## 📌 Metodología

Este documento se construyó cruzando dos fuentes verificables:
1. **Conteo de commits** por integrante (`git shortlog -sne HEAD` sobre un clon completo, con `.mailmap` aplicado).
2. **Bitácora de sesiones** (`10_Autoria/bitacora_sesiones.csv`), que registra en qué días participó cada quien y qué se decidió/hizo ese día, con base en los mensajes reales de commit.

## ⚠️ Alcance de los 28 días registrados

Los 28 días de la bitácora **cubren la totalidad del historial del repositorio hasta el 14/09/2026**: desde el primer commit (21/07/2026), incluyendo la ronda final de correcciones previa a la defensa (09–14/09/2026: reparación del fragmento de evidencia, RNF-21/22, matriz de trazabilidad, LOPDP, doble observación, corrección de `script.js`, actualización de guion/PPT/folleto, corrección de URL del repositorio, recompilación del ERS y regeneración del manifiesto de checksums). No es una muestra — es cada día distinto en el que hubo al menos un commit, sin excepciones. La bitácora no incluye aún el trabajo de cierre del examen suspenso (15/09/2026: reproducibilidad del paquete de datos, inventario EXIF, cálculo de potencia en el manuscrito y esta actualización), reflejado en el conteo total de commits de la tabla siguiente pero todavía no desglosado día a día.

## ⚠️ Importante: "días de participación" no equivale a "volumen de trabajo"

La tabla de días cuenta en cuántas fechas distintas aparece cada integrante, **no cuántos commits hizo**. Esto puede ser engañoso: por ejemplo, el 31/08/2026 concentró **597 commits en un solo día**, con los 5 integrantes participando. El indicador principal de aporte individual es el conteo total de commits (tabla siguiente), no la cantidad de días.

## ✅ Conteo total de commits — confirmado con clon completo (`git shortlog -sne HEAD`)

| Integrante | Commits totales | % del total (1.818) |
|---|---:|---:|
| Paul Alexander Tigasi Sampedro | 375 | 20,63 % |
| Thais Melanie Herrera Ramos | 373 | 20,52 % |
| Jamileth Estefanía Gamarra Zárate | 369 | 20,30 % |
| Mayummy Jailly Trujillo Vega | 361 | 19,86 % |
| Steven Santiago Díaz Pontón | 340 | 18,70 % |
| **Total** | **1.818** | **100 %** |

El reparto se mantiene parejo entre los cinco integrantes (18,70 % a 20,63 %). Recontado el 17/09/2026 sobre `git shortlog -sne HEAD` sobre un clon completo, con `.mailmap` aplicado, sobre el commit `6a464a6a83bb3e7338303eeb38689102c8442f88` (`origin/main`, verificado), con el manifiesto raíz (`checksums.sha256`) regenerado sobre ese mismo commit. Esta cifra es correcta a partir de ese commit; si el repositorio recibe commits nuevos después, deja de ser el total vigente — no se declara aquí como "recuento final" para no repetir el error de `[4.3.6]`, donde esa palabra quedó falsa en cuanto se subió el siguiente cierre correctivo.

## 🔍 Comparación con la vista "Contributors" de GitHub

GitHub ofrece una vista gráfica de commits por integrante en la pestaña "Insights → Contributors" del repositorio. Sus números, al 09/09/2026, no coincidían exactamente con el conteo de `git shortlog` de esa fecha. Esta comparación no se repitió en la actualización del 12/09/2026: la fuente oficial de este documento sigue siendo `git shortlog` sobre un clon completo, no la vista de GitHub, por lo que la tabla de abajo queda como referencia histórica del comportamiento de esa discrepancia, no como una cifra vigente.

| Integrante | GitHub (Insights) | `git shortlog` (clon completo) | Diferencia |
|---|---:|---:|---:|
| Paul Alexander Tigasi Sampedro | 292 | 298 | +6 |
| Thais Melanie Herrera Ramos | 277 | 289 | +12 |
| Steven Santiago Díaz Pontón | 278 | 285 | +7 |
| Mayummy Jailly Trujillo Vega | 278 | 279 | +1 |
| Jamileth Estefanía Gamarra Zárate | 277 | 278 | +1 |
| **Total** | **1.402** | **1.429** | **+27** |

### Por qué existe esta diferencia

1. **GitHub no aplica el `.mailmap` de la misma forma que Git.** El salto más grande (+12 en Thais) corresponde a los 8 commits de la identidad genérica `MediCita Team` que el `.mailmap` atribuye a Thais Melanie Herrera Ramos. `git shortlog` respeta ese archivo automáticamente; la vista de Contributors de GitHub sigue mostrando esa identidad por separado (visible como "Melanie-G23" sin fusionar en algunas capturas), y no refleja la atribución completa.
2. **La vista de GitHub tiene retraso de caché.** Es una analítica que se recalcula periódicamente, no en tiempo real. El resto de la diferencia (+14 repartidos entre los demás integrantes) corresponde a actividad de los días más recientes (07-08/09/2026) que la caché de GitHub todavía no reflejaba al momento de la captura.

### Cuál se usa como fuente oficial en este documento

El conteo de **`git shortlog -sne HEAD` sobre un clon completo (1.778)**, por ser una lectura directa del historial real de Git, sin intermediarios ni caché, y por aplicar correctamente el `.mailmap` ya adoptado por el equipo.

---

## 📊 Resumen cuantitativo secundario (días de participación)

| Integrante | Días con participación registrada (bitácora A1) |
|---|---:|
| Paul Alexander Tigasi Sampedro | 23 de 28 |
| Jamileth Estefanía Gamarra Zárate | 20 de 28 |
| Thais Melanie Herrera Ramos | 20 de 28 |
| Mayummy Jailly Trujillo Vega | 18 de 28 |
| Steven Santiago Díaz Pontón | 16 de 28 |

---

## 📝 Detalle cualitativo por integrante

### Paul Alexander Tigasi Sampedro (líder de equipo)

**Participación:** 23 de los 28 días registrados en la bitácora — la más alta del equipo.

**Aporte narrativo:** Carga inicial de fotografías del entorno; organización de la estructura de `02_Evidencias`; consolidación del ERS 2A; creación de guías de verificación de codificación temática y transcripciones; participó en la jornada de anonimización del 31/08; lideró la corrección final del repositorio en la Entrega 4 (2B): migración de evidencia audiovisual a GitHub Release, renombrado de scripts, construcción de `07_Datos/`, eliminación de `PE5_U5`, `.mailmap`, documentación de `10_Autoria/`, y la corrección final del manuscrito y del guion/presentación de defensa (07/09); en el cierre final (11-12/09) corrigió el ERS/SRS (sección de alcance del componente de IA, RNF-21 y RNF-22) y reparó dos fragmentos de código incompletos en `05_MVP/script.js` que impedían que la demostración interactiva respondiera; en la ronda de cierre de A8 (12-13/09) depositó la correspondencia institucional real en `10_Autoria/correspondencia/`, coordinó la recuperación de evidencia fotográfica fechada de 5 de las 7 sesiones de elicitación, e indicó el pixelado del rostro de cada persona entrevistada conservando visible solo al integrante del equipo que condujo la entrevista.

**Commits que lo acreditan:** ver columna `commits_producidos` de `bitacora_sesiones.csv`, filas 2026-07-21 a 2026-09-07 donde aparece `ptigasis-Alexander`.

---

### Steven Santiago Díaz Pontón

**Participación:** 16 de 28 días.

**Aporte narrativo:** Carga y organización de fotografías de entorno; creación de mockups de interfaz; trabajo en la práctica independiente PE5 (Unidad V); participó en la jornada de anonimización del 31/08; corrección de rutas de diagramas UML y renombrado de fotos con metadatos EXIF (04/09); registro de datos de Member Checking (06/09); corrección final del manuscrito y del guion de defensa (07/09); renombrado uniforme de los índices de carpeta a `Readme.md` (08/09); en el cierre final (09-12/09) actualizó el estado de Software Heritage y su SWHID, corrigió `run_all.py`, agregó el resumen del perfil agregado de participantes al README de datos, y actualizó el guion, el PPT y el folleto de defensa; completó el contenido de `resultados_.md` (antes vacío), y creó los README de las carpetas de tablas y figuras de publicación; corrigió `power_calculation_justificacion.md` para aclarar que el cálculo de potencia no forma parte del contenido prerregistrado en OSF, evitando una atribución no respaldada por la evidencia del prerregistro.

**Commits que lo acreditan:** ver `bitacora_sesiones.csv`, filas donde aparece `DIAZ PONTON STEVEN`.

---

### Jamileth Estefanía Gamarra Zárate

**Participación:** 20 de 28 días.

**Aporte narrativo:** Organización de fotos de entorno; limpieza de transcripciones duplicadas; incorporación de ORCID de los 5 integrantes en `CITATION.cff`; reorganización estructural de `02_Evidencias`; creación de mockups; trabajo en práctica PE5; participó en la jornada de anonimización; corrección de rutas de diagramas y fotos (04/09); actualización de `02_Evidencias`, `00_Restringido` y `Capturas` (05/09) — incluye la corrección del número de oficio (059→069) y la sesión de facilitación del Member Checking; aclaración de roles de participantes en la validación walkthrough (07/09); renombrado uniforme de índices a `Readme.md` (08/09); en el cierre final (09-12/09) agregó la columna de duración a `ficha_observacion.csv`, corrigió el formato y las filas de `diccionario_datos.csv` y de la matriz de trazabilidad, y renombró `Readme.md` a `README_datos.md` en el paquete de datos; dividió `run_all.py` en las etapas `leer_datos.py` y `procesar_datos.py` según lo exigido por el ítem A4, y completó el contenido de varios `README.md` vacíos de `03_Modelado/Diagramas_UML_Corregidos/` (casos de uso, secuencias).

**Commits que lo acreditan:** ver `bitacora_sesiones.csv`, filas donde aparece `Jami1405`.

---

### Thais Melanie Herrera Ramos

**Participación:** 20 de 28 días *(incluye los 8 commits atribuidos vía `.mailmap` desde la identidad `MediCita Team`, del 18-19/08)*.

**Aporte narrativo:** Limpieza de transcripciones y actualización de `CITATION.cff`; reorganización de `02_Evidencias`; creación de mockups; trabajo en las dos prácticas independientes PE5 (18-21/08); participó en la jornada de anonimización del 31/08; actualización de documentación (05/09); registro y facilitación de la sesión de Member Checking (06/09); corrección final del manuscrito y del guion de defensa (07/09); renombrado uniforme de índices a `Readme.md` (08/09); en el cierre final (09-12/09) documentó el resultado de la doble codificación (`resultado_kappa.md`), actualizó el estado de Software Heritage, registró la hoja de observación independiente de las sesiones VAL-MG/VAL-ENF, y documentó la separación entre la capa pública y la restringida de los datos; completó la división del script de análisis (`run_all.py` como coordinador y `generar_resultados.py`) exigida por el ítem A4; agregó las 16 filas reales que faltaban en `ficha_observacion.csv` (sesiones VAL-PSI y VAL-PAC02) y creó `generar_procesados.py`, cerrando el hueco por el cual la cadena de análisis no arrancaba realmente desde el dato crudo.

**Commits que lo acreditan:** ver `bitacora_sesiones.csv`, filas donde aparece `Thais Melanie Herrera Ramos`.

**Nota de atribución:** incluye 8 commits (18-19/08/2026) originalmente registrados bajo la identidad genérica `MediCita Team <team@medicita.local>` sobre la carpeta de práctica `PE5_U5_PFC_DIAZ_TIGASI_VERA/` (ya eliminada del repositorio), atribuidos mediante `.mailmap` el 03/09/2026.

---

### Mayummy Jailly Trujillo Vega

**Participación:** 18 de 28 días.

**Aporte narrativo:** Organización de fotos de entorno; reorganización de `02_Evidencias`; creación de mockups; trabajo en la práctica PE5 (Unidad V); participó en la jornada de anonimización del 31/08; actualización de documentación (05/09); registro de datos de Member Checking (06/09); renombrado uniforme de índices a `Readme.md` (08/09); en el cierre final (09-12/09) corrigió el video de verificación previa, actualizó el CHANGELOG y el estado del proyecto a completo, agregó el perfil agregado de participantes y el resultado de la doble observación independiente, y actualizó el video final de la defensa; documentó el proceso de revisión asistida por IA en `prompts_LLm_.md` (antes vacío) y creó el `Readme.md` de `scripts_analisis/` y el `README.md` de `Mockups_Prototipo_Final/`; ajustó `leer_datos.py` para que invoque la transformación real desde el dato crudo.

**Commits que lo acreditan:** ver `bitacora_sesiones.csv`, filas donde aparece `mtrujillov-sys`.

---

## 🔍 Nota metodológica

El reparto de participación por días es razonablemente parejo entre los cinco integrantes (16 a 23 de 28 días), consistente con lo ya señalado en el informe individual del docente: *"El reparto de confirmaciones en la ventana es notablemente parejo entre los cinco integrantes."* Paul Alexander Tigasi Sampedro, como líder de equipo, presenta la mayor participación por haber coordinado directamente la corrección final del repositorio en la Entrega 4 (2B), el cierre final previo a la defensa, y el cierre del examen suspenso del 15/09/2026.

---

## ✍️ Firma de los integrantes


| Integrante | Firma | Fecha |
|---|---|---|
| Paul Alexander Tigasi Sampedro | Tigasi Sampedro | 12/09/2026 10:33 |
| Steven Santiago Díaz Pontón |Steven Diaz | 12/09/2026 10:45 |
| Jamileth Estefanía Gamarra Zárate | Jamileth Gamarra | 12/09/2026 10:34 |
| Thais Melanie Herrera Ramos | Herrera Thais | 12/09/2026 10:28 |
| Mayummy Jailly Trujillo Vega | Trujillo Mayummy | 12/09/2026 10:31 |
