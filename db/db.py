from motor.motor_asyncio import AsyncIOMotorClient
import certifi

from config import MONGO_USERNAME, MONGO_CLUSTER, MONGO_PASS, TABLE_NAME

exampleUsersData = {
    "_id": 34,
    "first_name": "test",
    "last_name": "test",
    "username": "lgvrlgrvl",
}

class UserData:
    _id: int
    first_name: str
    last_name: str
    username: str

    def __init__(self, _id, first_name, last_name, username):
        self._id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    # convert class to dict
    def to_dict(self):
        return self.__dict__

    # convert dict to class
    @staticmethod
    def from_dict(obj):
        user = UserData(obj['_id'], obj['first_name'], obj['last_name'], obj['username'])
        return user


connect_str = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASS}@{MONGO_CLUSTER}/?retryWrites=true&w=majority"

client = AsyncIOMotorClient(connect_str, tlsCAFile=certifi.where())

db = client.get_database(TABLE_NAME)

collection_users_data = db['UserData']


async def init_db():
    pass