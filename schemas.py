from pydantic import BaseModel
from typing import Optional, Dict

class VacancyCreate(BaseModel):
    id: int
    city: str
    name: str
    employment: str
    experience: str
    schedule: str
    salary: str
    salary_curr: str
    url: str

class Vacancy(VacancyCreate):
    class Config:
        orm_mode = True
