from typing import List, Dict
import numpy as np
import random
import genes


class Hunter:
    
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y
        self.fitness: int = 0
        self.genes = genes.Genes(0, 0, 0, 0)
        self.kills: int = 0
        self.pos: List[int] = [x, y]
    
    def set_pos(self):
        self.pos = [self.x, self.y]
    
    def upgrade(self):
        pass
