import random

def jugar_piedra_papel_tijera():
    """Ejecuta el juego de Piedra, Papel o Tijera."""
    print("👊 Piedra, 📄 Papel o ✂️  Tijera")
    print("Elige una opción:")
    print("1 = 👊 Piedra")
    print("2 = 📄 Papel")
    print("3 = ✂️  Tijera")

    try:
        usuario = int(input("Tu elección (1-3): "))

        if usuario < 1 or usuario > 3:
            print("⚠️ Opción fuera de rango. Debes elegir 1, 2 o 3.")
        else:

            empate = True
            while empate:
                computadora = random.randint(1, 3)
                opciones = {1: "👊 Piedra", 2: "📄 Papel", 3: "✂️  Tijera"}

                print(f"Tú elegiste: {opciones[usuario]}")
                print(f"La computadora eligió: {opciones[computadora]}")

                if usuario == computadora:
                    print("🤝 ¡Empate! Se juega otra vez...\n")
                    # vuelve a pedir elección del usuario
                    usuario = int(input("Elige nuevamente (1-3): "))
                    while usuario < 1 or usuario > 3:
                        print("⚠️ Opción fuera de rango. Debes elegir 1, 2 o 3.")
                        usuario = int(input("Elige nuevamente (1-3): "))
                else:
                    empate = False
                    if (usuario == 1 and computadora == 3) or \
                    (usuario == 2 and computadora == 1) or \
                    (usuario == 3 and computadora == 2):
                        print("🎉 ¡Ganaste!")
                    else:
                        print("💻 La computadora ganó.")

    except ValueError:
        print("❌ Entrada no válida. Debes ingresar un número entero (1, 2 o 3).")

    finally:
        print("Gracias por jugar 🙌")
