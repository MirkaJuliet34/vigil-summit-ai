from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.database import Base


class EnrichedProfile(Base):

    __tablename__ = "enriched_profiles"

    id = Column(Integer, primary_key=True)

    lead_id = Column(
        Integer,
        ForeignKey("leads.id")
    )

    industry = Column(String)

    company_size = Column(String)

    seniority = Column(String)

    interests = Column(String)

    linkedin_url = Column(String)