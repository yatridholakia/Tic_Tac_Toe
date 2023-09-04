GRID_SIZE = 3
gameBoard = [[i * GRID_SIZE + j + 1 for j in range(GRID_SIZE)] for i in range(GRID_SIZE)]

def displayBoard(gameBoard):
    print("+---+---+---+")
    for row in gameBoard:
        print("|", end="")
        for item in row:
            print(f" {item}", end=" |")
        print("\n+---+---+---+")

def getUserInput():
    return int(input("Enter Position(0-9): "))

def checkForWinner(gameBoard, player):
    #check rows
    if(gameBoard[0][0] == player and gameBoard[0][1] == player and gameBoard[0][2] == player):
        return True
    elif(gameBoard[1][0] == player and gameBoard[1][1] == player and gameBoard[1][2] == player):
        return True
    elif(gameBoard[2][0] == player and gameBoard[2][1] == player and gameBoard[2][2] == player):
        return True
    
    #check columns
    if(gameBoard[0][0] == player and gameBoard[1][0] == player and gameBoard[2][0] == player):
        return True
    elif(gameBoard[0][1] == player and gameBoard[1][1] == player and gameBoard[2][1] == player):
        return True
    elif(gameBoard[0][2] == player and gameBoard[1][2] == player and gameBoard[2][2] == player):
        return True
    
    #check Diagonals
    if(gameBoard[0][0] == player and gameBoard[1][1] == player and gameBoard[2][2] == player):
        return True
    elif(gameBoard[0][2] == player and gameBoard[1][1] == player and gameBoard[2][0] == player):
        return True

def isGameOver(gameBoard, totalMoves):
    if(checkForWinner(gameBoard, player_one["sign"])):
        print(f"{player_one['name']} Won!")
        displayBoard(gameBoard)
        return True
    elif(checkForWinner(gameBoard, player_two["sign"])):
        print(f"{player_two['name']} Won!")
        displayBoard(gameBoard)
        return True
    elif(totalMoves == (GRID_SIZE * GRID_SIZE)):
        print("Match Draw!")
        displayBoard(gameBoard)
        return True
    else:
        return False

def updateBoard(gameBoard, index, sign):
    index = index - 1
    row = index // GRID_SIZE
    col = index % GRID_SIZE

    if isinstance(gameBoard[row][col], str):
        return False;

    gameBoard[row][col] = sign
    return True;

def switchTurns(sign):
    return "O" if sign == "X" else "X" 

print("Welcome to Tic Tac Toe!")
player_one = {"name": input("Enter Player One's Name(X): "), "sign": "X"}
player_two = {"name": input("Enter Player Two's Name(O): "), "sign": "O"}
turn = player_one["sign"]
totalMoves = 0
while(isGameOver(gameBoard, totalMoves) == False):
    displayBoard(gameBoard)
    player_name = player_one["name"] if turn == "X" else player_two["name"] 
    print(f"{player_name}'s Turn!")
    try:
        index = getUserInput()
        if(index < 10 and index > 0):
            if updateBoard(gameBoard, index, turn):
                turn = switchTurns(turn)
                totalMoves += 1
            else:
                print("Invalid Move. The cell is already occupied.")
        else:
            print("Invalid Move. Please enter a number between 1 and 9.")
            
    except ValueError:
        print("Invalid Input. Please enter a valid number.")
                
                



