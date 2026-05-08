# Primera Página Web con Reflex

Este proyecto consiste en el desarrollo de mi primera página web utilizando el framework **Reflex** con el lenguaje de programación **Python**.  
La página web tiene una temática de fútbol e incluye diseño personalizado, imagen, textos y botones interactivos.

---

# Objetivo del proyecto

El objetivo principal de este proyecto fue aprender a crear una aplicación web básica usando Reflex, comprender la estructura de un proyecto web, manejar dependencias con Poetry y subir el proyecto a GitHub utilizando commits.

---

# Tecnologías utilizadas

- Python 3.12.0
- Reflex
- Poetry
- Git
- GitHub
- Visual Studio Code

---

# Pasos realizados

## 1. Creación del repositorio

Primero creé un repositorio público en GitHub con el nombre:

```bash
primera_pagina
```

Este repositorio fue utilizado para guardar el código del proyecto y llevar control de versiones.

---

## 2. Clonación del repositorio

Luego abrí CMD y entré a mi carpeta de trabajo:

```bash
cd OneDrive
cd Reflex
```

Después cloné el repositorio:

```bash
git clone https://github.com/Julioblack09/primera_pagina-.git
```

Luego entré a la carpeta del proyecto:

```bash
cd primera_pagina-
```

---

## 3. Verificación de Python

Verifiqué que Python estuviera instalado correctamente:

```bash
python --version
```

La versión utilizada fue:

```bash
Python 3.12.0
```

---

## 4. Verificación de Poetry

También verifiqué que Poetry estuviera instalado:

```bash
poetry --version
```

Poetry fue utilizado para manejar las dependencias del proyecto.

---

## 5. Inicialización de Poetry

Inicialicé Poetry dentro del proyecto con:

```bash
poetry init
```

Este comando generó el archivo:

```bash
pyproject.toml
```

---

## 6. Configuración del archivo pyproject.toml

Se modificó la configuración de Python para evitar errores de compatibilidad con Reflex.

También se corrigió un problema con el nombre del proyecto, ya que Poetry no aceptaba el nombre con un guion al final.

El nombre fue cambiado de:

```toml
name = "primera_pagina-"
```

a:

```toml
name = "primera_pagina"
```

---

## 7. Instalación de Reflex

Después instalé Reflex usando Poetry:

```bash
poetry add reflex
```

Este comando instaló Reflex y todas las dependencias necesarias.

---

## 8. Inicialización del proyecto Reflex

Luego inicialicé Reflex con:

```bash
poetry run reflex init
```

Durante la inicialización seleccioné la opción:

```bash
0 - A blank Reflex app
```

Esta opción creó una aplicación en blanco para desarrollarla desde cero.

---

## 9. Ejecución de la aplicación

Para ejecutar la aplicación utilicé:

```bash
poetry run reflex run
```

La aplicación se ejecutó localmente en:

```text
http://localhost:3000
```

El backend se ejecutó en:

```text
http://0.0.0.0:8000
```

---

## 10. Diseño de la página web

La página fue personalizada con una temática de fútbol.

Se agregaron los siguientes elementos:

- Título principal
- Texto descriptivo
- Imagen relacionada con fútbol
- Botones interactivos
- Fondo degradado
- Diseño moderno y centrado

---

## 11. Botones funcionales

Se agregó una clase `State` para manejar el estado de la aplicación.

Los botones permiten mostrar diferentes mensajes relacionados con fútbol:

- Equipos
- Jugadores
- Curiosidades

Esto permitió agregar interacción básica dentro de la aplicación web.

---

# Problemas encontrados

## Error con el nombre del proyecto

Durante la instalación de Reflex apareció el siguiente error:

```bash
project.name must match pattern
```

Este error ocurrió porque el nombre del proyecto terminaba con un guion.

Para resolverlo se modificó el archivo `pyproject.toml` eliminando el guion final.

---

## Advertencia de OneDrive

Al ejecutar Reflex apareció una advertencia indicando que trabajar dentro de OneDrive puede afectar el rendimiento del proyecto.

A pesar de esto la aplicación logró ejecutarse correctamente.

---

## Error del frontend

También apareció el siguiente error:

```bash
TypeError: dispatch is not a function
```

Para intentar solucionarlo se eliminó la carpeta `.web` utilizando:

```bash
rmdir /s /q .web
```

Luego se volvió a ejecutar la aplicación.

---

# Commits realizados

Durante el proyecto se realizaron varios commits para guardar los avances:

```bash
git add .
git commit -m "configuramos Poetry y Python compatible"
git push origin main
```

```bash
git add .
git commit -m "instalamos Reflex en el proyecto"
git push origin main
```

```bash
git add .
git commit -m "inicializamos la aplicacion Reflex"
git push origin main
```

```bash
git add .
git commit -m "agregamos pagina de futbol con botones funcionales"
git push origin main
```

```bash
git add README.md
git commit -m "agregamos README completo del proyecto"
git push origin main
```

---

# Cómo ejecutar el proyecto

Primero clonar el repositorio:

```bash
git clone https://github.com/Julioblack09/primera_pagina-.git
```

Entrar a la carpeta:

```bash
cd primera_pagina-
```

Instalar dependencias:

```bash
poetry install
```

Ejecutar la aplicación:

```bash
poetry run reflex run
```

Abrir en el navegador:

```text
http://localhost:3000
```

---

# Conclusión

Durante este proyecto aprendí a crear una aplicación web básica utilizando Reflex y Python.

También aprendí a utilizar Poetry para manejar dependencias, Git para guardar cambios y GitHub para publicar proyectos.

Aunque se presentaron algunos errores durante el proceso, como problemas con el nombre del proyecto y errores del frontend, pude analizarlos y aplicar soluciones para continuar el desarrollo.

Este proyecto me permitió comprender mejor cómo funciona una aplicación web moderna desarrollada completamente con Python.

---

# Autor

Julio Black