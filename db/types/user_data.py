from db.types.type_interface import IType

class UserData(IType):
    _id: int
    first_name: str
    last_name: str
    username: str

    def __init__(self, _id, first_name, last_name, username):
        self._id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(obj) -> 'UserData':
        user = UserData(obj['_id'], obj['first_name'], obj['last_name'], obj['username'])
        return user
