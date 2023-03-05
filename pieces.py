from cmu_112_graphics import * 

class King:
    def __init__(self, color, image, x, y):
        self.color = color
        self.image = image
        self.x = x
        self.y = y
    def __repr__(self):
        return f'{self.color} King'
    def drawPiece(self, canvas):
        canvas.create_image(self.x, self.y, image = ImageTk.PhotoImage(self.image))
    def legalMoves(self, x, y, board):
        legalMoves = set()
        possDx = [-1, 0, 1]
        possDy = [-1, 0, 1]
        # check if move is one step
        # check if move does not interfere with piece of same color
        # check if move does not go beyond bounds of the board 
        for dx in possDx:
            for dy in possDy:
                if dx == 0 and dy == 0:
                    continue
                else:
                    if 0 <= x+dx < len(board) and 0 <= y+dy < len(board):
                        piece = board[y+dy][x+dx]
                        # king can not move in check(mate) position
                        if piece == None or piece.color != self.color:
                            legalMoves.add((x+dx, y+dy))
                        
        return legalMoves




class Queen:
    def __init__(self, color, image, x, y):
        self.color = color
        self.image = image
        self.x = x
        self.y = y
    def __repr__(self):
        return f'{self.color} Queen'
    def drawPiece(self, canvas):
        canvas.create_image(self.x, self.y, image = ImageTk.PhotoImage(self.image))
    def findSameBlocks(self, x, y, board):
        # one axis is for two of the same sign changes (pos, pos) or (neg, neg)
        bound1 = len(board) - 1 - x
        bound2 = -x
        bounds = list(range(bound2, bound1+1))
        down1 = None
        down2 = None
        i = 0
        # find any same color pieces in the way of same sign change diagonal moves
        while i < len(bounds):
            dx = bounds[i]
            # check if new row is within board 
            if 0 <= y+dx < len(board):
                if board[y+dx][x+dx] != None and (x+dx<x and y+dx<y):
                        down1 = dx
                elif board[y+dx][x+dx] != None and (x+dx>x and y+dx>y):
                        down2 = dx
                        break
            # if row not within board 
            else:
                if y+dx<y:
                    down1 = dx
                elif y+dx>y:
                    down2 = dx
            i += 1
        if down1 == None:
            down1 = bound2
        if down2 == None:
            down2 = bound1

        return down1, down2

    def findAlternatingBlock(self, x, y, board):
        # one axis is for one positive and one negative change or vice versa
        bound1 = len(board) - 1 - x
        bound2 = -x
        bounds = list(range(bound2, bound1+1))
        up1 = None
        up2 = None
        j = 0

        while j < len(bounds):
            dx = bounds[j]
            if 0 <= y-dx < len(board):

                if board[y-dx][x+dx] != None and x+dx<x and y-dx>y:
                        up1 = dx
                elif board[y-dx][x+dx] != None and x+dx>x and y-dx<y:
                        up2 = dx
                        break
            else:
                if y-dx>y:
                    up1 = dx
                elif y-dx<y:
                    up2 = dx
            j += 1
        if up1 == None:
            up1 = bound2
        if up2 == None:
            up2 = bound1

        return up1, up2

    def findHorizontalBlock(self, x, y, board):
        horBoundRight = len(board) - 1 - x
        horBoundLeft = -x
        horBounds = list(range(horBoundLeft, horBoundRight+1))
        
        leftBlock = None
        rightBlock = None
        i = 0

        # horizontal bounds
        while i < len(horBounds):
            dx = horBounds[i]
            if board[y][x+dx] != None and x+dx < x:
                leftBlock = dx
            elif board[y][x+dx] != None and x+dx > x:
                rightBlock = dx
                break
            i += 1
        if leftBlock == None:
            leftBlock = horBoundLeft
        if rightBlock == None:
            rightBlock = horBoundRight

        return leftBlock, rightBlock

    def findVerticalBlock(self, x, y, board):
        verBoundUp = len(board) - 1 - y
        verBoundDown = -y
        verBounds = list(range(verBoundDown, verBoundUp+1))

        upBlock = None
        downBlock = None
        j = 0

        while j < len(verBounds):
            dy = verBounds[j]
            if board[y+dy][x] != None and y+dy < y:
                downBlock = dy
            elif board[y+dy][x] != None and y+dy > y:
                upBlock = dy
                break
            j += 1

        if downBlock == None:
            downBlock = verBoundDown
        if upBlock == None:
            upBlock = verBoundUp
        
        return downBlock, upBlock

    def legalMoves(self, x, y, board):
        # queen can go in eight directions 
        legalMoves = set()
        # down diagonal
        same1 = self.findSameBlocks(x, y, board)[0]
        same2 = self.findSameBlocks(x, y, board)[1]
        for dx in range(same1, same2+1):
            # same signs
            if 0 <= y+dx < len(board):
                if board[y+dx][x+dx] == None or board[y+dx][x+dx].color != self.color:
                    legalMoves.add((x+dx, y+dx))
        # up diagonal 
        alter1 = self.findAlternatingBlock(x, y, board)[0]
        alter2 = self.findAlternatingBlock(x, y, board)[1]
        for dx in range(alter1, alter2+1):
            # alternating signs
            if 0 <= y-dx < len(board):
                if board[y-dx][x+dx] == None or board[y-dx][x+dx].color != self.color:
                    legalMoves.add((x+dx, y-dx))

        # calculate bounds for horizontal and vertical (both ways)
        horBoundRight = self.findHorizontalBlock(x, y, board)[1]
        horBoundLeft = self.findHorizontalBlock(x, y, board)[0]
        verBoundUp = self.findVerticalBlock(x, y, board)[1]
        verBoundDown = self.findVerticalBlock(x, y, board)[0]
        # horizontal movement
        for dx in range(horBoundLeft, horBoundRight+1):
            if board[y][x+dx] == None or board[y][x+dx].color != self.color:
                legalMoves.add((x+dx, y))
                
        # vertical movement
        for dy in range(verBoundDown, verBoundUp+1):
            if board[y+dy][x] == None or board[y+dy][x].color != self.color:
                legalMoves.add((x, y+dy))
        

        return legalMoves


class Knight:
    def __init__(self, color, image, x, y):
        self.color = color
        self.image = image
        self.x = x
        self.y = y
    def __repr__(self):
        return f'{self.color} Knight'
    def drawPiece(self, canvas):
        canvas.create_image(self.x, self.y, image = ImageTk.PhotoImage(self.image))
    def legalMoves(self, x, y, board):
        legalMoves = set()
        possDxy = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), 
                (-2, -1)]
        for dx, dy in possDxy:
            # verifies move is within bounds of the board
            if 0 <= x+dx < len(board) and 0 <= y+dy < len(board):
                # verifies checker is clear or piece already there is not white
                if board[y+dy][x+dx] == None or board[y+dy][x+dx].color != self.color:
                    legalMoves.add((x+dx, y+dy))
        return legalMoves



class Bishop:
    def __init__(self, color, image, x, y):
        self.color = color
        self.image = image
        self.x = x
        self.y = y
    def __repr__(self):
        return f'{self.color} Bishop'
    def drawPiece(self, canvas):
        canvas.create_image(self.x, self.y, image = ImageTk.PhotoImage(self.image))
    def findSameBlocks(self, x, y, board):
        # one axis is for two of the same sign changes (pos, pos) or (neg, neg)
        bound1 = len(board) - 1 - x
        bound2 = -x
        bounds = list(range(bound2, bound1+1))
        down1 = None
        down2 = None
        i = 0
        # find any same color pieces in the way of same sign change diagonal moves
        while i < len(bounds):
            dx = bounds[i]
            # check if new row is within board 
            if 0 <= y+dx < len(board):
                if board[y+dx][x+dx] != None and (x+dx<x and y+dx<y):
                        down1 = dx
                elif board[y+dx][x+dx] != None and (x+dx>x and y+dx>y):
                        down2 = dx
                        break
            # if row not within board 
            else:
                if y+dx<y:
                    down1 = dx
                elif y+dx>y:
                    down2 = dx
            i += 1
        if down1 == None:
            down1 = bound2
        if down2 == None:
            down2 = bound1

        return down1, down2

    def findAlternatingBlock(self, x, y, board):
        # one axis is for one positive and one negative change or vice versa
        bound1 = len(board) - 1 - x
        bound2 = -x
        bounds = list(range(bound2, bound1+1))
        up1 = None
        up2 = None
        j = 0

        while j < len(bounds):
            dx = bounds[j]
            if 0 <= y-dx < len(board):

                if board[y-dx][x+dx] != None and x+dx<x and y-dx>y:
                        up1 = dx
                elif board[y-dx][x+dx] != None and x+dx>x and y-dx<y:
                        up2 = dx
                        break
            else:
                if y-dx>y:
                    up1 = dx
                elif y-dx<y:
                    up2 = dx
            j += 1
        if up1 == None:
            up1 = bound2
        if up2 == None:
            up2 = bound1

        return up1, up2

    def legalMoves(self, x, y, board):
        # bishop can go in four directions 
        legalMoves = set()
        same1 = self.findSameBlocks(x, y, board)[0]
        same2 = self.findSameBlocks(x, y, board)[1]
        for dx in range(same1, same2+1):
            # same signs
            if 0 <= y+dx < len(board):
                if board[y+dx][x+dx] == None or board[y+dx][x+dx].color != self.color:
                    legalMoves.add((x+dx, y+dx))
            
        alter1 = self.findAlternatingBlock(x, y, board)[0]
        alter2 = self.findAlternatingBlock(x, y, board)[1]
        for dx in range(alter1, alter2+1):
            # alternating signs
            if 0 <= y-dx < len(board):
                if board[y-dx][x+dx] == None or board[y-dx][x+dx].color != self.color:
                    legalMoves.add((x+dx, y-dx))

        return legalMoves
        



class Rook:
    def __init__(self, color, image, x, y):
        self.color = color
        self.image = image
        self.x = x
        self.y = y
    def __repr__(self):
        return f'{self.color} Rook'
    def drawPiece(self, canvas):
        canvas.create_image(self.x, self.y, image = ImageTk.PhotoImage(self.image))
    def findHorizontalBlock(self, x, y, board):
        horBoundRight = len(board) - 1 - x
        horBoundLeft = -x
        horBounds = list(range(horBoundLeft, horBoundRight+1))
        
        leftBlock = None
        rightBlock = None
        i = 0

        # horizontal bounds
        while i < len(horBounds):
            dx = horBounds[i]
            if board[y][x+dx] != None and x+dx < x:
                leftBlock = dx
            elif board[y][x+dx] != None and x+dx > x:
                rightBlock = dx
                break
            i += 1
        if leftBlock == None:
            leftBlock = horBoundLeft
        if rightBlock == None:
            rightBlock = horBoundRight

        return leftBlock, rightBlock

    def findVerticalBlock(self, x, y, board):
        verBoundUp = len(board) - 1 - y
        verBoundDown = -y
        verBounds = list(range(verBoundDown, verBoundUp+1))

        upBlock = None
        downBlock = None
        j = 0

        while j < len(verBounds):
            dy = verBounds[j]
            if board[y+dy][x] != None and y+dy < y:
                downBlock = dy
            elif board[y+dy][x] != None and y+dy > y:
                upBlock = dy
                break
            j += 1

        if downBlock == None:
            downBlock = verBoundDown
        if upBlock == None:
            upBlock = verBoundUp
        
        return downBlock, upBlock


    def legalMoves(self, x, y, board):
        legalMoves = set()
        # calculate bounds for horizontal and vertical (both ways)
        horBoundRight = self.findHorizontalBlock(x, y, board)[1]
        horBoundLeft = self.findHorizontalBlock(x, y, board)[0]
        verBoundUp = self.findVerticalBlock(x, y, board)[1]
        verBoundDown = self.findVerticalBlock(x, y, board)[0]
        # horizontal movement
        for dx in range(horBoundLeft, horBoundRight+1):
            if board[y][x+dx] == None or board[y][x+dx].color != self.color:
                legalMoves.add((x+dx, y))
                
        # vertical movement
        for dy in range(verBoundDown, verBoundUp+1):
            if board[y+dy][x] == None or board[y+dy][x].color != self.color:
                legalMoves.add((x, y+dy))
                
        return legalMoves


class Pawn:
    def __init__(self, color, image, x, y):
        self.color = color
        self.image = image
        self.x = x
        self.y = y
    def __repr__(self):
        return f'{self.color} Pawn'
    def drawPiece(self, canvas):
        canvas.create_image(self.x, self.y, image = ImageTk.PhotoImage(self.image))
    # need to check for bounds 
    # need to check if same color piece is blocking path7
    def legalMoves(self, x, y, board):
        legalMoves = set()
        if self.color == 'white':
            if y == 6: 
                possDy = [-1, -2]
            else:
                possDy = [-1]
        if self.color == 'black':
            if y == 1:
                possDy = [-1, -2]
            else:
                possDy = [-1]
        for dy in possDy:
            if self.color == 'white':
                if 0 < y+dy <= len(board)-1 and board[y+dy][x] == None:
                    legalMoves.add((x, y+dy))
            elif self.color == 'black':
                if 0 < y-dy <= len(board)-1 and board[y-dy][x] == None:
                    legalMoves.add((x, y-dy)) 
        return legalMoves
    def attackMoves(self, x, y, board):
        attackMoves = set()
        attackDx = [-1, 1]
        attackDy = -1
        if y == 0 or y == len(board)-1:
            return attackMoves
        
        # establishing bounds
        if -1 >= x-1:
            attackDx = [1]
        elif x+1 >= len(board):
            attackDx = [-1]
        
        # testing attacking sides 
        for dx in attackDx:
            if self.color == 'white':
                checker = board[y+attackDy][x+dx]
                if checker != None:
                    if checker.color == 'black':
                        attackMoves.add((x+dx, y+attackDy))
            elif self.color == 'black':
                checker = board[y-attackDy][x+dx]
                if checker != None:
                    if checker.color == 'white':
                        attackMoves.add((x+dx, y-attackDy))
        return attackMoves
