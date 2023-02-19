from random import randrange

game_board = [[1,2,3],[4,5,6],[7,8,9]]

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print(f'''
+-------+-------+-------+
|       |       |       |
|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
|       |       |       |
+-------+-------+-------+
    ''')


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    global game_board
    move = int(input("Choose a field from the following - " + str(make_list_of_free_fields(game_board)) + ":"))
    i_count = 0
    for i in board:
        j_count = 0
        for j in i:
            if j == move:
                game_board[i_count][j_count] = "O"
                return
            j_count += 1
        i_count += 1




def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    available_options = []
    for i in board:
        for j in i:
            if j in [1,2,3,4,5,6,7,8,9]:
                available_options.append(j)

    return available_options


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    if board[0][0] == board[0][1] == board[0][2] == sign or \
        board[1][0] == board[1][1] == board[1][2] == sign or \
        board[2][0] == board[2][1] == board[2][2] == sign or \
        board[0][0] == board[1][0] == board[2][0] == sign or \
        board[0][1] == board[1][1] == board[2][1] == sign or \
        board[0][2] == board[1][2] == board[2][2] == sign or \
        board[0][0] == board[1][1] == board[2][2] == sign or \
        board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    else:
        return False

def draw_move(board):
    # The function draws the computer's move and updates the board.
    global game_board
    options = make_list_of_free_fields(game_board)
    choice = options[randrange(0,len(options))]
    i_count = 0
    for i in board:
        j_count = 0
        for j in i:    
            if j == choice:
                game_board[i_count][j_count] = "X"
                return
            j_count += 1
        i_count += 1
            
        

display_board(game_board)
while True:
    draw_move(game_board)
    display_board(game_board)
    if victory_for(game_board, "X"):
        print("Sorry, you lose!")
        break
    if make_list_of_free_fields(game_board) == []:
        print("Its a tie!")
        break
    enter_move(game_board)
    display_board(game_board)
    if victory_for(game_board, "O"):
        print("Congrats, you win!")
        break
    if make_list_of_free_fields(game_board) == []:
        print("Its a tie!")
        break