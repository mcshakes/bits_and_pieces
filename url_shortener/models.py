from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

Base = declarative_base()


class Link(Base):
    __tablename__ = "links"
    id = Column(Integer, primary_key=True)
    uri = Column(String)
    short_url = Column(String)
    created_at = Column(DateTime(timezone=True),
                        nullable=False, default=datetime.now)

    def __repr__(self):
        return "<Link(uri='{}', short_url='{}', date_created='{}')>"\
            .format(self.uri, self.short_url, self.date_created)
