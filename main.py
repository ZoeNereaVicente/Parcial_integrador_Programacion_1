from utils import agregar_tarea, completar_tarea, ver_tareas, canjear_puntos, ver_puntos

# Declaración de variables iniciales en el ámbito principal
tareas_diarias = []
puntos_usuario = 0

def mostrar_menu():
    """Muestra el menú principal de opciones."""
    print("\n--- Menú Principal ---")
    print("1. Agregar Tarea")
    print("2. Completar Tarea")
    print("3. Ver Tareas")
    print("4. Canjear Puntos")
    print("5. Ver Puntos")
    print("6. Salir")

def main():
    """Función principal que muestra el menú y maneja la interacción del usuario."""
    continuar_programa = True
    tareas_diarias = []
    puntos_usuario = 0
    
    while continuar_programa:
        mostrar_menu()
        opcion = input("Elige una opción (1-6): ").strip()

        if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 6:
            print("❌ Opción no válida. Por favor, elige un número del 1 al 6.")
            continue

        if opcion == '1':
            tareas_diarias = agregar_tarea(tareas_diarias)
        elif opcion == '2':
            tareas_diarias, puntos_usuario = completar_tarea(tareas_diarias, puntos_usuario)
        elif opcion == '3':
            ver_tareas(tareas_diarias, puntos_usuario)
        elif opcion == '4':
            puntos_usuario = canjear_puntos(puntos_usuario)
        elif opcion == '5':
            ver_puntos(puntos_usuario)
        elif opcion == '6':
            print("👋 ¡Gracias por usar Check & Play! ¡Nos vemos pronto!")
            continuar_programa = False

# --- Ejecución del programa ---
if __name__ == "__main__":
    main()