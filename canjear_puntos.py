def canjear_puntos(puntos):
    """Permite 'canjear' puntos, verificando que el usuario tenga suficientes."""
    try:
        puntos_a_canjear = int(input(f"Tienes {puntos} puntos. ¿Cuántos puntos quieres canjear? "))
        
        if puntos_a_canjear <= 0:
            print("❌ Debes canjear un valor positivo.")
        elif puntos_a_canjear <= puntos:
            puntos -= puntos_a_canjear
            print(f"🎉 ¡Canje exitoso! Canjeaste {puntos_a_canjear} puntos.")
            print(f"Te quedan {puntos} puntos.")
        else:
            print(f"❌ No tienes suficientes puntos para canjear esa cantidad. Solo tienes {puntos} puntos.")
    except ValueError:
        print("❌ Entrada no válida. Por favor, ingresa un número.")
    except Exception as e:
        print(f"❌ Ocurrió un error al canjear los puntos: {e}")
    finally:
        print("Proceso de canje de puntos finalizado.")
    return puntos