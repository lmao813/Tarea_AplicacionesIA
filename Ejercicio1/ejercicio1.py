from datetime import datetime

class CursoChatbot:
    def __init__(self):
        self.tareas = []

    def ejecutar(self):
        print("👋 Hola, soy tu asistente de tareas del curso.")
        while True:
            comando = input("\n¿Qué deseas hacer? (ver / añadir / eliminar / consultar / salir): ").strip().lower()
            if comando == "ver":
                self.ver_tareas()
            elif comando == "añadir":
                self.añadir_tarea()
            elif comando == "eliminar":
                self.eliminar_tarea()
            elif comando == "consultar":
                self.consultar_por_fecha()
            elif comando == "salir":
                print("👋 ¡Hasta pronto!")
                break
            else:
                print("Comando no reconocido. Intenta con: ver, añadir, eliminar, consultar o salir.")

    def ver_tareas(self):
        if not self.tareas:
            print("📭 No tienes tareas registradas.")
            return
        print("\n📋 Lista de tareas:")
        for i, tarea in enumerate(self.tareas, 1):
            print(f"{i}. {tarea['nombre']} (Entrega: {tarea['fecha'].strftime('%Y-%m-%d')})")

    def añadir_tarea(self):
        nombre = input("📌 Nombre de la tarea: ").strip()
        fecha_str = input("📅 Fecha de entrega (YYYY-MM-DD): ").strip()
        try:
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
            self.tareas.append({"nombre": nombre, "fecha": fecha})
            print("✅ Tarea añadida con éxito.")
        except ValueError:
            print("❌ Formato de fecha inválido. Usa YYYY-MM-DD.")

    def eliminar_tarea(self):
        self.ver_tareas()
        if not self.tareas:
            return
        try:
            idx = int(input("🔢 Número de la tarea a eliminar: ")) - 1
            if 0 <= idx < len(self.tareas):
                tarea = self.tareas.pop(idx)
                print(f"🗑️ Tarea '{tarea['nombre']}' eliminada.")
            else:
                print("❌ Número fuera de rango.")
        except ValueError:
            print("❌ Entrada inválida. Debes escribir un número.")

    def consultar_por_fecha(self):
        fecha_str = input("📅 Fecha a consultar (YYYY-MM-DD): ").strip()
        try:
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
            encontradas = [t for t in self.tareas if t["fecha"].date() == fecha.date()]
            if encontradas:
                print(f"\n📚 Tareas para el {fecha.strftime('%Y-%m-%d')}:")
                for tarea in encontradas:
                    print(f"- {tarea['nombre']}")
            else:
                print("📭 No hay tareas para esa fecha.")
        except ValueError:
            print("❌ Formato de fecha inválido. Usa YYYY-MM-DD.")

# Ejecutar chatbot
if __name__ == "__main__":
    bot = CursoChatbot()
    bot.ejecutar()
