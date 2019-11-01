from PreferenceType import *
class Preference:
    def __init__(self, preference):
        self.order = preference

    def setIssueName(self, domain):
        self.name_list = domain.getIssueName()

    def compareOrder(self, issue1, issue2):
        if self.order[issue1] > self.order[issue2]:
            return PreferenceType.BetterThan
        elif self.order[issue1] < self.order[issue2]:
            return PreferenceType.LessThan
        else:
            return PreferenceType.EqualTo

    def compareOrderByIssueName(self, issue1, issue2):
        return compareOrder(self.name_list.index(issue1), self.name_list.index(issue2))

    def getIssueToOrder(self, issue):
        return self.order[issue]

    def getIssueToOrderByIssueName(self, issue):
        return getIssueToOrder(self.name_list.index(issue))

    def getOrderToIssue(self, order):
        return self.order.index(order)

    def getOrderToIssueByIssueName(self, order):
        return self.name_list[getOrderToIssue()]
