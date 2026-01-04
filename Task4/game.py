import math

board = [" " for _ in range(9)]

# Print board
def print_board():
    print()
    for i in range(3):
        print(board[i*3], "|", board[i*3+1], "|", board[i*3+2])
        if i != 2:
            print("--+---+--")
    print()

# Check winner
def check_winner(player):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in win_combos:
        if all(board[i] == player for i in combo):
            return True
    return False

# Check draw
def is_draw():
    return " " not in board

# Minimax algorithm
def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# AI move
def ai_move():
    best_score = -math.inf
    best_move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = "O"

# Human move
def human_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("That spot is taken.")
        except:
            print("Invalid input!")

# Game loop
print("TIC TAC TOE – You (X) vs AI (O)")
print("Positions:")
print("1|2|3\n4|5|6\n7|8|9")

while True:
    print_board()
    human_move()
    if check_winner("X"):
        print_board()
        print("🎉 You Win!")
        break
    if is_draw():
        print("🤝 Draw!")
        break

    ai_move()
    if check_winner("O"):
        print_board()
        print("😈 AI Wins!")
        break
    if is_draw():
        print("🤝 Draw!")
        break
