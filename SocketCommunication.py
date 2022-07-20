import json
from p2pnetwork.node import Node
from Message import Message
from PeerDiscoveryHander import PeerDiscoveryHandler
from SocketConnector import SocketConnector
from BlockchainUtils import BlockchainUtils

class SocketCommunication(Node):

    def __init__(self, ip, port):
        super(SocketCommunication, self).__init__(ip, port, None)
        self.peers = []
        self.peer_discovery_handler = PeerDiscoveryHandler(self)
        self.SocketConnector = SocketConnector(ip, port)
       
    def connectToFirstNode(self):
        if self.SocketConnector.port != 10001:
            self.connect_with_node(self.SocketConnector.ip, 10001)
       
    def startSocketCommunication(self):
        self.start()
        self.peer_discovery_handler.start()
        self.connectToFirstNode()

    def inbound_node_connected(self, connected_node):
        self.peer_discovery_handler.handshake(connected_node)

    def outbound_node_connected(self, connected_node):
        self.peer_discovery_handler.handshake(connected_node)

    def node_message(self, connected_node, message):
        message = BlockchainUtils.decodeobject(json.dumps(message))
        if message.messageType == 'Discovery':
            self.peer_discovery_handler.handleMessage(message)

    def send(self, receiver, message):
        self.send_to_node(receiver, message)

    def broadcast(self, message):
        self.send_to_nodes(message)

        
