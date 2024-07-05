from fastapi import FastAPI, HTTPException, Depends
import requests
from sqlalchemy.orm import Session
from db import engine, get_db, Base, SessionLocal
from models import Vacancy
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_URL = "https://api.hh.ru/vacancies"


# Создание таблиц
@app.on_event("startup")
def startup():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    load_vacancies_on_startup()


def fetch_vacancies_from_hh(keyword: str, page: int = 0, per_page: int = 20):
    params = {
        "text": keyword,
        "page": page,
        "per_page": per_page
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching vacancies from HH.ru")

    return response.json().get("items", [])


def load_vacancies_on_startup():
    db = SessionLocal()
    try:
        vacancies_data = fetch_vacancies_from_hh("программист")

        for item in vacancies_data:
            vacancy = Vacancy(
                id=item.get("id"),
                city=item.get("area", {}).get("name") or "-",
                name=item.get("name") or "-",
                employment=item.get("employment", {}).get("name") or "-",
                experience=item.get("experience", {}).get("name") or "-",
                schedule=item.get("schedule", {}).get("name") or "-",
                salary=item.get("salary", {}).get("from") if item.get("salary") else "-",
                salary_curr=item.get("salary", {}).get("currency") if item.get("salary") else "-",
                url=item.get("alternate_url") or "-"
            )

            db.add(vacancy)

        db.commit()
    finally:
        db.close()


@app.get("/vacancies/")
def get_vacancies(db: Session = Depends(get_db)):
    vacancies = db.query(Vacancy).all()
    return vacancies

@app.on_event("shutdown")
def shutdown():
    db = Session(bind=engine)
    try:
        db.query(Vacancy).delete()
        db.commit()
    finally:
        db.close()
