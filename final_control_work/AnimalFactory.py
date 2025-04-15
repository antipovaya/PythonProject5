from Animal import Animal
from Animal import Pet
from Animal import Mammal
from Animal import PackAnimal
from Animal import Bird


class AnimalFactory:
    @staticmethod
    def create_animal(type_of_animal: str, *args) -> Animal:
        """
        Создает экземпляр животного на основе переданного типа и
        параметров.
        :param type_of_animal: Название типа животного (например, 'Dog'
        или 'Cat')
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
        }
        animal_classes_pack_animal = {
            'Осел': PackAnimal,
            'Мул': PackAnimal,
            'Верблюд': PackAnimal,
            'Лама': PackAnimal,
            'Олень': PackAnimal,
        }
        if type_of_animal in animal_classes_pet:
            return animal_classes_pet[type_of_animal](animal_classes_pet[type_of_animal], *args)
        elif type_of_animal in animal_classes_mammal:
            return animal_classes_mammal[type_of_animal](animal_classes_mammal[type_of_animal], *args)
        elif type_of_animal in animal_classes_bird:
            return animal_classes_bird[type_of_animal](animal_classes_bird[type_of_animal], *args)
        elif type_of_animal in animal_classes_pack_animal:
            return animal_classes_pack_animal[type_of_animal](animal_classes_pack_animal[type_of_animal], *args)
        else:
            raise ValueError(f"Unknown animal type: {type_of_animal}")

# Создаем экземпляры животных с использованием фабрики
dog = AnimalFactory.create_animal('Собака', 'Малыш', '2020-10-12', 'Россия', 'Шпиц')

wolf = AnimalFactory.create_animal('Волк', 'Петр', '2022-11-12', 'Россия', 'хищник', 'наземный')
print(wolf.get_age())

bird = AnimalFactory.create_animal('Сокол', 'Валера', '2015-11-12', 'Россия', 'хищник')
print(bird.get_age())

donkey = AnimalFactory.create_animal('Осел','Антон', '2013-09-12', 'Россия', 'Домашний осел', 140)
print(donkey.get_age())