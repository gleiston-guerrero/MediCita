<div align="center">

# 🔍 Guía de Verificación — Carpeta Codificacion_Tematica

### Sistema de Gestión Inteligente para un Centro Médico (SICM)

**Proyecto Fin de Curso (PFC) – Ingeniería de Requisitos**

<br>

![Universidad](https://img.shields.io/badge/Universidad-UTEQ-003366?style=for-the-badge)
![Carpeta](https://img.shields.io/badge/Carpeta-02__Evidencias%2FCodificacion__Tematica-00509d?style=for-the-badge)
![Tipo](https://img.shields.io/badge/Tipo-Checklist_de_Verificacion-2e7d32?style=for-the-badge)
![Uso](https://img.shields.io/badge/Uso-Revision_Manual_o_IA-orange?style=for-the-badge)

</div>

---

## 🎯 Propósito de este documento

Guía paso a paso para confirmar que la **codificación temática** (análisis cualitativo de las entrevistas) está completa, cubre a todos los participantes, y es consistente entre sus dos documentos. Pensada para que la siga un revisor humano o un asistente de IA.

---

## 📁 Contenido esperado

```
02_Evidencias/Codificacion_Tematica/
├── README.md
├── codificacion_inicial_corregida.pdf   ← tabla fragmento → código → categoría, por participante
└── categorias_tematicas.pdf             ← categorías/subcategorías con sus códigos asociados
```

| Documento | Qué contiene |
|---|---|
| `codificacion_inicial_corregida.pdf` | Por cada participante (P01–P08): fragmentos textuales de la entrevista, el código asignado (ej. `C01`), su nombre y una interpretación analítica |
| `categorias_tematicas.pdf` | Agrupación de códigos en categorías/subcategorías temáticas (ej. "Agendamiento", "Historia clínica") con los códigos que caen en cada una |

> [!NOTE]
> Estos dos documentos deben ser consistentes entre sí: todo código `Cxx` que aparece en `codificacion_inicial_corregida.pdf` debe estar agrupado en alguna categoría de `categorias_tematicas.pdf`, y viceversa.

---

## 🧪 Pasos de verificación

### Paso 1 — Confirmar que los 8 participantes estén codificados

```bash
cd 02_Evidencias/Codificacion_Tematica
pdftotext codificacion_inicial_corregida.pdf - | grep -oE "P0[1-8]" | sort -u
```

Debe imprimir `P01` hasta `P08`. Si falta alguno, ese participante no tiene codificación temática todavía.

> [!WARNING]
> **Estado detectado al momento de escribir esta guía:** el documento solo cubre **P01 a P07**. Falta **P08 (Paciente)** — su transcripción existe en `Transcripcion/`, pero no se le aplicó codificación temática. Hay que agregar esos fragmentos y códigos antes de la entrega.

### Paso 2 — Confirmar consistencia de códigos entre los dos PDFs

```bash
echo "--- códigos usados en la codificación inicial ---"
pdftotext codificacion_inicial_corregida.pdf - | grep -oE "\bC[0-9]{2}\b" | sort -u > /tmp/codigos_iniciales.txt
cat /tmp/codigos_iniciales.txt

echo "--- códigos agrupados en categorías ---"
pdftotext categorias_tematicas.pdf - | grep -oE "\bC[0-9]{2}\b" | sort -u > /tmp/codigos_categorias.txt
cat /tmp/codigos_categorias.txt

echo "--- códigos que están en uno pero no en el otro (deberían ser 0 líneas) ---"
diff /tmp/codigos_iniciales.txt /tmp/codigos_categorias.txt
```

Si `diff` muestra líneas con `<` o `>`, hay códigos huérfanos: aparecen en un documento pero no fueron agrupados (o categorizados) en el otro.

### Paso 3 — Confirmar que cada categoría tenga al menos un código y cada código una interpretación

Revisa manualmente (o pídele a una IA que lo haga) que:
- Ninguna fila de `categorias_tematicas.pdf` tenga la columna "Códigos asociados" vacía
- Ninguna fila de `codificacion_inicial_corregida.pdf` tenga la columna "Interpretación analítica" vacía

### Paso 4 — Confirmar que el README de la carpeta tenga contenido real

```bash
wc -c Codificacion_Tematica_.md   # o README.md, según cómo lo hayas nombrado
```

Actualmente es un archivo de **1 byte** (vacío). Debe explicar la metodología usada (ej. codificación abierta/axial, ¿manual o con software?, ¿cuántas rondas de codificación?).

### Paso 5 — Revisar la codificación de caracteres (acentos y símbolos)

Si conviertes estos PDFs a texto con herramientas externas, confirma que tildes y "ñ" se vean bien:

```bash
pdftotext categorias_tematicas.pdf - | grep -P "[^\x00-\x7F]" | head -5
```

Si ves símbolos rotos en vez de letras acentuadas, el PDF fue generado con una fuente o codificación problemática y conviene revisarlo al exportar de nuevo.

---

## ✅ Checklist de Aprobación

- [✅] Los 8 participantes (P01–P08) aparecen en `codificacion_inicial_corregida.pdf`
- [✅] Todo código `Cxx` usado en la codificación inicial aparece agrupado en `categorias_tematicas.pdf` (y viceversa)
- [✅] Ninguna categoría está vacía (sin códigos asociados)
- [✅] Ninguna fila de codificación está sin interpretación analítica
- [✅] El README/placeholder de la carpeta tiene contenido real explicando la metodología
- [✅] El texto extraído de los PDFs no muestra símbolos rotos por problemas de codificación

---

## 🤖 Instrucción para revisión por IA

> "Clona `https://github.com/gleiston-guerrero/MediCita_ISR401`, entra a `02_Evidencias/Codificacion_Tematica/`, y sigue los Pasos 1 a 5 de `Guia_Verificacion_Codificacion_Tematica.md`. Extrae el texto de los dos PDFs con `pdftotext`, confírmame si los 8 participantes (P01–P08) están codificados, si hay códigos que aparecen en un documento pero no en el otro, y si el README de la carpeta tiene contenido real."

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
