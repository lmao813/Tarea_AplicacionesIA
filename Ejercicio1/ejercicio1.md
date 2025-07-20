# 📝 Chatbot para Gestión de Tareas del Curso 

## 📌 Descripción del ejercicio  
Como parte del capítulo 7 del curso, se propuso diseñar un agente conversacional (chatbot) que facilitara la administración de tareas académicas. El objetivo era permitir al usuario interactuar mediante una interfaz de consola para realizar operaciones básicas sobre sus pendientes.

---

## ⚙️ Desarrollo del ejercicio  

Se desarrolló una **aplicación de consola** en Python que simula un agente de IA con funcionalidades clave:

1. **Ver tareas registradas**  
   Muestra todas las tareas almacenadas actualmente.

2. **Añadir nueva tarea**  
   Solicita al usuario:  
   - Nombre de la tarea  
   - Descripción  
   - Fecha de entrega  

3. **Eliminar tarea existente**  
   Permite remover tareas por índice.

4. **Consultar tareas por fecha**  
   Filtra y muestra las tareas que vencen en una fecha específica.

5. **Salir del chatbot**  
   Termina la conversación.

---

## 🧠 Lógica del agente  

- El chatbot funciona en un bucle que interpreta el texto ingresado.
- Los comandos válidos son: `ver`, `añadir`, `eliminar`, `consultar`, `salir`.
- La información se guarda en una estructura en memoria (`list` de `dicts`).
- Se utiliza `datetime` para validar fechas.

---
## 📊 Resultados
<img width="898" height="529" alt="image" src="https://github.com/user-attachments/assets/1b1f0a8e-7337-4f61-86ed-baa15e76c998" />

## 💬 Ejemplo de uso  

```plaintext
Bienvenido al gestor de tareas del curso.
¿Qué deseas hacer? (ver / añadir / eliminar / consultar / salir): añadir
Nombre de la tarea: Tarea de Machine Learning
Descripción: Implementar un modelo de SVM
Fecha de entrega (YYYY-MM-DD): 2025-07-24
Tarea añadida exitosamente.

¿Qué deseas hacer?: consultar
Introduce la fecha a consultar (YYYY-MM-DD): 2025-07-24

📋 Tareas para el 2025-07-24:
- Tarea de Machine Learning: Implementar un modelo de SVM
