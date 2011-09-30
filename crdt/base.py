from abc import ABCMeta, abstractmethod, abstractproperty
from copy import deepcopy


class StateCRDT(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass

    def clone(self):
        """Create a copy of this CRDT instance"""
        return self.__class__.from_payload(deepcopy(self.payload))
    

    @classmethod
    @abstractmethod
    def merge(cls, X, Y):
        """Merge two replicas of this CRDT"""
        pass

    @abstractmethod
    def descends_from(self, other):
        """Returns True if other descended from other"""
        pass

    @abstractproperty
    def value(self):
        """Returns the expected value generated from the payload"""
        pass

    @abstractproperty
    def payload(self):
        """This is a deepcopy-able version of the CRDT's payload.

        If the CRDT is going to be serialized to storage, this is the data that should be
        stored.
        """
        pass

    @classmethod
    def from_payload(cls, payload):
        """Create a new instance of this CRDT using a payload.  This is useful for
        creating an instance using a deserialized value from a datastore."""
        new = cls()
        new.payload = payload
        return new
