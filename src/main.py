def pos_taken(xy, pos_list):
    done = True
    while notdone:
        if xy in pos_list:
            xy = [random.randint(0, 100), random.randint(0, 100)]
        else: 
            notdone = False
            return xy[0], xy[1]

def create_game(num_hunter, num_prey):
    # List with objects.
    # 100x100 2D array. Gameboard print(len(game[0])) -- print(len(game))
    game = [["" for i in range(0, 100)] for i in range(0, 100)]
    hunters_666 = []
    prey_404 = []
    taken_pos = []
    # Creates the players in the gameboard.
    for i in range(0, num_prey):
        if i < num_hunter:
            # Creation of Hunters
            hunters_666.append(Hunter(999, 999))
            # Let check if this position is already taken.
            x = random.randint(0, 100)
            y = random.randint(0, 100)
            x, y = pos_taken([x, y], pos_taken) 
            hunters_666[i].x = x
            hunters_666[i].y = y
            game[x][y] = 666
        # Creation of prey.
        prey_404.append(Prey(999, 999))
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        x, y = pos_taken([x, y], pos_taken) 
        prey_404[i].x = x
        prey_404[i].y = y
        game_404[x][y] = 404
    return hunters, prey, game
  
def check_sur(col, row, lists):
    above_below = [lists[col - 1][row], lists[col + 1][row]] # col
    left_right = [lists[col][row - 1], lists[col][row + 1]] # row
    
    # 32, 10, 12, 30
    diagnoal = [lists[col + 1][row + 1], lists[col - 1][row - 1], 
                lists[col + 1][row - 1], lists[col - 1][row +  1]]
    print("Above Below -> {} \n".format(above_below))
    print("Left Right -> {} \n".format(left_right))
    print("Diagnoal, RB LT RT LB -> {} \n".format(diagnoal))

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
    for i in range(0, NUM_ITERATIONS): # O(2^n)
        for i in hunter:
            # Gets current pos.
            i.setpos()
            hunter_pos = i.pos
            # Check surroundings
            check_sur(hunter_pos[0], hunter_pos[1], hunter)
            
            
            
            
        
        
main()