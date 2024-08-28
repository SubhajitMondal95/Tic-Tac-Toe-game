import pygame
import sys
from ui import *
from minmax import minimax

pygame.init()

print("Tic-Tac-Toe!\n")

while True:
    window = open_window() 
    create_board(window)
    # Initialize board state
    state = [i for i in range(9)] 
    # Initialize terminal state as false
    terminal_state = False 

    while not terminal_state:   
        for event in pygame.event.get():
            # quit event
            if event.type == pygame.QUIT:  
                 sys.exit(0)    
            # mouse click event
            if event.type == pygame.MOUSEBUTTONDOWN: 
                # Human player's turn -> X
                player = "X"
                pos = pygame.mouse.get_pos() # Get mouse click position
                box = map_to_grid(pos)  # Map mouse click position to board box 0 - 8
                empty_boxes = find_empty_boxes(state) # Find empty boxes
                # If clicked box is empty  
                if box in empty_boxes:
                    place_on_grid(window, box, player) # Place symbol on window
                    state[box] = player # Update board state
                    empty_boxes = find_empty_boxes(state) # Find empty boxes
                    
                    # Check for terminal state
                    game_over = terminal_test(state, player) 
                    
                    # If terminal state is found
                    if game_over :
                        print("Player X won!")
                        pygame.event.get()
                        terminal_state = play_again()
                   
                    # AI player goes
                    player = "O"

                    # If there are empty boxes remaining
                    if len(empty_boxes) != 0:

                        # Minimax algorithm to determine AI's move
                        my_state = state[:] # create copy of state list for scope
                        best_move = minimax(my_state, player)
                        ai_box = int(best_move[0])
                        place_on_grid(window, ai_box, player)  # place AI symbol on window
                        state[ai_box] = player # update board state

                        # Check for terminal state
                        game_over = terminal_test(state,player) 
                        # Terminal state is found
                        if game_over:
                            print("Player O won!")
                            pygame.event.get()
                            terminal_state = play_again()
                

                   
                    
