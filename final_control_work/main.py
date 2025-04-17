from AnimalFactory import AnimalFactory
from AnimalRegistry import AnimalRegistry


def main():
    while True:
        command = input('Введите команду (0 - выход, 1 - запись, 2 - чтение, 3 - обновление, 4 - поиск): ')

        if command == '0':
            break

        elif command == '1':
            type_of_animal = input('Введите название животного (например, "Собака", "Кошка", "Курица" и пр.): ').lower()
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
        elif command == '2':
            additional_command = input('Введите команду для просмотра таблицы: 1 - домашние питомцы, '
                                       '2 - вьючные животные, '
                                       '3 - млекопитающие, '
                                       '4 - птицы ')
            if additional_command == '1':
                AnimalRegistry.reading_table('Pet')
            elif additional_command == '2':
                AnimalRegistry.reading_table('Pack_animal')
            elif additional_command == '3':
                AnimalRegistry.reading_table('Mammal')
            else:
                AnimalRegistry.reading_table('Bird')

        elif command == '3':
            additional_command = input('Введите команду для обновления таблицы: 1 - домашние питомцы, '
                                       '2 - вьючные животные, '
                                       '3 - млекопитающие, '
                                       '4 - птицы ')

            if additional_command == '1':
                AnimalRegistry.reading_table('Pet')
                AnimalRegistry.reading_table('Pet_commands')
                additional_command = input('Введите название таблицы, с которой хотите работать: ')
                if additional_command == 'Pet':
                    update_animal = int(input('Введите id строки, которую хотите обновить: '))
                    column_update = input('Введите название столбца, который хотите обновить: ')
                    if column_update == 'age':
                        new_value = int(input('Введите возраст: '))
                        AnimalRegistry.update_table('Pet', update_animal, column_update, new_value)
                    else:
                        new_value = input('Введите новое значение: ')
                        AnimalRegistry.update_table('Pet', update_animal, column_update, new_value)
                    AnimalRegistry.reading_table('Pet')
                elif additional_command == 'Pet_commands':
                    pet_id = int(input('Введите id питомца, которому хотите добавить новую команду: '))
                    command_pet = input('Введите название команды: ')
                    AnimalRegistry.writing_to_table_pet_commands(command_pet, pet_id)

            elif additional_command == '2':
                AnimalRegistry.reading_table('Pack_animal')
                update_animal = int(input('Введите id строки, которую хотите обновить: '))
                column_update = input('Введите название столбца, который хотите обновить: ')
                if column_update == 'age':
                    new_value = int(input('Введите возраст: '))
                    AnimalRegistry.update_table('Pack_animal', update_animal, column_update, new_value)
                else:
                    new_value = input('Введите новое значение: ')
                    AnimalRegistry.update_table('Pack_animal', update_animal, column_update, new_value)
                AnimalRegistry.reading_table('Pack_animal')

            elif additional_command == '3':
                AnimalRegistry.reading_table('Mammal')
                update_animal = int(input('Введите id строки, которую хотите обновить: '))
                column_update = input('Введите название столбца, который хотите обновить: ')
                if column_update == 'age':
                    new_value = int(input('Введите возраст: '))
                    AnimalRegistry.update_table('Mammal', update_animal, column_update, new_value)
                else:
                    new_value = input('Введите новое значение: ')
                    AnimalRegistry.update_table('Mammal', update_animal, column_update, new_value)
                AnimalRegistry.reading_table('Mammal')

            else:
                AnimalRegistry.reading_table('Bird')
                update_animal = int(input('Введите id строки, которую хотите обновить: '))
                column_update = input('Введите название столбца, который хотите обновить: ')
                if column_update == 'age':
                    new_value = int(input('Введите возраст: '))
                    AnimalRegistry.update_table('Bird', update_animal, column_update, new_value)
                else:
                    new_value = input('Введите новое значение: ')
                    AnimalRegistry.update_table('Bird', update_animal, column_update, new_value)
                AnimalRegistry.reading_table('Bird')

        elif command == '4':
            additional_command = input('В какой таблице осуществлять поиск? 1 - домашние питомцы, '
                                       '2 - вьючные животные, '
                                       '3 - млекопитающие, '
                                       '4 - птицы ')

            if additional_command == '1':
                AnimalRegistry.reading_table('Pet')
                column_search = input('По какому стобцу осуществлять поиск? ')
                search_value = input('Введите искомое значение: ')
                AnimalRegistry.search_in_table('Pet', column_search, search_value)

            elif additional_command == '2':
                AnimalRegistry.reading_table('Pack_animal')
                column_search = input('По какому стобцу осуществлять поиск? ')
                search_value = input('Введите искомое значение: ')
                AnimalRegistry.search_in_table('Pack_animal', column_search, search_value)

            elif additional_command == '3':
                AnimalRegistry.reading_table('Mammal')
                column_search = input('По какому стобцу осуществлять поиск? ')
                search_value = input('Введите искомое значение: ')
                AnimalRegistry.search_in_table('Mammal', column_search, search_value)

            elif additional_command == '4':
                AnimalRegistry.reading_table('Bird')
                column_search = input('По какому стобцу осуществлять поиск? ')
                search_value = input('Введите искомое значение: ')
                AnimalRegistry.search_in_table('Bird', column_search, search_value)



main()

