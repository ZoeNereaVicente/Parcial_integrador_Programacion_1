import os
from .jugar import jugar

def cargar_juegos_desde_txt(ruta_txt):
    juegos = []
    archivo = None
    try:
        archivo = open(ruta_txt, "r", encoding="utf-8")
        for linea in archivo:
            linea = linea.strip()
            # Validamos la línea e ignoramos la línea si comienza con #
            if linea and not linea.startswith("#"):
                # Creamos una lista separando los valores de cada linea
                partes = linea.split(";")                
                if len(partes) == 2:
                    nombre, costo_str = partes
                    if costo_str.strip().isdigit():
                        juegos.append({"nombre": nombre.strip(), "costo": int(costo_str)})
    except FileNotFoundError:
        print("❌  No se encontró el archivo.")
        return juegos
    except Exception as e:
        print(f"❌ Hubo un error inesperado: {e}")
        return juegos
    finally:
        if archivo:
            archivo.close()
    return juegos


def canjear_puntos(puntos):
    if puntos <= 0:
        print("❌ No tienes puntos para canjear.")
        return puntos

    ruta_txt = os.path.join(os.path.dirname(__file__), "..", "files", "juegos.txt")

    juegos = cargar_juegos_desde_txt(ruta_txt)

    if not juegos:
        print("❌ No hay juegos disponibles para canjear. Verifica 'juegos.txt'.")
        return puntos

    print(f"\nTienes {puntos} puntos disponibles.")
    print("Juegos disponibles para canjear:")

    canjeables = []
    for juego in juegos:
        if juego["costo"] <= puntos:
            canjeables.append(juego)
    canjeables.append({'nombre': "ALGO", 'costo': 8})
    if not canjeables:
        print("❌ No tienes suficientes puntos para ningún juego.")
        print(f"Te quedan {puntos} puntos.")
        return puntos

    numero_opcion = 1
    for juego in canjeables:
        print(f"{numero_opcion}. {juego['nombre']} ({juego['costo']} puntos)")
        numero_opcion = numero_opcion + 1
    print("0. Volver")
    
    eleccion = input("Elige una opción: ")

    if eleccion == "0":
        print("Volviendo al menú...")
        print(f"Te quedan {puntos} puntos.")
        return puntos

    if not eleccion.isdigit():
        print("❌ Entrada inválida.")
        print(f"Te quedan {puntos} puntos.")
        return puntos

    indice = int(eleccion) - 1
    if indice < 0 or indice >= len(canjeables):
        print("❌ Opción inválida.")
        print(f"Te quedan {puntos} puntos.")
        return puntos

    seleccionado = canjeables[indice]
    costo = seleccionado["costo"]
    puntos -= costo
    print(f"✅ Canje realizado: '{seleccionado['nombre']}' por {costo} puntos.")
    print(f"Te quedan {puntos} puntos.")
    print()

    # Esta función se encarga de ejecutar el juego seleccionado.
    # En caso de no encontrar el juego devuelve un booleano.
    hayError = jugar(seleccionado['nombre'])

    if (hayError):
        # Devolvemos los puntos al usuario
        puntos += costo
        print("Acreditando nuevamente los puntos...")
        print(f"✅ Acreditación realizada, te quedan {puntos} puntos.")

    return puntos
