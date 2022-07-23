

class ProofOfStake():

    def __init__(self):
       self.stakes = {}

    def updateStake(self, address, stake):
        if address in self.stakes.keys():
            self.stakes[address] += stake
        elif stake > 0:
            self.stakes[address] = stake
        self.stakes[address] = stake

    def getStake(self, address):
        if address in self.stakes.keys():
            return self.stakes[address]
        else:
            return None