from tictactoe import *
from ui import *

# return best ai move via minimax search
def minimax(state, current_player):

    if current_player == "O":
        best_move = [-1, -float("inf")]  # Initialize best move for maximizing player
    else:
        best_move = [-1, float("inf")]   # Initialize best move for minimizing player

    empty_boxes = find_empty_boxes(state)

    if terminal_test(state, 'X'):
        return [-1, -10]  # Return a high negative score if 'X' wins
    if terminal_test(state, 'O'):
        return [-1, 10]   # Return a high positive score if 'O' wins
    if len(empty_boxes) == 0:
        return [-1, 0]    # Return 0 for a draw

    for box in empty_boxes:
        index = int(box)
        state[index] = current_player  # Simulate placing current player's symbol on the region
        
        if terminal_test(state, 'O'):
            state[index] = index
            return [index, 10]
        
        score = minimax(state, get_opponent(current_player))  # Recursively evaluate the resulting state
        state[index] = box  # Undo the move

        score[0] = index  # Update the move index in the score tuple

        if current_player == "O":  # If the current player is 'O' (maximizing player)
            if score[1] > best_move[1]:  # Update the best move if the current score is higher
                best_move = score
        else:  # If the current player is 'X' (minimizing player)
            if score[1] < best_move[1]:  # Update the best move if the current score is lower
                best_move = score

    return best_move



