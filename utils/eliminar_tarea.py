# utils/eliminar_tarea.py

def eliminar_tarea(lista_tareas):
    """Elimina una tarea de la lista."""

    if not lista_tareas:
        print("\n⚠️ No hay tareas para eliminar.")
        return lista_tareas

    print("\n=== ELIMINAR TAREA ===")
    for i, tarea in enumerate(lista_tareas, start=1):
        estado = "✓" if tarea[1] else " "
        print(f"{i}. [{estado}] {tarea[0]}")

    try:
        seleccion = int(input("\nIngresa el número de la tarea que querés eliminar: ")) - 1

        if not (0 <= seleccion < len(lista_tareas)):
            print("❌ Número fuera de rango.")
            return lista_tareas

        tarea_eliminada = lista_tareas.pop(seleccion)
        print(f"\n🗑️ Tarea eliminada: {tarea_eliminada[0]}")

    except ValueError:
        print("❌ Entrada no válida. Debe ser un número.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
    finally:
        print("📌 Proceso de eliminar tarea finalizado.")

    return lista_tareas
