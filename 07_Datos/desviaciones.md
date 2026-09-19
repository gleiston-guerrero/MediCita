<div align="center">

# 📝 Registro de Desviaciones — 07_Datos

### Proyecto MediCita (SICM) — ISR-401

![Estado](https://img.shields.io/badge/Estado-Documentado-success?style=for-the-badge)
![Fuente](https://img.shields.io/badge/Fuente-OSF_10.17605%2FOSF.IO%2FDTYNC-informational?style=for-the-badge)

</div>

---

## 📌 Sobre este documento

El registro completo de desviaciones respecto del prerregistro OSF (DOI 10.17605/OSF.IO/DTYNC) ya existe en `06_Experimento/osf_deviations.pdf` y se referencia aquí en vez de duplicarlo, para mantener una sola fuente de verdad.

---

## 📋 Resumen de las desviaciones documentadas

### 1. Composición de los participantes de la segunda ronda

| | Prerregistrado | Ejecutado |
|---|---|---|
| **Participantes** | Las mismas 8 personas de la etapa de levantamiento, repitiendo sesión | 8 personas **externas distintas**, ajenas al centro médico, con rol asignado (A.13.1), ninguna coincide con las 8 de elicitación |
| **Sesiones** | 1 por participante = 8 | 10 (incluyen 2 sesiones adicionales de "paciente simulado" por integrantes del equipo, A.13.2) |
| **Estado al momento del prerregistro** | 0 de 8 sesiones ejecutadas | — |

Esta es una desviación real respecto del diseño prerregistrado: el plan original suponía la **misma cohorte** de 8 personas evaluando el prototipo en una segunda sesión, pero en la ejecución real se recurrió a un **grupo de participantes externos distinto y nuevo** (ver `08_Etica/Fe_de_Erratas_Adenda_Walkthrough.md` para el detalle completo y el conteo confirmado de 16 participantes externos totales).

### 2. Tratamiento declarado

Las sesiones adicionales respecto del plan original se reportan como desviaciones de ejecución. El documento es explícito en que estas sesiones adicionales **no se reinterpretan como participantes independientes** cuando corresponden a actividades complementarias o simuladas — mismo criterio aplicado en la Fe de Erratas para las sesiones 07 y 10, donde integrantes del equipo ejecutaron el rol de "paciente".

### 3. Regla vigente sobre datos faltantes

No fabricar ni imputar respuestas u observaciones inexistentes.

### 4. Confirmaciones puntuales de horario con el personal del centro médico

| | Documentado por escrito | Ejecutado |
|---|---|---|
| **Respaldo institucional (acceso al centro)** | Sí — solicitud, avales y oficio de respaldo, ver `10_Autoria/correspondencia/` | Completo, 4 de 4 documentos |
| **Coordinación previa de horario por sesión** | No | Se coordinó de forma verbal o telefónica directamente con el personal de cada área |
| **Evidencia de la fecha y hora reales de cada sesión** | Parcial — recuperada de fotografías con marca de tiempo, ver `10_Autoria/correspondencia/evidencia_entrevista/` | 5 de 7 sesiones de elicitación con evidencia fotográfica fechada |

El acceso institucional al centro médico está respaldado documentalmente en su totalidad (ver `10_Autoria/correspondencia/`). La coordinación previa de fecha y hora de cada sesión individual se manejó de palabra con el personal de cada área, sin dejar correo, mensaje ni nota firmada — esa parte de la desviación se mantiene.

Sin embargo, sí se recuperó evidencia fotográfica con marca de tiempo del dispositivo que registra cuándo ocurrió efectivamente cada sesión (no la coordinación previa, sino el momento real de ejecución):

| Fecha | Hora | Entrevista | Evidencia |
|---|---|---|---|
| 04/06/2026 | 09:34 | Nutrición | `evidencia_entrevista/2026-06-04_nutricion.png` |
| 04/06/2026 | 09:53 | Psicología | `evidencia_entrevista/2026-06-04_psicologia.png` |
| 04/06/2026 | 10:16 | Coordinación / Odontología (mismo cargo, misma persona) | `evidencia_entrevista/2026-06-04_coordinacion-odontologia.png` |
| 17/07/2026 | 13:21 | Recepción | `evidencia_entrevista/2026-07-17_recepcion.png` |
| 17/07/2026 | 13:35 | Enfermería | `evidencia_entrevista/2026-07-17_enfermeria.png` |

Las fotografías fueron pixeladas en el rostro de la persona entrevistada, conservando visible únicamente al integrante del equipo que condujo la entrevista, siguiendo el mismo criterio de anonimización ya aplicado en los consentimientos y demás evidencia visual del proyecto.

Dos sesiones de la primera ronda no cuentan con evidencia fotográfica recuperable — se perdió con el tiempo por limpieza de espacio de almacenamiento en los dispositivos del equipo. El equipo recuerda la hora aproximada de ambas, pero no puede respaldarla con una fotografía fechada:

| Fecha (aproximada, según memoria del equipo) | Hora aproximada | Entrevista | Evidencia fotográfica |
|---|---|---|---|
| 04/06/2026 | ~10:30 | Fisioterapia | No disponible — se perdió con el tiempo |
| 05/06/2026 | ~10:00 | Medicina General | No disponible — se perdió con el tiempo |

Estas dos sesiones sí están respaldadas por otros medios ya existentes en el repositorio (transcripciones, actas firmadas, videos de la entrevista), solo falta la fotografía puntual con marca de hora. Esta pérdida parcial se declara explícitamente en vez de reconstruirse o inventarse.

Se declara esta desviación explícitamente, siguiendo el mismo criterio de la sección 1: no se fabrica ni se reconstruye retroactivamente un registro que no existió o que ya no está disponible.
---

## 📄 Documento fuente completo

Ver `06_Experimento/osf_deviations.pdf` para el detalle completo, incluida la tabla de aspecto prerregistrado / estado / tratamiento.

---

## 5. Alteración indebida del número de oficio referenciado en el aval A3 (revertido 19/09/2026)

| | Original (firmado 04/09/2026, texto impreso fecha 20/08/2026) | Alterado (commit `087de51`, 05/09/2026) | Estado actual (19/09/2026) |
|---|---|---|---|
| Documento | `08_Etica/Categoria_A/CategoriaA_A3_Aval_Establecimiento.pdf`, punto 2 | mismo documento | revertido al original |
| Número de oficio referenciado | DGDS-059-2026 (escrito a mano en el original) | DGDS-069-2026 (imagen de 51×30 px pegada sobre el escaneo) | DGDS-059-2026 (restaurado) |

**Qué pasó:** el aval A3 fue firmado y sellado el 04/09/2026 (misma fecha y hora del sello — 10:12 a.m. — que el oficio de respaldo institucional, ambos firmados en la misma sesión con el coordinador de DGDS), y en su punto 2 hace referencia al oficio **DGDS-059-2026**, escrito a mano en el espacio en blanco del formato. El commit `087de51` (05/09/2026, autor `jgamarraz@uteq.edu.ec`) modificó el PDF pegando una imagen de 51×30 píxeles sobre ese número, cambiándolo a **DGDS-069-2026**.

**Verificación contra el documento físico (19/09/2026):** el equipo confirmó, contra el papel original en su poder, que el número escrito a mano por la organización es efectivamente **059**, no 069. El cambio a 069 no proviene de ningún documento físico ni de una corrección de la organización — fue una edición digital hecha por el equipo, pensando (de buena fe, pero de forma indebida) que ambos documentos debían coincidir en el número.

**Por qué fue un error:** editar el escaneo de un documento ya firmado para cambiar su contenido —aunque sea un solo número— altera un documento oficial sin autorización de quien lo firmó. Si el equipo considera que el aval A3 debería referenciar el oficio 069, la vía correcta es solicitar a la organización (DGDS) una fe de erratas o corrección firmada por ellos — nunca editar el documento ya firmado, ni en papel ni digitalmente.

**Corrección aplicada el 19/09/2026:** se restauró `CategoriaA_A3_Aval_Establecimiento.pdf` a la versión del commit `23fae6d` (anterior a la alteración), que contiene el escaneo original firmado con DGDS-059-2026, verificado además contra el documento físico. No se modificó el documento de ninguna otra forma.

**Commit de la reversión:** `0aad461`
