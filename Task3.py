# The Weather app
# Write a console application which takes as an input
# a city name and returns current weather in the format of your choice.
# For the current task, you can choose any weather API or website or use https://openweathermap.org
import requests


def main():
    api_key = 'e4aba97a2375bc5267a3cb3b17d27e9e'
    url = 'http://api.openweathermap.org/data/2.5/weather'

    while True:
        city = input('Enter the city name: ')
        if city.isalpha():
            break

    payload = {
        'q': city,
        'appid': api_key,
        'lang': 'ru',
        'units': 'metric'
    }

    resp = requests.get(url, params=payload)

    if resp.ok:
        data = resp.json()
        print(f"Країна: {data['sys']['country']}")
        print(f"Місто: {data['name']}")
        print(f"Температура: {data['main']['temp']} °C")
        print(f"Погода: {data['weather'][0]['description'].title()}")
    else:
        raise Exception("HTTP is not supported")


if __name__ == '__main__':
    try:
        main()
    except Exception as massage:
        print(massage)
