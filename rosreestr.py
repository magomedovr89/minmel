import os
import requests
from pprint import pprint

API_TOKEN = os.getenv('API_TOKEN')

###
headers_info = {'token': API_TOKEN}
info_url = 'https://apiegrn.ru/api/account/info'
###

user_info = requests.post(url=info_url, headers=headers_info)

###
headers_obj = {'Token': API_TOKEN}
data = {'query': '05:03:000003', 'deep': '0'}
obj_url = 'https://apiegrn.ru/api/cadaster/objectinfofull'
###

obj_info = requests.post(obj_url, headers=headers_obj, data=data)
pprint(obj_info.json())
