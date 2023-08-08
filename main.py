import requests


URL = 'https://wttr.in/'
payload = {
    'MnTQ': '',
    'lang': 'ru',
}


def get_weather(city_code: str):
    response = requests.get(URL+city_code, params=payload)
    response.raise_for_status()
    return response.text


def main():
    places = ['london', 'svo', 'череповец']
    for place in places:
        print(get_weather(place))


if __name__ == '__main__':
    main()
