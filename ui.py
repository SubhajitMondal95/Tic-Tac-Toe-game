import pygame
import sys

# Define UI colors
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

# Define UI dimensions
x_len = 600
y_len = 600
line_thickness = 3

# Open Pygame window
def open_window():
    screen = pygame.display.set_mode((x_len, y_len))
    pygame.display.set_caption('Tic-Tac-Toe')
    return screen

# Create game board
def create_board(screen):
    screen.fill(white)
    # Draw Tic-Tac-Toe grid
    pygame.draw.rect(screen, black, (0, 0, x_len, y_len), line_thickness * 3)
    pygame.draw.rect(screen, black, (0, 0, x_len, y_len / 3), line_thickness)
    pygame.draw.rect(screen, black, (0, 0, x_len, y_len * 2 / 3), line_thickness)
    pygame.draw.rect(screen, black, (0, 0, x_len / 3, y_len), line_thickness)
    pygame.draw.rect(screen, black, (0, 0, x_len * 2 / 3, y_len), line_thickness)
    pygame.display.update()

# Map mouse click to grid
def map_to_grid(pos):
    x = pos[0]
    y = pos[1]
    if x < x_len / 3:
        if y < y_len / 3:
            return 0
        elif y_len / 3 < y < y_len * 2 / 3:
            return 3
        else:
            return 6
    elif x_len / 3 < x < x_len * 2 / 3:
        if y < y_len / 3:
            return 1
        elif y_len / 3 < y < y_len * 2 / 3:
            return 4
        else:
            return 7
    else:
        if y < y_len / 3:
            return 2
        elif y_len / 3 < y < y_len * 2 / 3:
            return 5
        else:
            return 8

# Place symbol on grid
def place_on_grid(screen, box, player):
    font_size = 180
    font_family = 'Calibri'

    # Set color and position offsets based on player
    if player == "X":
        color = red
        offset_x = 55
        offset_y = 20
    elif player == "O":
        color = blue
        offset_x = 45
        offset_y = 20

    # Render text surface with player symbol
    myfont = pygame.font.SysFont(font_family, font_size)
    textsurface = myfont.render(player, True, color)

    # Calculate position offsets based on grid box
    if box == 1 or box == 4 or box == 7:
        offset_x += x_len / 3
    elif box == 2 or box == 5 or box == 8:
        offset_x += x_len * 2 / 3
    if box == 3 or box == 4 or box == 5:
        offset_y += y_len / 3
    elif box == 6 or box == 7 or box == 8:
        offset_y += y_len * 2 / 3

    # Blit text surface onto screen
    screen.blit(textsurface, (offset_x, offset_y))
    pygame.display.update() 

# Return opponent's symbol
def get_opponent(player):
    if player == "X":
        return "O"
    else:
        return "X"

# Find empty boxes
def find_empty_boxes(state):
    empty_boxes = []
    for i in range(0, len(state)):
        if state[i] not in ["X", "O"]:
            empty_boxes.append(state[i])
    return empty_boxes

# Search for terminal state
def terminal_test(state, player):
    empty_boxes = find_empty_boxes(state)
    winning_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    # Check winning conditions
    for condition in winning_conditions:
        if all(state[i] == player for i in condition):
            return True  # Player wins
    if len(empty_boxes) == 0:
        return True  # Draw
    return False

# Play again prompt
def play_again():
    while True:
        print("Play again? [Y/N]\n> ")
        answer = input().lower()
        if answer == "y":
            return True
        elif answer == "n":
            sys.exit(0)
        else:
            print("Please respond with 'Y' or 'N'.\n")

# Main game loop
def main():
    screen = open_window()
    create_board(screen)
    state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    terminal_state = False
    player = "X"

    while not terminal_state:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                region = map_to_grid(pos)
                empty_boxes = find_empty_boxes(state)
                if region in empty_boxes:
                    place_on_grid(screen, region, player)
                    state[region] = player
                    if terminal_test(state, player):
                        pygame.event.get()
                        terminal_state = play_again()
                    player = get_opponent(player)

if __name__ == "__main__":
    main()
