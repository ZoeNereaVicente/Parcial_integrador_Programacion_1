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

    print(f"\nTienes {puntos} puntos disponibles.")
    print("Minijuegos disponibles:")

    opciones = []
    if puntos >= 5:
        print("1. Adivinanza (5 puntos)")
        opciones.append("1")
    if puntos >= 5:
        print("2. Trivia (5 puntos)")
        opciones.append("2")
    if puntos >= 10:
        print("3. Batalla Naval (10 puntos)")
        opciones.append("3")
    if puntos >= 7:
        print("4. Memoria (7 puntos)")
        opciones.append("4")
    if puntos >= 5:
        print("5. Piedra, Papel o Tijera (5 puntos)")
        opciones.append("5")
    print("0. Volver")

    eleccion = input("Elige una opción: ")

    if eleccion == "1" and "1" in opciones:
        puntos -= 5
        jugar_adivinanza()
    elif eleccion == "2" and "2" in opciones:
        puntos -= 5
        jugar_trivia()
    elif eleccion == "3" and "3" in opciones:
        puntos -= 10
        jugar_batalla_naval()
    elif eleccion == "4" and "4" in opciones:
        puntos -= 7
        jugar_memoria()
    elif eleccion == "5" and "5" in opciones:
        puntos -= 5
        jugar_piedra_papel_tijera()
    elif eleccion == "0":
        print("Volviendo al menú...")
    else:
        print("❌ Opción inválida o puntos insuficientes.")

    print(f"Te quedan {puntos} puntos.")
    return puntos