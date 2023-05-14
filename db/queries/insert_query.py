from db.db import collection_users_data
from db.types.user_data import UserData

async def insert_user(user_id, first_name, last_name, username) -> None:
    ex = UserData(user_id, first_name, last_name, username).to_dict()
    await collection_users_data.insert_one(ex)
