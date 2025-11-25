from utils import agregar_tarea, completar_tarea, ver_tareas, canjear_puntos, ver_puntos, eliminar_tarea

def mostrar_menu():
    """Muestra el menú principal de opciones."""
    print("\n--- Menú Principal ---")
    print("1. Agregar Tarea")
    print("2. Completar Tarea")
    print("3. Ver Tareas")
    print("4. Eliminar Tarea")
    print("5. Ver Puntos")
    print("6. Canjear Puntos")
    print("7. Salir")

def main():
    """Función principal que muestra el menú y maneja la interacción del usuario."""
    tareas_diarias = []
    puntos_usuario = 0
    opcion = 0
    
    while not opcion == '7':
        mostrar_menu()
        opcion = input("Elige una opción (1-7): ").strip()

        if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 7:
            print("❌ Opción no válida. Por favor, elige un número del 1 al 7.")
            continue

        if opcion == '1':
            tareas_diarias = agregar_tarea(tareas_diarias)
        elif opcion == '2':
            tareas_diarias, puntos_usuario = completar_tarea(tareas_diarias, puntos_usuario)
        elif opcion == '3':
            ver_tareas(tareas_diarias, puntos_usuario)
        elif opcion == '4':
            tareas_diarias = eliminar_tarea(tareas_diarias)
        elif opcion == '5':
            ver_puntos(puntos_usuario)
        elif opcion == '6':
            puntos_usuario = canjear_puntos(puntos_usuario)
        elif opcion == '7':
            print("👋 ¡Gracias por usar Check & Play! ¡Nos vemos pronto!")
        
        
# --- Ejecución del programa ---
if __name__ == "__main__":
    main()