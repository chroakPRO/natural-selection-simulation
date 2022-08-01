from typing import List, Dict
import numpy as np
import random
import agents.GENES as GENES


class Hunter:

    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y
        self.FITNESS: int = 0
        self.GENES = GENES.GENES(0, 0, 0, 0)
        self.kills: int = 0
        self.POS: List[int] = [x, y]

    def set_POS(self):
        self.POS = [self.x, self.y]

    def upgrade(self):
        pass
