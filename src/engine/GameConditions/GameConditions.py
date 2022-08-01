import agents.enviornment as env
from typing import List, Dict, Tuple, NewType
Userid = NewType("Userid", str)

class GameConditions:

    num_prey: int
    num_hunter: int
    world: List[List[str]]
    agents: Dict[List[str], List[str]]

    self.x: int

    def __init__(self, num_prey: int, num_hunter: int):
        self.num_prey = num_prey
        self.num_hunter = num_hunter
        self.world = env.World()
        self.agents = {}
        self.agents_list = []
