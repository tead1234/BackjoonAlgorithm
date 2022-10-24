import requests
import json


def send_api(path, method):
    API_HOST = "https://api.twitter.com/2/users/"
    url = API_HOST + path
    headers = {'Content-Type': 'application/json', "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANh4iQEAAAAAHoKYK2DiRxuP4mYUa1G1hCROGwQ%3DlfIB4c5FZ5TMK0XJ8HcdLt5hZD5GmeEeVm51MhRJdluhNg6kOS"}
    body = {

    }
    try:
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))
        print("response status %r" % response.status_code)
        print("response text %r" % response.text)
    except Exception as ex:
        print(ex)


# 호출 예시
send_api("381696140/tweets", "GET")
