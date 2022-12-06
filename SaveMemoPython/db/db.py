import os.path

from sqlalchemy import create_engine, Table, Column, String

dbpath = os.path.join(os.path.dirname(__file__), 'memo.db')
dbcon = create_engine(f"sqlite:///{dbpath}", echo=True)
dbcon.connect()


class Remember(Table):
    remember = Column('remember', String(500))


def get_remembers() -> [str]:
    data = dbcon.execute('select * from remember')
    print("data ", data)
    return data


def save_text(text: str) -> None:
    dbcon.execute(f'insert into remember (remember) values({text})')
