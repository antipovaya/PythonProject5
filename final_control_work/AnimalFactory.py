from Animal import Animal
from Animal import Pet
from Animal import Mammal
from Animal import PackAnimal
from Animal import Bird


class AnimalFactory:
    count_animal = 0
    list_animal = []

    @staticmethod
    def create_animal(type_of_animal: str, *args) -> Animal:
        """
        Создает экземпляр животного на основе переданного типа и
        параметров.
        :param type_of_animal: Название типа животного
        :param args: Параметры для конструктора животного
        :return: Экземпляр соответствующего класса животного
        """
        animal_classes_pet = {
        'Собака' : Pet,
        'Кошка' : Pet,
        'Крыса' : Pet,
        'Хомяк' : Pet,
        'Кролик': Pet,
        'Шиншилла': Pet
        }
        animal_classes_mammal = {
            'Лев': Mammal,
            'Тигр': Mammal,
            'Жираф': Mammal,
            'Панда': Mammal,
            'Заяц': Mammal,
            'Медведь': Mammal,
            'Волк': Mammal,
        }
        animal_classes_bird = {
            'Сокол': Bird,
            'Сова': Bird,
            'Зяблик': Bird,
            'Сорока': Bird,
            'Галка': Bird,
            'Сойка': Bird,
            'Голубь': Bird,
            'Курица': Bird
        }
        animal_classes_pack_animal = {
            'Осел': PackAnimal,
            'Мул': PackAnimal,
            'Верблюд': PackAnimal,
            'Лама': PackAnimal,
            'Олень': PackAnimal,
        }
        if type_of_animal in animal_classes_pet:
            AnimalFactory.count_animal += 1
            return animal_classes_pet[type_of_animal](animal_classes_pet[type_of_animal], *args)
        elif type_of_animal in animal_classes_mammal:
            AnimalFactory.count_animal += 1
            return animal_classes_mammal[type_of_animal](animal_classes_mammal[type_of_animal], *args)
        elif type_of_animal in animal_classes_bird:
            AnimalFactory.count_animal += 1
            return animal_classes_bird[type_of_animal](animal_classes_bird[type_of_animal], *args)
        elif type_of_animal in animal_classes_pack_animal:
            AnimalFactory.count_animal += 1
            return animal_classes_pack_animal[type_of_animal](animal_classes_pack_animal[type_of_animal], *args)
        else:
            raise ValueError(f"Unknown animal type: {type_of_animal}")

# Создаем экземпляры животных с использованием фабрики
dog = AnimalFactory.create_animal('Собака', 'Малыш', '2020-10-12', 'Россия', 'Шпиц')

# print(type(dog.get_type_of_animal()))
# print(type(dog.get_name()))
# print(type(dog.get_date_of_birth()))
# print(type(dog.get_age()))
# print(type(dog.get_breed()))






