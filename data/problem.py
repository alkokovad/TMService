import sqlalchemy

from .db_session import SqlAlchemyBase


class Problems(SqlAlchemyBase):
    __tablename__ = 'problems'

    id = sqlalchemy.Column(sqlalchemy.INTEGER,
                           primary_key=True, autoincrement=False)

    description = sqlalchemy.Column(sqlalchemy.Text,
                                    primary_key=True, autoincrement=False)

    votes = sqlalchemy.Column(sqlalchemy.Integer,
                              primary_key=False, autoincrement=False)
