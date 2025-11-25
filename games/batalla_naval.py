import random

def jugar_batalla_naval():

    tamaño_tablero = 5

    print("\n=== 🚢 BATALLA NAVAL ===")
    print(f"El tablero es de {tamaño_tablero}x{tamaño_tablero} casillas.")
    print("Ingresa coordenadas como 'fila,col' (ej: 2,3)")
    print("Escribe 'rendirse' o 'salir' para terminar el juego.\n")

    # Crear tablero
    tablero = [["~"] * tamaño_tablero for _ in range(tamaño_tablero)]
    fila = random.randint(0, tamaño_tablero - 1)
    col_inicio = random.randint(0, tamaño_tablero - 3)

    for c in range(col_inicio, col_inicio + 3):
        tablero[fila][c] = "B"

    # Estado del juego
    estado = {
        "intentos": 0,
        "impactos": 0,
        "resultado": "en curso"
    }

    max_turnos = 10

    for turno in range(1, max_turnos + 1):
        print(f"\n🔄 Turno {turno}/{max_turnos}")
        entrada = input("Disparo (fila,col) o 'rendirse/salir': ").strip().lower()

        # Fin del juego por rendición
        if entrada in ("rendirse", "salir"):
            print("🏳️ Te rendiste. Fin del juego.")
            estado["resultado"] = "rendido"
            return estado

        # Procesar entrada
        try:
            fil, col = [int(x) for x in entrada.replace(" ", "").split(",")]
            fil -= 1
            col -= 1
        except:
            print("⚠️  Entrada inválida. Usa el formato fila,col.")
            continue

        # Validar límites
        if not (0 <= fil < tamaño_tablero and 0 <= col < tamaño_tablero):
            print("⛔ Coordenadas fuera del tablero.")
        else:
            estado["intentos"] += 1
            if tablero[fil][col] == "B":
                print("🔥 ¡Tocado!")
                tablero[fil][col] = "X"
                estado["impactos"] += 1

                if estado["impactos"] == 3:
                    print("🎉 ¡Hundiste el barco! Ganaste.")
                    estado["resultado"] = "ganado"
                    return estado

            elif tablero[fil][col] in ("X", "O"):
                print("🔁 Ya disparaste ahí.")

            else:
                print("💧 Agua.")
                tablero[fil][col] = "O"

    print("\n⏳ Se acabaron los turnos. Fin del juego.")
    estado["resultado"] = "perdido"
    return estado