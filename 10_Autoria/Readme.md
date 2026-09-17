<div align="center">

# 🧾 10_Autoria — Evidencia de Autoría y Trabajo Propio

### Proyecto MediCita (SICM) — ISR-401

![Progreso](https://img.shields.io/badge/Progreso-12_de_12_completos-success?style=for-the-badge)
![Criterio](https://img.shields.io/badge/Criterio_de_piso-P7-success?style=for-the-badge)
![Actualizado](https://img.shields.io/badge/Actualizado-17/09/2026-informational?style=for-the-badge)

</div>

---

## 📌 Sobre este índice

Índice del estado real de cada elemento exigido por la Sección 6 de
la Guía de Desarrollo del 02/09/2026. **Ningún elemento marcado como
pendiente contiene contenido inventado.**

**Cierre del examen suspenso (15/09/2026):** ver
[`retrospectiva_equipo.md`](retrospectiva_equipo.md) para el detalle de
qué hizo cada integrante y qué se corrigió en esta ronda de cierre.

---

## 📋 Estado por elemento

| Cód. | Elemento | Estado | Notas |
|---|---|:---:|---|
| A1 | [`bitacora_sesiones.csv`](bitacora_sesiones.csv) | 🟢 Completo | 46 filas: 28 días de trabajo interno del equipo (derivadas de commits, hasta el 14/09/2026) + 18 sesiones de campo con participante externo (8 entrevistas + 10 walkthroughs), cada una con columna `tipo` y enlace directo en `ruta_nota_campo` a su nota manuscrita en A5. |
| A2 | [`Capturas/`](Capturas/Readme.md) | 🟢 Completo | 15 capturas subidas; los 5 integrantes con mínimo 3 cada uno. |
| A3 | [`fuentes_editables/README.md`](fuentes_editables/README.md) | 🟢 Completo | 117 de 117 fuentes (.drawio/.puml) referenciadas 1 a 1 con la imagen que generan; se mantienen en `03_Modelado/` para no duplicar contenido. |
| A4 | [`grabaciones/`](grabaciones/grabaciones.md) | 🟢 Completo | 2 de 2 grabaciones mínimas. |
| A5 | [`notas_campo/`](notas_campo/notas_campo.md) | 🟢 Completo | 18 de 18 sesiones: 8 de elicitación (P01–P08) y 10 de la ronda de validación por walkthrough (V01–V10) — ver detalle en el propio archivo. |
| A6 | [`Fotos_equipos/`](Fotos_equipos/Fotos_equipos.md) | 🟢 Completo | 3 fotos con EXIF real verificado, 2 integrantes identificables. |
| A7 | [`doble_codificacion/`](doble_codificacion/) | 🟢 Completo | 38 segmentos codificados por 2 integrantes independientes. **Kappa = 0,6997 (acuerdo sustancial)**, IC 95% [0,5255–0,8739]. Resultado generado por script (`resultado_kappa.md`). |
| — | [`doble_observacion_sesiones/`](doble_observacion_sesiones/) | 🟢 Completo | Requisito adicional de la Sección 5 de la Guía de Desarrollo: doble observación independiente de 2 de 8 sesiones de validación (25%, sobre el mínimo del 20%). Kappa = -0,0714 (sin acuerdo por desbalance de categorías, explicado en detalle en `resultado_kappa_observacion.md`); acuerdo bruto real 70%. No sustituye a A7 — es un elemento distinto, sobre sesiones de validación, no sobre codificación temática de transcripciones. |
| A8 | [`correspondencia/README.md`](correspondencia/README.md) | 🟢 Completo | Las 4 comunicaciones confirmadas y firmadas. |
| A9 | [`declaracion_uso_ia.md`](declaracion_uso_ia.md) | 🟢 Completo | Firmado por los 5 integrantes (03-05/09/2026). |
| A10 | [`aporte_individual.md`](aporte_individual.md) | 🟢 Completo | Conteo real de commits (1.822 totales, sobre el commit `6db08a192c1946d4af5561f08c23f64caa77cb10`) y detalle cualitativo por integrante, basado en la bitácora A1. |
| A11 | [`exif_inventario.csv`](exif_inventario.csv) | 🟢 Completo | 34 de 34 elementos del expediente (29 fotografías y 5 capturas de pantalla), distribuidos en Fotos_Entorno, Fotos_Aplicacion, Fotos_equipos y correspondencia/evidencia_entrevista, con EXIF real, inferido por contexto, o marcado explícitamente `SIN_EXIF` cuando no aplica (p. ej. capturas de pantalla o fotos sin metadato tras compartirse por WhatsApp). |
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

Fuente: `git shortlog -sne HEAD` sobre un clon completo (historial íntegro, filtro `blob:none`), con `.mailmap` ya aplicado. Recontado el 17/09/2026 sobre el commit `6db08a192c1946d4af5561f08c23f64caa77cb10` (`origin/main`, verificado) — el último commit antes de crear la etiqueta `cierre-examen-suspenso-20260917f`, cifra vigente a partir de ese commit, no una declaración de cierre absoluto.

| Integrante | Commits | % del total |
|---|---:|---:|
| Paul Alexander Tigasi Sampedro | 375 | 20,58 % |
| Thais Melanie Herrera Ramos | 373 | 20,47 % |
| Jamileth Estefanía Gamarra Zárate | 370 | 20,31 % |
| Mayummy Jailly Trujillo Vega | 364 | 19,98 % |
| Steven Santiago Díaz Pontón | 340 | 18,66 % |
| **Total** | **1.822** | **100 %** |

El reparto es notablemente parejo entre los cinco integrantes (18,66 % a 20,58 %).
