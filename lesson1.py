import requests

URL = 'https://wttr.in/{city_code}?{params}lang={lang_code}'


def get_wheater(city_code: str, lang_code: str, params=''):
    params += '&'
    url = URL.format(city_code=city_code, lang_code=lang_code, params=params)
    response = requests.get(url)
    response.raise_for_status()
    return response


def main():
    print(get_wheater('london', 'ru', 'MnTq').text)
    print(get_wheater('svo', 'ru', 'MnTq').text)
    print(get_wheater('череповец', 'ru', 'MnTq').text)


if __name__ == '__main__':
    main()
