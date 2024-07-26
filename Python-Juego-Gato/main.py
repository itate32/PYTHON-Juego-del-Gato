# array de 3x3 para el tablero
board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

# función para imprimir en el tablero
def print_board(board):
    for row in board:
        print(" ".join(row))

# función para validar si un jugador ha ganado
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)):
        return True
    
    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

# primer ciclo del juego
current_player = "X"
while True:
    print_board(board)
    
    # Obtener el imput del jugador
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))
    
    # valida si la celda elegida está vacía
    if board[row][col] != "_":
        print("Cell already taken. Try again.")
        continue
    
    # Imprime el símbolo del jugador en el tablero
    board[row][col] = current_player
    
    # Valida si el jugador actual ha ganado
    if check_winner(board, current_player):
        print_board(board)
        print(f"Player {current_player} wins!")
        break
    
    # Comprobar si hay empate
    if all(all(cell != "_" for cell in row) for row in board):
        print_board(board)
        print("It's a tie!")
        break
    
    # Alterna los jugadores
    current_player = "O" if current_player == "X" else "X"