import random

def jugar_piedra_papel_tijera():

    print("👊 Piedra, 📄 Papel o ✂ Tijera")
    print("Elige una opción:")
    print("1 = 👊 Piedra")
    print("2 = 📄 Papel")
    print("3 = ✂ Tijera")
    print("0 = Salir del juego")

    opciones = {1: "👊 Piedra", 2: "📄 Papel", 3: "✂ Tijera"}

    # Evita que el programa se corte si ingresan letras
    def pedir_opcion(mensaje):
        intento = 0
        while intento < 3: 
            try:
                valor = int(input(mensaje))
                return valor
            except ValueError:
                intento += 1
                print("❌ Entrada no válida. Debes ingresar un número entero (0-3).")
                print(f"Intentos restantes: {3 - intento}")
        print("❌ Se agotaron los intentos. Se tomará la opción 0 (salir).")
        return 0

    # Primera elección del usuario
    usuario = pedir_opcion("Tu elección (0-3): ")
    seguir_jugando = True

    while seguir_jugando:

        # Validación de rango 
        if usuario < 0 or usuario > 3:
            print("⚠️  Opción fuera de rango. Elegí 0, 1, 2 o 3.")
            usuario = pedir_opcion("Tu elección (0-3): ")

        else:

            # Opción para salir
            if usuario == 0:
                seguir_jugando = False

            else:
                # Elección de la computadora
                computadora = random.randint(1, 3)

                print("Tú elegiste:", opciones[usuario])
                print("La computadora eligió:", opciones[computadora])

                # Caso de empate: se sigue jugando
                if usuario == computadora:
                    print("🤝 ¡Empate! Se juega de nuevo...\n")
                    usuario = pedir_opcion("Elegí nuevamente (1-3) o 0 para salir: ")

                else:
                    # Determina el ganador
                    if (usuario == 1 and computadora == 3) or \
                       (usuario == 2 and computadora == 1) or \
                       (usuario == 3 and computadora == 2):
                        print("🎉 ¡Ganaste!")
                    else:
                        print("💻 La computadora ganó.")

                    seguir_jugando = False

    print("Gracias por jugar 🙌")


