import requests


cookies = {'Куки'}

headers = {'Заголовки'}

params = {'Параметры'}

response = requests.get(
    'URL',
    params=params,
    cookies=cookies,
    headers=headers,
)