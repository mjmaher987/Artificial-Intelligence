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


class MinimaxPlayer(Player):
    def __init__(self, col, x, y, max_depth=4):
        super().__init__(col, x, y)
        self.max_depth = max_depth

    def calculate_value(self, board):
        return board.getScore(1) - board.getScore(0)

    def min_value(self, board, alpha, beta, depth):
        # print("We are in min_value function")
        # print("depth is = " + str(depth))
        value = 10000
        if depth == self.max_depth:  # TODO
            return self.calculate_value(board), None

        counter = 0
        min_action = -1
        while counter < 8:
            copied_board = deepcopy(board)
            pre_x = copied_board.getPlayerX(0)
            pre_y = copied_board.getPlayerY(0)
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
            move_ = copied_board.move(nxt, 2)
            answer = [0, 0]
            if move_ == -1:
                answer[0] = 1000
            else:
                if copied_board.getNumberOfMoves() == copied_board.maxNumberOfMoves:
                    answer[0] = self.calculate_value(copied_board)
                else:
                    answer = self.max_value(Board(copied_board), alpha, beta, depth + 1)

            if answer[0] < alpha:
                print("*******")
                return answer[0], min_action
            if answer[0] < value:
                value = answer[0]
                min_action = counter
            beta = min(beta, value)

            counter += 1
        return value, min_action

    def max_value(self, board, alpha, beta, depth):
        # print("We are in max_value function")
        # print("depth is = " + str(depth))
        if depth == self.max_depth:  # TODO
            return self.calculate_value(board), None

        counter = 0
        value = -10000
        max_action = -1
        while counter < 8:
            copied_board = deepcopy(board)
            pre_x = copied_board.getPlayerX(1)
            pre_y = copied_board.getPlayerY(1)
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
            move_ = copied_board.move(nxt, 1)
            answer = [0, 0]
            if move_ == -1:
                answer[0] = -1000
            else:
                if copied_board.getNumberOfMoves() == copied_board.maxNumberOfMoves:
                    answer[0] = self.calculate_value(copied_board)
                else:
                    answer = self.min_value(Board(copied_board), alpha, beta, depth + 1)
            # answer = self.min_value(Board(copied_board), alpha, beta, depth + 1)
            self.setX(pre_x)
            self.setY(pre_y)

            if answer[0] > beta:
                print("##Beta##")
                return answer[0], counter
            if answer[0] > value:
                value = answer[0]
                max_action = counter
            alpha = max(alpha, value)
            counter += 1
        return value, max_action

    def getMove(self, board):
        x_next = self.getX()
        y_next = self.getY()

        import multiprocessing

        # if __name__ == '__main__':
        #     # TODO
        #     """
        #     how to handle 2 seconds time limit?
        #     """
        # p = multiprocessing.Process(target=self.max_value, args=(board, 1000, -1000, 0,))
            #
            # p.start()
            # p.join(2)
            # print(p)
            # if p.is_alive():
            #     print("running... let's kill it...")
            #     p.terminate()
            #     p.join()
            #     print(-10)
            #     return IntPair(-10, -10)

        max_ = self.max_value(board, -1000, 1000, 0)
        counter = max_[1]
        # print("counter is " + str(counter))
        # print(max_[0])
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
        # print("answer is " + str(x_next) + " " + str(y_next))
        return IntPair(x_next, y_next)


if __name__ == '__main__':
    p1 = MinimaxPlayer(1, 0, 0)
    p2 = NaivePlayer(2, 7, 7)
    # p2 = MinimaxPlayer(2, 7, 7)

    g = Game(p1, p2)

    number_of_matches = 1
    score1, score2 = g.start(number_of_matches)

    print(score1 / number_of_matches)
