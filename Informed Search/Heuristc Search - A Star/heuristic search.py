# Mohammad Javad Maheronnaghsh
# Student Number: 99105691

import heapq
import time
import numpy as np

# global ans
# ans = ""

class State:
    final_indexes = []
    seen = set()  # convert these array to ndarrays
    frontier = []
    final_matrix = np.array([])
    final_flattened = np.array([])
    to_add = []
    ans = ""
    # global ans

    def __init__(self, matrix, array_of_way):

        State.seen.add((",".join(matrix.flatten())))
        self.matrix = matrix
        self.g = len(array_of_way)
        self.h = self.calculate_heuristic()
        self.to_add.append(self)
        self.way = array_of_way

    def __lt__(self, other):
        return self.g + self.h < other.g + other.h

    def expand(self):
        # create 2 * n new matrices
        for i in range(len(self.matrix)):
            new_matrix = self.matrix.copy()
            new_matrix[i] = np.roll(new_matrix[i], 1)
            boolean = True

            if (",".join(new_matrix.flatten())) in State.seen:
                # بررسی تکراری بودن استیت
                boolean = False
            if boolean:
                tuple_ = ('right', i)
                new_list = self.way.copy()
                new_list.append(tuple_)
                new = State(new_matrix, new_list)
                # global ans
                if np.all(new_matrix.flatten() == State.final_flattened):
                    State.ans += str(len(new.way)) + "\n"
                    for ways in new.way:
                        State.ans += str(ways[0]) + " "
                        State.ans += str(ways[1] + 1) + "\n"
                    return 1

        for i in range(len(self.matrix)):
            new_matrix = self.matrix.copy()
            new_matrix[i] = np.roll(new_matrix[i], -1)
            boolean = True
            if (",".join(new_matrix.flatten())) in State.seen:
                # بررسی تکراری بودن استیت
                boolean = False
            if boolean:
                tuple_ = ('left', i)
                new_list = self.way.copy()
                new_list.append(tuple_)
                new = State(new_matrix, new_list)

                # global ans
                if np.all(new_matrix.flatten() == State.final_flattened):
                    State.ans += str(len(new.way)) + "\n"
                    for ways in new.way:
                        State.ans += str(ways[0]) + " "
                        State.ans += str(ways[1] + 1) + "\n"
                    return 1

        # create 2 * n new matrices

        for i in range(len(self.matrix)):
            new_matrix = self.matrix.copy().T
            new_matrix[i] = np.roll(new_matrix[i], 1)
            new_matrix = new_matrix.T
            boolean = True
            if (",".join(new_matrix.flatten())) in State.seen:
                # بررسی تکراری بودن استیت
                boolean = False
            if boolean:
                tuple_ = ('down', i)
                new_list = self.way.copy()
                new_list.append(tuple_)
                new = State(new_matrix, new_list)
                # global ans
                if np.all(new_matrix.flatten() == State.final_flattened):
                    State.ans += str(len(new.way)) + "\n"
                    for ways in new.way:
                        State.ans += str(ways[0]) + " "
                        State.ans += str(ways[1] + 1) + "\n"
                    return 1

        for i in range(len(self.matrix)):
            new_matrix = self.matrix.copy().T
            new_matrix[i] = np.roll(new_matrix[i], -1)
            new_matrix = new_matrix.T
            boolean = True
            if (",".join(new_matrix.flatten())) in State.seen:
                # بررسی تکراری بودن استیت
                boolean = False
            if boolean:
                tuple_ = ('up', i)
                new_list = self.way.copy()
                new_list.append(tuple_)
                new = State(new_matrix, new_list)
                # global ans
                if np.all(new_matrix.flatten() == State.final_flattened):
                    State.ans += str(len(new.way)) + "\n"
                    for ways in new.way:
                        State.ans += str(ways[0]) + " "
                        State.ans += str(ways[1] + 1) + "\n"
                    return 1

        return 0

    def calculate_heuristic2(self):
        n = len(self.matrix)
        h = 0

        for i in range(n * n):
            matrix_idx = np.where(self.matrix == str(i))
            index_list_matrix = list(zip(matrix_idx[0], matrix_idx[1]))

            index_matrix = index_list_matrix[0]

            index_final = State.final_indexes[i]
            col_diff = abs(index_matrix[0] - index_final[0])
            row_diff = abs(index_matrix[1] - index_final[1])
            h += min(col_diff, abs(n - col_diff))
            h += min(row_diff, abs(n - row_diff))
        return h

    def calculate_heuristic(self):
        n = len(self.matrix)
        row_false = [0] * n
        col_false = [0] * n
        for i in range(n * n):
            matrix_idx = np.where(self.matrix == str(i))
            index_list_matrix = list(zip(matrix_idx[0], matrix_idx[1]))
            index_matrix = index_list_matrix[0]

            index_final = State.final_indexes[i]

            col_diff = abs(index_matrix[0] - index_final[0])
            row_diff = abs(index_matrix[1] - index_final[1])

            col_diff = min(col_diff, abs(n - col_diff))
            row_diff = min(row_diff, abs(n - row_diff))

            # if col_diff != 0:
            col_false[index_matrix[0]] += col_diff
            # if row_diff != 0:
            row_false[index_matrix[1]] += row_diff
        return max(col_false) + max(row_false)

    # def calculate_heuristic(self):
    #     n = len(self.matrix)
    #     row_false = [0] * n
    #     col_false = [0] * n
    #     for i in range(n * n):
    #         matrix_idx = np.where(self.matrix == i)
    #         index_list_matrix = list(zip(matrix_idx[0], matrix_idx[1]))
    #         index_matrix = index_list_matrix[0]
    #
    #         index_final = State.final_indexes[i]
    #
    #         col_diff = abs(index_matrix[0] - index_final[0])
    #         row_diff = abs(index_matrix[1] - index_final[1])
    #
    #         col_diff = min(col_diff, abs(n - col_diff))
    #         row_diff = min(row_diff, abs(n - row_diff))
    #
    #         if col_diff != 0:
    #             col_false[index_matrix[0]] += col_diff
    #         if row_diff != 0:
    #             row_false[index_matrix[1]] += row_diff
    #     return max(col_false) + max(row_false)

    # def calculate_heuristic22(self):
    #     n = len(self.matrix)
    #     h = 0
    #
    #     for i in State.special2:
    #         matrix_idx = np.where(self.matrix == i)
    #         index_list_matrix = list(zip(matrix_idx[0], matrix_idx[1]))
    #
    #         index_matrix = index_list_matrix[0]
    #
    #         index_final = State.final_indexes[i]
    #         col_diff = abs(index_matrix[0] - index_final[0])
    #         row_diff = abs(index_matrix[1] - index_final[1])
    #         h += min(col_diff, abs(n - col_diff))
    #         h += min(row_diff, abs(n - row_diff))
    #     return h


def scan_input():
    final_state = np.array([])
    for i in range(n):
        row = list(input().split())
        if len(final_state) > 0:
            final_state = np.vstack([final_state, row])
        else:
            final_state = np.array(row)
    State.final_matrix = final_state
    State.final_flattened = State.final_matrix.flatten()
    for i in range(n * n):
        final_idx = np.where(State.final_matrix == str(i))
        index_list_final = list(zip(final_idx[0], final_idx[1]))
        index_final = index_list_final[0]
        State.final_indexes.append(index_final)

    start_state = np.array([])
    for i in range(n):
        row = list(input().split())
        if len(start_state) > 0:
            start_state = np.vstack([start_state, row])
        else:
            start_state = np.array(row)

    list_ = []
    State(start_state, list_)

    return final_state, start_state


if __name__ == '__main__':
    # global ans
    # ans = ""
    heapq.heapify(State.frontier)
    n = int(input())

    final_state, start_state = scan_input()

    a = time.time()
    # global string_
    # string_ = ""
    while True:
        if State.to_add:
            heapq.heapify(State.to_add)
            # heapq.heappush(State.frontier, State.to_add.pop())
            State.frontier = heapq.merge(State.frontier, State.to_add)
            State.to_add = []
        # string_ += "*****\n"
        # string_ += "Number of seen nodes = " + str(len(State.seen)) + "\n"
        # print("*******")
        # print("Number of seen nodes = " + str(len(State.seen)))

        # min_state = heapq.heappop(State.frontier)
        min_state = heapq.heappop(list(State.frontier))
        # min_state = State.frontier.pop(0)
        # string_ += "Frontier size = " + str(len(State.frontier)) + '\n'
        # string_ += "h of min_state in frontier = " + str(min_state.h) + "\n"
        # string_ += "g of min state in frontier = " + str(min_state.g) + "\n"
        # print("Frontier size = " + str(len(State.frontier)))
        # print("h of min_state in frontier = " + str(min_state.h))
        # print("g of min state in frontier = " + str(min_state.g))

        answer = min_state.expand()
        b = time.time()
        # if b - a > 10:
        #     raise Exception

        if answer == 1:
            print(State.ans, end='')
            # print(len(State.seen))
            break

    print(b - a)
