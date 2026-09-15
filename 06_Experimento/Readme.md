<div align="center">

# 🧪 06_Experimento — Componente Empírico Reproducible

### Proyecto MediCita (SICM) — ISR-401

![Estado](https://img.shields.io/badge/Estado-Completo-success?style=for-the-badge)
![p-valor](https://img.shields.io/badge/p--valor-0.413-informational?style=for-the-badge)
![Cobertura](https://img.shields.io/badge/RF_Must-90.91%25-blue?style=for-the-badge)

</div>

---

## 📋 Contenido

| Carpeta/archivo | Descripción |
|---|---|
| `protocolo.pdf` | Protocolo de investigación registrado. |
| `osf_registration.pdf` | Prerregistro OSF (DOI 10.17605/OSF.IO/DTYNC). |
| `osf_deviations.pdf` | Desviaciones respecto del protocolo. |
| `instrumentos/` | Reubicado a `07_Datos/datos_crudos/` con la nueva Guía de Desarrollo (ver nota en la carpeta). |
| `prompst_LLm/` | Registro de uso de IA para revisión documental. |
| `scripts_analisis/run_all.py` | Script único de análisis cuantitativo. |

## 📊 Resultados principales

χ² = 1,992095 · Permutación (100.000 réplicas, semilla 42): p = 0,413086 · V de Cramer = 0,166337 · Cobertura RF Must: 20/22 (90,91%).

## ⚙️ Cómo reproducir

```bash
python 07_Datos/scripts/run_all.py
```

## ✅ Estado

Completo y reproducible.
