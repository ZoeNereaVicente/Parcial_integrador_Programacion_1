def validar_tarea(lista_tareas, intentos = 0):
    """Añade las validaciones de entrada y en caso de pasarlas agrega la nueva tarea."""

    # Caso base
    if intentos >= 3:
        print("\n❌ Se alcanzó el número máximo de intentos. Operación cancelada.")
        return lista_tareas
    
    nueva_tarea = input("\nIngresa la nueva tarea: ").strip().lower()

    # Validaciones
    if not nueva_tarea:
        print("⚠️ La tarea no puede estar vacía.")
        return validar_tarea(lista_tareas, intentos + 1)  
    elif any(caracter.isdigit() for caracter in nueva_tarea):
        print("⚠️ La tarea no puede contener números.")
        return validar_tarea(lista_tareas, intentos + 1)
    elif len(nueva_tarea) <= 3:
        print("⚠️ La tarea debe tener más de tres caracteres.")
        return validar_tarea(lista_tareas, intentos + 1)
    elif any(nueva_tarea == tarea[0].lower().strip() for tarea in lista_tareas):
        print("⚠️ Esa tarea ya existe en la lista.")
        return validar_tarea(lista_tareas, intentos + 1)

    # Si pasa todas las validaciones, se agrega la tarea.
    # Es una lista con dos elementos: la descripción y el estado inicial (pendiente)

    lista_tareas.append([nueva_tarea, False])
    print("✅ Tarea agregada con éxito.")
    return lista_tareas

def agregar_tarea(lista_tareas):
    """Añade una nueva tarea a la lista con validaciones de entrada."""
    try:
        lista_tareas = validar_tarea(lista_tareas)
    except Exception as e:
        print(f"❌ Ocurrió un error al agregar la tarea: {e}")
    finally:
        print("📌 Proceso de agregar tarea finalizado.")
    return lista_tareas