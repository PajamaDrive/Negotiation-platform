from Domain import *

class SampleDomain(Domain):
    def __init__(self):
        super().__init__()
        self.issue = {"Gold":4, "Iron":4, "Banana":4, "Spice":4}
        self.player_preference = Preference([1,2,3,4])
        self.agent_preference = [Preference([4,3,2,1])]
        self.time = 200
