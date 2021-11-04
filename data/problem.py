import sqlalchemy

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    description = sqlalchemy.Column(sqlalchemy.Text,
                                    primary_key=True, autoincrement=False)

    votes = sqlalchemy.Column(sqlalchemy.Integer,
                              primary_key=False, autoincrement=False)
