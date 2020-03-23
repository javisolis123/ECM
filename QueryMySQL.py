from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine, Float, DateTime
from sqlalchemy.sql import select, insert
import time
from sqlalchemy import update
hoy = str(time.strftime("%d/%m/%Y"))
metadata = MetaData()
diarios = Table(hoy, metadata,
     Column('id', Integer, primary_key=True),
     Column('temperatura', Float()),
     Column('humedad', Float()),
     Column('canal1', Float()),
     Column('canal2', Float()),
     Column('canal3', Float()),
     Column('canal4', Float()),
     Column('hora', DateTime()),
 )
config = Table('config', metadata,
     Column('id', Integer, primary_key=True),
     Column('tipo', Integer),
     Column('frec', Integer),
 )

engine = create_engine('mysql+pymysql://javi:javiersolis12@10.0.0.20/Juno')
connection = engine.connect()

if __name__ == "__main__":
    #arriba = update(config).where(config.c.id==1).values(tipo=0)
    arriba = update(config).where(config.c.id==1).values(tipo=0)
    print (arriba)
    connection.execute(arriba)
    """while True:
        metadata.create_all(engine)
        #print("Se creo con exito la Tabla users")
        #r = select([config.c.tipo])
        #print (r)
        #result = connection.execute(r).fetchone()
        #print(int(result[0]))
        rest = diarios.insert().values(temperatura = 10.10,
                                        humedad = 10.10,
                                        canal1 = 9.8,
                                        canal2 = 10.1,
                                        canal3 = 11.2,
                                        canal4 = 10.2,
                                        hora = time.strftime("%Y/%m/%d %H:%M:%S")
        )
        connection.execute(rest)"""

