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


def get_remembers(get_dates=True) -> [str]:
    text_data = []
    data = dbcon.execute('select data, tarih from remember')
    data = data.fetchall()
    for i in data:
        if get_dates:
            i = " - Tarih: ".join(i)
        else:
            i = i[0]
        text_data.append(i)

    return text_data


def save_text(data: str, ) -> None:
    if data and data != "":
        ins = remember_table.insert().values(data=data, tarih=datetime.utcnow())
        dbcon.engine.execute(ins)
