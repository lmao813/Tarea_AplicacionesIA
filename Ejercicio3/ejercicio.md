# 📝 Sistema RAG simple para el calendario académico UNAL 2025

## 📌 Descripción del ejercicio
Desarrollar un sistema RAG (Retrieval-Augmented Generation) básico que permita crear un chat informativo sobre el calendario académico 2025 de la Universidad Nacional de Colombia.
El sistema debía ser conversacional y ofrecer respuestas a preguntas como:
- ¿Cuándo empiezan clases?
- ¿Cuál es la fecha límite para inscribir asignaturas?
- ¿Cuándo son las ceremonias de grado?
---

## ⚙️ Desarrollo del ejercicio
Se optó por una solución liviana, de consola, basada únicamente en Python y librerías estándar de Machine Learning:
- Carga de contexto
Se cargó el texto completo de la Resolución del calendario académico 2025, incluyendo:
  - Fechas de inscripción de materias
  - Inicio/finalización de clases
  - Semana santa
  - Entrega de notas
  - Exámenes de admisión
  - Ceremonias de grado y excepciones para posgrado.

- Modelo de recuperación
Se implementó un sistema de recuperación basado en TF-IDF con scikit-learn.  
Cada línea relevante del calendario fue considerada como un "documento" independiente.  
Cuando el usuario hace una consulta, se calcula la similitud coseno entre su pregunta y los fragmentos, y se retorna el más similar.

- Interfaz de consola
Se desarrolló una interfaz de consola tipo chatbot.  
El usuario puede hacer preguntas en lenguaje natural y recibir respuestas extraídas del contexto cargado.

## 💻 Ejemplo de uso
```plaintext
🧠 Chat UNAL - Calendario Académico 2025
Escribe tu pregunta (escribe 'salir' para terminar):

Tú: ¿Cuándo empiezan las clases?
UNALBot: Iniciación de clases: 31 de marzo

Tú: ¿Cuándo son los grados?
UNALBot: Primera ceremonia de grados: Del 3 al 13 de junio

Tú: salir
👋 Hasta luego.
