from Animal import Animal
from Animal import Pet
from Animal import Mammal
from Animal import PackAnimal
from Animal import Bird
from AnimalFactory import AnimalFactory
from AnimalRegistry import AnimalRegistry


def main():
    while True:
        command = input('Введите команду (0 - выход, 1 - запись, 2 - чтение, 3 - поиск): ')

        if command == '0':
            break

        elif command == '1':
            type_of_animal = input('Введите название животного (например, "собака", "кошка", "курица" и пр.): ')
            name = input('Введите имя животного: ')
            date_of_birth = input('Введите дату рождения животного (в формате "2012-12-12"): ')
            birthplace = input('Введите место рождения животного: ')

            additional_command = input('Введите команду: 1 - это домашний питомец, '
                                       '2 - вьючное животное, '
                                       '3 - другое млекопитающее, '
                                       '4 - птица ')

            if additional_command == '1':
                breed = input('Введите породу: ')
                animal = AnimalFactory.create_animal(type_of_animal, name, date_of_birth, birthplace, breed)
                age_animal = animal.get_age()
                AnimalRegistry.create_table_pet()
                AnimalRegistry.writing_to_table_pet(type_of_animal,
                                                    animal.get_name(),
                                                    animal.get_date_of_birth(),
                                                    age_animal,
                                                    animal.get_birthplace(),
                                                    animal.get_breed())

            elif additional_command == '2':
                breed = input('Введите породу: ')
                lifting_capacity = input('Введите грузоподъемность вьючного животного (в кг): ')
                animal = AnimalFactory.create_animal(type_of_animal, name, date_of_birth, birthplace, breed, lifting_capacity)
                age_animal = animal.get_age()
                AnimalRegistry.create_table_pack_animal()
                AnimalRegistry.writing_to_table_pack_animal(type_of_animal,
                                                            animal.get_name(),
                                                            animal.get_date_of_birth(),
                                                            age_animal,
                                                            animal.get_birthplace(),
                                                            animal.get_breed(),
                                                            animal.get_lifting_capacity())

            elif additional_command == '3':
                nutrition = input('Введите способ питания животного: ')
                habitat = input('Введите среду обитания животного: ')
                animal = AnimalFactory.create_animal(type_of_animal, name, date_of_birth, birthplace, nutrition,
                                                     habitat)
                age_animal = animal.get_age()
                AnimalRegistry.create_table_mammal()
                AnimalRegistry.writing_to_table_mammal(type_of_animal,
                                                        animal.get_name(),
                                                        animal.get_date_of_birth(),
                                                        age_animal,
                                                        animal.get_birthplace(),
                                                        animal.get_nutrition(),
                                                        animal.get_habitat())
            elif additional_command == '4':
                nutrition = input('Введите способ питания животного: ')
                animal = AnimalFactory.create_animal(type_of_animal, name, date_of_birth, birthplace, nutrition)
                age_animal = animal.get_age()
                AnimalRegistry.create_table_bird()
                AnimalRegistry.writing_to_table_bird(animal.get_type_of_animal(),
                                                     animal.get_name(),
                                                     animal.get_date_of_birth(),
                                                     age_animal,
                                                     animal.get_birthplace(),
                                                     animal.get_nutrition())



main()

