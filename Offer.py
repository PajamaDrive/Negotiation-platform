import ast

class Offer:
    def __init__(self, negotiator_num = 2, issue_num = 0, quantity_of_each_issue = []):
        if issue_num == 0:
            raise AttributeError("number of issue is zero.")
        if len(quantity_of_each_issue) == 0:
            raise AttributeError("quantity of each issue is empty list.")
        if len(quantity_of_each_issue) != issue_num:
            raise AttributeError("number of issue must be equal to length of quantity of eash issue.")

        self.__negotiator_num = negotiator_num
        self.__issue_num = issue_num
        self.__quantity_of_each_negotiator = [[] for i in range(issue_num)]
        self.__quantity_of_undecided = []
        self.__quantity_of_each_issue = quantity_of_each_issue[:]
        self.__quantity_of_undecided = quantity_of_each_issue[:]

    def setQuantity(self, issue_id, quantity_of_each_negotiator):
        if len(quantity_of_each_negotiator) != len(self.__quantity_of_each_negotiator):
            raise AttributeError("number of quantity of each negotiator must be equal to " + str(len(self.__quantity_of_each_negotiator)))
        if issue_id >= self.__issue_num:
            raise AttributeError("issue id must be less than " + str(self.__issue_num))
        #総量が規定値を超えていないかチェック
        if sum(quantity_of_each_negotiator) > sum(self.__quantity_of_each_issue):
            raise AttributeError("quantity of issue" + str(issue_id + 1) + "must be less than " + str(sum(self.__quantity_of_each_issue)))
        #すでに入っている値を削除し新しい値をコピー
        self.__quantity_of_each_negotiator[issue_id].clear()
        self.__quantity_of_each_negotiator[issue_id] = quantity_of_each_negotiator[:]
        self.__quantity_of_undecided[issue_id] = self.__quantity_of_each_issue[issue_id] - sum(quantity_of_each_negotiator)

    def setQuantityOfAllIssue(self, quantity):
        for i in range(self.__issue_num):
            setQuantity(i, quantity[i])

    def getQuantity(self, issue_id):
        if issue_id >= self.__issue_num:
            raise AttributeError("issue id must be less than " + str(self.__issue_num))
        return self.__quantity_of_each_negotiator[issue_id]

    def getQuantityOfUndecided(self, issue_id):
        if issue_id >= self.__issue_num:
            raise AttributeError("issue id must be less than " + str(self.__issue_num))
        return self.__quantity_of_undecided[issue_id]

    def getQuantityOfCertainNegotiator(self, negotiator_id):
        if negotiator_id >= self.__negotiator_num:
            raise AttributeError("negotiator id must be less than " + str(self.__negotiator_num))
        return [self.__quantity_of_each_negotiator[i][negotiator_id] for i in range(self.__issue_num)]

    def __str__(self):
        return "'negotiator_quantity' : " + str(self.__quantity_of_each_negotiator) + ", 'undecided_quantity' : " + str(self.__quantity_of_undecided)

    def strToDict(self):
        return ast.literal_eval("{" + str(self) + "}")
