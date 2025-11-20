def jugar_piedra_papel_tijera():
    import random

    print("👊 Piedra, 📄 Papel o ✂ Tijera")
    print("Elige una opción:")
    print("1 = 👊 Piedra")
    print("2 = 📄 Papel")
    print("3 = ✂ Tijera")
    print("0 = Salir del juego")

    try:
        usuario = int(input("Tu elección (0-3): "))

        if usuario < 0 or usuario > 3:
            print("⚠️ Opción fuera de rango. Debes elegir 0, 1, 2 o 3.")
            return

        seguir_jugando = True

        if usuario == 0:
            seguir_jugando = False

        opciones = {1: "👊 Piedra", 2: "📄 Papel", 3: "✂ Tijera"}

        while seguir_jugando:

            computadora = random.randint(1, 3)

            print("Tú elegiste:", opciones[usuario])
            print("La computadora eligió:", opciones[computadora])

            if usuario == computadora:
                print("🤝 ¡Empate! Se juega de nuevo...\n")

                usuario = int(input("Elige nuevamente (1-3) o 0 para salir: "))

                if usuario < 0 or usuario > 3:
                    print("⚠️ Opción fuera de rango. Debes elegir 0, 1, 2 o 3.")
                    seguir_jugando = False
                elif usuario == 0:
                    seguir_jugando = False

            else:
                seguir_jugando = False
                if (usuario == 1 and computadora == 3) or \
                   (usuario == 2 and computadora == 1) or \
                   (usuario == 3 and computadora == 2):
                    print("🎉 ¡Ganaste!")
                else:
                    print("💻 La computadora ganó.")

    except ValueError:
        print("❌ Entrada no válida. Debes ingresar un número entero (0-3).")

    finally:
        print("Gracias por jugar 🙌")
