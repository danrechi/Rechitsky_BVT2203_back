import requests


def fetch_vacancies(search_text):
    url = 'https://api.hh.ru/vacancies'
    params = {'text': search_text}
    headers = {'User-Agent': 'api-test-agent'}

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"ошибк: {e}")
        return None
