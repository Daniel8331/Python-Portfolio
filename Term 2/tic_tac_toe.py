# Daniel Embley
# Tic Tac Toe
# 11/11

# Global Constants
X = "X"
O= "O"
EMPTY =" "
TIE = "Tie"
NUM_SQUARES = 9

# Working
def intro():
    """ Display Game Instructions """
    print(
    """
    Welcome to the greatest intellectual challengs of all time: Tic-Tac-Toe.
    This will be a showdown between you human brain and my silicon processor.

    You will make your move known by entering a number, 1 - 9. They number will
    correspond to the board position as illustrated:

                        1  |  2  |  3
                        ------------
                        4  |  5  |  6
                        ------------
                        7  |  8  |  9

    Prepare yourself, human. The ultimate battle is about to begin. \n
    """
    )

def new_board():
    board = []
    for i in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """Display Game Board on Screen """
    print(str.format ("""
                        {0}  |  {1}  |  {2}
                        --------------------
                        {3}  |  {4}  |  {5}
                        --------------------
                        {6}  |  {7}  |  {8}
    """,board[0] ,board[1] ,board[2] ,
         board[3] ,board[4] ,board[5] ,
         board[6] ,board[7] ,board[8]))

def ask_yes_no(question):
    """Ask a Yes or No question, and give a one letter response back"""
    response = None

    while response not in ("y","n","yes","no"):
        response = input(question).lower()
    x = response[0]
    return x

def assign_peice():
    """Assign Peices According to Who Goes First"""
    go_first = ask_yes_no ("Do you want to go first? (y/n)")

    if go_first == "y":
        player = X
        comp = O
    else:
        player = O
        comp = X
    return comp, player

def switch_turn(turn):
    if turn == X:
        return O
    else:
        return X

def ask_number(question, low, high):
    response = None
    while response not in range(low,high):
        try:
            response = int(input(question))
        except:
            print("Not a number")
    return response
            
def legal_moves(board):
    moves = []
    for square in range (NUM_SQUARES):
        if board [square] == EMPTY:
            moves.append(square)
    return moves

def player_turn(board, player):
    lm = legal_moves(board)
    move = None
    while move not in lm:
        move = ask_number("Enter a number between 1 and 9 " ,1,10)-1
        if move not in lm:
            print("\nThat sqare is already occupied, try something else. Choose another. \n")

    print("Fine...")
    return move

def winner (board):
    """Determine the game winner."""
    WAYS_TO_WIN = ((0, 1, 2),
                                (3, 4, 5) ,
                                (6, 7, 8) ,
                                (0, 3, 6) ,
                                (1, 4, 7) ,
                                (2, 5, 8) ,
                                (0, 4, 8) ,
                                (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None

def comp_turn(board, comp, player):
    copy_board = board[:]
    BEST_MOVES = (4,0,2,6,8,1,3,5,7)
    print("I shall take the square number", end=" ")
    
    for move in legal_moves(board):
        copy_board[move] = comp
        if winner(copy_board) == comp:
            print(move)
            return move
        copy_board[move] = EMPTY

    for move in legal_moves(board):
        copy_board[move] = player
        if winner(copy_board) == player:
            print(move)
            return move
        copy_board[move] = EMPTY

    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

def game():
    turn = X
    intro()
    board = new_board()
    display_board(board)
    comp, player = assign_peice()
    while not winner(board):
        if turn == player:
            move = player_turn(board,player)
            board [move] = player
        else:
            move = comp_turn(board, comp, player)
            board [move] = comp
        display_board(board)
        turn = switch_turn(turn)
    win = winner(board)
    if win == comp:
        print("You lose")
    elif win == player:
        print("You suck at this")
    else:
        print("Tie!")  
    
        








