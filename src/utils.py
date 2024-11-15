import os, json
from pathlib import Path

from src.external_api import get_currency_rate

"""""""""""""""""
Создаём необходимые для работы функции
"""""""""""""""""

path_to_json_file = os.path.join(Path(os.path.dirname(__file__)).parents[0], "data", "operations.json")
# Путь, через который можно найти файл с информацией о транзакциях. Склеиваем путь следующим образом:
# бёрем место нахождения текущего модуля через os.path.dirname(__file__), поднимаемся в директорию выше через parents[0],
# потом заходим в папку "data" и берём необходимый файл "operations.json".

"""""""""
1.Создаём функцию, которая в качестве аргумента путь к необходимому файлу "operations.json",преобразовывая json файл 
и возвращая информацию в виде списка. Кроме того, обрабатывается возможность отсутствия файла по выданному пути или 
возможности его повреждения(содержит не список или пуст) через обработки ошибки декодирования.
"""""""""
def take_info_about_transaction(path_of_json_file):
    try:                       #Пытаемся открыть файл формата json переводя его в список и выдавая этот список на выход
        with open(path_of_json_file, "r", encoding="utf-8") as file:
            info_about_transaction = json.load(file)
        return info_about_transaction

    except FileNotFoundError:  # Обрабатываем ошибку отсутсвия файла и возвращаем пустой список
        info_about_transaction = []
        return info_about_transaction

    except json.decoder.JSONDecodeError: # Если файл пустой, или не является списком, то возвращаем пустой список
        info_about_transaction = []
        return info_about_transaction
info = take_info_about_transaction(path_to_json_file)
print(info)


"""""""""
2. Создаем функцию, которая берёт в качестве аргумента id транзакции а на выходе сумму транзакции в рублях.
Если транзакции выполнена в другой валюте, то через функцию в модуле external_api.
"""""""""



def information_about_amount_of_transaction():
    client_id = int(input("Введите id для получения информации о сумме перевода:"))
    info_transaction = take_info_about_transaction(path_to_json_file)
    amount = 0
    for transaction in info_transaction:
        if transaction["id"] == client_id:
            if transaction['operationAmount']['currency']['code'] == "RUB":
                amount = transaction['operationAmount']['amount']
            elif transaction['operationAmount']['currency']['code'] == "USD":
                amount = get_currency_rate(transaction['operationAmount']['amount'])
    return amount

print(information_about_amount_of_transaction())