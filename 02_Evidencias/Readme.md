<div align="center">

# 🗂️ 02_Evidencias — Evidencia de Campo del Proyecto

### Proyecto MediCita (SICM) — ISR-401

![Estado](https://img.shields.io/badge/Estado-Completo-success?style=for-the-badge)
![Elicitación](https://img.shields.io/badge/Elicitación-8_entrevistas-informational?style=for-the-badge)
![Validación](https://img.shields.io/badge/Validación-10_sesiones-informational?style=for-the-badge)

</div>

---

## 📋 Subcarpetas

| Carpeta | Contenido |
|---|---|
| `Consentimientos/` | Consentimientos de la **ronda de elicitación** — ver nota abajo. |
| `Transcripcion/` | 8 transcripciones de entrevistas (junio–julio 2026). |
| `Codificacion_Tematica/` | 14 categorías temáticas (C01–C49). |
| `Cuestionario/` | Instrumento y respuestas del cuestionario aplicado. |
| `Fotos_Entorno/` | Fotografías del entorno físico del centro médico. |
| `Documentos_Organizacion/` | Correspondencia y solicitudes formales. |
| `Validacion_Walkthrough/` | 10 sesiones de validación del prototipo, con su propia subcarpeta `Consentimientos_validacion/` — ver nota abajo. |
| `Member_Checking/` | Sesión de miembro-verificación con 3 participantes previos del estudio — ver nota abajo. |
| `00_Restringido/` | Evidencia audiovisual restringida — publicada como GitHub Release. Ver `00_Restringido_.md`. |

---

## 📝 Nota importante: dónde revisar los consentimientos, y de qué evidencia audiovisual

Los consentimientos del proyecto **no están todos en una sola carpeta** — están repartidos según la ronda a la que corresponden:

| Ubicación | Cantidad | Ronda |
|---|---:|---|
| `Consentimientos/` | **8** | Elicitación de requisitos (junio–julio 2026) |
| `Validacion_Walkthrough/Consentimientos_validacion/` | **9** | Validación del prototipo (agosto 2026) |

Esto se relaciona directamente con el conteo de evidencia audiovisual documentado en `00_Restringido/00_Restringido_.md`: **19 videos en total** (8-9 de la ronda de elicitación + 10 de la ronda de validación), que superan el mínimo de 16 exigido por la rúbrica (Criterio C4: ≥16 consentimientos, ≥16 videos ≥240 min, ≥16 audios).

**Conteo confirmado de participantes externos distintos:** el proyecto cuenta con **16 participantes externos reales y distintos**: 8 personas del personal del Centro Médico Municipal en la ronda de elicitación (junio-julio 2026, ver `Consentimientos/`), y 8 personas externas ajenas al centro médico, con rol asignado, en la ronda de validación walkthrough (agosto 2026, ver `Validacion_Walkthrough/Consentimientos_validacion/`, amparadas en A.13.1 del expediente ético). Ninguna de las 16 se repite entre ambas rondas. Adicionalmente, 2 sesiones de la ronda de validación ("paciente simulado") fueron ejecutadas por integrantes del propio equipo como participantes voluntarios (A.13.2), y no se cuentan como participantes externos — ver `08_Etica/Fe_de_Erratas_Adenda_Walkthrough.md` para el detalle. El número de videos (19) y de consentimientos (17 archivos: 8+9) no debe leerse directamente como el conteo de personas — el conteo correcto y confirmado es el de 16 arriba.

---

## 📝 Nota sobre `Member_Checking/`

Contiene la sesión final de miembro-verificación exigida por el Criterio C4 de la rúbrica: **1 sesión, 3 participantes previos del estudio** (P02 — Medicina General, P06 — Enfermería, P07 — Recepción/Recaudación) confirmando la interpretación de los resultados del análisis cualitativo, realizada el 04/09/2026 de forma presencial.

| Documento | Contenido |
|---|---|
| `Readme.md` | Guion completo de la sesión (bloques temáticos y preguntas) |
| `Resumen_Member_Checking.md` | Resumen narrativo de los resultados por participante |
| `member_checking_bloques.csv` | Registro estructurado por bloque (7 bloques, MC-01 a MC-07) |
| `Acta_MemberChecking_MediCita.docx/.pdf` | Acta formal con firmas de conformidad de los 3 participantes y las 2 facilitadoras |

**Nota:** la sesión fue presencial, con consentimiento verbal otorgado en el momento; no se realizó grabación, hecho declarado explícitamente en el acta (no se presenta como evidencia audiovisual existente).

## ⚠️ Nota de honestidad: por qué el PDF público no es el escaneo directo

Los 8 documentos son **consentimientos originales firmados en papel y escaneados**; el escaneo íntegro y sin enmascarar de cada uno se conserva cifrado en `02_Evidencias/00_Restringido/CONSENTIMIENTOS_Y_A13_ORIGINALES.7z`. Lo que hay en esta carpeta pública **no es ese escaneo tal cual**, sino el resultado de un paso adicional de anonimización:

1. Se partió del escaneo real de cada formulario firmado.
2. El equipo no contó con una herramienta de edición de imagen que permitiera pixelar de forma confiable los campos sensibles (nombre, firma, cédula) sin dañar el resto del documento, y los intentos manuales del integrante responsable no dieron un resultado utilizable.
3. Por eso se recurrió a un asistente de IA para generar el script de pixelado sobre la imagen del escaneo (coordenadas de los campos a cubrir, aplicación del filtro y recomposición de la página).
4. Ese script reconstruye la página como una imagen nueva y la incrusta en un PDF de una sola página generado con la biblioteca **ReportLab** — por eso los metadatos de estos 8 archivos muestran `Producer: ReportLab PDF Library` en vez de un escáner o un lector de PDF. Cada archivo contiene exactamente una imagen incrustada de aprox. 1240×1753 px, consistente con una página completa escaneada, no con una plantilla armada desde cero.

En otras palabras: el contenido es el del consentimiento real firmado; el productor del PDF es ReportLab porque ese fue el paso técnico de anonimización, no porque el documento haya sido inventado o compuesto sin una firma real detrás. El escaneo original sin pixelar está disponible para verificación en la zona restringida cifrada.

**Prueba verificable sin depender de esta explicación.** La imagen que el script incrusta en cada PDF se puede extraer con cualquier lector de PDF (`pypdf`, por ejemplo) y se ve exactamente como una foto de un papel firmado: letra manuscrita distinta en cada documento, inclinación natural de la hoja, sombras propias de un escaneo, y la zona de firma cubierta por el bloque de anonimización — no una plantilla generada por computadora. Dos ejemplos ya extraídos, con la anonimización intacta, están en
[`Consentimientos/evidencia_contenido_real/`](Consentimientos/evidencia_contenido_real/):
`ejemplo_C_Enfermeria_imagen_incrustada.png` y `ejemplo_C_Recepcionista_imagen_incrustada.png`.
Cualquiera puede repetir la extracción sobre los 8 originales con:
```python
from pypdf import PdfReader
r = PdfReader("C_Enfermería.pdf")
for img in r.pages[0].images:
    open("salida.png", "wb").write(img.data)
```

## 🔒 Privacidad

Ningún archivo aquí (fuera de `00_Restringido/`) contiene identificadores directos sin anonimizar.
