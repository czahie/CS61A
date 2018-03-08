class State:
    """A State holds a current game state and all of its attributes"""

    def __init__(self):
        """Create a new gamestate"""
        self.gs = {}


    def getState(self, key=None):
        if key:
            return self.gs[key]
        return self.gs

    def updateState(self, key, val):
        self.gs[key] = val


