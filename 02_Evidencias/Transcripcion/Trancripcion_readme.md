<div align="center">

# 🔍 Guía de Verificación — Carpeta Transcripcion

### Sistema de Gestión Inteligente para un Centro Médico (SICM)

**Proyecto Fin de Curso (PFC) – Ingeniería de Requisitos**

<br>

![Universidad](https://img.shields.io/badge/Universidad-UTEQ-003366?style=for-the-badge)
![Carpeta](https://img.shields.io/badge/Carpeta-02__Evidencias%2FTranscripcion-00509d?style=for-the-badge)
![Tipo](https://img.shields.io/badge/Tipo-Checklist_de_Verificacion-2e7d32?style=for-the-badge)
![Uso](https://img.shields.io/badge/Uso-Revision_Manual_o_IA-orange?style=for-the-badge)

</div>

---

## 🎯 Propósito de este documento

Guía paso a paso para confirmar que las **transcripciones de las entrevistas** de elicitación de requisitos están completas, bien nombradas, anonimizadas y sin errores de codificación antes de la entrega. Pensada para que la siga un revisor humano o un asistente de IA.

---

## 📁 Contenido esperado

Un archivo `.txt` por participante entrevistado, más un `README.md` que explique el propósito de la carpeta:

| Código | Área / Rol entrevistado |
|:---:|---|
| P01 | Psicología |
| P02 | Medicina General |
| P03 | Terapia Física |
| P04 | Nutrición |
| P05 | Odontología / Coordinación |
| P06 | Enfermería |
| P07 | Recepción / Recaudación |
| P08 | Paciente |

```
02_Evidencias/Transcripcion/
├── README.md
├── AAAA_MM_DD_P01_Psicologia.txt
├── AAAA_MM_DD_P02_Medicina_General.txt
├── AAAA_MM_DD_P03_Terapia_Fisica.txt
├── AAAA_MM_DD_P04_Nutricion.txt
├── AAAA_MM_DD_P05_Odontologia.txt
├── AAAA_MM_DD_P06_Enfermeria.txt
├── AAAA_MM_DD_P07_Recepcion_Recaudacion.txt
└── AAAA_MM_DD_P08_Paciente.txt
```

> [!IMPORTANT]
> Estos archivos son la versión **pública y anonimizada** de las entrevistas — sin nombres reales, cédulas ni datos de contacto. La grabación original (audio/video) con identidad visible va cifrada aparte, en `00_Restringido/`, nunca aquí.

---

## 🧪 Pasos de verificación

### Paso 1 — Confirmar que estén los 8 participantes, ni uno de más ni de menos

```bash
cd 02_Evidencias/Transcripcion
ls *.txt | wc -l
```

Debe devolver **8**. Si hay menos, falta alguna entrevista; si hay más, puede haber un duplicado o un participante fuera del codebook de arriba.

### Paso 2 — Confirmar que el patrón de nombre sea consistente

Todos los archivos deben seguir el mismo formato `AAAA_MM_DD_PXX_Area.txt`, con **guiones bajos**, sin espacios.

```bash
ls *.txt | grep " "
```

Cualquier resultado aquí es un nombre con espacio suelto (rompe el patrón y puede causar problemas al referenciarlo desde otros documentos). Corrígelo con:

```bash
mv "nombre con espacios.txt" "Nombre_Sin_Espacios.txt"
```

### Paso 3 — Confirmar que todos los códigos de participante (P01–P08) estén presentes y sin repetir

```bash
grep -oE "P0[1-8]" <(ls *.txt) | sort -u
```

Debe imprimir `P01` a `P08`, cada uno una sola vez.

### Paso 4 — Revisar la codificación de caracteres (acentos y símbolos)

```bash
file *.txt
```

> [!WARNING]
> Si `file` marca un archivo como **"Non-ISO extended-ASCII"** en vez de "UTF-8", significa que tildes y "ñ" se van a ver rotos (ej. `Ã³` en vez de `ó`) al abrirlo en GitHub o en un editor que espere UTF-8. Conviértelo así:
> ```bash
> iconv -f WINDOWS-1252 -t UTF-8 archivo.txt -o archivo_utf8.txt && mv archivo_utf8.txt archivo.txt
> ```
> En Windows: abre el archivo en VS Code → esquina inferior derecha → clic en la codificación → **"Save with Encoding"** → **UTF-8**.

### Paso 5 — Confirmar que estén realmente anonimizados

```bash
grep -Ei "cedula|c[eé]dula|[0-9]{10}|tel[eé]fono|whatsapp" *.txt
```

Este comando busca posibles rastros de cédula (10 dígitos), teléfono o referencias directas a datos de contacto. **No debería devolver nada.** Si aparece algo, hay que redactar/quitar ese fragmento del texto antes de dejarlo público. (Nota: esto es una búsqueda de apoyo, no reemplaza una revisión manual línea por línea.)

### Paso 6 — Confirmar que el README de la carpeta tenga contenido real

```bash
wc -c README.md
```

Debe ser mayor a unos pocos bytes y explicar: qué son estos archivos, cómo se recolectaron (entrevista + grabación), y que la versión con identidad visible está resguardada en `00_Restringido/`.

---

## ✅ Checklist de Aprobación

- [✅] Hay exactamente 8 archivos `.txt`, uno por cada código P01–P08
- [✅] Ningún nombre de archivo tiene espacios sueltos ni dobles espacios
- [✅] Los 8 códigos de participante están presentes, sin duplicados ni faltantes
- [✅] Todos los `.txt` están guardados en UTF-8 (sin símbolos rotos tipo `Ã³`)
- [✅] Ningún archivo contiene cédulas, teléfonos u otros datos de contacto sin redactar
- [✅] Existe un `README.md` con contenido real explicando el propósito de la carpeta
- [✅] Los nombres de archivo siguen el mismo patrón `AAAA_MM_DD_PXX_Area.txt` en los 8 casos

---

## 🤖 Instrucción para revisión por IA

> "Clona `https://github.com/gleiston-guerrero/MediCita_ISR401`, entra a `02_Evidencias/Transcripcion/`, y sigue los Pasos 1 a 6 de `Guia_Verificacion_Transcripcion.md`. Confírmame si están los 8 participantes (P01 a P08), si algún nombre de archivo tiene espacios sueltos, si hay problemas de codificación UTF-8, si algún archivo contiene datos personales sin anonimizar (cédula, teléfono), y si el README de la carpeta tiene contenido real."

---

<div align="center">

## Universidad Técnica Estatal de Quevedo

### Facultad de Ciencias de la Computación

### Carrera de Ingeniería de Software

### Proyecto Fin de Curso

**Sistema de Gestión Inteligente para un Centro Médico (SICM)**

---

⭐ **Documento elaborado con fines exclusivamente académicos.**

</div>
