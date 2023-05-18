from motor.motor_asyncio import AsyncIOMotorClient
import certifi

from config import MONGO_USERNAME, MONGO_CLUSTER, MONGO_PASS, TABLE_NAME

connect_str = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASS}@{MONGO_CLUSTER}/?retryWrites=true&w=majority"
client = AsyncIOMotorClient(connect_str, tlsCAFile=certifi.where())
db = client.get_database(TABLE_NAME)

collection_users_data = db['UserData']
collection_expenses = db['Expenses']
collection_incomes = db['Incomes']


async def init_db():
    pass
