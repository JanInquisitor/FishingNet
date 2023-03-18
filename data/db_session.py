import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session

from data.modelbase import SqlAlchemyBase

__factory = None


def global_init(db_file: str):
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("You must specify a db file.")

    connection_string = "sqlite:///" + db_file.strip()
    print("Connecting to DB with {}".format(connection_string))

    engine = sa.create_engine(connection_string, echo=True)
    __factory = orm.sessionmaker(bind=engine)

    # This imports the classes model so that the create_all() function have access to them and creates de db tables
    from data import __all_models

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()
