from typing import List, Dict
import numpy as np
import random


""" ['Information']
I need to write some notes, while coding. So why not keep them up here for you to read.
So you easier can understand my code.

- Prey
I need to create an attribute list for prey.
What every "fitness parameters" does in practis.
Ex: if you have lets say 52 as speed attribute/rating. 
And I create a rule that says if you have over 50 in speed...
increase the chance of escape by 15%. 

I need to define this beforehand so i more easily modify the fitenss/mutation functions.

Gen 0: Health (How much health tbey have.)

Gen 1: Weight (How much damage they take)

Gen 2: attack power (This will always be 0)

Gen 3: Speed (How good they are at evading prey.)

Days Survied: How many iterations the prey has survived.

Enemy Close: How many times was the prey within X amount of blocks of hunter. (Day to day basis)


"""



class Prey:
    
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y
        self.fitness: int = 0
        self.days_survived: int = 0
        self.enemy_close: int = 0
        self.genes = []
        self.NUM_GENES = 0
        self.pos: List[int] = [x, y]
        
    
    def set_pos(self):
        self.pos: List[int] = [self.x, self.y]
    
        
    
    def calc_fitness(self, gen_array: List[int], days_survived: int) -> int:
        self.days_survived = days_survived
        self.genes = gen_array
        self.fitness = (self.days_survived / 0,45) * (self.genes[0] / 0.09) * (self.enemy_close / 0.02)
        return self.fitness
    
    # This needs total rework.
    def mutation(self, xx_genes: List[int], xy_genes: List[int]):        
        # Children
        child01 = []
        child02 = []
        
        # Single Point Crossover every parent is in pair and will produce 2 childern.
        gen_len = len(xx_genes)
        crossover_point = random.randint(0, gen_len)
        
        for i in range(gen_len):     
            # Cross-over-point - 
            if i >= crossover_point:
                # Picks the best one.
                if xx_genes[i] > xy_genes[i]:
                    child01[i] = xx_genes[i]
                    child02[i] = xy_genes[i]
                else:
                    child01[i] = xy_genes[i]
                    child02[i] = xy_genes[i]
            else:
                child01[i] = np.random.sample()
                child02[i] = np.random.sample()
            
            
    def set_random_genes(self):
        self.genes = []
        for i in range(0, self.NUM_GENES):
            self.genes[i] = np.random.sample()
    
    def move(self, health_left: int) -> bool:
        if health_left > 0:
            # Main code (Calculates how to move.)
            
            return True
        else: return False