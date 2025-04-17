from datetime import datetime


class Animal:
    """Базовый класс для хранения животных в питомнике."""
    def __init__(self, type_of_animal, name, date_of_birth, birthplace):
        """Инициализирует новый экземпляр класса Animal."""
        self.type_of_animal = type_of_animal  # вид, т.е. конкретное название животного
        self.name = name  # имя животного в заповеднике согласно документу
        self.date_of_birth = date_of_birth  # дата рождения, согласно документу
        self.birthplace = birthplace  # страна рождения

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
    def __init__(self, type_of_animal, name, date_of_birth, birthplace, nutrition, habitat):
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
    def __init__(self, type_of_animal, name, date_of_birth, birthplace, nutrition):
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
    def __init__(self, type_of_animal, name, date_of_birth, birthplace, breed):
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
    def __init__(self, type_of_animal, name, date_of_birth, birthplace, breed, lifting_capacity):
        super().__init__(type_of_animal, name, date_of_birth, birthplace, breed)
        self.lifting_capacity = lifting_capacity  #  грузоподъемность вьючного животного

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
