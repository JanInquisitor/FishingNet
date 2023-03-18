from datetime import datetime

import sqlalchemy as sa

from data.modelbase import SqlAlchemyBase


class Profile(SqlAlchemyBase):
    __tablename__ = "profiles"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)
    email = sa.Column(sa.String)
    summary = sa.Column(sa.String)
    created_date = sa.Column(sa.DateTime, default=datetime.now, index=True)
    updated_date = sa.Column(sa.DateTime, default=datetime.now, index=True)


    def __repr__(self):
        return "<Profile {}>".format(self.id)
