import os

from data import db_session
from data.Package import Package


def insert_a_package():
    p = Package()
    p.id = input('Package id / name: ').strip().lower()
    p.summary = input('Package summary: ').strip()
    p.author_name = input("Author: ").strip()

    import sqlalchemy.orm
    session: sqlalchemy.orm.Session = db_session.__factory()

    session.add(p)

    session.commit()


def main():
    init_db()
    while True:
        insert_a_package()


def init_db():
    top_folder = os.path.dirname(__file__)
    rel_file = os.path.join('..', 'dbsqlite', 'fishingnet.sqlite')
    db_file = os.path.join(top_folder, rel_file)
    db_session.global_init(db_file)


if __name__ == '__main__':
    main()
