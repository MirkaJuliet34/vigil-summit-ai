from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from app.database import Base


class Interaction(Base):

    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True)

    lead_id = Column(
        Integer,
        ForeignKey("leads.id")
    )

    channel = Column(String)

    interaction_type = Column(String)

    content = Column(Text)

    status = Column(String)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )