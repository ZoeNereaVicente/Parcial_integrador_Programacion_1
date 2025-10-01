def agregar_tarea(lista_tareas):
    """Añade una nueva tarea a la lista."""
    try:
        nueva_tarea = input("Ingresa la nueva tarea: ")
        # Se agrega la tarea como una lista con dos elementos: la descripción y el estado inicial (pendiente)
        lista_tareas.append([nueva_tarea, False])
        print("✅ Tarea agregada con éxito.")
    except Exception as e:
        print(f"❌ Ocurrió un error al agregar la tarea: {e}")
    finally:
        print("Proceso de agregar tarea finalizado.")
    return lista_tareas