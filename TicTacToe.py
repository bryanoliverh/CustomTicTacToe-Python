def newBoard(size):
    ticTacToeBoard = []
    for i in range(size):
        row = ['-'] * size
        ticTacToeBoard.append(row)
    return ticTacToeBoard

def prettyPrintingBoard(ticTacToeBoard):
    size = len(ticTacToeBoard)
    print("  ", end="")
    for i in range(size):
        print(f"{i} ", end="")
    print()
    for i in range(size):
        print(f"{i} ", end="")
        for j in range(size):
            print(f"{ticTacToeBoard[i][j]} ", end="")
        print()

def nextTile(playerName, symbol, size):
    while True:
        try:
            tiles = input(f"{playerName}, place your {symbol} tile: ")
            square1, square2 = tiles.split()
            if validateTile(square1, square2, size):
                return square1, square2
            else:
                print("Wrong tile coordinates!! Please re-enter")
        except ValueError:
            print("Invalid input format! Please enter two tile coordinates separated by a space.")

def validateTile(square1, square2, size):
    x1, y1 = int(square1[0]), int(square1[1])
    x2, y2 = int(square2[0]), int(square2[1])
    if x1 < 0 or x1 >= size or y1 < 0 or y1 >= size or x2 < 0 or x2 >= size or y2 < 0 or y2 >= size:
        return False
    if x1 == x2 and abs(y1-y2) == 1:
        return True
    if y1 == y2 and abs(x1-x2) == 1:
        return True
    return False

def tilePlacement(ticTacToeBoard, symbol, square1, square2):
    x1, y1 = int(square1[0]), int(square1[1])
    x2, y2 = int(square2[0]), int(square2[1])
    if ticTacToeBoard[x1][y1] != '-' or ticTacToeBoard[x2][y2] != '-':
        return False
    ticTacToeBoard[x1][y1] = symbol
    ticTacToeBoard[x2][y2] = symbol
    return True

def gameActive(ticTacToeBoard):
    size = len(ticTacToeBoard)
    for i in range(size):
        for j in range(size-1):
            if ticTacToeBoard[i][j] == '-' and ticTacToeBoard[i][j+1] == '-':
                return True
            if ticTacToeBoard[j][i] == '-' and ticTacToeBoard[j+1][i] == '-':
                return True
    return False

def countTiles(ticTacToeBoard, symbol):
    count = 0
    size = len(ticTacToeBoard)
    for i in range(size):
        for j in range(size):
            if ticTacToeBoard[i][j] == symbol:
                count += 1
    return count

def checkWinner(ticTacToeBoard, symbol1, symbol2):
    count1 = countTiles(ticTacToeBoard, symbol1)
    count2 = countTiles(ticTacToeBoard, symbol2)
    if count1 > count2:
        return symbol1
    elif count2 > count1:
        return symbol2
    else:
        return None

def startGame():
    try:
        player1 = input("Enter player 1 name: ")
        if not player1:
            raise ValueError("Player 1 name cannot be empty")
        player2 = input("Enter player 2 name: ")
        if not player2:
            raise ValueError("Player 2 name cannot be empty")
        size = int(input("Size of game ticTacToeBoard: "))
        ticTacToeBoard = newBoard(size)
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.\n")
        startGame()
        return
    symbol1, symbol2 = 'X', 'O'
    curPlayer = player1
    curSymbol = symbol1
    while gameActive(ticTacToeBoard):
        prettyPrintingBoard(ticTacToeBoard)
        square1, square2 = nextTile(curPlayer, curSymbol, size)
        while not tilePlacement(ticTacToeBoard, curSymbol, square1, square2):
            print("Square occupied!! Please re-enter")
            square1, square2 = nextTile(curPlayer, curSymbol, size)
        if curSymbol == symbol1:
            curPlayer = player2
            curSymbol = symbol2
        else:
            curPlayer = player1
            curSymbol = symbol1

    prettyPrintingBoard(ticTacToeBoard)

    countX, countO = 0, 0
    for row in ticTacToeBoard:
        countX += row.count(symbol1)
        countO += row.count(symbol2)

    if countX == countO:
        print("It's a tie!! Rematch...")
        startGame()
    elif gameActive(ticTacToeBoard):
        if countX > countO:
            print(f"{player1} {countX} - {player2} {countO}")
            print(f"{player1} is the winner!!")
        else:
            print(f"{player1} {countX} - {player2} {countO}")
            print(f"{player2} is the winner!!")
    else:
        if countX > countO:
            print(f"{player1} {countX} - {player2} {countO}")
            print(f"{player1} is the winner!!")
        elif countO > countX:
            print(f"{player1} {countX} - {player2} {countO}")
            print(f"{player2} is the winner!!")
        else:
            print(f"{player1} {countX} - {player2} {countO}")
            print("It's a tie!! Rematch...")
startGame()
