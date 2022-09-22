from abc import ABCMeta, abstractmethod
import pickle, json


class SerializationInterface(metaclass=ABCMeta):
    
    @abstractmethod
    def dump(self, object, file):
        pass

    @abstractmethod
    def load(self, file):
        pass

    @abstractmethod
    def dumps(self, object):
        pass

    @abstractmethod
    def loads(self, bytes):
        pass


class ToJson(SerializationInterface):

    def loads(self, bytes):
        unpacked = json.loads(bytes)
        return unpacked

    def dumps(self, object):
        byte_string = json.dumps(object)
        return byte_string

    def dump(self, object, file):
        with open(file, "w") as fh:
            json.dump(object, fh) 
       
    def load(self, file):
        with open(file, "r") as fh:
            unpacked = json.load(fh)
            return unpacked


class ToBin(SerializationInterface):

    def loads(self, bytes):
        unpacked = pickle.loads(bytes)
        return unpacked

    def dumps(self, object):
        byte_string = pickle.dumps(object)
        return byte_string

    def dump(self, object, file):
        with open(file, "wb") as fh:
            pickle.dump(object, fh) 
       
    def load(self, file):
        with open(file, "rb") as fh:
            unpacked = pickle.load(fh)
            return unpacked


