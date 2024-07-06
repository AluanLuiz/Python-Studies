import tkinter as tk
import random

class MinesweeperGame:
    def __init__(self, master, rows, cols, mines):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.revealed = [[False for _ in range(cols)] for _ in range(rows)]
        self.buttons = []
        self.mines_left = mines

        self.create_widgets()
        self.place_mines()
        self.calculate_numbers()

    def create_widgets(self):
        self.frame = tk.Frame(self.master)
        self.frame.grid()

        self.mines_left_label = tk.Label(self.frame, text=f'Minas Restantes: {self.mines_left}')
        self.mines_left_label.grid(row=0, column=0, columnspan=self.cols)

        for i in range(self.rows):
            row_buttons = []
            for j in range(self.cols):
                button = tk.Button(self.frame, width=2, height=1, command=lambda row=i, col=j: self.reveal(row, col))
                button.grid(row=i+1, column=j)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def place_mines(self):
        mines_placed = 0
        while mines_placed < self.mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if self.board[row][col] != 'X':
                self.board[row][col] = 'X'
                mines_placed += 1

    def calculate_numbers(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] != 'X':
                    count = self.count_adjacent_mines(row, col)
                    self.board[row][col] = str(count) if count > 0 else ' '

    def count_adjacent_mines(self, row, col):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (0 <= row + i < self.rows and
                    0 <= col + j < self.cols and
                    self.board[row + i][col + j] == 'X'):
                    count += 1
        return count

    def reveal(self, row, col):
        if self.revealed[row][col]:
            return
        self.revealed[row][col] = True
        if self.board[row][col] == 'X':
            self.buttons[row][col].config(text='*', fg='red', state='disabled', relief=tk.SUNKEN)
            self.game_over()
        else:
            self.buttons[row][col].config(text=self.board[row][col], state='disabled', relief=tk.SUNKEN)
            if self.board[row][col] == ' ':
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (0 <= row + i < self.rows and
                            0 <= col + j < self.cols):
                            self.reveal(row + i, col + j)
        self.update_buttons()

    def game_over(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == 'X':
                    self.buttons[i][j].config(text='*', fg='red', state='disabled', relief=tk.SUNKEN)
                else:
                    self.buttons[i][j].config(state='disabled')

    def update_buttons(self):
        self.mines_left = sum(row.count('X') for row in self.board) - sum(row.count(True) for row in self.revealed)
        self.mines_left_label.config(text=f'Minas Restantes: {self.mines_left}')

def main():
    root = tk.Tk()
    root.title("Campo Minado")
    rows = 10
    cols = 10
    mines = 15
    game = MinesweeperGame(root, rows, cols, mines)
    root.mainloop()

if __name__ == "__main__":
    main()
