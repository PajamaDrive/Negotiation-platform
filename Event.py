from abc import ABCMeta, abstractmethod

class Event(metaclass = ABCMeta):
    def __init__(self, negotiator_id):
        self.negotiator_id = negotiator_id
        self.event_type = "Event"

    def addHistory(self, history):
        history.addHistory(makeJSONFormatEvent(history.getHistoryNumber(), history.getCurrentGameTime()))

    @abstractmethod
    def makeJSONFormatEvent(self, history_number, event_time):
        pass
