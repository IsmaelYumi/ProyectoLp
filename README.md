# 🧩 Analizador Sintáctico en C#

## 📖 Descripción

Este proyecto implementa un **analizador sintáctico** para el lenguaje **C#**, desarrollado con fines educativos y experimentales.  
El objetivo es analizar fragmentos de código fuente escritos en C#, verificando si cumplen con las reglas gramaticales definidas para el lenguaje.  

Incluye:
- Un **analizador léxico** que convierte el código fuente en una secuencia de tokens.
- Un **analizador sintáctico** (basado en una gramática libre de contexto) que valida la estructura del código.
- Reportes de **errores léxicos y sintácticos** detallados.

## 🧠 Características principales

- Implementación basada en **análisis descendente recursivo** o **LL(1)** (según tu elección).
- Soporte para:
  - Declaraciones de variables
  - Estructuras condicionales (`if`, `else`)
  - Bucles (`while`, `for`)
  - Expresiones aritméticas y lógicas
- Manejo de errores sintácticos con mensajes claros.
- Módulo independiente para el análisis léxico.
