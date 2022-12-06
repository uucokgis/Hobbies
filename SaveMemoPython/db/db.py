from datetime import datetime
import os.path

from sqlalchemy import create_engine, Table, MetaData, Column, Integer, DateTime, String, insert, values

dbpath = os.path.join(os.path.dirname(__file__), 'memo.db')
dbcon = create_engine(f"sqlite:///{dbpath}", echo=True)
dbcon.connect()

meta = MetaData()
remember_table = Table(
    'remember', meta,
    Column('data', String, nullable=False),
    Column('id', Integer, primary_key=True),
    Column('tarih', DateTime, nullable=False)
)
meta.create_all(dbcon)


def get_remembers() -> [str]:
    data = dbcon.execute('select * from remember')
    print("data ", data)
    return data


def save_text(data: str, ) -> None:
    ins = remember_table.insert().values(data=data, tarih=datetime.utcnow())
    dbcon.engine.execute(ins)
