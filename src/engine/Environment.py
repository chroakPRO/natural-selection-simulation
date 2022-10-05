from logging import exception
from typing import List, Dict, Tuple
import numpy as np
import random
import agents.GENES as GENES
from agents.prey import Prey
from agents.hunter import Hunter


# Environment class
class Environment:

    def __init__(self, size: int, num_prey: int, num_hunter: int):
        self.size = size
        self.num_prey = num_prey
        self.num_hunter = num_hunter
        self.agents_total = num_prey + num_hunter
        self.agents = [{
            "x": [],
            "y": [],
            "type": object
        }]
        # Should be seperated into more functions.
        # --- TODO: Step 0.5: Generating world array...
        self.world = [["" for i in range(0, self.size)]
                      for i in range(0, self.size)]

    # --- TODO: Start up process...
    # --- TODO: Step 1: Generating world...

    def generate_world(self) -> bool:
        # TODO: generate world, but not sure how.
        try:
            print("Generating world...")

            return True
        except Exception as e:
            print(e)
            return False

from logging import exception
from typing import List, Dict, Tuple
import numpy as np
import random
import agents.GENES as GENES
from agents.prey import Prey
from agents.hunter import Hunter


# Environment class
class Environment:

    def __init__(self, size: int, num_prey: int, num_hunter: int):
        self.size = size
        self.num_prey = num_prey
        self.num_hunter = num_hunter
        self.agents_total = num_prey + num_hunter
        self.agents = [{
            "x": [],
            "y": [],
            "type": object
        }]
        self.world = []

    # --- TODO: Start up process...
    # --- TODO: Step 1: Generating world...

    def generate_world(self) -> bool:
        # TODO: generate world, but not sure how.
        try:
            print("Generating world...")

            return True
        except Exception as e:
            print(e)
            return False

    # --- TODO: Step 2: Generating agents...
    def create_agents(self) -> bool:
        #  TODO: unsure...
        """
        Creates agents [worker function]
        :return: True if successful, False if unsuccessful
        """
        try:
            if len(self.agents_list) > 0:
                print("Agents already created")
                return True
            # else: create game
            POSitions = [[random.randint(0, self.size) for j in range(
                0, 2)] for i in range(0, self.agents_total)]
            for j, i in enumerate(POSitions):
                # Creation of agents
                # Create prey
                if j <= self.num_prey:
                    # Create object
                    self.agents_list.append(Prey(i[0], i[1]))
                    # Add to world
                    self.world[i[0]][i[1]] = "P"
                    # Create Permanent Record
                    self.agents[j]["x"] = i[0]
                    self.agents[j]["y"] = i[1]
                    self.agents[j]["type"] = Prey(i[0], i[1])
                    # Debugging
                    print("Prey created at x: {} y: {}".format(i[0], i[1]))
                # Create hunter
                elif j > self.num_prey:
                    self.agents_list.append(Hunter(i[0], i[1]))
                    # Add to world
                    self.world[i[0]][i[1]] = "H"

                    # Create Permanent Record
                    self.agents[j]["x"] = i[0]
                    self.agents[j]["y"] = i[1]
                    self.agents[j]["type"] = Hunter(i[0], i[1])

                    # Debugging
                    print("Hunter created at x: {} y: {}".format(i[0], i[1]))
            return True
        except Exception as e:
            print(e)
            return False

    # --- TODO: utility functions --- #

    def set_hunter(self, x: int, y: int, hunter: List[Hunter]) -> bool:
        self.world[x][y] = "H"
        return True

    def set_prey(self, x: int, y: int, prey: List[Prey]) -> bool:
        self.world[x][y] = "P"
        return True

    def set_empty(self, x: int, y: int) -> bool:
        self.world[x][y] = ""
        return True

    def get_data(self, x: int, y: int, id: int) -> Tuple(int, int, object):
        return self.agents[id]["x"], self.agents[id]["y"], self.agents[id]["type"]

    # --- TODO: Worker functions --- #

    def check_surrounding(self, x: int, y: int) -> bool:
        # TODO: function comment
        # Desc: Checks if the surrounding of the animal is empty

        # temp storage for calculating...
        temp_list = []
        temp_hunter = []
        temp_prey = []

        above_below = [
            i for i in range(-1, 1, 2) if self.world[x[i]][y] == "H"]
        left_right = [i for i in range(-1, 1, 2) if self.world[x][y[i]] == "H"]
        diagonal = [temp_hunter.append(
            i) for i in range(-1, 1, 2) if self.world[x[i]][y[i]] == "H"]

        # Have made so this can be update to return hunters POSition.
        # Use case: match up between prey and hunter, maybe prey livs.
        if len(temp_hunter) > 0:

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

        if 1 in above_below or 1 in left_right or 1 in diagonal:
            return True
        else:
            return False

            if len(self.agents_list) > 0:
                print("Agents already created")
                return True
            # else: create game
            POSitions = [[random.randint(0, self.size) for j in range(
                0, 2)] for i in range(0, self.agents_total)]
            for j, i in enumerate(POSitions):
                # Creation of agents
                # Create prey
                if j <= self.num_prey:
                    # Create object
                    self.agents_list.append(Prey(i[0], i[1]))
                    # Add to world
                    self.world[i[0]][i[1]] = "P"
                    # Create Permanent Record
                    self.agents[j]["x"] = i[0]
                    self.agents[j]["y"] = i[1]
                    self.agents[j]["type"] = Prey(i[0], i[1])
                    # Debugging
                    print("Prey created at x: {} y: {}".format(i[0], i[1]))
                # Create hunter
                elif j > self.num_prey:
                    self.agents_list.append(Hunter(i[0], i[1]))
                    # Add to world
                    self.world[i[0]][i[1]] = "H"

                    # Create Permanent Record
                    self.agents[j]["x"] = i[0]
                    self.agents[j]["y"] = i[1]
                    self.agents[j]["type"] = Hunter(i[0], i[1])

                    # Debugging
                    print("Hunter created at x: {} y: {}".format(i[0], i[1]))
            return True
        except Exception as e:
            print(e)
            return False

    # --- TODO: utility functions --- #

    def set_hunter(self, x: int, y: int, hunter: List[Hunter]) -> bool:
        self.world[x][y] = "H"
        return True

    def set_prey(self, x: int, y: int, prey: List[Prey]) -> bool:
        self.world[x][y] = "P"
        return True

    def set_empty(self, x: int, y: int) -> bool:
        self.world[x][y] = ""
        return True

    def get_data(self, x: int, y: int, id: int) -> Tuple(int, int, object):
        return self.agents[id]["x"], self.agents[id]["y"], self.agents[id]["type"]

    # --- TODO: Worker functions --- #

    def check_surrounding(self, x: int, y: int) -> bool:
        # TODO: function comment
        # Desc: Checks if the surrounding of the animal is empty

        # temp storage for calculating...
        temp_list = []
        temp_hunter = []
        temp_prey = []

        above_below = [
            i for i in range(-1, 1, 2) if self.world[x[i]][y] == "H"]
        left_right = [i for i in range(-1, 1, 2) if self.world[x][y[i]] == "H"]
        diagonal = [temp_hunter.append(
            i) for i in range(-1, 1, 2) if self.world[x[i]][y[i]] == "H"]

        # Have made so this can be update to return hunters POSition.
        # Use case: match up between prey and hunter, maybe prey livs.
        if len(temp_hunter) > 0:

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

        if 1 in above_below or 1 in left_right or 1 in diagonal:
            return True
        else:
            return False
