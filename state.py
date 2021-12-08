from indexing import *


def calculate_score(computer, human, distance):
    if human == 0:
        computer_score = pow(10, computer) - distance
        return computer_score, 0
    elif computer == 0:
        human_score = pow(10, human) - distance
        return 0, human_score


class State:
    board = ""

    def __init__(self, board):
        self.board = board

    def heuristic(self):
        computer_score = 0
        human_score = 0
        # horizontally
        for i in range(0, board_height):
            scores = self.connect_four(self, i, right)
            computer_score += scores[0]
            human_score += scores[1]
        # vertically
        for i in range(0, board_width):
            scores = self.connect_four(self, i, up)
            computer_score += scores[0]
            human_score += scores[1]
        #  Diagonally
        for i in range(0, board_height / 2):
            scores = self.connect_four(self, i, up_right)
            computer_score += scores[0]
            human_score += scores[1]
        for i in range(0, board_width / 2 * board_height, board_height):
            scores = self.connect_four(self, i, up_right)
            computer_score += scores[0]
            human_score += scores[1]

    # def horizontal_count(self,start):
    def calculate_distance(self, index):
        distance = 0
        while index != -1 and self.board[index] == '0':
            distance += 1
            index = down(index)
        return distance

    def connect_four(self, i, direction):
        temp, index = i
        while index != -1:
            index = temp
            human = 0
            computer = 0
            distance = 0
            for _ in range(0, 4):
                if self.board[index] == '1':
                    computer += 1
                elif self.board[index] == '2':
                    human += 1
                else:
                    distance += self.calculate_distance(index)
                index = direction(index)
            temp = direction(temp)
        return calculate_score(computer, human, distance)
