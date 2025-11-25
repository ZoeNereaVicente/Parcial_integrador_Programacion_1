import random

def jugar_adivinanza():
    """Juego de adivinanzas sencillo como mini recompensa/distractor."""
    # Lista de adivinanzas (lista de diccionarios)
    adivinanzas = [
        {"acertijo": "Blanca por dentro, verde por fuera. Si quieres que te lo diga, espera.", "respuesta": "pera", "pista":"Es una fruta."},
        {"acertijo": "Tiene agujas pero no cose; tiene números pero no cuenta.", "respuesta": "reloj", "pista":"Marca las horas."},
        {"acertijo": "Blanca por la mañana, roja al mediodía y negra por la noche; ¿qué es?", "respuesta": "la manzana", "pista":"Fruta clásica."},
        {"acertijo": "No es madera y tiene hojas; no es libro y tiene páginas; ¿qué es?", "respuesta": "árbol", "pista":"Crece en la tierra."},
        {"acertijo": "Camina sin patas y enseña el hogar; lleva su casa siempre al caminar.", "respuesta": "caracol", "pista":"Lento y con caparazón."}
    ]

    indices_disponibles = set(range(len(adivinanzas)))
    adivinanzas_correctas = 0
    max_aciertos = 2  # límite de aciertos para terminar el juego

    print("\n🎲 Bienvenid@ al juego de Adivinanzas — 'Adivina y Gana'!")
    print("Tienes 3 oportunidades por adivinanza. Puedes pedir pista (escribe 'pista').")
    print("Escribe 'salir' en cualquier momento para volver al menú principal.")

    while indices_disponibles and adivinanzas_correctas < max_aciertos:
        idx = random.choice(list(indices_disponibles))
        ad = adivinanzas[idx]
        indices_disponibles.remove(idx)

        intentos = 3
        usado_pista = False

        while intentos > 0:
            print(f"\nAdivinanza: {ad['acertijo']}")
            respuesta_usuario = input("Tu respuesta: ").strip().lower()

            if respuesta_usuario == 'salir':
                print("Saliendo del juego...")
                return
            if respuesta_usuario == 'pista':
                if not usado_pista:
                    print(f"💡 Pista: {ad['pista']}")
                    usado_pista = True
                else:
                    print("Ya usaste la pista para esta adivinanza.")
                continue

            # Normalizar respuesta
            palabras_usuario = set(respuesta_usuario.split())
            palabras_solucion = set(ad['respuesta'].split())

            if palabras_usuario & palabras_solucion:
                print("✅ ¡Correcto!")
                adivinanzas_correctas += 1
                break
            else:
                intentos -= 1
                if intentos > 0:
                    print(f"❌ Incorrecto. Te quedan {intentos} intentos.")
                else:
                    print(f"❌ Se terminaron los intentos. La respuesta correcta era: '{ad['respuesta']}'")

        if adivinanzas_correctas >= max_aciertos:
            print("\n🎉 Has alcanzado el límite de aciertos. ¡Buen trabajo!")
            return

        # Preguntar si quiere seguir jugando (opcional, dentro del límite de aciertos)
        seguir = input("\n¿Querés otra adivinanza? (s/n): ").strip().lower()
        if seguir not in ('s','si','y','yes'):
            print("Volviendo al menú principal...")
            return
