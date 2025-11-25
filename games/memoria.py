import random

# -----------------------------------------
# Generar tablero utilizando diccionarios
# -----------------------------------------
def generar_tablero():
    letras = ["A", "B", "C", "D"]
    pares = letras * 2
    random.shuffle(pares)

    tablero = {i + 1: pares[i] for i in range(8)}
    descubiertas = {i + 1: False for i in range(8)}
    return tablero, descubiertas


# -----------------------------------------
# Mostrar tablero
# -----------------------------------------
def mostrar_tablero(tablero, descubiertas):
    print("\n🧩 TABLERO:")
    for i, letra in tablero.items():
        if descubiertas[i]:
            print(f"[{i}:{letra}]", end="  ")
        else:
            print(f"[{i}:*]", end="  ")

        if i % 4 == 0:
            print()
    print()


# -----------------------------------------
# Validación segura de elección
# -----------------------------------------
def pedir_posicion(descubiertas, mensaje):
    entrada = input(mensaje).strip().lower()

    # Permitir salir del juego
    if entrada == "salir":
        return "salir"

    if not entrada.isdigit():
        print("⚠️  Error: Debes ingresar un número válido (1-8) o 'salir'.")
        return pedir_posicion(descubiertas, mensaje)

    numero = int(entrada)

    if numero not in descubiertas:
        print("⚠️  Error: Esa posición no existe en el tablero.")
        return pedir_posicion(descubiertas, mensaje)

    if descubiertas[numero]:
        print("⚠️  Error: Esa casilla ya está descubierta.")
        return pedir_posicion(descubiertas, mensaje)

    return numero


# -----------------------------------------
# Lógica principal del juego
# -----------------------------------------
def turno(tablero, descubiertas):
    # Caso base → si ya gano
    if all(descubiertas.values()):
        print("🎉 ¡Felicitaciones! Descubriste todas las parejas.")
        return

    mostrar_tablero(tablero, descubiertas)

    # Pedir primera posición
    posicion1 = pedir_posicion(descubiertas, "👉 Elegí la primera casilla (1-8 o 'salir'): ")
    if posicion1 == "salir":
        print("👋 Juego finalizado por el usuario.")
        return

    # Pedir segunda posición
    posicion2 = pedir_posicion(descubiertas, "👉 Elegí la segunda casilla (1-8 o 'salir'): ")
    if posicion2 == "salir":
        print("👋 Juego finalizado por el usuario.")
        return

    print(f"\n🔍 Elegiste {posicion1} → {tablero[posicion1]}")
    print(f"🔍 Elegiste {posicion2} → {tablero[posicion2]}\n")

    if tablero[posicion1] == tablero[posicion2]:
        print("✅ ¡Acertaste! Se descubrió una pareja.\n")
        descubiertas[posicion1] = True
        descubiertas[posicion2] = True
    else:
        print("❌ No acertaste. ¡Seguí intentando!\n")

    # Llamada recursiva → siguiente ronda
    turno(tablero, descubiertas)


# -----------------------------------------
# Inicio del juego
# -----------------------------------------
def jugar_memoria():
    print("\n=== 🧠 JUEGO DE MEMORIA ===")
    print("Escribí 'salir' en cualquier momento para terminar la partida.\n")

    tablero, descubiertas = generar_tablero()
    turno(tablero, descubiertas)
