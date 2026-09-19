# Registro de correcciones — G1 (parte 1)

Este archivo registra, para cada corrección aplicada sobre la **versión actual** del repositorio (G1, parte 1 del plan de mejora de datos del 19/09/2026), qué cambió, por qué, con qué evidencia y en qué commit. La parte 2 de G1 (limpieza del historial) no está incluida aquí: requiere autorización escrita del docente y se documenta aparte cuando corresponda.

Regla seguida: cada corrección es un commit independiente; ningún dato personal se creó ni se estimó — donde no se pudo verificar un dato exacto (por ejemplo coordenadas GPS ya eliminadas), simplemente se retiró.

---

## 1. Nombre y edad de P08 en notas de campo

- **Archivo:** `10_Autoria/notas_campo/2026-07-22_P08_paciente_notas-campo.pdf`
- **Qué contenía:** el PDF es una sola página con una imagen JPEG escaneada (sin capa de texto — verificado con `pdftotext` y `pdfimages -list`, cero caracteres extraíbles). En la imagen, la línea "Participantes:" incluye el nombre completo y la edad exacta de P08.
- **Corrección:** se cubrió con un rectángulo opaco (no un recuadro superpuesto en un editor de PDF — el PDF se regeneró reemplazando el flujo JPEG embebido dentro del mismo objeto `/Im1`, mismas dimensiones 1019×1543, misma página A4) el nombre y la edad, con margen adicional para cubrir descendentes de letra (ej. la "p" de "Sampedro"). Se verificó pixel por pixel que no quedan trazos visibles en los bordes de la máscara, y que `pdftotext` sigue devolviendo cero texto extraíble tras la regeneración (no hay capa de texto que pudiera "seguir debajo").
- **Evidencia:** verificación visual antes/después + `pdfinfo`/`pdfimages -list`/`pdftotext` antes y después, ejecutados el 19/09/2026.
- **Original sin enmascarar:** no se sube al repositorio público; debe conservarse únicamente en el contenedor restringido cifrado del equipo.
- **Commit:** `<pendiente-de-commit-1>`

## 2. Ubicación GPS de 7 fotografías

- **Archivos:**
  - `02_Evidencias/Fotos_Entorno/Entrada al centro médico.jpg`
  - `02_Evidencias/Fotos_Entorno/Espacio de espera.jpg`
  - `02_Evidencias/Fotos_Entorno/Exterior del centro médico(entrada).jpg`
  - `02_Evidencias/Fotos_Entorno/Sala de espera.jpg`
  - `10_Autoria/Fotos_equipos/2026_09_04_Area_Recepción(Recaudación).jpg`
  - `10_Autoria/Fotos_equipos/2026_09_04_Facha_Establecimiento.jpg`
  - `10_Autoria/Fotos_equipos/2026_09_04_Pasillo_Entrda(principal).jpg`
- **Qué contenían:** bloque EXIF `GPSInfo` completo (latitud, longitud, altitud, marca de tiempo GPS) — verificado con Pillow antes de la corrección.
- **Corrección:** se eliminó únicamente el IFD GPS con `piexif` (`exif_dict["GPS"] = {}`, re-serializado y reinsertado en el JPEG). Se conservaron `DateTimeOriginal`/`DateTime`, `Make` y `Model`, que son la evidencia declarada en el inventario EXIF. Verificado de forma independiente con Pillow (`_getexif()`) tras la corrección: GPS ausente, fecha y modelo intactos, dimensiones de imagen sin cambios.
- **Nota técnica:** en las 3 fotos Xiaomi, `piexif.dump` fallaba por un tag EXIF no esencial malformado (tag 41729, `SceneCaptureType`, valor `0` mal tipado — defecto conocido del firmware de cámara, no relacionado con GPS/fecha/modelo); se descartó únicamente ese tag para poder reserializar. No afecta ningún dato usado como evidencia.
- **Commit:** `<pendiente-de-commit-2>`

## 3. Fachada del establecimiento: rótulo institucional visible

- **Archivos:**
  - `10_Autoria/Fotos_equipos/2026_09_04_Facha_Establecimiento.jpg`
  - `10_Autoria/Fotos_equipos/verificacion_automatica/2026_09_04_Facha_Establecimiento.jpg_DETECCION.jpg` (derivada de detección de rostros)
- **Qué contenía:** además del GPS (corrección #2), la fotografía muestra de frente el rótulo institucional completo (escudo + texto "...GESTIÓN.../...SOCIAL") sobre la fachada.
- **Corrección:** se optó por **tapar el rótulo** (no retirar la foto), para conservar la evidencia de visita presencial del equipo (2 integrantes identificables, ver `Fotos_equipos.md`) que exige el criterio de aceptación de G1/10_Autoria. Se cubrió con un rectángulo opaco la franja completa del rótulo (escudo + texto), verificado visualmente que no quedan letras ni el escudo visibles y que los rostros de los integrantes (y las cajas verdes de detección en la derivada) quedan intactos.
- **Pendiente de decisión del equipo:** confirmar que "tapar" (no "retirar") es la opción preferida; si prefieren retirar la foto en su lugar, avisar antes de aplicar este commit.
- **Nota adicional (fuera de alcance de G1, para su conocimiento):** la placa del motociclista al fondo es parcialmente legible; el correo de G1 no pide actuar sobre esto, se deja constancia por si el equipo quiere revisarlo aparte.
- **Commit:** `<pendiente-de-commit-2>` (mismo commit que el resto de fotos GPS, ver arriba)

## 4. Inventario EXIF actualizado

- **Archivo:** `10_Autoria/exif_inventario.csv`
- **Corrección:** se actualizó `hash_sha256` de las 7 filas correspondientes a las fotos corregidas (arriba) con el hash del archivo ya sin GPS, y se anotó en `estado_y_metodo` la fecha y el método de eliminación del GPS (y, para la fachada, que también se cubrió el rótulo).
- **Commit:** `<pendiente-de-commit-2>`

## 5. Nombre de la organización

- **Archivos corregidos** (todo lo encontrado con `git grep -niE "Quevedo|DGDS|Gestión de Desarrollo Social|GAD Municipal|Centro Médico Municipal"`, **excluyendo** toda mención de "Universidad Técnica Estatal de Quevedo (UTEQ)", que es la propia universidad del equipo y no requiere seudónimo):
  - `README.md` (línea 124)
  - `08_Etica/Readme.md` (insignia)
  - `01_ERS/ERS_SRS_2A_V1.0.tex`, `01_ERS/ERS_SRS_2B_V2.0.tex` (tabla de codificación, 2 menciones cada uno)
  - `02_Evidencias/Documentos_Organizacion/Readme.md`
  - `02_Evidencias/Readme.md`
  - `07_Datos/registro_deposito.md`
  - `08_Etica/Fe_de_Erratas_Adenda_Walkthrough.md`
  - `10_Autoria/Fotos_equipos/Fotos_equipos.md` (4 menciones)
  - `10_Autoria/correspondencia/README.md` (insignia + 4 menciones en la tabla de correspondencia — se mantuvieron los nombres propios de las personas firmantes, que G1 no pide anonimizar, solo el nombre de la organización)
- **Corrección:** se sustituyó cada mención por el seudónimo **"Centro Médico Municipal Piloto"** (decidido por el equipo el 19/09/2026; en insignias shields.io, `Centro_Medico_Municipal_Piloto`, sin espacios/acentos por restricción del formato de badge).
- **NO se tocó** (fuera del alcance explícito de G1 — requiere decisión aparte del equipo, marcado aquí para que no se pierda):
  - El nombre de archivo `Oficio_Respaldo_Institucional_DGDS.pdf` (referenciado en `08_Etica/Readme.md:60` y `10_Autoria/correspondencia/README.md:24`) sigue conteniendo "DGDS". Renombrar el archivo físico afecta enlaces y (potencialmente) el aval firmado por la organización — G2 dice explícitamente que "cualquier corrección del aval la firma la organización", así que no se renombró sin decisión del equipo/docente.
  - `CHANGELOG.md:527`: el código de oficio `(DGDS-069-2026)` identifica el documento físico real; cambiarlo podría romper la trazabilidad al oficio original. Se deja para decisión explícita.
- **Commit:** `<pendiente-de-commit-3>` (después de que el equipo fije el seudónimo)

## 6. CSV público del cuestionario: edad exacta → rangos

- **Archivo:** `02_Evidencias/Cuestionario/Respuestas/Resultado_Cuestionario_IR_SGICM.csv`
- **Qué contenía:** edad exacta y servicio detallado (incluida psicología) de 66 personas.
- **Corrección:** el CSV público ahora se **genera con un script** (`02_Evidencias/Cuestionario/Respuestas/scripts/generar_csv_publico.py`), no se edita a mano. El script:
  - Convierte `Edad` a rango: `14-17`, `18-24`, `25-34`, `35-44`, `45+`.
  - Agrupa la columna de servicio en solo dos categorías (`Medicina General` / `Otro servicio o combinación`), porque al cruzar rango de edad × servicio detallado quedaban combinaciones de una sola persona (ej. 45+ × Odontología = 1); el criterio del correo de G1 exige agrupar también el servicio en ese caso.
  - Verifica automáticamente, antes de escribir el archivo, que ninguna combinación (rango_edad, servicio) tenga un solo caso; si la hubiera, el script se detiene sin publicar nada.
  - Corrige además una inconsistencia de formato ya presente en el crudo (ENC-41 tenía `"19 años"` en vez de `19` en la columna Edad) extrayendo el número — no se inventó ni se estimó ningún valor.
- **Distribución resultante (todas las celdas ≥ 2, verificado):**

  | Rango edad | Medicina General | Otro servicio o combinación |
  |---|---:|---:|
  | 14-17 | 2 | 5 |
  | 18-24 | 13 | 15 |
  | 25-34 | 15 | 3 |
  | 35-44 | 6 | 2 |
  | 45+ | 3 | 2 |

- **PENDIENTE — acción del equipo (no puedo hacerla yo):** el crudo con la edad exacta debe salir del repositorio público y vivir solo en el contenedor restringido cifrado. En `02_Evidencias/00_Restringido/` ya existe `Resultado_Cuestionario_IR_SGICM_restringido.7z` (protegido con contraseña que no tengo). El equipo debe:
  1. Verificar/actualizar ese `.7z` para que contenga el crudo con la edad exacta (dejé una copia de referencia en `repo-limpieza-work/PARA_CONTENEDOR_RESTRINGIDO_NO_SUBIR/Resultado_Cuestionario_IR_SGICM_crudo_edad_exacta.csv` — **no subir esa carpeta al repo**).
  2. Guardar esa misma ruta (o una copia) fuera del repo, y usarla como `--crudo` al correr el script cada vez que haga falta regenerar el CSV público.
- **Commit:** `<pendiente-de-commit-4>`

## 7. Manifiestos

- Tras aplicar los commits anteriores, correr desde la raíz del repo:
  ```bash
  sh generar_checksums.sh
  git add checksums.sha256
  git commit -m "chore(datos): regenerar checksums.sha256 tras correcciones G1 parte 1"
  ```
- **Commit:** `<pendiente-de-commit-5>`
