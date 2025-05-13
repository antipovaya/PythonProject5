# Доп. задание* (не обязательное): напишите программу на Python, которая будет вычислять хэш-значения.

import hashlib

# Хэширование строки с использованием SHA-256

def string_to_hash(data):
    hash_object = hashlib.sha256(data.encode())
    print(hash_object.hexdigest())  # Выводим хэш в виде шестнадцатеричной строки

data = "cat"
string_to_hash(data)