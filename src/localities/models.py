from sqlalchemy import Column, Integer, String
from src.database import Base


class Locality(Base):
    __tablename__ = "localities"

    id = Column(Integer, primary_key=True, index=True)
    country_name = Column(String, nullable=False, index=True)
    city_name = Column(String, nullable=False, index=True)