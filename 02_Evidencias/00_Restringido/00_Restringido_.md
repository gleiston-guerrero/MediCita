<div align="center">

# 🔐 00_Restringido — Evidencia Audiovisual Restringida

### Proyecto MediCita (SICM) — ISR-401

![Acceso](https://img.shields.io/badge/Acceso-Restringido-red?style=for-the-badge)
![Videos](https://img.shields.io/badge/Videos-19_(MG--01_a_MG--20)-informational?style=for-the-badge)
![Audios](https://img.shields.io/badge/Audios-18_(PS--01_a_PS--18)-informational?style=for-the-badge)
![Verificado](https://img.shields.io/badge/Integridad-Verificada-success?style=for-the-badge)

</div>

---

## ⚠️ Cómo clonar este repositorio correctamente

Este repositorio contiene un historial de commits extenso. Para clonarlo de forma rápida y liviana (~366 MB), use un clon superficial:

```bash
git clone --depth 1 https://github.com/gleiston-guerrero/MediCita_ISR401.git
```

Un `git clone` normal (sin `--depth 1`) descargará el historial completo de versiones, incluyendo evidencia audiovisual ya migrada a GitHub Releases, lo que puede superar 14 GB.

## 🎬 Dónde está la evidencia audiovisual

Los archivos `.7z` de video/audio se movieron a un GitHub Release para reducir el peso de clonado:

**https://github.com/gleiston-guerrero/MediCita_ISR401/releases/tag/evidencia-restringida-v1**

El movimiento no modificó el contenido de los archivos: los hashes SHA-256 declarados en `fichas_tecnicas.csv` corresponden exactamente a los archivos publicados en ese Release.

---

## 👥 Dónde revisar los consentimientos correspondientes a estos videos

Los consentimientos **no están en esta carpeta** (aquí solo hay evidencia audiovisual y su ficha técnica). Están repartidos en dos ubicaciones de `02_Evidencias/`, según la ronda:

| Ubicación | Cantidad | Ronda | Corresponde a |
|---|---:|---|---|
| `02_Evidencias/Consentimientos/` | 8 | Elicitación (jun-jul 2026) | Videos MG-01 a MG-10 (sin MG-09) |
| `02_Evidencias/Validacion_Walkthrough/Consentimientos_validacion/` | 9 | Validación (ago 2026) | Videos MG-11 a MG-20 |

**Nota metodológica:** el número de videos (19) supera el mínimo de 16 exigido en cantidad de archivos, pero **no debe leerse automáticamente como 17-19 participantes distintos** — varias sesiones de validación fueron ejecutadas por integrantes del propio equipo actuando roles. Ver `08_Etica/Fe_de_Erratas_Adenda_Walkthrough.md` para el detalle verificado de cuáles.

---

## 📋 Notas de verificación de evidencia

### Nota 1 — MG-05 y MG-06

**✅ RESUELTO.**

| Archivo | Duración |
|---|---:|
| MG-05 | 00:05:36 |
| MG-06 | 00:06:16 |
| **Total** | **00:11:52** |

La duración de MG-05 fue verificada directamente contra el archivo de video original. El hash es único y no duplica el correspondiente a MG-06.

El audio PS-04 tiene una duración de 00:12:52. Existe una diferencia de aproximadamente un minuto entre el corte del audio y los cortes de video correspondientes a la misma sesión. La diferencia fue verificada y documentada por el equipo.

### Nota 2 — MG-13 y MG-17

**✅ RESUELTO.**

| Archivo | Resolución | FPS | Bitrate |
|---|---|---:|---:|
| MG-13 | 4K (3840×2160) | 29,98 | 94.394 kbps |
| MG-17 | 1080p | 29,52 | 19.984 kbps |

Los tamaños registrados son coherentes con la duración y el bitrate de las grabaciones.

---

## 📊 Resumen general

| Indicador | Valor |
|---|---:|
| Audios registrados | 18 |
| Duración total de audio | 242,85 min |
| Videos registrados | 19 |
| Duración total de video | 241:51 |
| Códigos de video | MG-01 a MG-20 (sin MG-09) |

## 🔒 Acceso

Sujeto a las condiciones éticas descritas en `08_Etica/`.
