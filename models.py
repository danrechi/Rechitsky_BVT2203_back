from sqlalchemy import Column, Integer, String, JSON
from db import Base

class Vacancy(Base):
    __tablename__ = "vacancies"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    name = Column(String)
    employment = Column(String)
    experience = Column(String)
    schedule = Column(String)
    salary = Column(String)
    salary_curr = Column(String)
    url = Column(String)
