# Robots.txt
# Download and save to file robots.txt from wikipedia, twitter websites etc.
import requests


url = 'https://ru.wikipedia.org/robots.txt'
resp = requests.get(url)

if resp.ok:
    with open('robots.txt', 'w', encoding='utf-8') as file_object:
        file_object.write(resp.text)
else:
    raise Exception('HTTP is not supported')
