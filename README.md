# 🧩 Analizador Sintáctico en C#

## 📖 Descripción

Este proyecto implementa un **analizador sintáctico** para el lenguaje **C#**, desarrollado con fines educativos y experimentales.  
El objetivo es analizar fragmentos de código fuente escritos en C#, verificando si cumplen con las reglas gramaticales definidas para el lenguaje.  

Incluye:
- Un **analizador léxico** que convierte el código fuente en una secuencia de tokens.
- Un **analizador sintáctico** (basado en una gramática libre de contexto) que valida la estructura del código.
- Reportes de **errores léxicos, sintácticos y semánticos** detallados.

## 🧠 Características principales

- Implementación basada en **PLY (Python Lex-Yacc)**.
- Soporte para:
  - Declaraciones de variables
  - Estructuras condicionales (`if`, `else`)
  - Bucles (`while`)
  - Expresiones aritméticas y lógicas
  - Llamadas a métodos (`Console.WriteLine`, etc.)
- Manejo de errores sintácticos y semánticos con mensajes claros.
- Generación automática de logs para cada análisis.

---

# 🚀 Cómo usar el proyecto

## 1️⃣ Instalar dependencias

Este proyecto utiliza **PLY**, por lo que primero debes instalarlo:

```sh
pip install ply
```
## 2️⃣ Ejecutar el archivo principal

```sh
pip install ply

python Proyecto/main.py

