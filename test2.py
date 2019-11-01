import SampleDomain
from Player import *

class Hoge(Player):
    def hoge(self):
        d = SampleDomain.SampleDomain()
        print(d.getPlayerPreference())
