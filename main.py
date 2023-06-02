from rule import check_win
import random
import time
import json


with open('data.json', 'r') as f:
    data = json.load(f)


class TrainingGame:
    def __init__(self) -> None:
        self.board = [' ' for _ in range(9)]
        self.AI_1_mark = 'O'
        self.AI_2_mark = 'X'
        self.AI_1_record = []
        self.AI_2_record = []
    
    def get_empty_cells(self) -> list:
        return [i for i in range(9) if self.board[i] == ' ']

    def get_board(self) -> list:
        return self.board
    
    def play_ai_1(self) -> dict:
        board_to_string = self.get_board_to_string(self.AI_1_mark)
        empty_cells = self.get_empty_cells()
        random_cell = random.choice(empty_cells)
        self.board[random_cell] = self.AI_1_mark
        return {
            'board_to_string': board_to_string,
            'cell': random_cell
        }

    def play_ai_2(self) -> dict:
        board_to_string = self.get_board_to_string(self.AI_2_mark)
        empty_cells = self.get_empty_cells()
        random_cell = random.choice(empty_cells)
        self.board[random_cell] = self.AI_2_mark
        return {
            'board_to_string': board_to_string,
            'cell': random_cell
        }
    
    def get_board_to_string(self, ai) -> str:
        board_to_string = ''.join(self.board).replace(' ', '_')
        if ai == 'O':
            board_to_string = board_to_string.replace('O', '1').replace('X', '2')
        elif ai == 'X':
            board_to_string = board_to_string.replace('O', '2').replace('X', '1')
        return board_to_string
    
    def print_board(self):
        print(' | '.join(self.board[0:3]))
        print(' | '.join(self.board[3:6]))
        print(' | '.join(self.board[6:9]))
        print('-----------------')

    def update_data(self, board_to_string, cell, increasement):
        board_to_string = str(board_to_string)
        cell = str(cell)
        if board_to_string not in data:
            data[board_to_string] = {
                cell: increasement
            }
        if cell not in data[board_to_string]:
            data[board_to_string][cell] = increasement
        else:
            data[board_to_string][cell] += increasement


    def play(self):
        while True:
            if len(self.get_empty_cells()) == 0:
                break
            ai_1 = self.play_ai_1()
            self.AI_1_record.append(ai_1)

            if check_win(self.board, self.AI_1_mark):
                for i in self.AI_1_record:
                    self.update_data(i['board_to_string'], i['cell'], 1)
                for i in self.AI_2_record:
                    self.update_data(i['board_to_string'], i['cell'], -1)
                break


            if len(self.get_empty_cells()) == 0:
                break

            ai_2 = self.play_ai_2()
            self.AI_2_record.append(ai_2)

            if check_win(self.board, self.AI_2_mark):
                for i in self.AI_2_record:
                    self.update_data(i['board_to_string'], i['cell'], 1)
                for i in self.AI_1_record:
                    self.update_data(i['board_to_string'], i['cell'], -1)
                break
        


if __name__ == '__main__':
    start = time.time()
    for i in range(100000):
        print("Game: ", i)
        game = TrainingGame()
        game.play()
    
    with open('data.json', 'w') as f:
        json.dump(data, f)



    print(time.time() - start)