from db.types.type_interface import IType

class UserData(IType):
    _id: int
    first_name: str
    last_name: str
    username: str
    balance: float

    def __init__(self, _id, first_name, last_name, username, balance=0):
        self._id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.balance = balance

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(obj) -> 'UserData':
        user = UserData(obj['_id'], obj['first_name'], obj['last_name'], obj['username'], obj['balance'])
        return user
