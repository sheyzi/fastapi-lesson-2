from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CONNECTION_STRING = "sqlite:///./db.sqlite3"

# This is a comment

engine = create_engine(CONNECTION_STRING,
                       connect_args={"check_same_thread": False},
                       echo=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
