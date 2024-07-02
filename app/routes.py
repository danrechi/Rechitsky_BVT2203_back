from flask import Blueprint, jsonify, request
from .models import db, Vacancy
from .utils import fetch_vacancies

api = Blueprint('api', __name__)


@api.route('/parse-vacancies', methods=['POST'])
def parse_vacancies():
    data = request.get_json()
    search_text = data.get('search_text', '')

    vacancies_data = fetch_vacancies(search_text)
    if vacancies_data:
        for item in vacancies_data.get('items', []):
            address = item.get('address', {})
            if address:

                vacancy = Vacancy(
                    address_building=address.get('building'),
                    address_city=address.get('city'),
                    address_description=address.get('description'),
                    address_street=address.get('street')
                )
                db.session.add(vacancy)
        db.session.commit()
        return jsonify({'message': 'парс'}), 200
    else:
        return jsonify({'error': 'не парс'}), 500
