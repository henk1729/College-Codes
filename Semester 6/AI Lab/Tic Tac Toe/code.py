board = {
    1 : '-',
    2 : '-',
    3 : '-',
    4 : '-',
    5 : '-',
    6 : '-',
    7 : '-',
    8 : '-',
    9 : '-'
}
move_cnt = 0
grid_size = 3


def drawBoard(match_ongoing):
    if match_ongoing:
        print()
        print("Player ", move_cnt%2 + 1, " turn", end=" ")
        if move_cnt%2:
            print("(X)")
        else:
            print("(O)")
        
    for row in range(grid_size):
        for col in range(grid_size):
            print(board[grid_size*row + col + 1], end=" ")
        print()
        
    if match_ongoing:
        inputMove()
    
        
def inputMove():
    move = int(input("Enter cell no.: "))
    performMove(move)
    
    
def performMove(move):
    global board
    global move_cnt
    
    if move_cnt%2:
        board[move] = 'X'
    else:
        board[move] = 'O'
    move_cnt += 1
    gameOver()
    
    
def gameOver():
    # horizontal strike
    for row in range(grid_size):
        leftmost_cell = board[grid_size*row + 1]
        if leftmost_cell != '-' and board[grid_size*row + 2] == leftmost_cell and board[grid_size*row + 3] == leftmost_cell:
            print()
            if move_cnt%2:
                print("Player 1 won!")
            else:
                print("Player 2 won!")
            return True
        
    # vertical strike
    for col in range(grid_size):
        topmost_cell = board[col + 1]
        if topmost_cell != '-' and board[grid_size + col + 1] == topmost_cell and board[grid_size*2 + col + 1] == topmost_cell:
            print()
            if move_cnt%2:
                print("Player 1 won!")
            else:
                print("Player 2 won!")
            return True
        
    # diagonal strike
    centre_cell = board[5]
    if centre_cell != '-':
        if (board[1] == centre_cell and board[9] == centre_cell) or (board[3] == centre_cell and board[7] == centre_cell):
            print()
            if move_cnt%2:
                print("Player 1 won!")
            else:
                print("Player 2 won!")
            return True
    
    # match tied
    if move_cnt == 9:
        print()
        print("Match tied!")
        return True
        
    return False


while(gameOver() != True):
    drawBoard(True)
drawBoard(False)
print()
print("Thankyou for playing.")
