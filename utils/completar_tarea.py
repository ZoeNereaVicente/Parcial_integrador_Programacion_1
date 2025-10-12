from .ver_tareas import ver_tareas

def completar_tarea(lista_tareas, puntos):
    """Permite marcar una tarea como completada y ganar puntos."""
    tarea_existe = ver_tareas(lista_tareas, puntos)

    if tarea_existe:
        try:
            entrada = input("Ingresa el número de la tarea que completaste: ").strip()
            if not entrada.isdigit():
                print("❌ Entrada no válida. Debes ingresar un número entero.")
                return lista_tareas, puntos

            indice_tarea = int(entrada) - 1

            # Validar que el índice esté dentro del rango de la lista
            if 0 <= indice_tarea < len(lista_tareas):
                estado_actual = lista_tareas[indice_tarea][1]
                
                if not estado_actual:
                    lista_tareas[indice_tarea][1] = True
                    puntos_ganados = 10
                    puntos += puntos_ganados
                    print(f"🥳 ¡Felicitaciones! Completaste la tarea y ganaste {puntos_ganados} puntos.")
                else:
                    print("⚠️ Esa tarea ya estaba completada.")
            else:
                print("❌ Número de tarea fuera de rango. Intenta con un número válido.")
        
        except Exception as e:
            print(f"❌ Ocurrió un error al completar la tarea: {e}")
        finally:
            print("📌 Proceso de completar tarea finalizado.")
    else:
        print("⚠️ No hay tareas disponibles para completar.")
    
    return lista_tareas, puntos