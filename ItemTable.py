class ItemTable(Offer):
    def __init__(self, issue_num = 0, quantity_of_each_issue = []):
        super().__init__(issue_num, quantity_of_each_issue)

    def updateTable(self, offer):
        for i in range(issue_num):
