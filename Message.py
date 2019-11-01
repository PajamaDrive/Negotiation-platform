import ast
from StaticMessage import *
from EmotionType import *

class Message:
    def __init__(self, passage):
        self.passage = passage

    def parseMessage(self):
        return messageToEmotion(self.passage)

    def __str__(self):
        return self.passage

    def strToDict(self):
        return ast.literal_eval("{" + str(self) + "}")
