from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

class Base(DeclarativeBase):
    pass

def create_session_factory(database_url: str):
    engine = create_engine(database_url, echo=False)
    factory = sessionmaker(
        bind=engine,
        class_=Session,
        autoflush=False,
        autocommit=False,
        expire_on_commit=False
    )
    return engine, factory
