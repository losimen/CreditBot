from db.db import collection_users_data

from db.types.user_data import UserData

async def get_user_data(user_id) -> UserData:
    user_data = None
    try:
        user_info = await collection_users_data.find_one({"_id": user_id})
        user_data = UserData.from_dict(user_info)
        return user_data
    except TypeError:
        return user_data