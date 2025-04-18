from datetime import datetime


class Animal:
    """Базовый класс для хранения животных в питомнике."""
    def __init__(self, type_of_animal, name, date_of_birth, birthplace):
        """Инициализирует новый экземпляр класса Animal.
        :param type_of_animal: Вид, т.е. конкретное название животного
        :param name: Имя животного, согласно документу
        :param date_of_birth: Дата рождения животного, согласно документу (в формате '2012-12-22')
        :param birthplace: Страна рождения
        """
        self.type_of_animal = type_of_animal
        self.name = name
        self.date_of_birth = date_of_birth
        self.birthplace = birthplace

    def get_age(self, date_format='%Y-%m-%d'):
        pass

    def get_type_of_animal(self):
        pass

    def get_name(self):
        pass

    def get_date_of_birth(self):
        pass

    def get_birthplace(self):
        pass


class Mammal(Animal):
    """Класс для хранения млекопитающих в питомнике."""
    def __init__(self, type_of_animal, name, date_of_birth, birthplace, nutrition, habitat):
        """Инициализирует новый экземпляр класса Mammal.
        :param type_of_animal: Вид, т.е. конкретное название животного
        :param name: Имя животного, согласно документу
        :param date_of_birth: Дата рождения животного, согласно документу (в формате '2012-12-22')
        :param birthplace: Страна рождения
        :param nutrition: Тип питания
        :param habitat: Среда обитания
        """
        super().__init__(type_of_animal, name, date_of_birth, birthplace)
        self.nutrition = nutrition  # питание
        self.habitat = habitat  #  среда обитания

    def get_age(self, date_format='%Y-%m-%d'):
        birthdate = datetime.strptime(self.date_of_birth, date_format)   # Преобразуем дату из строкового формата '%Y-%m-%d'
        return (datetime.now() - birthdate).days // 365  # (Прожитые дни) производим деление на (дни в году) – получаем возраст

    def get_type_of_animal(self):
        return self.type_of_animal

    def get_name(self):
        return self.name

    def get_date_of_birth(self):
        return self.date_of_birth

    def get_birthplace(self):
        return self.birthplace

    def get_nutrition(self):
        return self.nutrition

    def get_habitat(self):
        return self.habitat


class Bird(Animal):
    """Класс для хранения птиц в питомнике."""
    def __init__(self, type_of_animal, name, date_of_birth, birthplace, nutrition):
        """Инициализирует новый экземпляр класса Bird.
        :param type_of_animal: Вид, т.е. конкретное название животного
        :param name: Имя животного, согласно документу
        :param date_of_birth: Дата рождения животного, согласно документу (в формате '2012-12-22')
        :param birthplace: Страна рождения
        :param nutrition: Тип питания
        """
        super().__init__(type_of_animal, name, date_of_birth, birthplace)
        self.nutrition = nutrition  # питание

    def get_age(self, date_format='%Y-%m-%d'):
        birthdate = datetime.strptime(self.date_of_birth, date_format)   # Преобразуем дату из строкового формата '%Y-%m-%d'
        return (datetime.now() - birthdate).days // 365  # (Прожитые дни) производим деление на (дни в году) – получаем возраст

    def get_type_of_animal(self):
        return self.type_of_animal

    def get_name(self):
        return self.name

    def get_date_of_birth(self):
        return self.date_of_birth

    def get_birthplace(self):
        return self.birthplace

    def get_nutrition(self):
        return self.nutrition


class Pet(Animal):
    """Класс для хранения домашних питомцев в питомнике."""
    def __init__(self, type_of_animal, name, date_of_birth, birthplace, breed):
        """Инициализирует новый экземпляр класса Pet.
        :param type_of_animal: Вид, т.е. конкретное название животного
        :param name: Имя животного, согласно документу
        :param date_of_birth: Дата рождения животного, согласно документу (в формате '2012-12-22')
        :param birthplace: Страна рождения
        :param breed: Порода
        """
        super().__init__(type_of_animal, name, date_of_birth, birthplace)
        self.breed = breed
        self.commands = []

    def get_age(self, date_format='%Y-%m-%d'):
        birthdate = datetime.strptime(self.date_of_birth, date_format)   # Преобразуем дату из строкового формата '%Y-%m-%d'
        return (datetime.now() - birthdate).days // 365  # (Прожитые дни) производим деление на (дни в году) – получаем возраст

    def get_type_of_animal(self):
        return self.type_of_animal

    def get_name(self):
        return self.name

    def get_date_of_birth(self):
        return self.date_of_birth

    def get_birthplace(self):
        return self.birthplace

    def get_breed(self):
        return self.breed

    def set_commands(self, command):
        self.commands.append(command)


class PackAnimal(Pet):
    """Класс для хранения вьючных животных в питомнике."""
    def __init__(self, type_of_animal, name, date_of_birth, birthplace, breed, lifting_capacity):
        """Инициализирует новый экземпляр класса PackAnimal.
        :param type_of_animal: Вид, т.е. конкретное название животного
        :param name: Имя животного, согласно документу
        :param date_of_birth: Дата рождения животного, согласно документу (в формате '2012-12-22')
        :param birthplace: Страна рождения
        :param breed: Порода
        :param lifting_capacity: Грузоподъемность вьючного животного
        """
        super().__init__(type_of_animal, name, date_of_birth, birthplace, breed)
        self.lifting_capacity = lifting_capacity

    def get_name(self):
        return self.name

    def get_date_of_birth(self):
        return self.date_of_birth

    def get_birthplace(self):
        return self.birthplace

    def get_breed(self):
        return self.breed

    def get_lifting_capacity(self):
        return self.lifting_capacity

# cat = Pet("Кошка", "Ася", "2020-10-12", "Россия", "Британская")
# print(cat.get_age())
