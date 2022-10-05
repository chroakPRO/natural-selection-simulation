from typing import List, Dict
import numpy as np
import random


""" ['Information']
I need to write some notes, while coding. So why not keep them up here for you to read.
So you easier can understand my code.

- Prey
I need to create an attribute list for prey.
What every "FITNESS parameters" does in practis.
Ex: if you have lets say 52 as SPEED attribute/rating.
And I create a rule that says if you have over 50 in SPEED...
increase the chance of escape by 15%.

I need to define this beforehand so i more easily modify the fitenss/mutation functions.

Gen 0: HEALTH (How much HEALTH tbey have.)

Gen 1: WEIGHT (How much damage they take)

Gen 2: ATTACK power (This will always be 0)

Gen 3: SPEED (How good they are at evading prey.)

Days Survied: How many iterations the prey has survived.

Enemy Close: How many times was the prey within X amount of blocks of hunter. (Day to day basis)


"""


class Prey:
    def __init__(self, x: int, y: int):
        """_summary_

        Args:
            x (int): _description_
            y (int): _description_
        """
        self.x: int = x
        self.y: int = y
        self.FITNESS: int = 0
        self.days_survived: int = 0
        self.enemy_close: int = 0
        self.GENES = []
        self.NUM_GENES = NUM_GENES
        self.POS: List[int] = [x, y]

    def set_POS(self, x: int, y: int):
        """_summary_

        Args:
            x (int): _description_
            y (int): _description_
        """
        self.POS: List[int] = [x, y]

    def calc_FITNESS(self, gen_array: List[int], days_survived: int) -> int:
        """_summary_

        Args:
            gen_array (List[int]): _description_
            days_survived (int): _description_

        Returns:
            int: _description_
        """
        self.days_survived = days_survived
        self.GENES = gen_array
        self.FITNESS = (
            (self.days_survived / 0, 45)
            * (self.GENES[0] / 0.09)
            * (self.enemy_close / 0.02)
        )
        return self.FITNESS

    # This needs total rework.
    def mutation(self, xx_GENES: List[int], xy_GENES: List[int]):
        """_summary_

        Args:
            xx_GENES (List[int]): _description_
            xy_GENES (List[int]): _description_
        """
        # Children
        child01 = []
        child02 = []

        # Single Point Crossover every parent is in pair and will produce 2 childern.
        gen_len = len(xx_GENES)
        crossover_point = random.randint(0, gen_len)

        for i in range(gen_len):
            if i >= crossover_point:
                # Picks the best one.
                if xx_GENES[i] > xy_GENES[i]:
                    child01[i] = xx_GENES[i]
                    child02[i] = xy_GENES[i]
                else:
                    child01[i] = xy_GENES[i]
                    child02[i] = xy_GENES[i]
            else:
                chlild01[i] = np.random.sample()
                child02[i] = np.random.sample()

    def set_random_GENES(self):
        self.GENES = []
        for i in range(0, self.NUM_GENES):
            self.GENES[i] = np.random.sample()

    def move(self, HEALTH_left: int) -> bool:
        if HEALTH_left > 0:
            # Main code (Calculates how to move.)

            return True
        else:
            return False


# The hunter dosen't have children.
# They are the same throughout the whole simulation.
# But they do get improvement if they kill alot.


class Hunter:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y
        self.FITNESS: int = 0
        self.GENES = GENES(0, 0, 0, 0)
        self.kills: int = 0
        self.POS: List[int] = [x, y]

    e

    def set_POS():
        self.POS = [self.x, self.y]

    def upgrade(self):
        pass


class GENES:
    def __init__(self, HEALTH: int, WEIGHT: int, ATTACK: int, SPEED: int):
        self.HEALTH: int = HEALTH
        self.WEIGHT: int = WEIGHT
        self.ATTACK: int = ATTACK
        self.SPEED: int = SPEED


def POS_taken(xy, POS_list):
    notdone = True
    while notdone:
        if xy in POS_list:
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
    taken_POS = []
    # Creates the players in the gameboard.
    for i in range(0, num_prey):
        if i < num_hunter:
            # Creation of Hunters
            hunters_666.append(Hunter(999, 999))
            # Let check if this POSition is already taken.
            x = random.randint(0, 100)
            y = random.randint(0, 100)
            x, y = POS_taken([x, y], POS_taken)
            hunters_666[i].x = x
            hunters_666[i].y = y
            game[x][y] = 666
        # Creation of prey.
        prey_404.append(Prey(999, 999))
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        x, y = POS_taken([x, y], POS_taken)
        prey_404[i].x = x
        prey_404[i].y = y
        game_404[x][y] = 404
    return hunters, prey, game


def check_sur(col, row, lists):
    above_below = [lists[col - 1][row], lists[col + 1][row]]  # col
    left_right = [lists[col][row - 1], lists[col][row + 1]]  # row

    # 32, 10, 12, 30
    diagnoal = [
        lists[col + 1][row + 1],
        lists[col - 1][row - 1],
        lists[col + 1][row - 1],
        lists[col - 1][row + 1],
    ]
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
    # hunter_POS = [[random.randint(0, 100), random.randint(0, 100)] for i in range(0, NUM_HUNTERS)]
    # prey_POS = [[random.randint(0, 100), random.randint(0, 100)] for i in range(0, NUM_PREY)]
    # OLD CODE.
    # hunter = [Hunter(999, 999) for i in range(0, NUM_HUNTERS)]
    # prey = [Prey() for i in range(0, NUM_PREY)]

    # Like this
    hunter, prey, game = create_game(NUM_HUNTERS, NUM_PREY)

    # This is where the simulation starts.
    # Num of iterations
    NUM_ITERATIONS = 15
    count = 0
    for i in range(0, NUM_ITERATIONS):  # O(2^n)
        for i in hunter:
            # Gets current POS.
            i.setPOS()
            hunter_POS = i.POS
            # Check surroundings
            check_sur(hunter_POS[0], hunter_POS[1], hunter)


main()


""" ['Random Code']


x = [[10, 11, 12],
     [20, 21, 22],
     [30, 31, 32]]

# row and col

#x[1][1] = (x[1][0], x[1][2], x[0][1], x[2][1])
NUM1 = 1

p = [x[NUM1][NUM1 - 1], x[NUM1][NUM1 + 1], x[NUM1 - 1][NUM1], x[NUM1 + 1][NUM1]]
print(p)

def check_sur(col, row, lists):
    above_below = [lists[col - 1][row], lists[col + 1][row]] # col
    left_right = [lists[col][row - 1], lists[col][row + 1]] # row
    
    # 32, 10, 12, 30
    diagnoal = [lists[col + 1][row + 1], lists[col - 1][row - 1], 
                lists[col + 1][row - 1], lists[col - 1][row +  1]]
    print("Above Below -> {} \n".format(above_below))
    print("Left Right -> {} \n".format(left_right))
    print("Diagnoal, RB LT RT LB -> {} \n".format(diagnoal))
    
    
        
check_sur(1, 1, x)


"""
