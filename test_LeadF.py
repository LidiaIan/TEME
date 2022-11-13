import requests


def post_md5():
    api_url = "https://azureauthapiv2.bigdbm.com/connect/token"
    payload = {
        "HashList": ["00000002a8bad17e35b8863bbd4f4d52", "0000000a2d662397bca1196daa94efc4"]}
    headers = {
        'content-type': 'application/json'
    }
    response = requests.post(api_url, data=payload, headers=headers)
    print(response.json())
    print('*' * 120)


post_md5()
