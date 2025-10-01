def ver_tareas(lista_tareas, puntos):
    """Muestra todas las tareas y su estado (pendiente o completada)."""
    if not lista_tareas:
        print("¡Tu lista de tareas está vacía! 🧐")
        return
        
    print("\n--- Mi Lista de Tareas ---")
    
    # Uso de bucle for y índice manual en lugar de enumerate
    for i in range(len(lista_tareas)):
        tarea = lista_tareas[i]
        # El estado de la tarea es el segundo elemento de la lista anidada
        estado = "✅ Completada" if tarea[1] else "⏳ Pendiente"
        print(f"{i + 1}. {tarea[0]} - [{estado}]")
    print("--------------------------")
    print(f"Puntos actuales: {puntos} 💰")