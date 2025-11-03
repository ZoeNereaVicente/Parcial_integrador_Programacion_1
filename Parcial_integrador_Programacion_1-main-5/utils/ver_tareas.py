def ver_tareas(lista_tareas, puntos):
    """Muestra todas las tareas y su estado (pendiente o completada)."""
    if not lista_tareas:
        print("📭 ¡Tu lista de tareas está vacía!")
        return False

    print("\n📝 --- Mi Lista de Tareas ---")
    
    for i, tarea in enumerate(lista_tareas):
        if isinstance(tarea, list) and len(tarea) == 2:
            estado = "✅ Completada" if tarea[1] else "⏳ Pendiente"
            print(f"{i + 1}. {tarea[0]} - [{estado}]")
        else:
            print(f"{i + 1}. ⚠️ Tarea mal formada: {tarea}")
    
    print("----------------------------")
    print(f"💰 Puntos actuales: {puntos}")
    return True