<div align="center">

# 🔍 Guía de Verificación — Carpeta Cuestionario

### Sistema de Gestión Inteligente para un Centro Médico (SICM)

**Proyecto Fin de Curso (PFC) – Ingeniería de Requisitos**

<br>

![Universidad](https://img.shields.io/badge/Universidad-UTEQ-003366?style=for-the-badge)
![Carpeta](https://img.shields.io/badge/Carpeta-02__Evidencias%2FCuestionario-00509d?style=for-the-badge)
![Tipo](https://img.shields.io/badge/Tipo-Checklist_de_Verificacion-2e7d32?style=for-the-badge)
![Uso](https://img.shields.io/badge/Uso-Revision_Manual_o_IA-orange?style=for-the-badge)
</div>

---

## 🎯 Propósito de este documento

Guía paso a paso para confirmar que la evidencia del **cuestionario aplicado a usuarios y pacientes** está completa, bien organizada y sin errores antes de la entrega. Pensada para que la siga un revisor humano o un asistente de IA.

---

## 📁 Estructura esperada

Según el árbol obligatorio de la Entrega 3, `Fotos_Aplicacion/` y `Respuestas/` deben ir **dentro** de `Cuestionario/`, no como carpetas hermanas sueltas en `02_Evidencias/`:

```
02_Evidencias/
└── Cuestionario/
    ├── README.md                          ← descripción del cuestionario (quién, cuándo, cómo)
    ├── Fotos_Aplicacion/
    │   └── (fotos de la aplicación del cuestionario en campo)
    └── Respuestas/
        ├── Resultado_Cuestionario_IR_SGICM.csv   ← datos crudos exportados
        └── Respuestas_cuestionario.md            ← resumen/análisis de resultados
```

> [!WARNING]
> **Estado actual detectado:** `Fotos_Aplicacion/` y `Respuestas/` están sueltas al mismo nivel que `Cuestionario/` (como hermanas), en vez de estar anidadas dentro. Hay que moverlas. Ver Paso 1.

---

## 🧪 Pasos de verificación

### Paso 1 — Confirmar que la jerarquía de carpetas es correcta

```bash
cd 02_Evidencias
find Cuestionario -type d
```

**Debe mostrar** `Cuestionario`, `Cuestionario/Fotos_Aplicacion` y `Cuestionario/Respuestas`. Si `Fotos_Aplicacion` y `Respuestas` aparecen como carpetas separadas en la raíz de `02_Evidencias` (fuera de `Cuestionario/`), muévelas:

```bash
git mv Fotos_Aplicacion Cuestionario/Fotos_Aplicacion
git mv Respuestas Cuestionario/Respuestas
```

### Paso 2 — Confirmar que no queden placeholders vacíos

Los archivos `_.md` que sirven de "reserva de espacio" no deben quedar vacíos en la entrega final; deben tener contenido real o eliminarse.

```bash
find Cuestionario -name "*.md" -size -10c
```

Cualquier archivo que aparezca aquí (menos de 10 bytes) está vacío y necesita contenido real o debe borrarse si ya no se usa.

### Paso 3 — Confirmar que `Fotos_Aplicacion/` tenga fotos reales

```bash
find Cuestionario/Fotos_Aplicacion -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" \)
```

Debe devolver al menos una imagen. Si la carpeta solo tiene el `.md` de placeholder y ninguna imagen, faltan las fotos de evidencia de aplicación del cuestionario.

### Paso 4 — Confirmar que los datos de `Respuestas/` estén completos y coincidan

```bash
cd Cuestionario/Respuestas
wc -l Resultado_Cuestionario_IR_SGICM.csv
```

Compara el número de filas del CSV (menos 1 por el encabezado) contra el número de respuestas que declara `Respuestas_cuestionario.md` (busca un badge o texto tipo "Respuestas: N"). Deben coincidir.

```bash
grep -o "Respuestas-[0-9]*" Respuestas_cuestionario.md
```

### Paso 5 — Revisar la codificación de caracteres (acentos y emojis)

```bash
file Respuestas_cuestionario.md
```

> [!IMPORTANT]
> Se detectó que `Respuestas_cuestionario.md` **no está guardado en UTF-8** — el comando `file` lo marca como *"Non-ISO extended-ASCII"*. Esto hace que tildes, "ñ" y emojis se vean como símbolos rotos (ej. `Ã³` en vez de `ó`, `ð` en vez de un emoji 📊) al abrirlo en GitHub o en cualquier editor que espere UTF-8.

**Cómo corregirlo:**
```bash
iconv -f WINDOWS-1252 -t UTF-8 Respuestas_cuestionario.md -o Respuestas_cuestionario_utf8.md
mv Respuestas_cuestionario_utf8.md Respuestas_cuestionario.md
```
En Windows, abre el archivo en VS Code → esquina inferior derecha → clic en la codificación actual → **"Save with Encoding"** → elige **UTF-8**.

### Paso 6 — Validar que el CSV abre correctamente

```bash
python3 -c "import csv; r=list(csv.reader(open('Resultado_Cuestionario_IR_SGICM.csv', encoding='latin-1'))); print('Filas:', len(r), '| Columnas:', len(r[0]) if r else 0)"
```

Si arroja error de decodificación, el CSV también necesita conversión a UTF-8 con el mismo método del Paso 5.

---

## ✅ Checklist de Aprobación

- [✅] `Fotos_Aplicacion/` y `Respuestas/` están anidadas dentro de `Cuestionario/` (no sueltas en `02_Evidencias/`)
- [✅] Ningún `.md` de la carpeta quedó vacío (0-1 byte) sin contenido real
- [✅] `Fotos_Aplicacion/` contiene al menos una imagen real, no solo el placeholder
- [✅] El número de filas del CSV coincide con el número de respuestas declarado en `Respuestas_cuestionario.md`
- [✅] `Respuestas_cuestionario.md` y el `.csv` están guardados en UTF-8 (sin símbolos rotos tipo `Ã³` o `ð`)
- [✅] Existe un `README.md` dentro de `Cuestionario/` que explique quién aplicó el cuestionario, a quién, cuándo y con qué herramienta (ej. Google Forms)
- [✅] El CSV abre sin errores de codificación

---

## 🤖 Instrucción para revisión por IA

> "Clona `https://github.com/gleiston-guerrero/MediCita_ISR401`, entra a `02_Evidencias/Cuestionario/`, y sigue los Pasos 1 a 6 de `Guia_Verificacion_Cuestionario.md`. Confírmame si `Fotos_Aplicacion` y `Respuestas` ya están anidadas dentro de `Cuestionario/`, si hay archivos vacíos, si las fotos de aplicación existen, si el conteo de respuestas del CSV coincide con lo declarado, y si hay problemas de codificación de caracteres en los archivos de texto."

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
