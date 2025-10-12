from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    photo_url = Column(String, nullable=True)
    birth_date = Column(Date, nullable=True)
    locality_id = Column(Integer, ForeignKey("localities.id"))

    locality = relationship("src.localities.models.Locality", lazy="selectin")
