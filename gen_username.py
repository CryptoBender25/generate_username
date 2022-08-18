import requests
import fake_useragent

headers = {
    'authority': 'plarium.com',
    'accept': '*/*',
    'accept-language': 'ru,ru-RU;q=0.9,en;q=0.8',
    'app_id': '0',
    'content-type': 'application/json',
    'game_id': '0',
    'language_id': '1',
    'origin': 'https://plarium.com',
    'referer': 'https://plarium.com/ru/resource/generator/nickname-generator/',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sitemap_id': '1',
    'theme_id': '1',
    'time-zone': '0',
    'user-agent': fake_useragent.UserAgent().chrome,
}

params = {
    'group': '2',
    'gender': '0',
}
q = []

w = input("Сколько раз делать запрос(1 запрос - 10 юзернеймов) ")
with open("usernames.txt", "a") as f:
    for i in range(int(w)):
        response = requests.post('https://plarium.com/services/api/nicknames/new/create', params=params, cookies=cookies, headers=headers)
        for j in response.json() :
            if len(j) < 15 and (not j in q):
                q.append(j)
        print(i)
    f.write("\n".join(q))