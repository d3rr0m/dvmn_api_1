import requests

URL = 'https://wttr.in/'
payload = {
    'MnTQ': '',
    '%26': '',
    'lang': 'ru',
}


def get_wheater(city_code: str, payload):
    response = requests.get(URL, params=payload)
    response.raise_for_status()
    print(response.url)
    return response


def main():
    print(get_wheater('london', 'ru', 'MnTq').text)
    print(get_wheater('svo', 'ru', 'MnTq').text)
    print(get_wheater('череповец', 'ru', 'MnTq').text)


if __name__ == '__main__':
    main()
