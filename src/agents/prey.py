from typing import List, Dict
import numpy as np
import random
import agents.GENES as GENES


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
        self.x: np.uint16 = x
        self.y: np.uint16 = y
        self.FITNESS: np.uint16 = 0
        self.days_survived: np.uint16 = 0
        self.enemy_close: np.uint8 = 0
        self.HEALTH: np.uint16 = 2
        self.WEIGHT: np.uint16 = 3
        self.ATTACK: np.uint16 = 4
        self.SPEED: np.uint16 = 7
        self.GENES = GENES.GENES(
            self.HEALTH, self.WEIGHT, self.ATTACK, self.SPEED)
        self.NUM_GENES: np.uint16 = 0
        self.POS: List[int] = [x, y]
        self.KILLED: bool = False

    def set_POS(self):
        self.POS: List[int] = [self.x, self.y]

    # This needs total rework.
    def mutation(self, xx_GENES: List[int], xy_GENES: List[int]):
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
                child01[i] = np.random.sample()
                child02[i] = np.random.sample()

    def kill(self) -> bool:
        """
        Kills the prey.
        """
        self.KILLED = True
        return True

    def set_random_GENES(self):
        """
        Sets random GENES for the prey.
        """
        self.GENES = []
        for i in range(0, self.NUM_GENES):
            self.GENES[i] = np.random.sample()

    def move(self) -> bool:
        """
        Moves the prey.
        """

        if not self.KILLED:
            # Main code (Calculates how to move.)

            return True
        else:
            return False
