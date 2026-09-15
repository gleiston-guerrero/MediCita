<div align="center">

# 🔁 retrospectiva_equipo.md — Cierre del Examen Suspenso

### Proyecto MediCita (SICM) — ISR-401

![Estado](https://img.shields.io/badge/Estado-Completo-success?style=for-the-badge)
![Fuente](https://img.shields.io/badge/Fuente-git_log_%2B_commits_reales-informational?style=for-the-badge)
![Actualizado](https://img.shields.io/badge/Actualizado-15/09/2026-blue?style=for-the-badge)

</div>

---

## 📌 Sobre este documento

Cubre el trabajo realizado desde el lunes 2026-09-14 hasta el cierre del
examen suspenso, en respuesta directa a la Guía de cierre y rúbrica del
examen suspenso emitida el 15/09/2026. El detalle por integrante se
construyó cruzando el historial real de commits (`git log`) con los
cambios efectivamente aplicados al repositorio.

---

## 👥 Qué hicimos, por integrante

| Integrante | Usuario | Qué hizo |
|---|---|---|
| **Mayummy Jailly Trujillo Vega** | `mtrujillov-sys` | Reforzó la descripción del método de la V de Cramér en los resultados y en el JSON de salida; documentó el proceso de anonimización en el README; actualizó los enlaces del repositorio tras el cambio de cuenta de GitHub; actualizó la bitácora de sesiones y las estadísticas de participación. |
| **Steven Santiago Díaz Pontón** | `DIAZ PONTON STEVEN` | Creó el README de `fuentes_editables/`; aclaró la visibilidad de los integrantes del equipo en las fotografías de evaluación; corrigió enlaces del repositorio en `CHANGELOG.md` y en varios README. |
| **Thais Melanie Herrera Ramos** | `Melanie-G23` | Revisó la entrada A3 del README con detalles de fuente actualizados; implementó `detectar_rostros.py` y la sección de verificación objetiva por detección de rostros sobre las fotos del equipo; agregó el intervalo de confianza a `resumen_descriptivo.csv`. |
| **Jamileth Estefanía Gamarra Zárate** | `Jami1405` | Depositó las 10 notas de campo manuscritas escaneadas de las sesiones de validación por walkthrough (`V01` a `V10`, 2026-08-28/30) en `10_Autoria/notas_campo/`; actualizó `checksums_datos.sha256`; retiró la versión obsoleta del ERS (`ERS_SRS_2A_v1.0.pdf`). |
| **Paul Alexander Tigasis Sampedro** (líder de equipo) | `ptigasis-Alexander` | Corrigió las rutas del manifiesto `checksums_datos.sha256`; actualizó los enlaces de la demo y del prototipo público en el README; coordinó el cierre de los pendientes de la guía del examen suspenso: reproducibilidad del paquete de datos (§12), cobertura de RF Must y cálculo de potencia en el manuscrito (§16), y esta retrospectiva. |

---

## 🛠️ Qué corregimos puntualmente en el cierre

**Reproducibilidad del paquete de datos (§12).** `resumen_descriptivo.csv` había sido reformateado a mano (de punto y coma con BOM, la salida real del script, a comas sin BOM) el 2026-09-15 a las 00:21, lo que rompía la verificación `sha256sum -c checksums_datos.sha256 --quiet` aunque los valores numéricos fueran correctos. Se regeneró el archivo ejecutando la orden única (`python 07_Datos/scripts/generar_paquete_datos.py`) y se actualizó el manifiesto para que coincida con la salida real del pipeline.

**Cobertura de RF Must y cálculo de potencia (§16).** Se incorporó al manuscrito el cálculo de potencia a priori (Cohen's *d* = 0,5, α = 0,05, potencia = 0,80, *n* = 128) como referencia de diseño frente a las diez sesiones de validación disponibles, y se reforzó la sección de amenazas a la validez con esa comparación explícita. El manuscrito se recompiló desde el `.tex` versionado.

---

## 💡 Qué aprendimos

- Un archivo puede tener el valor correcto y aun así fallar la verificación de integridad: reformatear a mano una salida generada por script (aunque sea solo el separador o la codificación) rompe la reproducibilidad byte a byte que el propio repositorio declara. La lección para el resto del proyecto es no tocar a mano ningún archivo bajo `resultados/` o `datos_procesados/`: si el formato necesita cambiar, el cambio va en el script generador, no en la salida.
- Reportar un resultado (como la cobertura de RF Must) no basta si el cálculo que lo acompaña —en este caso, la potencia estadística— se queda solo en el archivo de datos y no llega al manuscrito: el evaluador lee el informe, no el JSON.
- Cerrar entregables de a uno, verificando con el comando exacto de la guía antes de pasar al siguiente, evitó reabrir trabajo ya dado por terminado.
