<div align="center">

# 💻 MVP — SICM (Sistema de Gestión Inteligente para un Centro Médico)

### Demostración guiada, prototipo final revisado y accesible en vivo

**Proyecto Fin de Curso (PFC) – Ingeniería de Requisitos (ISR-401)**

<br>

![Universidad](https://img.shields.io/badge/Universidad-UTEQ-003366?style=for-the-badge)
![Estado](https://img.shields.io/badge/Estado-Publicado-success?style=for-the-badge)
![Validacion](https://img.shields.io/badge/Validacion-Walkthrough-success?style=for-the-badge)
![Tecnologia](https://img.shields.io/badge/Tecnologia-HTML_%2F_CSS_%2F_JS-00509d?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)

</div>

---

## 🔗 Enlace directo (revisar aquí)

<div align="center">

### 👉 [Abrir demostración del MVP](https://ptigasis-alexander.github.io/MediCita_ISR401/)

</div>

Este enlace es **público**, no requiere instalación ni cuenta de GitHub y funciona directamente desde el navegador.

La demostración publicada permite revisar los principales módulos y flujos del sistema SICM mediante una presentación automática con narración y navegación simulada.

> **Importante:** GitHub Pages publica actualmente el contenido de `05_MVP` como raíz del sitio. Por este motivo, el enlace correcto es el indicado anteriormente y no la antigua ruta `/05_MVP/`.

---

## 📖 Qué es este MVP

Es una **demostración guiada y autorreproducible** del sistema SICM.

Simula la navegación por las principales interfaces del sistema y permite observar el flujo de atención de diferentes usuarios y áreas del centro médico.

La demostración fue **actualizada después del proceso de Validación Walkthrough**, incorporando las principales observaciones identificadas durante las sesiones con los participantes.

La demostración tiene una duración aproximada de:

### ⏱️ 5 minutos — 300 segundos — 20 escenas

Entre los módulos y procesos representados se encuentran:

- Inicio de sesión y control por roles
- Gestión de pacientes
- Agendamiento de citas
- Recepción
- Recaudación y pagos
- Enfermería
- Medicina General
- Historia clínica
- Recetas médicas
- Odontología
- Psicología
- Nutrición
- Terapia Física
- Derivaciones
- Notificaciones
- Coordinación
- Reportes
- Auditoría

---

## 🎮 Controles disponibles

La demostración incluye los siguientes controles:

- 🔊 Activar o silenciar la narración
- ⏸️ Pausar o reanudar la demostración
- ⛶ Pantalla completa
- 🔠 `A+` para aumentar el tamaño del texto

La narración utiliza las capacidades disponibles en el navegador para acompañar automáticamente cada una de las escenas.

---

## 🖥️ Prototipo final revisado

Además de la demostración guiada, esta carpeta contiene la **versión final revisada del prototipo del sistema SICM**.

Este prototipo corresponde a la versión obtenida después del siguiente proceso:

**Prototipo inicial → Validación Walkthrough → Observaciones → Correcciones → Prototipo final revisado**

El objetivo fue incorporar las observaciones de los participantes **sin modificar de forma radical la estructura ni las interfaces originales del sistema**.

Por lo tanto, se conservaron:

- Distribución general de los módulos
- Menú lateral
- Estructura de navegación
- Identidad visual
- Organización por roles
- Flujo general de atención

Las modificaciones se concentraron principalmente en funcionalidades, campos, mensajes, accesibilidad y necesidades detectadas durante la validación.

---

## ✅ Mejoras incorporadas después de la validación

Entre las principales mejoras incorporadas al prototipo final y representadas en la demostración se encuentran:

- Identificación mediante **cédula o pasaporte**
- Consideración de pacientes menores de edad
- Información de representante legal cuando corresponde
- Teléfono de contacto de emergencia
- Mensajes de confirmación más claros
- Control `A+` para mejorar la legibilidad
- Selección de profesional al solicitar una cita
- Visualización más clara de horarios disponibles
- Agenda por día, semana y mes
- Consulta de pagos y comprobantes
- Registro de frecuencia respiratoria
- Registro de saturación de oxígeno
- Notas y procedimientos de Enfermería
- Historia clínica filtrable por especialidad
- Antecedentes psicológicos previos
- Objetivo terapéutico en Psicología
- Mejoras en el registro de Terapia Física
- Número y duración de sesión
- Prioridad de atención
- Registro de ejercicios realizados
- Derivaciones con área de origen y destino
- Contexto clínico para el área receptora
- Apoyo de accesibilidad mediante dictado por voz
- Gestión de profesionales y horarios desde Coordinación
- Reportes automáticos por área
- Mejoras en notificaciones y trazabilidad

---

## 💊 Flujo de recetas médicas

La versión revisada representa el flujo de medicamentos solicitado durante el desarrollo y validación del sistema.

Los profesionales autorizados de:

- **Medicina General**
- **Odontología**

pueden registrar una receta médica.

Una vez registrada, la receta se envía al área de **Enfermería**.

Enfermería puede consultar:

- Paciente
- Medicamento
- Dosis
- Frecuencia
- Cantidad
- Indicaciones

Después de entregar el medicamento al paciente, Enfermería puede marcarlo como:

### ✅ Medicamento entregado

De esta manera se mantiene la trazabilidad entre la prescripción y la entrega del medicamento.

---

## 🏥 Áreas y roles representados

El MVP representa los principales actores y áreas definidos para SICM:

| Rol o área | Funciones representadas |
|---|---|
| 👤 Paciente | Datos personales, citas, pagos y consulta de información |
| 🗂️ Recepción | Registro, búsqueda de pacientes y gestión de citas |
| 💳 Recaudación | Registro de pagos y comprobantes |
| 💉 Enfermería | Triage, signos vitales, notas y entrega de medicamentos |
| 🩺 Medicina General | Atención, historia clínica y recetas |
| 🦷 Odontología | Odontograma, procedimientos y recetas |
| 🧠 Psicología | Antecedentes, evolución y objetivos terapéuticos |
| 🥗 Nutrición | Evaluación y seguimiento nutricional |
| 🦵 Terapia Física | Sesiones, ejercicios, duración y evolución |
| ⚙️ Coordinación | Profesionales, horarios, permisos y supervisión |

---

## 📊 Reportes y trazabilidad

El prototipo contempla reportes generados a partir de la información registrada durante las atenciones.

Se representan indicadores correspondientes a diferentes áreas, entre ellas:

- Medicina General
- Odontología
- Enfermería
- Psicología
- Nutrición
- Terapia Física

También se representa un registro de auditoría para mantener trazabilidad sobre determinadas operaciones realizadas dentro del sistema.

---

## 🧪 Relación con la Validación Walkthrough

Las modificaciones realizadas no corresponden únicamente a cambios visuales.

Las mejoras fueron incorporadas considerando las observaciones obtenidas durante las sesiones de **Validación Walkthrough**.

Las evidencias correspondientes a este proceso se encuentran documentadas dentro del repositorio.

El flujo de trabajo seguido fue:

```text
Requisitos
    ↓
Prototipo inicial
    ↓
Validación Walkthrough
    ↓
Observaciones de participantes
    ↓
Análisis de resultados
    ↓
Correcciones
    ↓
Prototipo final revisado
    ↓
MVP actualizado
```

Esto permite mantener coherencia entre:

- Requisitos
- Validación
- Observaciones
- Interfaces
- Prototipo
- MVP
- Trazabilidad

---

## ⚠️ Alcance del MVP

El MVP publicado es una **simulación interactiva autocontenida** desarrollada con HTML, CSS y JavaScript.

Su objetivo es demostrar visualmente el comportamiento esperado del sistema.

Por tratarse de un prototipo académico:

- No utiliza una base de datos clínica de producción
- No almacena información médica real
- No procesa pagos reales
- No sustituye un sistema médico productivo
- Los datos mostrados son simulados
- Algunas operaciones representan el comportamiento esperado del sistema

---

## 🤖 Instrucción para revisión por IA

Si se desea realizar una revisión asistida por IA, puede utilizarse la siguiente instrucción:

> "Abre `https://ptigasis-alexander.github.io/MediCita_ISR401/`, revisa la demostración guiada del sistema SICM e identifica los módulos y funcionalidades representados. Contrasta la demostración y el prototipo final revisado con las evidencias de Validación Walkthrough del repositorio, indicando qué observaciones fueron incorporadas y verificando que la página cargue correctamente sin errores 404 ni recursos CSS/JS rotos."

---

## 🧪 Cómo verificar que está correctamente publicado

```bash
curl -I https://ptigasis-alexander.github.io/MediCita_ISR401/
```

La respuesta esperada es:

```text
HTTP/2 200
```

La publicación se realiza mediante **GitHub Actions**, utilizando únicamente los archivos necesarios de la carpeta `05_MVP`.

> Si se presenta un problema de publicación, revisar **Actions → Deploy MediCita MVP** y comprobar que la ejecución más reciente finalice con estado `Success`.

---

## 🐳 Despliegue reproducible con Docker

El MVP también puede ejecutarse localmente mediante **Docker y Docker Compose**, sin necesidad de abrir manualmente el archivo `index.html`.

Este mecanismo permite reproducir el despliegue del prototipo en un entorno limpio utilizando un servidor web Nginx.

### Requisitos

Antes de ejecutar el prototipo, debe estar instalado:

- Docker Desktop
- Docker Compose

### Clonar el repositorio

```bash
git clone https://github.com/gleiston-guerrero/MediCita_ISR401.git
```

### Ingresar a la carpeta del MVP

```bash
cd MediCita_ISR401/05_MVP
```

### Construir e iniciar el contenedor

```bash
docker compose up --build
```

Después de finalizar la construcción, abrir en el navegador:

```text
http://localhost:8080
```

El prototipo será servido mediante **Nginx** dentro de un contenedor Docker.

### Detener el MVP

Para detener y eliminar el contenedor creado, ejecutar:

```bash
docker compose down
```

### Reconstruir después de realizar cambios

Si se modifican los archivos HTML, CSS o JavaScript, ejecutar nuevamente:

```bash
docker compose up --build
```

### Verificar el contenedor

Para comprobar que el contenedor se encuentra en ejecución:

```bash
docker ps
```

Debe aparecer un contenedor llamado:

```text
medicita_mvp
```

Este procedimiento proporciona un despliegue reproducible mediante una única orden:

```bash
docker compose up --build
```

---

## 📂 Archivos de esta carpeta

| Archivo | Función |
|---|---|
| [`index.html`](index.html) | Estructura de la demostración guiada |
| [`style.css`](style.css) | Diseño visual, componentes y animaciones |
| [`script.js`](script.js) | Reproducción automática, escenas, narración y controles |
| [`05_MVP_.md`](05_MVP_.md) | Documentación del MVP y de la versión revisada |
| [`MediCita_prototipo_final_actualizado.html`](MediCita_prototipo_final_actualizado.html) | Prototipo final revisado después de la Validación Walkthrough |
| [`Dockerfile`](Dockerfile) | Construcción de la imagen del MVP mediante Nginx |
| [`docker-compose.yml`](docker-compose.yml) | Configuración para iniciar el despliegue reproducible |

> El prototipo final permite realizar una revisión más detallada de las interfaces y funcionalidades, mientras que la demostración guiada presenta los principales flujos del sistema de manera automática.

---

## 🔍 Orden recomendado de revisión

Para evaluar esta sección del repositorio se recomienda:

1. Abrir la **demostración publicada en GitHub Pages**.
2. Ejecutar los **5 minutos de la demostración guiada**.
3. Revisar el **prototipo final actualizado**.
4. Ejecutar el MVP mediante **Docker Compose**.
5. Consultar las evidencias de **Validación Walkthrough**.
6. Contrastar las observaciones con las mejoras incorporadas.
7. Revisar la trazabilidad con los requisitos correspondientes.

---

## 🛠️ Tecnologías utilizadas

- HTML5
- CSS3
- JavaScript
- Web Speech API
- Docker
- Docker Compose
- Nginx
- GitHub Pages
- GitHub Actions

---

<div align="center">

## 📌 Estado actual

### ✅ Demostración guiada actualizada

### ✅ Prototipo final revisado

### ✅ Mejoras de Validación Walkthrough incorporadas

### ✅ Despliegue reproducible mediante Docker Compose

### ✅ GitHub Pages publicado

### ✅ Acceso público

<br>

## Universidad Técnica Estatal de Quevedo

### Facultad de Ciencias de la Computación

### Carrera de Ingeniería de Software

### Proyecto Fin de Curso

**Sistema de Gestión Inteligente para un Centro Médico (SICM)**

---

⭐ **Documento elaborado con fines exclusivamente académicos.**

</div>
