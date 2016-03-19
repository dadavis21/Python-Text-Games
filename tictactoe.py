import random
def drawBoard(board):
      # This function prints out the board that it was passed.

      # "board" is a list of 10 strings representing the board (ignore index 0)
      print('   |   |')
      print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
      print('   |   |')
      print('-----------')
      print('   |   |')
      print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
      print('   |   |')
      print('-----------')
      print('   |   |')
      print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
      print('   |   |')
def inputPlayerLetter():
    player = ""
    while not (player == "X" or player == "O"):
        player = raw_input("Do you want to be X or O?\n")
        player = player.upper()
    if player == "X":
        return ["X","O"]
    else:
        return ["O","X"]
def whoGoesFirst():
    player = random.randint(1,2)
    if(player == 1):
        return "player"
    else:
        return "computer"
def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')
def makeMove(board, letter, move):
    board[move] = letter
def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or
    (bo[9] == le and bo[5] == le and bo[1] == le))
def getBoardCopy(board):
    dupBoard = []
    for space in board:
        dupBoard.append(space)
    return dupBoard
def isSpaceFree(board, move):
    return board[move] == " "
def getPlayerMove(board):
    move = ""
    while(True):
        move = raw_input("What is your next move? (1-9)\n")
        if (move not in "1 2 3 4 5 6 7 8 9".split()):
            print("Please enter an integer")
        else:
            move = int(move)
            if (move > 9 or move < 1):
                print("Please enter an integer between 1 and 9")
            elif (not isSpaceFree(board, move)):
                print("Please enter a space that is not taken")
            else:
                break
    return int(move)
def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for move in movesList:
        if (isSpaceFree(board,move)):
            possibleMoves.append(move)
    if (len(possibleMoves) > 0):
        return random.choice(possibleMoves)
    else:
        return None
def getComputerMove(board, computerLetter):
    if (computerLetter == "X"):
        playerLetter = "O"
    else:
        playerLetter = "X"
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if (isSpaceFree(copy, i)):
            makeMove(copy, computerLetter, i)
            if (isWinner(copy, computerLetter)):
                return i
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if (isSpaceFree(board, i)):
            makeMove(copy, playerLetter, i)
            if (isWinner(copy, playerLetter)):
                return i
    corner = chooseRandomMoveFromList(board, [1,3,7,9])
    side = chooseRandomMoveFromList(board, [2,4,6])
    if (corner != None):
        return corner
    elif (isSpaceFree(board, 5)):
        return 5
    else:
        return side
def isBoardFull(board):
    for i in range(1,10):
        if (isSpaceFree(board, i)):
            return False
    return True
print("Welcome to Tic-Tac-Toe!")
while True:
    letters = inputPlayerLetter()
    player = letters[0]
    computer = letters[1]
    first = whoGoesFirst()
    print("The " + first + " will go first.")
    gameIsDone = False
    board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    while True:
        if (first == "player"):
            board[getPlayerMove(board)] = player
            if (isWinner(board, player)):
                print("You have beaten the computer. You win!")
                drawBoard(board)
                break
            elif (isWinner(board, computer)):
                print("The computer has beaten you. You lose!")
                drawBoard(board)
                break
            elif (isBoardFull(board)):
                print("The board is full and no one has won. Cats game!")
                break
            board[getComputerMove(board, first[1])] = computer
            drawBoard(board)
        else:
            board[getComputerMove(board, first[1])] = computer
            drawBoard(board)
            if (isWinner(board, player)):
                print("You have beaten the computer. You win!")
                break
            elif (isWinner(board, computer)):
                print("The computer has beaten you. You lose!")
                break
            elif (isBoardFull(board)):
                print("The board is full and no one has won. Cats game!")
                break
            board[getPlayerMove(board)] = player
        if (isWinner(board, player)):
            print("You have beaten the computer. You win!")
            break
        elif (isWinner(board, computer)):
            print("The computer has beaten you. You lose!")
            break
    replay = raw_input("Would you like to play again? (yes or no)\n")
    if(replay == "no"):
        break
