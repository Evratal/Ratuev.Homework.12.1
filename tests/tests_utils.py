

""""""""""""""""""""""
Пишем тесты для чтения файла.
"""""""""""""""""""""""
import os
from pathlib import Path

from src.utils import take_info_about_transaction


def test_taking_info():
    path_to_json_file = os.path.join(Path(os.path.dirname(__file__)).parents[0], "data", "operations.json")
    path_to_json_file_1 = os.path.join(Path(os.path.dirname(__file__)).parents[0], "data", "operations_test.json")
    path_to_json_file_2 = os.path.join(Path(os.path.dirname(__file__)).parents[0], "data", "operations_not_exist.json")
    assert take_info_about_transaction(path_to_json_file)[0]['id'] == 441945886
    assert take_info_about_transaction(path_to_json_file_1) == []
    assert take_info_about_transaction(path_to_json_file_2) == []
