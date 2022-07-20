from Crypto.Hash import SHA256
import json
import jsonpickle


class BlockchainUtils():

    @staticmethod
    def hash(data):
        dataString = json.dumps(data)
        dataBytes = dataString.encode('utf-8')
        dataHash = SHA256.new(dataBytes)
        return dataHash

    @staticmethod
    def encodeobject(obj):
        return jsonpickle.encode(obj, unpicklable=True) 

    @staticmethod
    def decodeobject(obj):
        return jsonpickle.decode(obj)
