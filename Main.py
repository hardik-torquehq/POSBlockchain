from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
from Blockchain import Blockchain
import pprint
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel
from Node import Node
import sys

if __name__ == '__main__':
    ip = sys.argv[1]
    port = int(sys.argv[2])

    node = Node(ip, port)
    node.startP2P()

    if(port == 10002):
        node.p2p.connect_with_node(ip, 10001)
    