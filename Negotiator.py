from abc import ABCMeta, abstractmethod
from Preference import *
from NegotiatorType import *

class Negotiator(metaclass = ABCMeta):
    def __init__(self):
        self.player_type = None
        self.preference = None

    @abstractmethod
    def sendOffer(self):
        pass

    @abstractmethod
    def recieveOffer(self):
        pass

    @abstractmethod
    def acceptOffer(self):
        pass

    @abstractmethod
    def rejectOffer(self):
        pass

    @abstractmethod
    def sendStaticMessage(self):
        pass

    @abstractmethod
    def recieveStaticMessage(self):
        pass

    @abstractmethod
    def sendThreadMessage(self):
        pass

    @abstractmethod
    def recieveThreadMessage(self):
        pass

    @abstractmethod
    def sendPreferenceMessage(self):
        pass

    @abstractmethod
    def recievePreferenceMessage(self):
        pass

    @abstractmethod
    def sendRewardMessage(self):
        pass

    @abstractmethod
    def recieveRewardMessage(self):
        pass

    @abstractmethod
    def sendEmotion(self):
        pass

    @abstractmethod
    def recieveEmotion(self):
        pass
