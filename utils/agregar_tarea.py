def validar_nueva_tarea(lista_tareas):
    nueva_tarea = input("Ingresa la nueva tarea: ")
    if any(caracter.isdigit() for caracter in nueva_tarea):
        print("⚠️ La tarea no debe contener números.")
        return validar_nueva_tarea(lista_tareas)
    elif (len(nueva_tarea) <= 3):
        print("⚠️ La tarea tiene que tener más de tres caracteres.")
        return validar_nueva_tarea(lista_tareas) 
    else:
        # Se agrega la tarea como una lista con dos elementos: la descripción y el estado inicial (pendiente)
        lista_tareas.append([nueva_tarea, False])
        print("✅ Tarea agregada con éxito.")
    return lista_tareas


def agregar_tarea(lista_tareas):
    """Añade una nueva tarea a la lista."""
    try:
        return validar_nueva_tarea(lista_tareas)
    except Exception as e:
        print(f"❌ Ocurrió un error al agregar la tarea: {e}")
    finally:
        print("Proceso de agregar tarea finalizado.")