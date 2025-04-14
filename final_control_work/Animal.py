from datetime import datetime


class Animal:

    def __init__(self, name, type_of_animal, date_of_birth, birthplace):
        self.name = name  # имя животного в заповеднике согласно документу
        #self.animal_class = animal_class  # класс, к которому относится животное (млекопитающее, земноводное и пр.)
        self.type_of_animal = type_of_animal  # вид, т.е. конкретное название животного
        self.date_of_birth = date_of_birth  # дата рождения, согласно документу
        self.birthplace = birthplace  # страна рождения

    def get_age(self, date_format='%Y-%m-%d'):
        birthdate = datetime.strptime(self.date_of_birth, date_format)   # Преобразуем дату из строкового формата '%Y-%m-%d'
        return (datetime.now() - birthdate).days // 365  # (Прожитые дни) производим деление на (дни в году) – получаем возраст


class Mammal(Animal):
    def __init__(self, name, type_of_animal, date_of_birth, birthplace, nutrition, habitat):
        super().__init__(name, type_of_animal, date_of_birth, birthplace)
        self.nutrition = nutrition  # питание
        self.habitat = habitat  #  среда обитания


class Bird(Animal):
    def __init__(self, name, type_of_animal, date_of_birth, birthplace, nutrition, habitat):
        super().__init__(name, type_of_animal, date_of_birth, birthplace)
        self.nutrition = nutrition  # питание

# не забыть добавить список команд!!!

class Pet(Animal):
    def __init__(self, name, type_of_animal, date_of_birth, birthplace, breed):
        super().__init__(name, type_of_animal, date_of_birth, birthplace)
        self.breed = breed


class PackAnimal(Pet):
    def __init__(self, name, type_of_animal, date_of_birth, birthplace, breed, lifting_capacity):
        super().__init__(name, type_of_animal, date_of_birth, birthplace, breed)
        self.lifting_capacity = lifting_capacity  #  грузоподъемность вьючного животного


animal = Animal("Буба",  "Макака", "2020-10-12", "Россия")
print(animal.get_age())