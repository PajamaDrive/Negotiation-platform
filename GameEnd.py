class GameEnd(Event):
    def __init__(self):
        self.event_type = "GameEnd"

    def addHistory(self, history):
        history.addHistory(makeJSONFormatEvent())

    def makeJSONFormatEvent(self, history_number):
        pass
