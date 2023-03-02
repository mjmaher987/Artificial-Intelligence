import numpy as np
import random
import time
from Helper_codes.graphics import *
from copy import deepcopy


class Cell:
    __x = 0
    __y = 0
    __color = 0
    __id = -1
    __terminalSourceId = -1

    def __init__(self, *args):

        if isinstance(args[0], Cell):
            c1 = args[0]
            cell = deepcopy(c1)
            self.__y = cell.getY()
            self.__x = cell.getX()
            self.__color = cell.getColor()
            self.__id = cell.getId()
            self.__terminalSourceId = cell.getTerminalSourceId()

        elif len(args) == 2:
            self.__x = args[0]
            self.__y = args[1]
        elif len(args) == 3:
            self.__x = args[0]
            self.__y = args[1]
            self.__color = args[2]

    def getY(self):
        return self.__y

    def getX(self):
        return self.__x

    def getColor(self):
        return self.__color

    def getId(self):
        return self.__id

    def setColor(self, color):
        self.__color = color

    def assignId(self, id):
        self.__id = id

    def getTerminalSourceId(self):
        return self.__terminalSourceId

    def setTerminalSourceId(self, terminalSourceId):
        self.__terminalSourceId = terminalSourceId


class IntPair:
    x = 0
    y = 0

    def __init__(self, *args):

        if isinstance(args[0], IntPair):
            intp = args[0]
            self.x = intp.x
            self.y = intp.y

        elif len(args) == 2:
            self.x = args[0]
            self.y = args[1]


class Player:
    __col = 0
    __x = 0
    __y = 0
    __victories = 0
    __buildingBlocks = False

    def __init__(self, col, x, y):
        self.__col = col
        self.__x = x
        self.__y = y

    def getCol(self):
        return self.__col

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def setBuildingBlocks(self, buildingBlocks):
        self.__buildingBlocks = buildingBlocks

    def getBuildingBlocks(self):
        return self.__buildingBlocks

    def win(self):
        self.__victories += 1

    def getVictories(self):
        return self.__victories


class NaivePlayer(Player):

    def __init__(self, col, x, y):
        super().__init__(col, x, y)

    def getMove(self, board):
        x_next = self.getX()
        y_next = self.getY()
        start = time.time()
        while ((x_next == self.getX()) and (y_next == self.getY())):
            rnd = random.randrange(4)
            if (time.time() - start > 2):
                return IntPair(-10, -10)
            if ((rnd == 0) and (self.getX() + 1 < board.getSize()) and (
                    board.getCell(self.getX() + 1, self.getY()).getColor() == 0)):
                x_next += 1
            elif ((rnd == 1) and (self.getX() - 1 >= 0) and (
                    board.getCell(self.getX() - 1, self.getY()).getColor() == 0)):
                x_next -= 1
            elif ((rnd == 2) and (self.getY() + 1 < board.getSize()) and (
                    board.getCell(self.getX(), self.getY() + 1).getColor() == 0)):
                y_next += 1
            elif ((rnd == 3) and (self.getY() - 1 >= 0) and (
                    board.getCell(self.getX(), self.getY() - 1).getColor() == 0)):
                y_next -= 1

        return IntPair(x_next, y_next)


class Board:
    __size = 8
    maxNumberOfMoves = 80
    __cells = [[Cell for j in range(8)] for i in range(8)]
    __score = [int] * 2
    __numberOfMoves = 0
    __terminals = [IntPair for i in range(8)]
    players = [Player for i in range(2)]
    __playerTerminalSourceId = [int] * 2

    def __init__(self, *args):
        self.players = [Player for i in range(2)]
        self.__terminals = [IntPair for i in range(8)]
        self.__playerTerminalSourceId = [int] * 2
        self.__cells = [[Cell for j in range(8)] for i in range(8)]
        if isinstance(args[0], list):

            self.players = args[0]

            for i in range(self.__size):
                for j in range(self.__size):
                    self.__cells[i][j] = Cell(i, j, 0)

            randomList = []

            for i in range(self.__size * self.__size - 2):
                randomList.append(i)

            random.shuffle(randomList)

            for i in range(8):
                point = randomList.pop(i)
                xTrm = int((point - point % self.__size) / self.__size)
                yTrm = int(point % self.__size)
                self.__terminals[i] = IntPair(xTrm, yTrm)
                self.__cells[xTrm][yTrm].assignId(i)

            self.__score[0] = 0
            self.__score[1] = 0
            self.__playerTerminalSourceId[0] = -1
            self.__playerTerminalSourceId[1] = -1

        elif isinstance(args[0], Board):

            b1 = args[0]

            board = (deepcopy(b1))

            for i in range(self.__size):
                for j in range(self.__size):
                    self.__cells[i][j] = Cell(deepcopy(board.__cells[i][j]))

            p1 = Player(board.players[0].getCol(), board.players[0].getX(), board.players[0].getY())
            p2 = Player(board.players[1].getCol(), board.players[1].getX(), board.players[1].getY())
            self.players = [p1, p2]
            self.__terminals = deepcopy(board.__terminals)
            self.__numberOfMoves = board.getNumberOfMoves()
            self.__score = board.__score
            self.__playerTerminalSourceId[0] = board.__playerTerminalSourceId[0]
            self.__playerTerminalSourceId[1] = board.__playerTerminalSourceId[1]

    def getCell(self, x, y):
        return self.__cells[x][y]

    def getNumberOfMoves(self):
        return self.__numberOfMoves

    def win(self):
        return 0

    def getSize(self):
        return self.__size

    def setNumberOfMoves(self, n):
        self.__numberOfMoves = n

    def getPlayerTerminalSourceId(self):
        return self.__playerTerminalSourceId

    def move(self, nextPlace, playerColor):
        self.__numberOfMoves += 1
        currentPlace = IntPair(self.players[playerColor - 1].getX(), self.players[playerColor - 1].getY())

        if ((nextPlace.x < 0) | (nextPlace.y < 0) | (nextPlace.x >= self.__size) | (nextPlace.y >= self.__size)):
            return -1
        elif ((abs(currentPlace.y - nextPlace.y) > 1) | (abs(currentPlace.x - nextPlace.x) > 1)):
            return -1
        elif (self.__cells[nextPlace.x][nextPlace.y].getColor() != 0):
            return -1
        elif ((nextPlace.x == self.players[2 - playerColor].getX()) and (
                nextPlace.y == self.players[2 - playerColor].getY())):
            return -1
        elif (self.__numberOfMoves > self.maxNumberOfMoves):
            return -2
        else:
            id = self.__cells[nextPlace.x][nextPlace.y].getId()
            if (id == -1):
                if (self.__playerTerminalSourceId[playerColor - 1] != -1):
                    self.__cells[nextPlace.x][nextPlace.y].setColor(playerColor)

            else:
                if (self.__playerTerminalSourceId[playerColor - 1] == -1):
                    self.players[playerColor - 1].setBuildingBlocks(True)
                    self.__playerTerminalSourceId[playerColor - 1] = id
                    self.__cells[nextPlace.x][nextPlace.y].setColor(playerColor)

                else:
                    self.players[playerColor - 1].setBuildingBlocks(False)
                    self.__playerTerminalSourceId[playerColor - 1] = -1
                    self.__cells[nextPlace.x][nextPlace.y].setColor(playerColor)

        self.players[playerColor - 1].setX(nextPlace.x)
        self.players[playerColor - 1].setY(nextPlace.y)
        return 0

    def getScore(self, player):
        x = self.players[player - 1].getX()
        y = self.players[player - 1].getY()
        checked = np.zeros((self.__size, self.__size), dtype=bool)
        for i in range(self.__size):
            for j in range(self.__size):
                checked[i][j] = False

        walls = 0
        for i in range(self.__size):
            for j in range(self.__size):
                if (self.getCell(i, j).getColor() == player):
                    walls += 1

        return self.movableSquares(x, y, checked) + walls

    def movableSquares(self, x, y, checked):

        score = 1
        checked[x][y] = True
        if ((x + 1 < self.__size) and (self.getCell(x + 1, y).getColor() == 0) and (not checked[x + 1][y])):
            checked[x + 1][y] = True
            score += self.movableSquares(x + 1, y, checked)

        if ((y + 1 < self.__size) and (self.getCell(x, y + 1).getColor() == 0) and (not checked[x][y + 1])):
            checked[x][y + 1] = True
            score += self.movableSquares(x, y + 1, checked)

        if ((x - 1 >= 0) and (self.getCell(x - 1, y).getColor() == 0) and (not checked[x - 1][y])):
            checked[x - 1][y] = True
            score += self.movableSquares(x - 1, y, checked)

        if ((y - 1 >= 0) and (self.getCell(x, y - 1).getColor() == 0) and (not checked[x][y - 1])):
            checked[x][y - 1] = True
            score += self.movableSquares(x, y - 1, checked)

        if ((y + 1 < self.__size) and (x + 1 < self.__size) and (self.getCell(x + 1, y + 1).getColor() == 0) and (
                not checked[x + 1][y + 1])):
            checked[x + 1][y + 1] = True
            score += self.movableSquares(x + 1, y + 1, checked)

        if ((y + 1 < self.__size) and (x - 1 >= 0) and (self.getCell(x - 1, y + 1).getColor() == 0) and (
                not checked[x - 1][y + 1])):
            checked[x - 1][y + 1] = True
            score += self.movableSquares(x - 1, y + 1, checked)

        if ((y - 1 >= 0) and (x + 1 < self.__size) and (self.getCell(x + 1, y - 1).getColor() == 0) and (
                not checked[x + 1][y - 1])):
            checked[x + 1][y - 1] = True
            score += self.movableSquares(x + 1, y - 1, checked)

        if ((y - 1 >= 0) and (x - 1 >= 0) and (self.getCell(x - 1, y - 1).getColor() == 0) and (
                not checked[x - 1][y - 1])):
            checked[x - 1][y - 1] = True
            score += self.movableSquares(x - 1, y - 1, checked)

        return score

    def getPlayerX(self, color):
        return self.players[color - 1].getX()

    def getPlayerY(self, color):
        return self.players[color - 1].getY()


class Game:
    __players = [Player for i in range(2)]
    __turn = 0
    __board = None
    __nextPlace = None
    __initialX1 = 0
    __initialX2 = 0
    __initialY1 = 0
    __initialY2 = 0
    gamePanel = None
    colors = ["gray", "blue", "red", "orange"]

    @staticmethod
    def getPlayers():
        return Game.__players

    def __init__(self, p1, p2):
        self.__players = [Player for i in range(2)]
        self.__players[0] = p1
        self.__players[1] = p2
        self.__initialX1 = p1.getX()
        self.__initialX2 = p2.getX()
        self.__initialY1 = p1.getY()
        self.__initialY2 = p2.getY()

    def setXYPlayer1(self, x, y):
        self.__players[0].setX(x)
        self.__players[0].setY(y)

    def setXYPlayer_Oppenent(self, x, y):
        self.__players[1].setX(x)
        self.__players[1].setY(y)

    def start(self, numberOfMatches):
        for k in range(numberOfMatches):
            __turn = 0
            __nextPlace = None
            self.__players[0].setX(self.__initialX1)
            self.__players[0].setY(self.__initialY1)
            self.__players[1].setX(self.__initialX2)
            self.__players[1].setY(self.__initialY2)
            self.__board = Board(self.__players)
            if numberOfMatches == 1:
                win = GraphWin(width=800, height=600)
                win.setCoords(0, 0, 10, 10)
                mySquare = Rectangle(Point(1, 1), Point(9, 9))
                mySquare.draw(win)
            while (self.__board.win() == 0):
                if numberOfMatches == 1:
                    for i in range(0, 8):
                        for j in range(0, 8):
                            if ((self.__board.getCell(i, j).getId() != -1) and (
                                    self.__board.getCell(i, j).getColor() == 0)):
                                m = Rectangle(Point(i + 1, j + 1), Point(i + 2, j + 2))
                                m.setFill(self.colors[3])
                                m.draw(win)

                            else:
                                m = Rectangle(Point(i + 1, j + 1), Point(i + 2, j + 2))
                                m.setFill(self.colors[self.__board.getCell(i, j).getColor()])
                                m.draw(win)

                    for j in range(2):
                        x = self.__board.getPlayerX(j + 1)
                        y = self.__board.getPlayerY(j + 1)
                        m = Rectangle(Point(x + 1, y + 1), Point(x + 2, y + 2))
                        m.setFill(self.colors[j + 1])
                        m.draw(win)

                self.__nextPlace = self.__players[self.__turn].getMove(Board(self.__board))
                print("Real X = " + str(self.__players[0].getX()) + " Real Y = " + str(self.__players[0].getY()))
                if (self.__nextPlace.x == -10):
                    self.__players[1 - self.__turn].win()
                    if numberOfMatches == 1:
                        win.close()
                        print("Player " + str(self.__players[self.__turn].getCol()) + " has exceeded the time limit\n" +
                              "Player " + str(self.__players[1 - self.__turn].getCol()) + " has won\n")
                        return self.__players[0].getVictories(), self.__players[1].getVictories()
                    break

                res = self.__board.move(self.__nextPlace, self.__turn + 1)
                if (res == -2):

                    if (self.__board.getScore(1) > self.__board.getScore(2)):
                        if numberOfMatches == 1:
                            print("No more moves!")
                            print("Player 1 has won")
                            print("score player 1: " + str(self.__board.getScore(1)))
                            print("score player 2: " + str(self.__board.getScore(2)) + "\n")
                        self.__players[0].win()
                    elif (self.__board.getScore(1) < self.__board.getScore(2)):
                        if numberOfMatches == 1:
                            print("No more moves!")
                            print("Player 2 has won")
                            print("score player 1: " + str(self.__board.getScore(1)))
                            print("score player 2: " + str(self.__board.getScore(2)) + "\n")
                        self.__players[1].win()
                    elif numberOfMatches == 1:
                        print("No more moves!")
                        print("Draw!")
                        print("score player 1: " + str(self.__board.getScore(1)))
                        print("score player 2: " + str(self.__board.getScore(2)) + "\n")
                    if numberOfMatches == 1:
                        win.close()
                        return self.__players[0].getVictories(), self.__players[1].getVictories()
                    break

                if (res == -1):
                    self.__players[1 - self.__turn].win()
                    if numberOfMatches == 1:
                        win.close()
                        print("Player " + str(self.__players[self.__turn].getCol()) + " has made an invalid move\n" +
                              "Player " + str(self.__players[1 - self.__turn].getCol()) + " has won\n")
                        return self.__players[0].getVictories(), self.__players[1].getVictories()
                    break

                self.__turn = 1 - self.__turn

            if numberOfMatches == 1:
                win.close()

        return self.__players[0].getVictories(), self.__players[1].getVictories()
