
class GameManager:

    def __init__(self, game):
        self.game = game
        self.game.game_manager = self
        self.game.start_game()