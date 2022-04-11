from paddle import Paddle

class Player():
    def __init__(self, x, y, name):
        self.paddle = Paddle(x, y)
        self.score = 0
        self.name = name

    def __eq__(self, other):
        return isinstance(other, Player) and self.name == other.name
