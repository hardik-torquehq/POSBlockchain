import time


class Block():

    def __init__(self, transactions, lastHash, forger, blockCount):
        self.blockCount = blockCount
        self.transactions = transactions
        self.lastHash = lastHash
        self.timestamp = time.time()
        self.forger = forger
        self.signature = ''

    def toJson(self):
        data = {}
        data['blockCount'] = self.blockCount
        data['lastHash'] = self.lastHash
        data['signature'] = self.signature
        data['forger'] = self.forger
        data['timestamp'] = self.timestamp
        jsonTransactions = []
        for transaction in self.transactions:
            jsonTransactions.append(transaction.toJson())
        data['transactions'] = jsonTransactions
        return data
