import os, json
from pathlib import Path
"""""""""""""""""
Создаём необходимые для работы функции
"""""""""""""""""

path_to_json_file = os.path.join(Path(os.path.dirname(__file__)).parents[0], "data", "operations.json")
#Путь, через который можно найти файл с информацией о транзакциях

def take_info_about_transaction(path_of_json_file):
    with open(path_of_json_file, "r", encoding="utf-8") as file:
        info_about_transaction = json.load(file)
    return info_about_transaction
info = take_info_about_transaction(path_to_json_file)
print(info)
print(info[0])
print(info[0]['id'])