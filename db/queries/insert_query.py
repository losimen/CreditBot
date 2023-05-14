from db.db import collection_users_data, UserData


async def insert_user(user_id, first_name, last_name, username):
    ex = UserData(user_id, first_name, last_name, username).to_dict()
    await collection_users_data.insert_one(ex)
