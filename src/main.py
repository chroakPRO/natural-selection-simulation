import random
import hunter
import prey
import genes

def pos_taken(xy, pos_list):
    notdone = True
    while notdone:
        if xy in pos_list:
            xy = [random.randint(0, 100), random.randint(0, 100)]
        else: 
            notdone = False
            return xy[0], xy[1]


def create_list(iterations: int, animal_type: str) -> List[List[int]]:
    """
    Creates a list of animal objects
    :param iterations: Number of iterations
    :param animal_type: Type of animal
    :return: List of animal objects
    """

    list_pos = [[random.randint(0, 100), random.randint(0, 100)] for i in range(0, iterations)]
    for i in iterations:
        if animal_type == "hunter":
            list_pos[i] = hunter.Hunter(list_pos[i][0], list_pos[i][1])
        elif animal_type == "prey":
            list_pos[i] = prey.Prey(list_pos[i][0], list_pos[i][1])
        else:
            print("Animal type not found")
    return list_pos


def create_game(num_hunter: int, num_prey: int) -> (List[object], List[object], List[List[int]]):
    """
    Creates the game
    :param num_hunter: Number of hunters
    :param num_prey: Number of prey
    :return: List of hunters, list of prey, 2D array of game
    """

    # List with objects.
    # 100x100 2D array. Gameboard print(len(game[0])) -- print(len(game))
    game = [["" for i in range(0, 100)] for i in range(0, 100)]
    
    # Creates the players in the gameboard.
    hunters_pos = create_list(num_hunter)
    prey_pos = create_list(num_prey)
    
    # Creates the players in the gameboard.
    hunters = [hunter.Hunter(i[0], i[1]) for i in range(0, hunter_pos)]
    prey = [prey.Prey(i[0], i[1]) for i in range(0, prey_pos)]

    # Returns the list of hunters, list of prey, 2D array of game
    return hunters, prey, game
  
def check_sur(col, row, game_board) -> bool:
    """
    Check the surroundings of a position.
    :param col: Column
    :param row: Row
    :param game_board: Gameboard
    """
    hunter_pos = []
    """ OLD CODE
    # Check the surroundings of the 
    above_below = [game_board[col - 1][row], game_board[col + 1][row]] # col
    left_right = [game_board[col][row - 1], game_board[col][row + 1]] # row
    
    # 32, 10, 12, 30
    diagnoal = [game_board[col + 1][row + 1], game_board[col - 1][row - 1], 
                game_board[col + 1][row - 1], game_board[col - 1][row +  1]]
    if "H" in above_below:
"""
    # List comphrension to return columns and rows if above_below or left_right is a hunter.
    # Above_below
    # List comphrension example
    above_below = [i for i in range(-1, 1, 2) if game_board[col [i]][row] == "H"]
    left_right = [i for i in range(-1, 1, 2) if game_board[col][row[i]] == "H"]
    diagnoal = [hunter_pos.append(i) for i in range(-1, 1, 2) if game_board[col[i]][row [i]] == "H"]
    

    # Have made so this can be update to return hunters position.
    # Use case: match up between prey and hunter, maybe prey livs.
    if len(hunter_pos) > 0:
        
        x = random.randint(0, 100)
        # if x is greater then 5 (%) then prey dies.
        if x > 5:
            return True
        # else prey lives.
        else: 
            return False
    else:
        return False
    above = []

    
    # Check if above_below, left_right, diagnol are 0 if not return 1
    
    if 1 in above_below or 1 in left_right or 1 in diagnoal:
        return True
    else:
        return False

   # print("Above Below -> {} \n".format(above_below))
   # print("Left Right -> {} \n".format(left_right))
   # print("Diagnoal, RB LT RT LB -> {} \n".format(diagnoal))

def ITER_ENDS():
    pass

def main():
    NUM_HUNTERS = 2
    NUM_PREY = 10
    # 100x100 2D array. Gameboard print(len(game[0])) -- print(len(game))
    
    # OLD CODE.
    # hunter_pos = [[random.randint(0, 100), random.randint(0, 100)] for i in range(0, NUM_HUNTERS)]
    # prey_pos = [[random.randint(0, 100), random.randint(0, 100)] for i in range(0, NUM_PREY)]
    
    # OLD CODE.
    # hunter = [Hunter(999, 999) for i in range(0, NUM_HUNTERS)]
    # prey = [Prey() for i in range(0, NUM_PREY)]
    
    # Like this
    hunter, prey, game = create_game(NUM_HUNTERS, NUM_PREY)

    # This is where the simulation starts.
    # Num of iterations
    NUM_ITERATIONS = 15
    count = 0
    
    prey_next_to_hunter = []

    for i in range(0, NUM_ITERATIONS):
        # Loop through the prey
        for j in range(0, len(prey)):
            if check_sur(prey[j].x, prey[j].y, game):
                prey[j].kill()
                prey_next_to_hunter.append(prey[j])
            else:
                prey[j].move(game)
                # Loop through the hunters

            
"""
for i in range(0, NUM_ITERATIONS): # O(2^n)
        for i in hunter:
            # Gets current pos.
            i.setpos()
            hunter_pos = i.pos
            # Check surroundings
            check_sur(hunter_pos[0], hunter_pos[1], hunter)
   """         
    

        
main()
