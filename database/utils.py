from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from database.base import engine
from database.models import (Users, Products, Carts, Orders, Categories, FinallyCarts)
from sqlalchemy import update, select

def get_session():
    return Session(engine)



def db_register_user(full_name: str, chat_id, int):
    """registering a user in base"""

    try:
        with get_session() as session:
            query = Users(name=full_name, telegram=chat_id)
            session.add(query)
            session.commit()
        return False
    except IntegrityError:
        return True

def db_update_user(chat_id: int, phone: str):
    """getting user phone number"""

    with get_session() as session:
        query = update(Users).where(Users.telegram == chat_id).values(phone=phone)
        session.execute(query)
        session.commit()

def db_create_user_cart(chat_id:int):
    """creating user cart"""
    try:
        with get_session() as session:
            subquery = session.scalar(select(Users).where(Users.telegram == chat_id))
            query = Carts(user_id=subquery.id)
            session.add(query)
            session.commit()
            return True
    except IntegrityError:
        return False
