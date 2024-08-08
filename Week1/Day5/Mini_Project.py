def print_board(board): #board is a list of list - 2D array - matrix basicaly 
    print("***************")
    #make for loops to print the rows not manually - I will try manualy first 
    print(f"* {board[0][0]}  | {board[0][1]} | {board[0][2]}  *")
    #line 2 breakline needs to be printed here - I wont print breakline because it makes things more complex unnecesary.    print("_ _ _ | _ _ _ | _ _ _")
    print(f"* {board[1][0]}  | {board[1][1]} | {board[1][2]}  *")
    #line 4 breakline needs to be printed here  - I wont print breakline because it makes things more complex unnecesary.
    print(f"* {board[2][0]}  | {board[2][1]} | {board[2][2]}  *")
    print("***************")

def player_input(player):
    """Get a valid move from the player."""
    while True:
        try:
            print(f"{player}, enter your move as row and column numbers (0-2):")
            row, col = map(int, input().split())
            if row in range(3) and col in range(3): #ensuring the valid input, inside the 3x3 matrix    
                return row, col
            else:
                print("Invalid input. Please enter row and column numbers between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter two numbers separated by space.")

def check_win(board):
    """Returns True if there is a winner, False otherwise."""
    # Check rows for horizontal win
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True
        
    # Check for vertical wins
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True
        
    # Check for diagonal wins
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False

def check_tie(board):
    """Returns True if the game is a tie, False otherwise."""
    for row in board:
        if ' ' in row:
            return False
    return True

def make_turn(board, row, col, player_mark):
    """Updates the board with the player's move if valid."""
    if board[row][col] == ' ':
        board[row][col] = player_mark
        return True
    else:
        return False

def main():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    player_1 = "Player 1"
    player_2 = "Player 2"
    marks = {'Player 1': 'X', 'Player 2': 'O'} #This dictionary helps keep track of which symbol (mark) each player is using.
    current_player = player_1
    
    print_board(board)
    
    while True:
        # Get player input
        row, col = player_input(current_player)

        # Attempt to make the move
        if make_turn(board, row, col, marks[current_player]):
            """#we use this dictionary to determine which mark to place on the board for the current player:
            marks[current_player]: This expression looks up the current player's mark in the dictionary. 
            If current_player is 'Player 1', it returns 'X'. If current_player is 'Player 2', it returns 'O"""
            print_board(board)
        else:
            print("That spot is already taken, try another spot.")
            continue

        # Check for a win
        if check_win(board):
            print(f"Congratulations, {current_player}! You've won!")
            break

        # Check for a tie
        if check_tie(board):
            print("The game is a tie!")
            break

        # Switch players
        if current_player == player_1:
            current_player = player_2
        else:
            current_player = player_1

        # # more complicated way to switch players, basicaly the same as written in 93-96, would be:
        # current_player = player_2 if current_player == player_1 else player_1

main()
