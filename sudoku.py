import pygame
import sys
from sudoku_generator import Board

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 540, 600
BACKGROUND_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
SELECTED_CELL_COLOR = (200, 200, 200)
FONT = pygame.font.SysFont("comicsans", 40)

# Blue background color
BOARD_BACKGROUND_COLOR = (211, 232, 255)
TEXT_INPUT_COLOR = (128, 128, 128)

# Screen Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

def draw_game_start():
    # Title font
    start_title_font = pygame.font.Font(None, 50)
    mode_display_font = pygame.font.Font(None, 45)
    button_font = pygame.font.Font(None, 30)

    # Background color
    screen.fill(BOARD_BACKGROUND_COLOR)

    # Draw title
    title_surface = start_title_font.render("Welcome to Sudoku", 0, (0, 0, 0))
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)    # draws the title with rect

    # Game Mode Selection
    mode_surface = mode_display_font.render("Select Game Mode:", 0, (0, 0, 0))
    mode_rectangle = mode_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 10))
    screen.blit(mode_surface, mode_rectangle)

    # Buttons: text
    easy_text = button_font.render("Easy", 0, (255, 255, 255))
    medium_text = button_font.render("Medium", 0, (255, 255, 255))
    hard_text = button_font.render("Hard", 0, (255, 255, 255))

    # Buttons: background and color
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill((0, 33, 165))
    easy_surface.blit(easy_text, (10, 10))
    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill((0, 33, 165))
    medium_surface.blit(medium_text, (10, 10))
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill((0, 33, 165))
    hard_surface.blit(hard_text, (10, 10))

    # Buttons: Rectangle
    easy_rectangle = easy_surface.get_rect(center=(WIDTH // 2 - 150, HEIGHT // 3 + 170))
    medium_rectangle = medium_surface.get_rect(center=(WIDTH // 2, HEIGHT // 3 + 170))
    hard_rectangle = hard_surface.get_rect(center=(WIDTH // 2 + 150, HEIGHT // 3 + 170))

    # Draw Buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    return "easy"
                if medium_rectangle.collidepoint(event.pos):
                    return "medium"
                if hard_rectangle.collidepoint(event.pos):
                    return "hard"
    pygame.display.update()

def bottom_menu():
    # Button font
    bottom_button_font = pygame.font.Font(None, 25)

    # Buttons: text
    reset_text = bottom_button_font.render("RESET", 0, (255, 255, 255))
    restart_text = bottom_button_font.render("RESTART", 0, (255, 255, 255))
    exit_text = bottom_button_font.render("EXIT", 0, (255, 255, 255))
    solve_text = bottom_button_font.render("SOLVE", 0, (255, 255, 255))

    # Buttons: background and color
    button_color = (255, 140, 0)  # Orange color
    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill(button_color)
    reset_surface.blit(reset_text, (10, 10))
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(button_color)
    restart_surface.blit(restart_text, (10, 10))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(button_color)
    exit_surface.blit(exit_text, (10, 10))
    solve_surface = pygame.Surface((solve_text.get_size()[0] + 20, solve_text.get_size()[1] + 20))
    solve_surface.fill(button_color)
    solve_surface.blit(solve_text, (10, 10))

    # Buttons: Rectangle
    reset_rectangle = reset_surface.get_rect(center=(WIDTH // 2 - 155, HEIGHT - 30))
    restart_rectangle = restart_surface.get_rect(center=(WIDTH // 2 - 50, HEIGHT - 30))
    exit_rectangle = exit_surface.get_rect(center=(WIDTH // 2 + 50, HEIGHT - 30))
    solve_rectangle = solve_surface.get_rect(center=(WIDTH // 2 + 137, HEIGHT - 30))

    # Draw Buttons
    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exit_surface, exit_rectangle)
    screen.blit(solve_surface, solve_rectangle)


    pygame.display.update()

    return reset_rectangle, restart_rectangle, exit_rectangle, solve_rectangle
def draw_end_screen(message):
    end_title_font = pygame.font.Font(None, 75)
    button_font = pygame.font.Font(None, 30)

    screen.fill(BOARD_BACKGROUND_COLOR)

    title_surface = end_title_font.render(message, 0, (0, 0, 0))
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(title_surface, title_rectangle)

    button_text = button_font.render("EXIT" if message == "Game Won!" else "RESTART", 0, (255, 255, 255))
    button_surface = pygame.Surface((button_text.get_size()[0] + 20, button_text.get_size()[1] + 20))
    button_surface.fill((255, 140, 0))
    button_surface.blit(button_text, (10, 10))
    button_rectangle = button_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

    screen.blit(button_surface, button_rectangle)
    pygame.display.update()

    return button_rectangle

# Main Function
def main():
    # Set up the board
    difficulty = draw_game_start()
    board = Board(WIDTH, HEIGHT - 60, screen, difficulty, LINE_COLOR, FONT)
    solved = False

    # Game loop
    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)

        # Draw the Board
        board.draw()

        # Draw Bottom Menu
        reset_rectangle, restart_rectangle, exit_rectangle, solve_rectangle = bottom_menu()

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked_cell = board.click(*pos)
                if clicked_cell:
                    board.select(*clicked_cell)

                # Bottom menu interaction
                if reset_rectangle.collidepoint(event.pos):
                    board.reset_to_original()
                elif restart_rectangle.collidepoint(event.pos):
                    main()  # Restart the game
                elif exit_rectangle.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                elif solve_rectangle.collidepoint(event.pos):
                    board.solve()
                    solved = True

            if event.type == pygame.KEYDOWN:
                if board.selected_cell:
                    if event.key in [pygame.K_1, pygame.K_KP1]:
                        board.sketch(1)
                    elif event.key in [pygame.K_2, pygame.K_KP2]:
                        board.sketch(2)
                    elif event.key in [pygame.K_3, pygame.K_KP3]:
                        board.sketch(3)
                    elif event.key in [pygame.K_4, pygame.K_KP4]:
                        board.sketch(4)
                    elif event.key in [pygame.K_5, pygame.K_KP5]:
                        board.sketch(5)
                    elif event.key in [pygame.K_6, pygame.K_KP6]:
                        board.sketch(6)
                    elif event.key in [pygame.K_7, pygame.K_KP7]:
                        board.sketch(7)
                    elif event.key in [pygame.K_8, pygame.K_KP8]:
                        board.sketch(8)
                    elif event.key in [pygame.K_9, pygame.K_KP9]:
                        board.sketch(9)
                    elif event.key == pygame.K_RETURN:
                        board.place_number(board.selected_cell.sketched_value)
                        board.update_board()
                        if board.is_full() and board.check_board():
                            button_rect = draw_end_screen("Game Won!")
                            while True:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        if button_rect.collidepoint(event.pos):
                                            pygame.quit()
                                            sys.exit()
                        elif board.is_full():
                            button_rect = draw_end_screen("Game Over :(")
                            while True:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        if button_rect.collidepoint(event.pos):
                                            main()
                    elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                        board.clear()
                    elif event.key == pygame.K_UP:
                        board.move_selection('up')
                    elif event.key == pygame.K_DOWN:
                        board.move_selection('down')
                    elif event.key == pygame.K_LEFT:
                        board.move_selection('left')
                    elif event.key == pygame.K_RIGHT:
                        board.move_selection('right')

        pygame.display.update()

if __name__ == "__main__":
    main()