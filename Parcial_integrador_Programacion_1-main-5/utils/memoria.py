#!/usr/bin/env python3
"""
Juego de Memoria (Consola)
- Usa recursividad (play_round es recursivo para continuar hasta ganar)
- Usa diccionarios (board: posición -> valor, revealed: posición -> bool)
- Validaciones complejas de entrada (formato, rango, ya revelado, pares impares, etc.)

Uso: python memoria.py
"""

import random, string, re, sys, math, time

EMOJIS = ["🍎","🍌","🍇","🍓","🍒","🍑","🍍","🥝","🍉","🥥","🍐","🍊","🍋","🍈","🥭","🍏"]

def clear_screen():
    print("\\n" * 30)

def build_board(rows, cols):
    total = rows * cols
    if total % 2 != 0:
        raise ValueError("El tablero debe tener un número par de casillas (filas*columnas).")
    # choose symbols
    needed_pairs = total // 2
    symbols = EMOJIS.copy()
    if needed_pairs > len(symbols):
        # generate number labels if not enough emojis
        symbols.extend([f"{i}" for i in range(1, needed_pairs - len(symbols) + 1)])
    chosen = symbols[:needed_pairs] * 2
    random.shuffle(chosen)
    # positions like A1, A2... B1...
    board = {}
    idx = 0
    for r in range(rows):
        for c in range(cols):
            pos = f"{string.ascii_uppercase[r]}{c+1}"
            board[pos] = chosen[idx]
            idx += 1
    return board

def render_board(rows, cols, revealed, last_two=None):
    # last_two: list of positions to temporarily reveal
    header = "   " + "  ".join([str(c+1).rjust(2) for c in range(cols)])
    print(header)
    for r in range(rows):
        row_label = string.ascii_uppercase[r]
        line = [row_label.rjust(2)]
        for c in range(cols):
            pos = f"{row_label}{c+1}"
            if revealed.get(pos, False) or (last_two and pos in last_two):
                line.append(str(board[pos]).rjust(2))
            else:
                line.append("■".rjust(2))
        print(" ".join(line))
    print("")

def validate_size(inp):
    # accept like '4x4' or '3 x 4' or two numbers separated by space/comma
    match = re.match(r"^\s*(\d+)\s*[x, ]\s*(\d+)\s*$", inp, re.I)
    if not match:
        raise ValueError("Formato inválido. Ejemplo válido: 4x4 o 3 4")
    r = int(match.group(1)); c = int(match.group(2))
    if r <= 0 or c <= 0:
        raise ValueError("Filas y columnas deben ser enteros positivos.")
    if r * c > 100:
        raise ValueError("Tablero demasiado grande (máx 100 casillas).")
    return r, c

def normalize_pos(pos, rows, cols):
    # Accepts inputs like 'a1', 'A1', '  B 2  '
    pos = pos.strip().upper().replace(" ", "")
    if not re.match(r"^[A-Z]\d+$", pos):
        raise ValueError("Posición inválida. Use formato LetraNúmero, p.ej. A1.")
    row = ord(pos[0]) - ord('A')
    col = int(pos[1:]) - 1
    if row < 0 or row >= rows or col < 0 or col >= cols:
        raise ValueError("Posición fuera de rango.")
    return f"{chr(ord('A') + row)}{col+1}"

def all_revealed(revealed):
    return all(revealed.values())

# recursion demonstrated here: the function calls itself until the game ends
def play_round(board, rows, cols, revealed, attempts, best_score, hint_tokens):
    clear_screen()
    print(f"Intentos: {attempts} | Mejores intentos (session): {best_score if best_score is not None else '---'} | Pistas restantes: {hint_tokens}")
    render_board(rows, cols, revealed)
    if all_revealed(revealed):
        print("¡Felicidades! Completaste el tablero.")
        return attempts
    # input validations (complejas)
    try:
        raw1 = input("Elige primera casilla (o 'H' para pista): ").strip()
        if raw1.upper() == "H":
            if hint_tokens <= 0:
                print("No te quedan pistas.")
                time.sleep(1.2)
                return play_round(board, rows, cols, revealed, attempts, best_score, hint_tokens)
            # give a hint: reveal a random unrevealed pair temporarily
            unrevealed = [p for p, v in revealed.items() if not v]
            if not unrevealed:
                return play_round(board, rows, cols, revealed, attempts, best_score, hint_tokens)
            sample = random.choice(unrevealed)
            val = board[sample]
            pair = [p for p, val2 in board.items() if val2 == val and not revealed[p]]
            print(f"Pista: la casilla {sample} forma pareja con {', '.join(pair)}")
            hint_tokens -= 1
            time.sleep(2)
            return play_round(board, rows, cols, revealed, attempts, best_score, hint_tokens)
        p1 = normalize_pos(raw1, rows, cols)
        if revealed.get(p1, False):
            print("Esa casilla ya está descubierta. Elige otra.")
            time.sleep(1.2)
            return play_round(board, rows, cols, revealed, attempts, best_score, hint_tokens)
        raw2 = input("Elige segunda casilla: ").strip()
        p2 = normalize_pos(raw2, rows, cols)
        if p1 == p2:
            print("No puedes elegir la misma casilla dos veces.")
            time.sleep(1.2)
            return play_round(board, rows, cols, revealed, attempts, best_score, hint_tokens)
        if revealed.get(p2, False):
            print("La segunda casilla ya está descubierta. Elige otra.")
            time.sleep(1.2)
            return play_round(board, rows, cols, revealed, attempts, best_score, hint_tokens)
    except ValueError as e:
        print("Error de validación:", e)
        time.sleep(1.2)
        return play_round(board, rows, cols, revealed, attempts, best_score, hint_tokens)

    # reveal temporarily and show board
    clear_screen()
    print(f"Intentos: {attempts} | Pistas: {hint_tokens}")
    render_board(rows, cols, revealed, last_two=[p1,p2])
    time.sleep(1.2)

    attempts += 1
    if board[p1] == board[p2]:
        print("¡Encontraste una pareja!")
        revealed[p1] = True
        revealed[p2] = True
    else:
        print("No coinciden. Intenta de nuevo.")
    time.sleep(1.0)
    # recursive call to continue the game
    return play_round(board, rows, cols, revealed, attempts, best_score, hint_tokens)

def start_game():
    print("=== Juego de Memoria (Consola) ===")
    print("Introduce el tamaño del tablero en formato 'filas x columnas' (ej: 4x4). Debe ser par.")
    while True:
        try:
            size = input("Tamaño por defecto (4x4) o ingresa tamaño: ").strip() or "4x4"
            rows, cols = validate_size(size)
            break
        except ValueError as e:
            print("Error:", e)
    global board
    board = build_board(rows, cols)
    revealed = {pos: False for pos in board.keys()}
    attempts = 0
    best_score = None
    hint_tokens = max(1, (rows*cols)//8)  # some hints available
    final_attempts = play_round(board, rows, cols, revealed, attempts, best_score, hint_tokens)
    print(f"Completaste el juego en {final_attempts} intentos. ¡Gracias por jugar!")

if __name__ == "__main__":
    try:
        start_game()
    except KeyboardInterrupt:
        print("\\nJuego interrumpido. Hasta la próxima.")