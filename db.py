import json


class Database:
    def __init__(self, path):
        self.path = path
        self.data = self.load()

    def save(self):
        with open(self.path, 'w') as f:
            json.dump(self.data, f)

    def load(self):
        try:
            with open(self.path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    async def plus(self, board_to_string, cell):
        cell = str(cell)
        if board_to_string not in self.data:
            self.data[board_to_string] = {
                cell: 1
            }
        else:
            if cell not in self.data[board_to_string]:
                self.data[board_to_string][cell] = 1
            self.data[board_to_string][cell] += 1
        await self.save_async()

    async def minus(self, board_to_string, cell):
        cell = str(cell)
        if board_to_string not in self.data:
            self.data[board_to_string] = {
                cell: -1
            }
        else:
            if cell not in self.data[board_to_string]:
                self.data[board_to_string][cell] = -1
            self.data[board_to_string][cell] -= 1
        await self.save_async()

    async def update(self, board_to_string, cell, increment):
        cell = str(cell)
        if board_to_string not in self.data:
            self.data[board_to_string] = {
                cell: increment
            }
        else:
            if cell not in self.data[board_to_string]:
                self.data[board_to_string][cell] = increment
            self.data[board_to_string][cell] += increment
        await self.save_async()

    async def save_async(self):
        with open(self.path, 'w') as f:
            json.dump(self.data, f)




if __name__ == '__main__':
    print('db.py')
