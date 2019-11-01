class GameStart(Event):
    def __init__(self):
        self.event_type = "GameStart"

    def addHistory(self, history):
        history.addHistory(makeJSONFormatEvent())

    def makeJSONFormatEvent(self, history_number):
        pass
