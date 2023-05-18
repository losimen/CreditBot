from abc import ABC, abstractmethod


class IType(ABC):
    @abstractmethod
    def to_dict(self):
        pass

    @staticmethod
    @abstractmethod
    def from_dict(obj):
        pass
