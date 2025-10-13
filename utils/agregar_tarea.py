def agregar_tarea(lista_tareas):
    """Añade una nueva tarea a la lista con validaciones de entrada."""
    try:
        nueva_tarea = input("Ingresa la nueva tarea: ").strip().lower()

        # Validaciones
        if not nueva_tarea:
            print("⚠️ La tarea no puede estar vacía.")
        elif any(caracter.isdigit() for caracter in nueva_tarea):
            print("⚠️ La tarea no puede contener números.")
        elif len(nueva_tarea) <= 3:
            print("⚠️ La tarea debe tener más de tres caracteres.")
        elif any(nueva_tarea == tarea[0].lower().strip() for tarea in lista_tareas):
            print("⚠️ Esa tarea ya existe en la lista.")
        else:
            # Se agrega la tarea como una lista con dos elementos: la descripción y el estado inicial (pendiente)
            lista_tareas.append([nueva_tarea, False])
            print("✅ Tarea agregada con éxito.")
    except Exception as e:
        print(f"❌ Ocurrió un error al agregar la tarea: {e}")
    finally:
        print("📌 Proceso de agregar tarea finalizado.")
    return lista_tareas