<div align="center">

# 🔗 Registro de Depósito — 07_Datos

### Proyecto MediCita (SICM) — ISR-401

![Zenodo](https://img.shields.io/badge/Zenodo-Publicado-success?style=for-the-badge)
![OSF](https://img.shields.io/badge/OSF-Prerregistrado-success?style=for-the-badge)
![Software Heritage](https://img.shields.io/badge/Software_Heritage-Obtenido-success?style=for-the-badge)

</div>

---

## 📦 Depósito de replicación (Zenodo)

| Campo | Valor |
|---|---|
| **DOI** | 10.5281/zenodo.22236373 |
| **Título** | "Replication package for..." (MediCita/SICM) |
| **Licencia** | CC BY 4.0 |

## 📋 Prerregistro (OSF)

| Campo | Valor |
|---|---|
| **Identificador** | dtync |
| **DOI** | 10.17605/OSF.IO/DTYNC |
| **Fecha de registro** | 27 de agosto de 2026 |
| **Estado declarado al momento del prerregistro** | 0 de 8 sesiones de validación ejecutadas (ver `06_Experimento/osf_registration.pdf`) |

## 🗄️ Archivado permanente (Software Heritage)

| Campo | Valor |
|---|---|
| **Estado** | 🟢 Obtenido. SWHID `swh:1:dir:6fbdc09760140cb9d176d33621b1262e1b9de2c2` (09/09/2026), incorporado en `CITATION.cff`. |
| **Repositorio archivado** | `MediCita_ISR401-archive` (sin `02_Evidencias/00_Restringido/*.7z*`) |

---

## ⚠️ Nota sobre alcance: qué queda fuera de los 3 depósitos, y por qué

Ninguno de los tres depósitos anteriores (Zenodo, OSF, Software Heritage) incluye el contenido de `02_Evidencias/00_Restringido/` — la carpeta donde se conserva la evidencia audiovisual **original y sin anonimizar** (se ve el rostro y se escucha la voz real de cada persona). Publicarla en un depósito abierto sería una filtración irreversible de datos personales, por eso se excluye a propósito de los tres.

### Qué hay exactamente ahí, y de dónde sale cada pieza

| Origen | Cantidad de videos | Cantidad de audios | Fecha |
|---|---:|---:|---|
| Ronda de elicitación (8 personas reales del Centro Médico Municipal Piloto) | 9 *(Medicina General se dividió en 2 partes)* | 9 | Junio–julio 2026 |
| Ronda de validación walkthrough (8 personas externas + 2 sesiones del propio equipo) | 10 | 9 | Agosto 2026 |
| **Total** | **19** | **18** | |

Verificado directamente contra `02_Evidencias/00_Restringido/fichas_tecnicas.csv` (37 registros con identificador, archivo, código de participante, fecha, duración, códec, tamaño y hash SHA-256 cada uno).

### Verificación de que no se filtró nada

Se confirmó, mediante búsqueda directa en el contenido de los tres depósitos, que **ningún nombre de archivo de video/audio ni código de participante (MG-XX)** aparece referenciado dentro de `dataset_zenodo/`, `osf_registration.pdf` ni `osf_deviations.tex`. Lo que sí está en los tres depósitos son los datos ya derivados y anonimizados de esas sesiones (transcripciones sin nombres, observaciones codificadas, tablas estadísticas) — nunca el archivo audiovisual original.
