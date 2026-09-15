<div align="center">

# 🧾 10_Autoria — Evidencia de Autoría y Trabajo Propio

### Proyecto MediCita (SICM) — ISR-401

![Progreso](https://img.shields.io/badge/Progreso-11_de_12_completos-yellow?style=for-the-badge)
![Criterio](https://img.shields.io/badge/Criterio_de_piso-P7-success?style=for-the-badge)
![Actualizado](https://img.shields.io/badge/Actualizado-15/09/2026-informational?style=for-the-badge)

</div>

---

## 📌 Sobre este índice

Índice del estado real de cada elemento exigido por la Sección 6 de
la Guía de Desarrollo del 02/09/2026. **Ningún elemento marcado como
pendiente contiene contenido inventado.**

---

## 📋 Estado por elemento

| Cód. | Elemento | Estado | Notas |
|---|---|:---:|---|
| A1 | [`bitacora_sesiones.csv`](bitacora_sesiones.csv) | 🟢 Completo | 27 días con sus campos completos y actualizados, hasta el 14/09/2026 inclusive. |
| A2 | [`Capturas/`](Capturas/Readme.md) | 🟢 Completo | 15 capturas subidas; los 5 integrantes con mínimo 3 cada uno. |
| A3 | [`fuentes_editables/README.md`](fuentes_editables/README.md) | 🟢 Completo | 117 de 117 fuentes (.drawio/.puml) referenciadas 1 a 1 con la imagen que generan; se mantienen en `03_Modelado/` para no duplicar contenido. |
| A4 | [`grabaciones/`](grabaciones/grabaciones.md) | 🟢 Completo | 2 de 2 grabaciones mínimas. |
| A5 | [`notas_campo/`](notas_campo/notas_campo.md) | 🟡 Parcial | 8 de 8 de elicitación completo; 0 de 10 de la ronda de validación (walkthrough) — ver detalle en el propio archivo. |
| A6 | [`Fotos_equipos/`](Fotos_equipos/Fotos_equipos.md) | 🟢 Completo | 3 fotos con EXIF real verificado, 2 integrantes identificables. |
| A7 | [`doble_codificacion/`](doble_codificacion/) | 🟢 Completo | 38 segmentos codificados por 2 integrantes independientes. **Kappa = 0,6997 (acuerdo sustancial)**, IC 95% [0,5255–0,8739]. Resultado generado por script (`resultado_kappa.md`). |
| — | [`doble_observacion_sesiones/`](doble_observacion_sesiones/) | 🟢 Completo | Requisito adicional de la Sección 5 de la Guía de Desarrollo: doble observación independiente de 2 de 8 sesiones de validación (25%, sobre el mínimo del 20%). Kappa = -0,0714 (sin acuerdo por desbalance de categorías, explicado en detalle en `resultado_kappa_observacion.md`); acuerdo bruto real 70%. No sustituye a A7 — es un elemento distinto, sobre sesiones de validación, no sobre codificación temática de transcripciones. |
| A8 | [`correspondencia/README.md`](correspondencia/README.md) | 🟢 Completo | Las 4 comunicaciones confirmadas y firmadas. |
| A9 | [`declaracion_uso_ia.md`](declaracion_uso_ia.md) | 🟢 Completo | Firmado por los 5 integrantes (03-05/09/2026). |
| A10 | [`aporte_individual.md`](aporte_individual.md) | 🟢 Completo | Conteo real de commits (1.656 totales) y detalle cualitativo por integrante, basado en la bitácora A1. |
| A11 | [`exif_inventario.csv`](exif_inventario.csv) | 🟢 Completo | Fotos con EXIF real, inferido por contexto, o marcado explícitamente sin dato. |
| A12 | `.mailmap` | 🟢 Completo | Atribuye los 8 commits de `MediCita Team` a Thais Melanie Herrera Ramos. |

**Leyenda:** 🟢 Completo · 🟡 En progreso · 🔴 Pendiente/vacío

---

## 📄 Verificación previa (Sección 11 de la guía)

| Documento | Estado |
|---|:---:|
| [`verificacion_previa.docx`](verificacion_previa.pdf) |  🟢 Firmada — 12 de 12 comprobaciones técnicas ya en SÍ. |

---

## 📊 Resultado de la doble codificación (A7)

| Indicador | Valor |
|---|---:|
| Segmentos codificados | 38 |
| Cohen's Kappa | 0,6997 |
| Intervalo de confianza 95% | [0,5255 – 0,8739] |
| Interpretación (Landis & Koch, 1977) | Sustancial |

---

## 📊 Dato de referencia para A10 — commits reales por integrante

Fuente: `git shortlog -sne HEAD` sobre un clon completo (historial íntegro, filtro `blob:none`), con `.mailmap` ya aplicado. **Confirmado y definitivo.**

| Integrante | Commits | % del total |
|---|---:|---:|
| Thais Melanie Herrera Ramos | 338 | 20,41 % |
| Paul Alexander Tigasi Sampedro | 337 | 20,35 % |
| Steven Santiago Díaz Pontón | 331 | 19,99 % |
| Jamileth Estefanía Gamarra Zárate | 327 | 19,75 % |
| Mayummy Jailly Trujillo Vega | 323 | 19,50 % |
| **Total** | **1.656** | **100 %** |

El reparto es notablemente parejo entre los cinco integrantes (19,50 % a 20,41 %).
