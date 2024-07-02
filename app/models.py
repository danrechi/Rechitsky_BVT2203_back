from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Vacancy(db.Model):
    __tablename__ = 'vacancies'
    id = db.Column(db.Integer, primary_key=True)  # Добавляем первичный ключ

    address_building = db.Column(db.String(255))
    address_city = db.Column(db.String(255))
    address_description = db.Column(db.String(255))
    address_street = db.Column(db.String(255))

