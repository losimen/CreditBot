from datetime import datetime
from db.types.type_interface import IType


class Income(IType):
    user_id: int
    amount: float
    description: str
    date: datetime

    def __init__(self, user_id, amount, description, date):
        self.user_id = user_id
        self.amount = amount
        self.description = description
        self.date = date

    def to_dict(self) -> dict:
        return self.__dict__

    @staticmethod
    def from_dict(obj) -> 'Income':
        expense = Income(obj['user_id'], obj['amount'], obj['description'], obj['date'])
        return expense
