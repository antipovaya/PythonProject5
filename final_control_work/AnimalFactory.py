from Animal import Animal
from Animal import Pet
from Animal import Mammal
from Animal import PackAnimal
from Animal import Bird


class AnimalFactory:
    """Класс-фабрика для создания экземпляров наследников класса Animal."""
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
        'собака' : Pet,
        'кошка' : Pet,
        'крыса' : Pet,
        'хомяк' : Pet,
        'кролик': Pet,
        'шиншилла': Pet
        }
        animal_classes_mammal = {
            'лев': Mammal,
            'тигр': Mammal,
            'жираф': Mammal,
            'панда': Mammal,
            'заяц': Mammal,
            'медведь': Mammal,
            'волк': Mammal,
        }
        animal_classes_bird = {
            'сокол': Bird,
            'сова': Bird,
            'зяблик': Bird,
            'сорока': Bird,
            'галка': Bird,
            'сойка': Bird,
            'голубь': Bird,
            'курица': Bird,
            'пингвин': Bird
        }
        animal_classes_pack_animal = {
            'осел': PackAnimal,
            'мул': PackAnimal,
            'верблюд': PackAnimal,
            'лама': PackAnimal,
            'олень': PackAnimal,
            'лошадь': PackAnimal,
            'буйвол': PackAnimal
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
# dog = AnimalFactory.create_animal('Собака', 'Малыш', '2020-10-12', 'Россия', 'Шпиц')






