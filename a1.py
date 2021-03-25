"""
Sliding Puzzle Game
Assignment 1
Semester 1, 2021
CSSE1001/CSSE7030
"""

from a1_support import *
import math


# Replace these <strings> with your name, student number and email address.
__author__ = "<Your Name>, <Your Student Number>"
__email__ = "<Your Student Email>"

# def check_win(puzzle: str, solution: str) -> bool:
def check_win(puzzle, solution):
    solution_list = list(solution)
    solution_list[-1] = ' '
    
    if puzzle == ''.join(solution_list):
        return True
    else:
        return False

def swap_position(puzzle, from_index, to_index):
    from_letter = puzzle[from_index]
    to_letter = puzzle[to_index]
    puzzle_list = list(puzzle)
    
    puzzle_list[from_index] = to_letter
    puzzle_list[to_index] = from_letter
    return ''.join(puzzle_list)

def move(puzzle, direction):
    
    n = int(math.sqrt(len(puzzle)))
    matrix = [list(puzzle[index : index + n]) for index in range(0, len(puzzle), n)]

    #the index of th blank
    current_position = [None, None]
    for index in range(len(matrix)):
        if matrix[index].__contains__(' '):
            # current_position = f"{index}{matrix[index].index(' ')}"   #indexcolumn
            current_position[0] = index
            current_position[1] = matrix[index].index(' ')
    
    move_to = None
    if direction == "U":
        move_to = [-1, 0] #moving up
    if direction == "D":
        move_to = [1, 0] #moving down
    elif direction == "R":
        move_to = [0, 1]
    elif direction == "L":
        move_to = [0, -1]

    new_position = [None, None]

    x_axis = current_position[0] + move_to[0]
    y_axis = current_position[1] + move_to[1]
    
    new_position[0] = x_axis
    new_position[1] = y_axis

    
    for axis in new_position:
        if axis > n-1 or axis < 0:
            return None
    #make the move
    matrix[current_position[0]][current_position[1]] = matrix[new_position[0]][new_position[1]]
    matrix[new_position[0]][new_position[1]] = ' '
    
    soln = ''.join([''.join(x) for x in matrix])
    
    return soln
    

# move("abcdefgh ", "U")
# print(move("abcdefgh ", "D"))
def print_grid(puzzle):
    n = int(math.sqrt(len(puzzle)))
    matrix = [list(puzzle[index : index + n]) for index in range(0, len(puzzle), n)]
    first_line = ''.join([(HORIZONTAL_WALL*3)+CORNER for _ in range(n)])

    divider = f"{CORNER}{first_line}"
    print(divider)
    for row in matrix:
        line = "|" + ''.join([f" {x} |" for x in row])
        print(line)
        print(divider)

# print_grid("nevagonagiveu up")
print_grid("nevergonnalet udooooowwwn")

def shuffle_puzzle(solution: str) -> str:
    """
    Shuffle a puzzle solution to produce a solvable sliding puzzle.

    Parameters:
        solution (str): a solution to be converted into a shuffled puzzle.

    Returns:
        (str): a solvable shuffled game with an empty tile at the
               bottom right corner.

    References:
        - https://en.wikipedia.org/wiki/15_puzzle#Solvability
        - https://www.youtube.com/watch?v=YI1WqYKHi78&ab_channel=Numberphile

    Note: This function uses the swap_position function that you have to
          implement on your own. Use this function when the swap_position
          function is ready
    """
    shuffled_solution = solution[:-1]

    # Do more shuffling for bigger puzzles.
    swaps = len(solution) * 2
    for _ in range(swaps):
        # Pick two indices in the puzzle randomly.
        index1, index2 = random.sample(range(len(shuffled_solution)), k=2)
        shuffled_solution = swap_position(shuffled_solution, index1, index2)

    return shuffled_solution + EMPTY


# Write your functions here


def main():
    """Entry point to gameplay"""
    print("Implement your solution and run this file")


if __name__ == "__main__":
    main()
