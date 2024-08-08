def print_board(board): #board is a list of list - 2D array - matrix basicaly 
    print("***************")
    #make for loops to print the rows not manually - I will try manualy first 
    print(f"* {board[0][0]}  | {board[0][1]} | {board[0][2]}  *")
    #line 2 breakline needs to be printed here - I wont print breakline because it makes things more complex unnecesary.    print("_ _ _ | _ _ _ | _ _ _")
    print(f"* {board[1][0]}  | {board[1][1]} | {board[1][2]}  *")
    #line 4 breakline needs to be printed here  - I wont print breakline because it makes things more complex unnecesary.
    print(f"* {board[2][0]}  | {board[2][1]} | {board[2][2]}  *")
    print("***************")


def check_win(board):
    """Arguments are in a 3x3 nested list - TicTacToe board
    Returns true if there is a winner and false otherwise"""

    #check rows for horizontal win
    for row in range(len(board)):
        if row[0] == row[1] == row[2] != ' ':
            return True
        
    #check for vertical wins
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True
        
    #check for diagonal wins
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    elif board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    else:
        return False



def make_turn(board, row, col, player_input): # -> a string, returning the result of the turn 

    #so once we have the arguments, we are going to first check for mistakes and only then record the move

    if row <0 or row > 2 or col <0 or col > 2:
        return "Invalid input, you must enter a row and a column between 0 and 2"
    
    if board[row][col] != ' ':
        return "That spot is already taken, try another spot"
    
    board[row][col] = player_input

    return board




def main():
    board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    player_1 = "Player 1"
    player_2 = "Player 2"
    current_player = player_1
    print_board(board)

    while True:
        print(f"{current_player} - enter the row and column to place the mark:")
        row,col=map(int,input().split())
     # Gabriel: add here the logic to check if the row and column are valid - I did that in make_turn function
    
        # add to check whos turn it is
        # add check for tie (after 9 plays)
        board[row][col]='X'
        print_board(board)

main()