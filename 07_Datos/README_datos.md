<div align="center">

# 📦 07_Datos — Paquete de Datos del Componente Empírico

### Proyecto MediCita (SICM) — ISR-401

![Estado](https://img.shields.io/badge/Estado-Completo-success?style=for-the-badge)
![Reproducible](https://img.shields.io/badge/Reproducible-Sí-success?style=for-the-badge)
![Licencia](https://img.shields.io/badge/Licencia-CC_BY_4.0-informational?style=for-the-badge)

</div>

---

## 📌 Nota sobre la numeración de carpetas

`07_Datos/` coexiste con `07_Publicacion/`. El prefijo "07" de esta carpeta corresponde a la numeración exigida por la Sección 7 de la Guía de Desarrollo del 02/09/2026, independiente de la numeración secuencial 01–09 de las entregas del PFC. No hay conflicto de nombres ni de contenido entre ambas.

---

## 🔓 Capa pública vs. capa restringida

Este paquete es **capa pública anonimizada**: todo archivo de `datos_crudos/`, `datos_procesados/` y `resultados/` usa exclusivamente códigos de participante (P01–P08, PS-XX, MG-XX) y códigos de sesión (VAL-MG, ELIC-P01, etc.), nunca nombres reales, cédulas, ni datos de contacto. Ningún archivo de esta carpeta permite reidentificar a un paciente o miembro del personal por sí solo.

La **capa restringida** —grabaciones originales, consentimientos sin pixelar, y cualquier archivo que sí pueda vincularse a una identidad real— vive exclusivamente en `02_Evidencias/00_Restringido/` (cifrada en volúmenes `.7z`, publicada como GitHub Release aparte) y en `08_Etica/`. Nada de esa capa se mezcla con este paquete de datos abierto.

---

## 📋 Qué contiene

| Carpeta/archivo | Descripción |
|---|---|
| `datos_crudos/` | Exactamente como salieron del instrumento, sin ninguna edición manual. Incluye la ficha de observación y el manifiesto de transcripciones de validación con su hash SHA-256 por archivo. |
| `datos_procesados/` | Obtenido únicamente mediante los scripts versionados. Nunca editado a mano. |
| `resultados/` | Tablas y cifras finales generadas por script: cobertura de RF Must, resultados estadísticos (chi-cuadrado, prueba de permutación, V de Cramér) y cálculo de potencia con su justificación. |
| `scripts/` | Script orquestador único que reproduce todo el paquete. |
| `diccionario_datos.csv` | Descripción columna por columna de cada archivo de este paquete. |
| `checksums_datos.sha256` | Hash SHA-256 de cada archivo, para verificar integridad tras la descarga. |

---
## 👥 Perfil agregado de los participantes de validación

Para incorporar en `07_Datos/README_datos.md`, después de la sección "Qué contiene" y antes de "Cómo se generó".

---

Resumen agregado de las 8 sesiones de validación con prototipo (walkthrough), sin ningún dato que permita reidentificar a pacientes ni a personal sanitario — solo código de participante (P01–P08), área y duración.

| Área | Código participante | Duración | Fecha |
|---|---|---|---|
| Coordinación | P05 | 00:13:35 | 28/08/2026 |
| Enfermería | P06 | 00:17:18 | 28/08/2026 |
| Medicina General | P02 | 00:15:35 | 28/08/2026 |
| Nutrición | P04 | 00:14:43 | 28/08/2026 |
| Odontología | P05 | 00:08:07 | 28/08/2026 |
| Paciente (simulación) | P08 | 00:13:25 | 28/08/2026 |
| Recepción/Recaudación | P07 | 00:16:24 | 28/08/2026 |
| Terapia Física | P03 | 00:14:05 | 28/08/2026 |

**Totales:**
- 8 sesiones de validación, cubriendo 7 participantes únicos (P05 participó en dos sesiones: Coordinación y Odontología).
- Duración promedio: 00:14:09 · mínima: 00:08:07 (Odontología) · máxima: 00:17:18 (Enfermería).
- Todas las sesiones se realizaron en una sola jornada: 28/08/2026.

Tabla fuente (formato CSV, para reprocesar): [`datos_procesados/perfil_agregado_participantes.csv`](datos_procesados/perfil_agregado_participantes.csv).

## ⚙️ Cómo se generó

Todos los datos de `datos_procesados/` y `resultados/` provienen del pipeline real del proyecto, en `06_Experimento/scripts_analisis/run_all.py` (y `verificar_rf_must.js` para la verificación técnica de RF Must). Este paquete **no reimplementa** ese análisis: lo ejecuta y sincroniza sus salidas hacia esta carpeta, para que exista una única fuente de verdad.

## 🔁 Cómo se reproduce

Con Python 3 y las dependencias del proyecto instaladas (`matplotlib`, `scipy`), de cualquiera de estas dos formas (el script ubica la raíz del repositorio por su propia ubicación, no por el directorio de trabajo):

```bash
# Desde la raíz del repositorio
python 07_Datos/scripts/run_all.py

# O parado dentro de 07_Datos/
cd 07_Datos && python scripts/run_all.py
```

Esto ejecuta el pipeline real y sincroniza sus salidas hacia `07_Datos/datos_procesados/` y `07_Datos/resultados/`. Los archivos de `datos_crudos/` no se regeneran (son el punto de partida, no una salida del análisis).

## ✅ Cómo se verifica la integridad

`checksums_datos.sha256` usa rutas relativas a esta carpeta, por lo que la verificación se corre **parado dentro de `07_Datos/`**:

```bash
cd 07_Datos && sha256sum -c checksums_datos.sha256 --quiet
```

No debe imprimir nada si el paquete está íntegro.

## 📄 Licencia de los datos

Ver `LICENSE-DATA.txt` — distinta de la licencia del código del repositorio.

## 📝 Desviaciones respecto del protocolo

Ver `desviaciones.md`.

## 🔗 Identificador persistente del depósito

Ver `registro_deposito.md`.
