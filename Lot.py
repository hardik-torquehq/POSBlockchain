from BlockchainUtils import BlockchainUtils

class Lot():

    def __init__(self, publicKey, interation, lastBHash):
        self.publicKey = publicKey
        self.interation = interation
        self.lastBHash = lastBHash
    
    def lastHash(self):
        hashData = self.publicKey + self.lastBHash
        for __ in range(self.interation):
            hashData = BlockchainUtils.hash(hashData).hexdigest()
        return hashData
