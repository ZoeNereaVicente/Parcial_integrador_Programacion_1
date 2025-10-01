from agregar_tarea import agregar_tarea
from completar_tarea import completar_tarea
from ver_tareas import ver_tareas
from canjear_puntos import canjear_puntos

# Declaración de variables iniciales en el ámbito principal
tareas_diarias = []
puntos_usuario = 0

def main():
    """Función principal que muestra el menú y maneja la interacción del usuario."""
    continuar_programa = True
    tareas_diarias = []
    puntos_usuario = 0
    
    while continuar_programa:
        print("\n--- Menú Principal ---")
        print("1. Agregar Tarea")
        print("2. Completar Tarea")
        print("3. Ver Tareas")
        print("4. Canjear Puntos")
        print("5. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            tareas_diarias = agregar_tarea(tareas_diarias)
        elif opcion == '2':
            tareas_diarias, puntos_usuario = completar_tarea(tareas_diarias, puntos_usuario)
        elif opcion == '3':
            ver_tareas(tareas_diarias, puntos_usuario)
        elif opcion == '4':
            puntos_usuario = canjear_puntos(puntos_usuario)
        elif opcion == '5':
            print("👋 ¡Gracias por usar el programa! ¡Hasta la próxima!")
            continuar_programa = False
        else:
            print("❌ Opción no válida. Por favor, elige un número del 1 al 5.")

# --- Ejecución del programa ---
if __name__ == "__main__":
    main()