import requests

def randomgender(gender: str, number: int):
    payload = {
        "results":number,
        "gender":gender
    }
    url = 'https://randomuser.me/api'
    respons = requests.get(url, params=payload)
    if respons.status_code == 200:
        users = []
        for user in respons.json()['results']:
            users.append({
                'first': user['name']['first'],
                'last': user['name']['last'],
                'url': user['picture']['large'],
                
            })
        return users
    return {}

def randomdog(name: str, number: int):
    animals = []
    for i in range(number):
        url = 'https://random.dog/woof.json'
        respons = requests.get(url)
        url = respons.json()['url']
        animals.append({
            'url': url,
            "first":"Black",
            "last":name.capitalize()
        })
    return animals

def randomcat(name: str, number: int):
    animals = []
    for i in range(number):
        url = "https://api.thecatapi.com/v1/images/search"
        respons = requests.get(url)
        url = respons.json()[0]['url']
        animals.append({
            "url":url,
            "first":"White",
            "last":name.capitalize()
        })
    return animals


