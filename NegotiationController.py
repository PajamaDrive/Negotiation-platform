class NegotiationController:
    def __init__(self, negotiator_num, domain, agents):
        self.negotiator_num = negotiator_num
        self.domain = domain
        self.agent = [agents[i] for i in range(len(agents))]

if __name__ == "__main__":
    nc = NegotiationController.NegotiationController()
