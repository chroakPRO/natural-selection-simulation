from typing import List, Dict
import numpy as np
import random


class Hunter:
    
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y
        self.fitness: int = 0
        self.genes = Genes(0, 0, 0, 0)
        self.kills: int = 0
        self.pos: List[int] = [x, y]
    e
    def set_pos():
        self.pos = [self.x, self.y]
    
    def upgrade(self):
        pass