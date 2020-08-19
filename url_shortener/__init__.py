from url_shortener import URLShortener
from flask import Flask
from sqlalchemy import create_engine
from contextlib import contextmanager

from sqlalchemy.orm import sessionmaker
from config import DATABASE_URI
from models import Base, Link

engine = create_engine(DATABASE_URI)

app = Flask(__name__)

Session = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    db_session = Session()

    try:
        yield db_session

        if db_session.commit():
            print("Succesful commit")
    except Exception:
        db_session.rollback()
        raise
    finally:
        db_session.close()


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def return_shortened_link(uri):
    url = URLShortener(uri)
    return url.shorten(8)


if __name__ == "__main__":
    recreate_database()
    # uri = "https://www.freecodecamp.org/learn/coding-interview-prep/take-home-projects/build-a-roguelike-dungeon-crawler-game"
    # short = return_shortened_link(uri)
    uri = "https://www.poopage.com/try-it-like-you-like-t"
    short = return_shortened_link(uri)

    link = Link(
        uri=uri,
        short_url=short
    )

    with session_scope() as s:
        # print(s)
        s.add(link)
