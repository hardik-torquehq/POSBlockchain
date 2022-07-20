import threading
import time
from Message import Message
from BlockchainUtils import BlockchainUtils

class PeerDiscoveryHandler():

    def __init__(self, node):
        self.socketcommunication = node

    def start(self):
        threading.Thread(target=self.status).start()
        threading.Thread(target=self.discovery).start()

    def status(self):
        while True:
            print('current connectios:')
            for peer in self.socketcommunication.peers:
                print(peer.ip, peer.port)
            time.sleep(10)

    def discovery(self):
        while True:
            handshakeMessage = self.handshakeMessage()
            self.socketcommunication.broadcast(handshakeMessage)
            time.sleep(10)
            
    def handshake(self, connected_node):
        handshakeMessage = self.handshakeMessage()
        self.socketcommunication.send(connected_node, handshakeMessage)

    def handshakeMessage(self):
        ownConnector = self.socketcommunication.SocketConnector
        ownPeers = self.socketcommunication.peers
        data = ownPeers
        messageType = 'Discovery'
        message = Message(ownConnector, messageType, data)
        encodeMessage = BlockchainUtils.encodeobject(message)
        return encodeMessage

    def handleMessage(self, message):
        peerSocketConnector = message.senderConnector
        peersPeerList = message.data
        newPeer = True
        for peer in self.socketcommunication.peers:
            if peer.equals(peerSocketConnector):
                newPeer = False
                break
        if newPeer == True:
            self.socketcommunication.peers.append(peerSocketConnector)
            for peersPeer in peersPeerList:
                peerKnown = False
                for peer in self.socketcommunication.peers:
                    if peer.equals(peersPeer):
                        peerKnown = True
                        break
                if not peerKnown and not peersPeer.equals(self.socketcommunication.SocketConnector):
                    self.socketcommunication.connect_with_node(peersPeer.ip, peersPeer.port)

            