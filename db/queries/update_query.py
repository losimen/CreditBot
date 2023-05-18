from db.db import collection_users_data


async def update_user_balance(user_id: int, balance: float) -> None:
    await collection_users_data.update_one({'_id': user_id}, {'$set': {'balance': balance}})
