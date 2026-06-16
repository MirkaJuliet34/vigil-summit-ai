from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from app.database import Base


class Lead(Base):

    __tablename__ = "leads"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    email = Column(String)

    phone = Column(String)

    company = Column(String)

    position = Column(String)

    score = Column(Integer, default=0)

    status = Column(String, default="new")

    next_action = Column(String, default="")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )