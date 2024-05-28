"""
RBG values for each color used in the game
"""

class Color:
    def __ini__(self):
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.blue = (0, 0, 255)
        self.slate_blue = (50, 50, 150)
        self.navy_blue = (0, 0, 100)
        self.yellow = (255, 255, 0)
        self.orange = (255, 165, 0)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

    def use(self, color: str):
        return getattr(self, color, self.black) # doesn't work