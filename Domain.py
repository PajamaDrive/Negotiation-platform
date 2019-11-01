from abc import ABCMeta, abstractmethod
from Preference import *

class Domain(metaclass = ABCMeta):
    def __init__(self):
        self.issue = {}
        self.player_preference = None
        self.agent_preference = []
        self.time = None

    def getTotalTime(self):
        return self.time

    def getPlayerPreference(self):
        return self.player_preference

    def getAgentPreference(self, agent_id):
        return self.agent_preference[agent_id]

    def getQuantity(self):
        return list(self.issue.values())

    def getIssueName(self):
        return list(self.issue.keys())

    def getIssueNum(self):
        return len(self.issue)
