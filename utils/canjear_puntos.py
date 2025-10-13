import random

# Minijuegos con validaciones

def jugar_adivinanza():
    print("\n🎯 Juego de Adivinanza")
    numero = random.randint(1, 10)
    while True:
        intento = input("Adivina el número del 1 al 10: ")
        if intento.isdigit():
            intento = int(intento)
            if 1 <= intento <= 10:
                break
            else:
                print("❌ El número debe estar entre 1 y 10.")
        else:
            print("❌ Entrada inválida. Debes ingresar un número.")
    if intento == numero:
        print("¡Correcto! Ganaste.")
    else:
        print(f"Incorrecto. El número era {numero}.")

def jugar_trivia():
    print("\n🧠 Juego de Trivia")
    print("¿Cuál es la capital de Francia?")
    print("1. Berlín\n2. Madrid\n3. París\n4. Roma")
    while True:
        respuesta = input("Tu respuesta (1-4): ")
        if respuesta in ["1", "2", "3", "4"]:
            break
        else:
            print("❌ Entrada inválida. Elige una opción del 1 al 4.")
    if respuesta == "3":
        print("¡Correcto!")
    else:
        print("Incorrecto. La respuesta correcta es París.")

def jugar_batalla_naval():
    print("\n🚢 Batalla Naval Simplificada")
    barco = random.randint(1, 9)
    while True:
        intento = input("Elige una posición del 1 al 9 para atacar: ")
        if intento.isdigit():
            intento = int(intento)
            if 1 <= intento <= 9:
                break
            else:
                print("❌ La posición debe estar entre 1 y 9.")
        else:
            print("❌ Entrada inválida. Debes ingresar un número.")
    if intento == barco:
        print("¡Hundiste el barco!")
    else:
        print(f"Fallaste. El barco estaba en la posición {barco}.")

def jugar_memoria():
    print("\n🧠 Juego de Memoria")
    pares = ["🐶", "🐱", "🐶", "🐱"]
    random.shuffle(pares)
    print("Recuerda la posición de los pares:")
    print(pares)
    input("Presiona Enter cuando estés listo para responder...")
    while True:
        respuesta = input("¿Dónde estaba el segundo 🐶? (0-3): ")
        if respuesta.isdigit():
            respuesta = int(respuesta)
            if 0 <= respuesta <= 3:
                break
            else:
                print("❌ Debes ingresar un número entre 0 y 3.")
        else:
            print("❌ Entrada inválida. Debes ingresar un número.")
    if pares[respuesta] == "🐶" and pares.index("🐶") != respuesta:
        print("¡Correcto!")
    else:
        print("Incorrecto.")

def jugar_piedra_papel_tijera():
    print("\n✊🖐✌ Piedra, Papel o Tijera")
    opciones = ["piedra", "papel", "tijera"]
    while True:
        usuario = input("Elige piedra, papel o tijera: ").lower()
        if usuario in opciones:
            break
        else:
            print("❌ Entrada inválida. Elige entre piedra, papel o tijera.")
    maquina = random.choice(opciones)
    print(f"La máquina eligió: {maquina}")
    if usuario == maquina:
        print("Empate!")
    elif (usuario == "piedra" and maquina == "tijera") or \
         (usuario == "papel" and maquina == "piedra") or \
         (usuario == "tijera" and maquina == "papel"):
        print("¡Ganaste!")
    else:
        print("Perdiste.")

# Función principal para canjear puntos

def canjear_puntos(puntos):
    if puntos <= 0:
        print("❌ No tienes puntos para canjear.")
        return puntos

    juegos_disponibles = {
        "1": {"nombre": "Adivinanza", "costo": 5, "funcion": jugar_adivinanza},
        "2": {"nombre": "Trivia", "costo": 5, "funcion": jugar_trivia},
        "3": {"nombre": "Batalla Naval", "costo": 10, "funcion": jugar_batalla_naval},
        "4": {"nombre": "Memoria", "costo": 7, "funcion": jugar_memoria},
        "5": {"nombre": "Piedra, Papel o Tijera", "costo": 5, "funcion": jugar_piedra_papel_tijera}
    }

    print(f"\n🎮 Tienes {puntos} puntos disponibles.")
    print("Minijuegos disponibles para canjear:")

    for clave, juego in juegos_disponibles.items():
        print(f"{clave}. {juego['nombre']} ({juego['costo']} puntos)")
    print("0. Volver")

    eleccion = input("Elige una opción: ").strip()

    if eleccion == "0":
        print("🔙 Volviendo al menú...")
    elif eleccion in juegos_disponibles:
        juego = juegos_disponibles[eleccion]
        if puntos >= juego["costo"]:
            puntos -= juego["costo"]
            juego["funcion"]()
        else:
            print("⚠️ No tienes puntos suficientes para este minijuego.")
    else:
        print("❌ Opción inválida o puntos insuficientes.")

    print(f"💰 Te quedan {puntos} puntos.")
    return puntos