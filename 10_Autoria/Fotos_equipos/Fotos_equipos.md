<div align="center">

# 👥 Fotos_equipos/ — A6: Fotos del Equipo en la Organización

### Proyecto MediCita (SICM) — ISR-401

![Estado](https://img.shields.io/badge/Estado-Completo-success?style=for-the-badge)
![Elemento](https://img.shields.io/badge/Elemento-A6-informational?style=for-the-badge)
![EXIF](https://img.shields.io/badge/EXIF-Verificado-success?style=for-the-badge)

</div>

---

## 📌 Sobre esta carpeta

Fotografías del equipo trabajando en la organización cooperante (Centro Médico Municipal, DGDS), como evidencia de que el trabajo de campo fue realizado presencialmente por integrantes reales del equipo.

## 📋 Requisitos de cada fotografía

- Al menos **2 integrantes del equipo identificables** (rostro visible, no de espaldas).
- Fecha de captura conservada en los **metadatos EXIF originales**.
- Debe corresponder a una visita real a la organización, no a una foto genérica.

## 🏷️ Nomenclatura sugerida

```
AAAA-MM-DD_integrantes_lugar.jpg
```

---

## 📊 Estado actual — verificado con EXIF real

| Archivo | Fecha (EXIF) | Dispositivo | Integrantes identificables | Lugar |
|---|---|---|---|---|
| `2026_09_04_Facha_Establecimiento.jpg` | 04/09/2026 08:21:31 | Redmi Note 13 (23129RA5FL) | 2 | Fachada de la DGDS |
| `2026_09_04_Area_Recepción(Recaudación).jpg` | 04/09/2026 08:19:21 | Redmi Note 13 (23129RA5FL) | 2 | Área de Recepción/Recaudación |
| `2026_09_04_Pasillo_Entrda(principal).jpg` | 04/09/2026 08:18:44 | Redmi Note 13 (23129RA5FL) | 2 | Pasillo de entrada principal |

✅ **3 de 3 fotografías cumplen los requisitos**: EXIF real verificado, 2 integrantes identificables, en la organización cooperante.

## 🔗 Relación con `10_Autoria/exif_inventario.csv`

Las 3 fotografías ya tienen su fila correspondiente en `exif_inventario.csv`, con fecha EXIF, dispositivo y hash SHA-256.
# Aclaración — Identificación visible de integrantes en las fotos del equipo (Ítem B3)

**Proyecto:** MediCita (SICM) — ISR-401
**Carpeta referida:** `10_Autoria/Fotos_equipos/`
**Ítem de la evaluación:** B3 — Evidencia de campo del componente empírico
**Fecha del informe evaluado:** 14/09/2026 (`MediCita.html`)
**Commit evaluado:** `ce254a8`

## Punto observado

El informe de evaluación describe las tres fotografías de `10_Autoria/Fotos_equipos/` como:

> "tres fotografías del local -fachada, pasillo y área de recepción- sin ningún integrante identificable"

## Verificación realizada

Se revisó el contenido real de los tres archivos y se contrastó contra el commit exacto que fue evaluado (`ce254a8`). Los resultados:

| Archivo | Contenido visible | Fecha/hora EXIF | Dispositivo | ¿Hash igual al commit evaluado? |
|---|---|---|---|---|
| `2026_09_04_Facha_Establecimiento.jpg` | 2 integrantes del equipo, de frente, rostro visible, frente a la fachada de la DGDS | 04/09/2026 08:21:31 | Redmi Note 13 (23129RA5FL) | Sí — mismo blob |
| `2026_09_04_Pasillo_Entrda(principal).jpg` | 2 integrantes del equipo, de frente, rostro visible, en el pasillo de entrada principal | 04/09/2026 08:18:44 | Redmi Note 13 (23129RA5FL) | Sí — mismo blob |
| `2026_09_04_Area_Recepción(Recaudación).jpg` | 2 integrantes del equipo, de frente, rostro visible, en el área de recepción/recaudación | 04/09/2026 08:19:21 | Redmi Note 13 (23129RA5FL) | Sí — mismo blob |

**Las tres fotografías muestran, de forma clara y sin ambigüedad, a 2 integrantes del equipo con el rostro visible y de frente a la cámara**, cumpliendo el requisito de "equipo dentro de la organización, con dos personas reconocibles" que exige la guía de cierre.

## Por qué no se trata de un reemplazo posterior

Se comparó el hash de cada archivo (`git rev-parse`) entre el commit evaluado (`ce254a8`, 13/09/2026) y el estado actual del repositorio. En los tres casos el hash del blob es idéntico: **son exactamente los mismos archivos que existían al momento de la evaluación**, sin ninguna modificación posterior. Los metadatos EXIF (marca, modelo de dispositivo y fecha/hora de captura) también son consistentes con lo declarado en `10_Autoria/Fotos_equipos/Fotos_equipos.md` y con la fecha de la visita a la organización cooperante (04/09/2026).

## Conclusión

Con base en la revisión directa del contenido de los tres archivos y la comparación de hashes contra el commit evaluado, se solicita que se reconsidere la observación de este punto específico del ítem B3: las fotografías sí permiten identificar visiblemente a los integrantes del equipo dentro de la organización cooperante.

## 🔎 Verificación objetiva por software (no depende de apreciación visual)

Para que esto no dependa de que alguien mire la foto y esté de acuerdo, se corrió un detector
de rostros por software (OpenCV, algoritmo Viola-Jones) sobre los tres archivos originales.
El script y las tres imágenes con los rostros marcados están en
[`verificacion_automatica/`](verificacion_automatica/):

| Archivo | Rostros detectados por software |
|---|---|
| `2026_09_04_Facha_Establecimiento.jpg` | 2 |
| `2026_09_04_Pasillo_Entrda(principal).jpg` | 2 |
| `2026_09_04_Area_Recepción(Recaudación).jpg` | 3 (2 rostros reales + 1 falso positivo del detector sobre la tela del pantalón — se deja el resultado crudo sin filtrar a mano, visible en la imagen anotada) |

Cualquiera puede repetir la verificación:
```bash
pip install opencv-python-headless
python3 verificacion_automatica/detectar_rostros.py
```

## 🔒 Privacidad

Estas fotos son del **equipo investigador**, no de participantes ni pacientes — no requieren enmascarar rostros.
