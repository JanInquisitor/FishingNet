import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session

from fishingnet.data.modelbase import SqlAlchemyBase

__factory = None


def global_init(username, password, hostname, port, database_name):
    global __factory

    if __factory:
        return

    if not username or not password or not hostname or not port or not database_name:
        raise Exception("You must specify PostgreSQL connection details.")

    # connection_string = f"postgresql://{username}:{password}@{hostname}:{port}/{database_name}"
    connection_string = f"postgresql://{hostname}:{port}/{database_name}"
    print("Connecting to DB with {}".format(connection_string))

    engine = sa.create_engine(connection_string, echo=True)
    __factory = orm.sessionmaker(bind=engine)

    # This imports the model classes so that the create_all() function has access to them to create the database tables
    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()
