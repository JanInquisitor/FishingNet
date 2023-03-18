# This file is for testing and reference only
import sqlalchemy.orm

from data import db_session

Release = tuple()


# Reference function, don't use. Delete at earliest convenience.
def lastest_packages(limit=10):
    session = db_session.create_session()

    releases = session.query(Release).order_by(Release.created_date.desc()).limit(limit).all()

    session.close()

    return releases


def packages():
    return [{"package": "SQLAlchemy"}, {"package": "Flask"}]
