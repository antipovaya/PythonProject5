# Написать программу на Python, которая проверяет вводимый пользователем пароль на сложность:
# — не менее 8 символов
# — наличие прописных и строчных букв
# — наличие цифр
# и переводит его в хэш-значение.
import hashlib
import bcrypt


is_numeric = False
is_upper = False
is_lower = False
while not is_numeric or not is_upper or not is_lower:
    password_user = input('Введите пароль: ')
    is_numeric = False
    is_upper = False
    is_lower = False
    for i in password_user:
        if i.isnumeric():
            is_numeric = True
        elif i.isupper():
            is_upper = True
        elif i.islower():
            is_lower = True
    if len(password_user) > 8 and is_numeric and is_upper and is_lower:
        print('Пароль: Oк')
        hash_object = hashlib.sha256(password_user.encode())
        print(f'Хэш значение пароля: {hash_object.hexdigest()}')  # Выводим хэш в виде шестнадцатеричной строки
        # Используем библиотеку bcrypt
        print(f'Хэш значение пароля: {bcrypt.hashpw(password_user.encode(), bcrypt.gensalt(rounds=14))}') #bcrypt.gensalt(rounds=12) — количество раундов хеширования, по умолчанию 12. Чем выше этот параметр, тем медленнее и безопаснее будет процесс
    else:
        print('Пароль слишком простой')



