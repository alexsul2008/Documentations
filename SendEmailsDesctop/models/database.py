# import asyncio
from typing import Annotated

from sqlalchemy import String, create_engine
from sqlalchemy.exc import OperationalError
# from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine  #, AsyncSession
from sqlalchemy.orm import DeclarativeBase, sessionmaker #, Session

from config import settings

sync_engine = create_engine(
    url = settings.DATABASE_URL_psycopg,
    # echo = True,
    pool_size=50,
    # max_overflow=10,
    pool_pre_ping=True
)

sync_engine_gasi = create_engine(
    url = settings.DATABASE_URL_gasi,
    pool_size=50,
    pool_pre_ping=True
)

# async_engine = create_async_engine(
#     url = settings.DATABASE_URL_asyncpg,
#     echo = True,
# )

session_factory = sessionmaker(bind=sync_engine)()
session_factory_gasi = sessionmaker(bind=sync_engine_gasi)()

# bind User operations to engine 1, Account operations to engine 2


str_2 = Annotated[str, 2]
str_10 = Annotated[str, 10]
str_15 = Annotated[str, 15]
str_30 = Annotated[str, 30]
str_31 = Annotated[str, 31]
str_63 = Annotated[str, 63]
str_100 = Annotated[str, 100]
str_200 = Annotated[str, 200]
str_256 = Annotated[str, 256]
str_300 = Annotated[str, 300]

str_127 = Annotated[str, 127]

class BaseGasi(DeclarativeBase):
    type_annotation_map = {
        str_31: String(31),
        str_63: String(63),
        str_127: String(127),
        str_200: String(200),
        str_300: String(300),
    }

class Base(DeclarativeBase):
    type_annotation_map = {
        str_2: String(2),
        str_10: String(10),
        str_15: String(15),
        str_30: String(30),
        str_100: String(100),
        str_256: String(256)
    }

    repr_cols_num = 3
    repr_cols = tuple()

    def __repr__ (self):
        """Relationships не используются в repr(), т.к. могут вести к неожиданным подгрузкам"""
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f"{col}={getattr(self, col)}")

        return f"<{self.__class__.__name__} {', '.join(cols)}>"

# print(f'{Base.metadata=}')
# print(f'{BaseGasi.metadata=}')
# print(f'{Base.registry=}')
# print(f'{BaseGasi.registry=}')

# Session = sessionmaker()
# Session.configure(binds={Base: sync_engine, BaseGasi: sync_engine_gasi})
#
# print(f'{Session1=}')

def currect_connect_in_db(engine):
    try:
        conn = engine.connect()
        conn.close()
        return True
    except OperationalError as error:
        return False





















































# from sqlalchemy import create_engine
# # from sqlalchemy.ext.declarative import declarative_base
# # from sqlalchemy.orm import sessionmaker
#
# from sqlalchemy_utils import database_exists, create_database, drop_database
# from local_settings import postgresql as settings
#
# def get_engine(user, passwd, host, port, db):
#     url = f"postgresql+psycopg://{user}:{passwd}@{host}:{port}/{db}"
#     if not database_exists(url):
#         create_database(url)
#     engine = create_engine(url, pool_size = 50, echo = True, pool_pre_ping=True, isolation_level="REPEATABLE READ")
#
#     return engine
#
# # DATABASE_NAME = 'sandemail.sqlite3'
# # # DATABASE_NAME = 'db.sqlite3'
# #
# # engine = create_engine(f'sqlite:///{DATABASE_NAME}', echo=False)
# # Session = sessionmaker(bind=engine)
# #
# # Base = declarative_base()
#
# # engine = create_engine("postgresql+psycopg2://emailsoper:emailsoper@10.40.176.133:6433/sendemails")
# engine = get_engine(settings['pguser'],
#                     settings['pgpasswd'],
#                     settings['host'],
#                     settings['port'],
#                     settings['db'])
#
#
# # Session = sessionmaker(bind=engine, autoflush=False)
# #
# # Base = declarative_base()
#
#
#
#
#
# # def create_db():
# #     Base.metadata.create_all(engine)