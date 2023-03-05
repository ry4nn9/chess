from cmu_112_graphics import * 
import pieces

def appStarted(app):
    app.boardWd = app.width - 2/10*app.width
    app.boardHt = app.height - 2/10*app.height
    app.margin = 70
    app.wbH = app.height - app.margin - app.margin//2
    app.bbH = app.margin + app.margin//2
    app.wW = app.margin + app.margin//2
    app.bW = app.margin + app.margin//2

###############################################################################
# white pieces (images) 
    # king pieces 
    app.whiteKingImage = app.loadImage('whiteKing.png')
    app.whiteKingScaled = app.scaleImage(app.whiteKingImage, 1/5)

    # queen pieces
    app.whiteQueenImage = app.loadImage('whiteQueen.png')
    app.whiteQueenScaled = app.scaleImage(app.whiteQueenImage, 1/5)

    # bishop pieces
    app.whiteBishopImage = app.loadImage('whiteBishop.png')
    app.whiteBishopScaled = app.scaleImage(app.whiteBishopImage, 1/5)

    # rook pieces
    app.whiteRookImage = app.loadImage('whiteRook.png')
    app.whiteRookScaled = app.scaleImage(app.whiteRookImage, 1/4.5)

    # knight pieces
    app.whiteKnightImage = app.loadImage('whiteKnight.png')
    app.whiteKnightScaled = app.scaleImage(app.whiteKnightImage, 1/5)

    # creating objects for each white non-pawn (back) piece 
    app.whiteRook2 = pieces.Rook('white', app.whiteRookScaled, app.wW, app.wbH)
    app.wW += app.margin
    app.whiteKnight2 = pieces.Knight('white', app.whiteKnightScaled, app.wW, app.wbH)
    app.wW += app.margin
    app.whiteBishop1 = pieces.Bishop('white', app.whiteBishopScaled, app.wW, app.wbH)
    app.wW += app.margin
    app.whiteKing = pieces.King('white', app.whiteKingScaled, app.wW, app.wbH)
    app.wW += app.margin
    app.whiteQueen = pieces.Queen('white', app.whiteQueenScaled, app.wW, app.wbH)
    app.wW += app.margin
    app.whiteBishop2 = pieces.Bishop('white', app.whiteBishopScaled, app.wW, app.wbH)
    app.wW += app.margin
    app.whiteKnight1 = pieces.Knight('white', app.whiteKnightScaled, app.wW, app.wbH)
    app.wW += app.margin
    app.whiteRook1 = pieces.Rook('white', app.whiteRookScaled, app.wW, app.wbH)


    # pawn pieces
    app.whitePawnImage = app.loadImage('whitePawn.png')
    app.whitePawnScaled = app.scaleImage(app.whitePawnImage, 1/5)

    # (pawns)
    app.whitePawns = []
    x = app.margin + app.margin//2
    y = app.height - 2*app.margin - app.margin//2
    for i in range(8):
        app.whitePawn = pieces.Pawn('white', app.whitePawnScaled, x, y)
        app.whitePawns.append(app.whitePawn)
        x += app.margin

###############################################################################
# black pieces (images) 
    # king pieces 
    app.blackKingImage = app.loadImage('blackKing.png')
    app.blackKingScaled = app.scaleImage(app.blackKingImage, 1/5)

    # queen pieces
    app.blackQueenImage = app.loadImage('blackQueen.png')
    app.blackQueenScaled = app.scaleImage(app.blackQueenImage, 1/5)

    # bishop pieces
    app.blackBishopImage = app.loadImage('blackBishop.png')
    app.blackBishopScaled = app.scaleImage(app.blackBishopImage, 1/5)

    # rook pieces
    app.blackRookImage = app.loadImage('blackRook.png')
    app.blackRookScaled = app.scaleImage(app.blackRookImage, 1/4.5)

    # knight pieces
    app.blackKnightImage = app.loadImage('blackKnight.png')
    app.blackKnightScaled = app.scaleImage(app.blackKnightImage, 1/5)

    # creating objects for each black non-pawn (back) pieces
    app.blackRook2 = pieces.Rook('black', app.blackRookScaled, app.bW, app.bbH)
    app.bW += app.margin
    app.blackKnight2 = pieces.Knight('black', app.blackKnightScaled, app.bW, app.bbH)
    app.bW += app.margin
    app.blackBishop1 = pieces.Bishop('black', app.blackBishopScaled, app.bW, app.bbH)
    app.bW += app.margin
    app.blackKing = pieces.King('black', app.blackKingScaled, app.bW, app.bbH)
    app.bW += app.margin
    app.blackQueen = pieces.Queen('black', app.blackQueenScaled, app.bW, app.bbH)
    app.bW += app.margin
    app.blackBishop2 = pieces.Bishop('black', app.blackBishopScaled, app.bW, app.bbH)
    app.bW += app.margin
    app.blackKnight1 = pieces.Knight('black', app.blackKnightScaled, app.bW, app.bbH)
    app.bW += app.margin
    app.blackRook1 = pieces.Rook('black', app.blackRookScaled, app.bW, app.bbH)


    # pawn pieces
    app.blackPawnImage = app.loadImage('blackPawn.png')
    app.blackPawnScaled = app.scaleImage(app.blackPawnImage, 1/5)
    
    # (pawns)
    app.blackPawns = []
    x = app.margin + app.margin//2
    y = 2*app.margin + app.margin//2
    for i in range(8):
        app.blackPawn = pieces.Pawn('black', app.blackPawnScaled, x, y)
        app.blackPawns.append(app.blackPawn)
        x += app.margin

###############################################################################
# game play 
    # if piece is selected 
    app.selectPiece = False
    app.selectBoxX = None
    app.selectBoxY = None
    app.selectX = None
    app.selectY = None
    app.selectedChecker = None
    app.color = 'None'

    # move piece
    app.moveX = None
    app.moveY = None
    app.moveCount = 0

    # board
    app.board = [[app.blackRook2, app.blackKnight2, app.blackBishop1, app.blackKing, 
    app.blackQueen, app.blackBishop2, app.blackKnight1, app.blackRook1]] 
    app.board += [list(app.blackPawns)]
    app.board += [[None] * 8 for i in range(4)]
    app.board += [list(app.whitePawns)]
    app.board += [[app.whiteRook2, app.whiteKnight2, app.whiteBishop1, app.whiteKing,
    app.whiteQueen, app.whiteBishop2, app.whiteKnight1, app.whiteRook1]]

    # store x and y mouse Pressed
    app.eventX = None
    app.eventY = None

    # turns
    app.whiteTurn = True
    app.blackTurn = False


def keyPressed(app, event):
    if event.key == 'r':
        appStarted(app)

    
def mousePressed(app, event):
    app.eventX = event.x
    app.eventY = event.y
    app.selectPiece = not app.selectPiece

    # transfers selected piece when selected piece of same color is clicked on
    if insideBoard(app, event.x, event.y):
        x = getBoxPressed(app, event.x, event.y)[0]
        y = getBoxPressed(app, event.x, event.y)[1]
        app.tempX = x 
        app.tempY = y
        checker = app.board[app.tempY][app.tempX]
        
        if checker != None:
            if checker.color == 'None':
                app.selectPiece = True
                app.selectX = app.tempX
                app.selectY = app.tempY
            elif checker.color == app.color:
                app.selectPiece = True
                app.selectX = app.tempX
                app.selectY = app.tempY

    if app.selectPiece:
        if app.whiteTurn:
            if checker != None and checker.color != 'white':
                print('Choose a white piece.')
                app.selectPiece = False
                
        elif app.blackTurn:
            if checker != None and checker.color != 'black':
                print('Choose a black piece.')
                app.selectPiece = False
                

    if app.selectPiece:
        if insideBoard(app, event.x, event.y):
            boxX = getCoordinates(app, event.x, event.y)[0]
            boxY = getCoordinates(app, event.x, event.y)[1]
            app.selectBoxX = boxX
            app.selectBoxY = boxY
            x = getBoxPressed(app, event.x, event.y)[0]
            y = getBoxPressed(app, event.x, event.y)[1]
            app.selectX = x 
            app.selectY = y

            app.selectedChecker = app.board[app.selectY][app.selectX]
            if app.selectedChecker != None:
                app.color = app.selectedChecker.color
            print(f'\nSelected: {app.selectedChecker} - {app.selectX, app.selectY}')
            print(f'{app.selectBoxX, app.selectBoxY}')
            if app.selectedChecker != None:
                print(app.selectedChecker.legalMoves(app.selectX, app.selectY, app.board))
                if isinstance(app.selectedChecker, pieces.Pawn):
                    print('Pawn Attack:', app.selectedChecker.attackMoves(app.selectX, app.selectY, app.board))
            
    else:
        if app.selectedChecker != None:
            app.moveX = event.x
            app.moveY = event.y
            selectedMove = getBoxPressed(app, app.moveX, app.moveY)
            x = selectedMove[0]
            y = selectedMove[1]
            
            if isinstance(app.selectedChecker, pieces.Pawn):
                attackMoves = app.selectedChecker.attackMoves(app.selectX, app.selectY, app.board)
                if selectedMove in attackMoves:
                    app.selectedChecker.x = getCoordinates(app, app.moveX, app.moveY)[0]
                    app.selectedChecker.y = getCoordinates(app, app.moveX, app.moveY)[1]
                    app.board[app.selectY][app.selectX] = None
                    app.board[y][x] = app.selectedChecker
                    print(f'Moved: {app.selectedChecker} - {selectedMove}')
                    print(f'{app.selectedChecker.x, app.selectedChecker.y}')
                    print('\n')
                    app.moveCount += 1
                    app.whiteTurn = not app.whiteTurn
                    app.blackTurn = not app.blackTurn
                    return
            
            legalMoves = app.selectedChecker.legalMoves(app.selectX, app.selectY, app.board)
            if selectedMove in legalMoves:
                app.selectedChecker.x = getCoordinates(app, app.moveX, app.moveY)[0]
                app.selectedChecker.y = getCoordinates(app, app.moveX, app.moveY)[1]
                app.board[app.selectY][app.selectX] = None
                app.board[y][x] = app.selectedChecker
                print(f'Moved: {app.selectedChecker} - {selectedMove}')
                print(f'{app.selectedChecker.x, app.selectedChecker.y}')
                print('\n')
                app.moveCount += 1
                app.whiteTurn = not app.whiteTurn
                app.blackTurn = not app.blackTurn
            
            else:
                print(f'Output: Player selected illegal move. {selectedMove}')
            
            print('\n')
            print("King's Legal Moves:", findKingMoves(app))
            print(isCheck(app))
            # for row in app.board:
            #     print(row)

def findKingMoves(app):
    if app.whiteTurn:
        kingColor = 'black'
    elif app.blackTurn:
        kingColor = 'white'
    rows = len(app.board)
    cols = len(app.board[0])
    for row in range(rows):
        for col in range(cols):
            checker = app.board[row][col]
            if isinstance(checker, pieces.King) and checker.color != kingColor:
                # legalMoves = checker.legalMoves(col, row, app.board)
                legalMoves = {(col, row)}
                return legalMoves

def isCheck(app):
    if app.whiteTurn:
        kingColor = 'black'
    elif app.blackTurn:
        kingColor = 'white'
    rows = len(app.board)
    cols = len(app.board[0])
    legalMoveDict = {}
    for row in range(rows):
        for col in range(cols):
            checker = app.board[row][col]
            if checker != None and not isinstance(checker, pieces.King):
                if isinstance(checker, pieces.Pawn):
                    attackMoves = checker.attackMoves(col, row, app.board)
                    legalMoves = checker.legalMoves(col, row, app.board)
                    legalMoves.update(attackMoves)
                    legalMoveDict[checker] = legalMoves
                else:
                    legalMoves = checker.legalMoves(col, row, app.board)
                    legalMoveDict[checker] = legalMoves
    for piece in legalMoveDict:
        for move in legalMoveDict[piece]:
            if move in findKingMoves(app) and piece.color == kingColor:
                return True

    return False
        
def kingCoord(app):
    if app.whiteTurn:
        kingColor = 'black'
    elif app.blackTurn:
        kingColor = 'white'
    rows = len(app.board)
    cols = len(app.board[0])
    for row in range(rows):
        for col in range(cols):
            checker = app.board[row][col]
            if isinstance(checker, pieces.King) and checker.color != kingColor:
                kingX = (row+1)*app.margin+(app.margin//2)
                kingY = (col+1)*app.margin+(app.margin//2)
                return kingY, kingX
    

def drawChessBoard(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height,
                            fill = 'gray12')
    # 8x8 board
    x0 = app.margin
    y0 = app.margin
    x1 = x0 + app.margin
    y1 = y0 + app.margin
    count = 0
    for row in range(8):
        for col in range(8):
            count += 1
            if count % 2 == 0:
                canvas.create_rectangle(x0, y0, x1, y1, fill = 'LightSteelBlue', 
                outline = 'black', width = 2)
            else:
                canvas.create_rectangle(x0, y0, x1, y1, fill = 'LightSteelBlue4', 
                outline = 'black', width = 2)
            x0, x1 = x1, x1 + app.margin
        y0, y1 = y1, y1+app.margin
        x0 = app.margin
        x1 = x0 + app.margin
        count += 1
    # draw grid numbers
    # x-axis
    number = 0
    x = app.margin + app.margin//2
    y = app.width - app.margin//2
    for i in range(8):
        canvas.create_text(x, y, text = number, font = 'Arial 15 bold', fill = 'white')
        x += app.margin
        number += 1
    # y-axis
    number = 0
    x = app.height - app.margin//2
    y = app.margin + app.margin//2
    for i in range(8):
        canvas.create_text(x, y, text = number, font = 'Arial 15 bold', fill = 'white')
        y += app.margin
        number += 1
    

def drawPieces(app, canvas):
    rows = len(app.board)
    cols = len(app.board[0])
    for row in range(rows):
        for col in range(cols):
            piece = app.board[row][col]
            if piece != None:
                piece.drawPiece(canvas)

def drawTurn(app, canvas):
    fontType = 'Verdana'
    if app.whiteTurn:
        canvas.create_text(app.width//2, app.margin//2, text = "White's Turn",
        font = f'{fontType} 30 bold', fill = 'snow')
    elif app.blackTurn:
        canvas.create_text(app.width//2, app.margin//2, text = "Black's Turn",
        font = f'{fontType} 30 bold', fill = 'snow')


def drawSelectAnimation(app, canvas, x, y, i, j):
    radius = app.margin//2
    if app.selectPiece:
        if insideBoard(app, app.eventX, app.eventY):
            if app.board[app.selectY][app.selectX] != None:
                canvas.create_oval(x - radius, y - radius, x + radius, y + radius, 
                outline = 'green', width = 5)
    
def drawCheckAnimation(app, canvas, x, y):
    radius = app.margin//2
    if isCheck(app):
        canvas.create_oval(x-radius, y-radius, x+radius, y+radius, 
                            outline = 'red', width = 5)
        canvas.create_text(1050, app.height//2, text = 'Check', fill = 'red', 
        font = 'Verdana 40 bold')

def insideBoard(app, x, y):
    # checks if user clicked inside board
    hb0 = app.margin
    hb1 = app.width - 700 - app.margin
    vb0 = app.margin
    vb1 = app.height - app.margin
    if x < hb0 or x > hb1:
        return False
    elif y < vb0 or y > vb1:
        return False
    else:
        return True

def getCoordinates(app, x, y):
    # gets coordinate pressed on board
    half = app.margin//2
    boxX = ((x // app.margin) * app.margin) + half
    boxY = ((y // app.margin) * app.margin) + half
    return boxX, boxY

def getBoxPressed(app, x, y):
    # gets indices for list of board
    indice1 = (x // app.margin) - 1
    indice2 = (y // app.margin) - 1
    return indice1, indice2

def redrawAll(app, canvas):
    drawChessBoard(app, canvas)
    drawPieces(app, canvas)
    drawCheckAnimation(app, canvas, kingCoord(app)[0], kingCoord(app)[1])
    drawTurn(app, canvas)
    if app.selectBoxX != None and app.selectBoxY != None:
        drawSelectAnimation(app, canvas, app.selectBoxX, app.selectBoxY, 
        app.selectX, app.selectY)
    


runApp(width = 1400, height = 700)

# make sure king can not move into check position
# castling 
# pawn reaching end of board
# timed play?
# keeping track of pieces obtained 
# animations for check, checkmate, draw
# making repetitive moves --> draw