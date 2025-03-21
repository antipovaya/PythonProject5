import os
from pprint import pprint

def get_directory_files(path):
    """Функция вывода содержимого директории"""
    structure = []
    for file_or_directory in os.listdir(path):
        full_name = os.path.join(os.path.abspath(path),
                                                       file_or_directory)
        if os.path.isfile(full_name):
            structure.append((os.path.abspath(path), file_or_directory))
        else:
            structure.extend(get_directory_files(full_name))
    return structure


my_res = get_directory_files("C:/Users/7Ya/PycharmProjects/PythonProject5/algorithms")  # не забывать про обраьные слэши
pprint(my_res)
