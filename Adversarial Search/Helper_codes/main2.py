import numpy as np
import random
import time

from graphics import *
from question3 import Cell
from question3 import IntPair
from question3 import Player
from question3 import NaivePlayer
from question3 import Board
from question3 import Game
from copy import deepcopy

from timeit import default_timer as timer

import numpy as np
import random
from copy import deepcopy


# from timeit import default_timer as timer


class MinimaxPlayer(Player):
    time_ = 0
    g = None

    def __init__(self, col, x, y, max_depth=4):
        super().__init__(col, x, y)
        self.max_depth = max_depth

    # def my_move(self, board, nextPlace, playerColor):
    #     board.setNumberOfMoves(board.getNumberOfMoves() + 1)
    #
    #     board.getCell(nextPlace.x, nextPlace.y).setColor(playerColor)
    #
    #     board.players[playerColor-1].setX(nextPlace.x)
    #     board.players[playerColor-1].setY(nextPlace.y)

    def calculate_value(self, board):
        xx = abs(board.getPlayerX(1) - board.getPlayerX(2))
        yy = abs(board.getPlayerY(1) - board.getPlayerY(2))
        if xx == 0 and yy == 0:
            return board.getScore(1) - board.getScore(2) + 40
        elif xx == 0:
            return board.getScore(1) - board.getScore(2) + 20 + 10 / yy
        elif yy == 0:
            return board.getScore(1) - board.getScore(2) + 20 + 10 / xx
        return board.getScore(1) - board.getScore(2) + 10/xx + 10/yy

    def check_if_can_move(self, board, nextPlace, currentPlace, playerColor):
        if ((nextPlace.x < 0) | (nextPlace.y < 0) | (nextPlace.x >= 8) | (nextPlace.y >= 8)):
            return False
        elif ((abs(currentPlace.y - nextPlace.y) > 1) | (abs(currentPlace.x - nextPlace.x) > 1)):
            print("Invalid Call!")
            return False
        elif (board.getCell(nextPlace.x, nextPlace.y).getColor() != 0):
            return False
        elif ((nextPlace.x == board.players[2 - playerColor].getX()) and (
                nextPlace.y == board.players[2 - playerColor].getY())):
            return False
        elif (board.getNumberOfMoves() + 1 > 80):
            return False
        return True

    def min_value(self, board, alpha, beta, depth):
        # print("MinValue - Depth = " + str(depth))
        value = 1000000
        if depth == self.max_depth:
            return self.calculate_value(board), None
        min_action = -1
        array = [0, 1, 2, 3, 4, 5, 6, 7]
        from random import shuffle
        shuffle(array)
        for counter in array:
            pre_x = board.getPlayerX(0)
            pre_y = board.getPlayerY(0)
            currentPlace = IntPair(pre_x, pre_y)
            if counter == 0:
                self.setX(pre_x + 1)
                self.setY(pre_y + 1)
            elif counter == 1:
                self.setX(pre_x + 1)
                self.setY(pre_y + 0)
            elif counter == 2:
                self.setX(pre_x + 1)
                self.setY(pre_y - 1)
            elif counter == 3:
                self.setX(pre_x + 0)
                self.setY(pre_y + 1)
            elif counter == 4:
                self.setX(pre_x + 0)
                self.setY(pre_y - 1)
            elif counter == 5:
                self.setX(pre_x - 1)
                self.setY(pre_y + 1)
            elif counter == 6:
                self.setX(pre_x - 1)
                self.setY(pre_y + 0)
            elif counter == 7:
                self.setX(pre_x - 1)
                self.setY(pre_y - 1)
            x = self.getX()
            y = self.getY()
            nxt = IntPair(x, y)
            if self.check_if_can_move(board, nxt, currentPlace, 2) == False:
                continue
            copied_board = deepcopy(board)

            move_ = copied_board.move(nxt, 2)
            answer = [0, 0]
            if move_ == -1:
                answer[0] = 1000
            else:
                if copied_board.getNumberOfMoves() == copied_board.maxNumberOfMoves:
                    answer[0] = self.calculate_value(copied_board)
                else:
                    answer = self.max_value(Board(copied_board), alpha, beta, depth + 1)
            self.setX(pre_x)
            self.setY(pre_y)
            if answer[0] < alpha:
                return answer[0], counter
            if answer[0] < value:
                value = answer[0]
                min_action = counter
            beta = min(beta, value)

        if value == 1000000:
            # return 20000 ,0
            return self.calculate_value(board), -8
        return value, min_action

    def max_value(self, board, alpha, beta, depth):
        # print("MaxValue - Depth = " + str(depth))
        if depth == self.max_depth:
            return self.calculate_value(board), None

        value = -1000000
        max_action = -1
        array = [0, 1, 2, 3, 4, 5, 6, 7]
        from random import shuffle
        shuffle(array)
        for counter in array:
            pre_x = board.getPlayerX(1)
            pre_y = board.getPlayerY(1)
            currentPlace = IntPair(pre_x, pre_y)
            if counter == 0:
                self.setX(pre_x + 1)
                self.setY(pre_y + 1)
            elif counter == 1:
                self.setX(pre_x + 1)
                self.setY(pre_y + 0)
            elif counter == 2:
                self.setX(pre_x + 1)
                self.setY(pre_y - 1)
            elif counter == 3:
                self.setX(pre_x + 0)
                self.setY(pre_y + 1)
            elif counter == 4:
                self.setX(pre_x + 0)
                self.setY(pre_y - 1)
            elif counter == 5:
                self.setX(pre_x - 1)
                self.setY(pre_y + 1)
            elif counter == 6:
                self.setX(pre_x - 1)
                self.setY(pre_y + 0)
            elif counter == 7:
                self.setX(pre_x - 1)
                self.setY(pre_y - 1)
            x = self.getX()
            y = self.getY()
            nxt = IntPair(x, y)
            if self.check_if_can_move(board, nxt, currentPlace, 1) == False:
                continue
            copied_board = deepcopy(board)
            move_ = copied_board.move(nxt, 1)
            answer = [0, 0]
            if move_ == -1:
                answer[0] = -100000
            else:
                if copied_board.getNumberOfMoves() == copied_board.maxNumberOfMoves:
                    answer[0] = self.calculate_value(copied_board)
                else:
                    answer = self.min_value(Board(copied_board), alpha, beta, depth + 1)
            self.setX(pre_x)
            self.setY(pre_y)
            if answer[0] > beta:
                return answer[0], counter
            if answer[0] > value:
                value = answer[0]
                max_action = counter
            alpha = max(alpha, value)
        if value == -1000000:
            if depth == 0:
                print("WHAT?")
                return -10, -10
            return self.calculate_value(board), -8
        return value, max_action

    def getMove(self, board):
        x_next = board.getPlayerX(1)
        y_next = board.getPlayerY(1)
        self.setX(x_next)
        self.setY(y_next)
        x_next_opponent = board.getPlayerX(2)
        y_next_opponent = board.getPlayerY(2)

        pre_x = x_next
        pre_y = y_next

        max_ = self.max_value(deepcopy(board), -100000, 100000, 0)

        if max_[0] == -10:
            return IntPair(-10, -10)
        counter = max_[1]

        if counter == 0:
            x_next = x_next + 1
            y_next = y_next + 1

        elif counter == 1:
            x_next = x_next + 1
            y_next = y_next + 0

        elif counter == 2:
            x_next = x_next + 1
            y_next = y_next - 1

        elif counter == 3:
            x_next = x_next + 0
            y_next = y_next + 1


        elif counter == 4:
            x_next = x_next + 0
            y_next = y_next - 1

        elif counter == 5:
            x_next = x_next - 1
            y_next = y_next + 1

        elif counter == 6:
            x_next = x_next - 1
            y_next = y_next + 0

        elif counter == 7:
            x_next = x_next - 1
            y_next = y_next - 1
        # board.players[0].setX(pre_x)
        # board.players[0].setY(pre_y)
        # Game.getPlayers()[0].setX(pre_x)
        # Game.getPlayers()[0].setY(pre_y)
        g1 = MinimaxPlayer.g
        g1.setXYPlayer1(pre_x, pre_y)
        print("X = " + str(pre_x) + " Y = " + str(pre_y))
        # g1.setXYPlayer_Oppenent(x_next_opponent, y_next_opponent)

        return IntPair(x_next, y_next)


if __name__ == '__main__':
    p1 = MinimaxPlayer(1, 0, 0)
    p2 = NaivePlayer(2, 7, 7)
    # p2 = MinimaxPlayer(2, 7, 7)

    MinimaxPlayer.g = Game(p1, p2)

    number_of_matches = 1
    score1, score2 = MinimaxPlayer.g.start(number_of_matches)

    print(score1 / number_of_matches)
