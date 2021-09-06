# Load data
# Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .
# As a result, store all comments in chronological order in JSON and dump it to a file.
import requests
import json


def main():
    url = 'https://api.pushshift.io/reddit/comment/search/'
    resp = requests.get(url)
    subreddit = []
    if resp.ok:
        with open('subreddit.json', 'w') as file_object:
            json.dump(resp.json(), file_object, indent=2)
        with open('subreddit.json') as file_object:
            file_read = json.load(file_object)
        for i in file_read.values():
            for j in range(len(i)):
                subreddit.append({i[j]['id']: {'author': i[j]['author'], 'subreddit': i[j]['subreddit']}})
        with open('subreddit.json', 'w') as file_object:
            json.dump(subreddit, file_object, indent=2)
    else:
        raise Exception("HTTP is not supported")


if __name__ == '__main__':
    try:
        main()
    except Exception as massage:
        print(massage)
