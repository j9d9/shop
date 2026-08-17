from os.path import join
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from database.base import engine
from database.models import (Users, Products, Carts, Orders, Categories, FinallyCarts)
from sqlalchemy import update, select, func.sum, join

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

        def db_get_all_category():
            '''getting all categories'''
            with get_session() as session:
                query = select(Categories)
                return  session.scalars(query).all

def db_get_finally_price():
    '''getting finalxx price'''
    with get_session() as session:
        query = select(func.sum(FinallyCarts.final_price)).select_from(
            join(Carts, FinallyCarts, Carts.id == FinallyCarts.cart_id).join(Users, Users.id == Carts.user_id).where(
                Users.telegram == chat_id)

        )
        return session.scalar(query).fetchone()[0]


    def db_get_last_orders(chat_id, limit = 10):
        '''getting last orders'''
        with get_session() as session:
            query = (
                select(Orders)
                join(Carts, Orsers.cart_id == Cards.id)
                join(Users, Users.id == Carts.user_id)
                where(Users.telegram == chat_id).
                order_by(Orders_id.desc()).
                limit(limit)
            )
            return session.scalars(query).all()

