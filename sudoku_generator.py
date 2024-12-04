import math
import random
import pygame
"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/
"""

class SudokuGenerator:
    '''
    Create a sudoku board - initialize class variables and set up the 2D board
    This should initialize:
    self.row_length     - the length of each row
    self.removed_cells  - the total number of cells to be removed
    self.board          - a 2D list of ints to represent the board
    self.box_length     - the square root of row_length

    Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

    Return:
    None
    '''
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for _ in range(row_length)] for _ in range(row_length)]
        self.solution_board = None
        self.box_length = int(math.sqrt(row_length))

    '''
    Returns a 2D python list of numbers which represents the board

    Parameters: None
    Return: list[list]
    '''
    def get_board(self):
        return self.board

    '''
    Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

    Parameters: None
    Return: None
    '''
    def get_solution(self):
        return self.solution_board

    def print_board(self):
        for row in self.board:
            print(row)

    '''
    Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

    Parameters:
    row is the index of the row we are checking
    num is the value we are looking for in the row

    Return: boolean
    '''
    def valid_in_row(self, row, num):
        return num not in self.board[row]

    '''
    Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

    Parameters:
    col is the index of the column we are checking
    num is the value we are looking for in the column

    Return: boolean
    '''
    def valid_in_col(self, col, num):
        for row in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True

    '''
    Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

    Parameters:
    row_start and col_start are the starting indices of the box to check
    i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
    num is the value we are looking for in the box

    Return: boolean
    '''
    def valid_in_box(self, row_start, col_start, num):
        for row in range(self.box_length):
            for col in range(self.box_length):
                if self.board[row_start + row][col_start + col] == num:
                    return False
        return True

    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

    Parameters:
    row and col are the row index and col index of the cell to check in the board
    num is the value to test if it is safe to enter in this cell

    Return: boolean
    '''

    def is_valid(self, row, col, num):
        return (self.valid_in_row(row, num) and
                self.valid_in_col(col, num) and
                self.valid_in_box(row - row % self.box_length, col - col % self.box_length, num))

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

    Parameters:
    row_start and col_start are the starting indices of the box to check
    i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

    Return: None
    '''
    def fill_box(self, row_start, col_start):
        nums = list(range(1, self.row_length + 1))
        random.shuffle(nums)
        for i in range(self.box_length):
            for j in range(self.box_length):
                self.board[row_start + i][col_start + j] = nums.pop()

    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

    Parameters: None
    Return: None
    '''
    def fill_diagonal(self):
        for i in range(0, self.row_length, self.box_length):
            self.fill_box(i, i)

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled

    Parameters:
    row, col specify the coordinates of the first empty (0) cell

    Return:
    boolean (whether or not we could solve the board)
    '''
    def fill_remaining(self, row, col):
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

    Parameters: None
    Return: None
    '''

    def fill_values(self):
        self.fill_diagonal()
        filled = self.fill_remaining(0, 0)  # Correct starting point
        self.solution_board = [row[:] for row in self.board]
        print(f"Board filled: {filled}")  # Debugging

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called

    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

    Parameters: None
    Return: None
    '''

    def remove_cells(self):
        count = self.removed_cells
        while count > 0:
            row = random.randint(0, self.row_length - 1)
            col = random.randint(0, self.row_length - 1)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                count -= 1

'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    return board




class Cell:
    def __init__(self, value, row, col, screen, line_color, font):
        self.value = value
        self.sketched_value = 0
        self.row = row
        self.col = col
        self.screen = screen  # Ensure screen is passed correctly
        self.line_color = line_color  # Add line color to Cell class
        self.font = font  # Add font to Cell class
        self.selected = False
        self.cell_background_color = (211, 232, 255)
        self.original_value = value  # Store the original value


    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        cell_size = self.screen.get_width() // 9
        x = self.col * cell_size
        y = self.row * cell_size

        # Draw cell background
        pygame.draw.rect(self.screen, self.cell_background_color, (x, y, cell_size, cell_size))

        # Highlight cell background
        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), (x, y, cell_size, cell_size), 5)  # Red border for selected

        # Draw sketched value
        if self.sketched_value != 0 and self.value == 0:
            text = self.font.render(str(self.sketched_value), True, (128, 128, 128))  # Light gray for sketched
            text_rect = text.get_rect(center=(x + cell_size // 4, y + cell_size // 3))
            self.screen.blit(text, text_rect)

        # Draw cell value
        if self.value != 0:
            text = self.font.render(str(self.value), True, (0, 0, 0))
            text_rect = text.get_rect(center=(x + cell_size // 2, y + cell_size // 2))
            self.screen.blit(text, text_rect)

        # Draw cell border
        pygame.draw.rect(self.screen, self.line_color, (x, y, cell_size, cell_size), 1)

class Board:
    def __init__(self, width, height, screen, difficulty, line_color, font):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.line_color = line_color  # Add line color to Board class
        self.font = font  # Add font to Board class
        self.board_background_color = (211, 232, 255) #set board color same as in pdf

        if difficulty == 'easy':
            removed_cells = 30
        elif difficulty == 'medium':
            removed_cells = 40
        elif difficulty == 'hard':
            removed_cells = 50
        else:
            removed_cells = 30

        # Generate board using SudokuGenerator
        self.board = SudokuGenerator(9, removed_cells+1)
        self.board.fill_values()  # Fill the board correctly
        print("Initial solved board:")
        self.board.print_board()  # Debugging: Print the solved board
        self.board.remove_cells()  # Then remove cells based on difficulty
        self.cells = [
            [Cell(self.board.get_board()[i][j], i, j, self.screen, self.line_color, self.font) for j in range(9)]
            for i in range(9)
        ]
        self.original_board = [[cell.value for cell in row] for row in self.cells]
        self.solution = self.board.get_solution()  # 保存正确答案
        self.selected_cell = None
        self.solved = False


    def draw(self):
        # Fill the screen with the board background color
        self.screen.fill(self.board_background_color)

        # Calculate cell size based on board dimensions
        cell_size = self.width // 9

        # Draw each cell
        for row in self.cells:
            for cell in row:
                cell.draw()

        # Draw vertical and horizontal lines for the grid
        for i in range(10):  # 10 lines to cover all 9 cells + edges
            # Determine line width: thicker lines for 3x3 grid borders
            vertical_line_width = 4 if i % 3 == 0 else 1

            # Draw vertical lines
            pygame.draw.line(
                self.screen,
                self.line_color,
                (i * cell_size, 0),
                (i * cell_size, self.height),
                vertical_line_width

            )

            # Draw horizontal lines
            horizontal_line_width = 4 if i % 3 == 0 else 1
            pygame.draw.line(
                self.screen,
                self.line_color,
                (0, i * cell_size),
                (self.width, i * cell_size),
                horizontal_line_width
            )

    def select(self, row, col):
        if self.selected_cell:
            self.selected_cell.selected = False
        self.selected_cell = self.cells[row][col]
        self.selected_cell.selected = True

    def click(self, x, y):
        if 0 <= x <= self.width and 0 <= y <= self.height:
            cell_width = self.width // 9
            cell_height = self.height // 9
            return y // cell_height, x // cell_width
        return None

    def clear(self):
        if self.selected_cell and self.original_board[self.selected_cell.row][self.selected_cell.col] == 0:
            # Only allow clearing if the cell is not part of the original puzzle
            self.selected_cell.set_cell_value(0)
            self.selected_cell.set_sketched_value(0)

    def sketch(self, value):
        if self.selected_cell and self.selected_cell.value == 0:
            self.selected_cell.set_sketched_value(value)

    def place_number(self, value):
        if self.selected_cell and self.original_board[self.selected_cell.row][self.selected_cell.col] == 0:
            self.selected_cell.set_cell_value(value)  # Use the passed value
            self.update_board()
        #     if self.is_full():
        #         return self.check_victory()
        # return None


    def reset_to_original(self):
        for i in range(9):
            for j in range(9):
                if self.original_board[i][j] == 0:
                    self.cells[i][j].set_cell_value(0)
                    self.cells[i][j].set_sketched_value(0)

    def is_full(self):
        for row in self.cells:
            for cell in row:
                if cell.value == 0:
                    return False
        return True

    def update_board(self):
        for i in range(9):
            for j in range(9):
                self.board.board[i][j] = self.cells[i][j].value


    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.cells[i][j].value == 0:
                    return i, j
        return None

    def check_board(self):
        self.update_board()
        for i in range(9):
            for j in range(9):
                num = self.board.board[i][j]
                self.board.board[i][j] = 0
                if not self.board.is_valid(i, j, num):
                    return False
                self.board.board[i][j] = num
        return True

    def check_victory(self):
        self.update_board()
        for i in range(9):
            for j in range(9):
                num = self.board.board[i][j]
                if not self.board.is_valid(i, j, num):
                    return False
        self.solved = True
        return True

    def solve(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].set_cell_value(self.solution[i][j])
                self.cells[i][j].set_sketched_value(0)
        self.update_board()
        self.solved = True

    def move_selection(self, direction):
        if self.selected_cell:
            row, col = self.selected_cell.row, self.selected_cell.col
            if direction == 'up' and row > 0:
                self.select(row - 1, col)
            elif direction == 'down' and row < 8:
                self.select(row + 1, col)
            elif direction == 'left' and col > 0:
                self.select(row, col - 1)
            elif direction == 'right' and col < 8:
                self.select(row, col + 1)
