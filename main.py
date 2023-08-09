import requests


URL = 'https://wttr.in/'


def get_weather(city_code: str, payload: dict):
    response = requests.get(f'{URL}{city_code}', params=payload)
    response.raise_for_status()
    return response.text


def main():
    payload = {
    'MnTQ': '',
    'lang': 'ru',
    }
    places = ['london', 'svo', 'череповец']
    for place in places:
        print(get_weather(place, payload))


if __name__ == '__main__':
    main()
