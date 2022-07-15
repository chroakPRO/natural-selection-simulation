import agents.enviornment as env


class GameManager:

    def __init__(self, game):
        self.game = game
        self.game.game_manager = self
        self.game.start_game()


        # Settings up enviornment
        # def __init__(self, size: int, num_prey: int, num_hunter: int):
        self.environment = env.Enviornment(10, 3, 1)
        self.game_board = self.environment.world

    def initial(self):
        pass        
