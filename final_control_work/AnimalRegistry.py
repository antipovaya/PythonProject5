import sqlite3
import pandas as pd

class AnimalRegistry:
    """Класс для ведения реестра животных питомника."""
    @staticmethod
    def create_table_mammal():
        """
        Создает базу данных и таблицу Mammal, если они отсутствуют.
        """
        with sqlite3.connect('Animal_registry.db') as connection:
            # Create a cursor object
            cursor = connection.cursor()

            # Write the SQL command to create the Mammal table
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS Mammal (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type_of_animal TEXT NOT NULL,
                name TEXT NOT NULL,
                date_of_birth TEXT NOT NULL,
                age INTEGER,
                birthplace TEXT NOT NULL,
                nutrition TEXT,
                habitat TEXT
            );
            '''

            # Execute the SQL command
            cursor.execute(create_table_query)

            # Commit the changes
            connection.commit()

            # Print a confirmation message
            print("Таблица 'Mammal' создана!")

    @staticmethod
    def writing_to_table_mammal(type_of_animal, name, date_of_birth, age, birthplace, nutrition, habitat):
        """
        Записывает строку в таблицу Mammal.
        :param type_of_animal: Название типа животного
        :param name: Имя животного
        :param date_of_birth: Дата рождения животного
        :param age: Возраст животного
        :param birthplace: Место рождения животного (страна)
        :param nutrition: Тип питания животного (хищник, травоядный, смешанный)
        :param habitat: Среда обитания животного (наземный, наземно-древесный, водный, полуводный, летающий)
        :return: Запись строки в соответстующей таблице
        """
        with sqlite3.connect('Animal_registry.db') as connection:
            cursor = connection.cursor()

            # Insert a record into the Mammal table
            insert_query = '''
            INSERT INTO Mammal (type_of_animal, name, date_of_birth, age, birthplace, nutrition, habitat) 
            VALUES (?, ?, ?, ?, ?, ?, ?);
            '''
            mammal_data = (type_of_animal, name, date_of_birth, age, birthplace, nutrition, habitat)

            cursor.execute(insert_query, mammal_data)

            # Commit the changes automatically
            connection.commit()

            # No need to call connection.close(); it's done automatically!
            print("Запись создана")

    @staticmethod
    def create_table_bird():
        """
        Создает базу данных и таблицу Bird, если они отсутствуют.
        """
        with sqlite3.connect('Animal_registry.db') as connection:
            # Create a cursor object
            cursor = connection.cursor()

            # Write the SQL command to create the Bird table
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS Bird (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type_of_animal TEXT NOT NULL,
                name TEXT NOT NULL,
                date_of_birth TEXT NOT NULL,
                age INTEGER,
                birthplace TEXT NOT NULL,
                nutrition TEXT
            );
            '''

            # Execute the SQL command
            cursor.execute(create_table_query)

            # Commit the changes
            connection.commit()

            # Print a confirmation message
            print("Таблица 'Bird' создана!")

    @staticmethod
    def writing_to_table_bird(type_of_animal, name, date_of_birth, age, birthplace, nutrition):
        """
        Записывает строку в таблицу Bird.
        :param type_of_animal: Название типа животного
        :param name: Имя животного
        :param date_of_birth: Дата рождения животного
        :param age: Возраст животного
        :param birthplace: Место рождения животного (страна)
        :param nutrition: Тип питания животного (хищник, растительноядный, насекомоядный)
        :return: Запись строки в соответстующей таблице
        """
        with sqlite3.connect('Animal_registry.db') as connection:
            cursor = connection.cursor()

            # Insert a record into the Bird table
            insert_query = '''
            INSERT INTO Bird (type_of_animal, name, date_of_birth, age, birthplace, nutrition) 
            VALUES (?, ?, ?, ?, ?, ?);
            '''
            bird_data = (type_of_animal, name, date_of_birth, age, birthplace, nutrition)

            cursor.execute(insert_query, bird_data)

            # Commit the changes automatically
            connection.commit()

            # No need to call connection.close(); it's done automatically!
            print("Запись создана")

    @staticmethod
    def create_table_pet():
        """
        Создает базу данных и таблицу Pet, если они отсутствуют.
        """
        with sqlite3.connect('Animal_registry.db') as connection:
            # Create a cursor object
            cursor = connection.cursor()

            # Write the SQL command to create the Pet table
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS Pet (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type_of_animal TEXT NOT NULL,
                name TEXT NOT NULL,
                date_of_birth TEXT NOT NULL,
                age INTEGER,
                birthplace TEXT NOT NULL,
                breed TEXT
            );
            '''

            # Execute the SQL command
            cursor.execute(create_table_query)

            # Commit the changes
            connection.commit()

            # Print a confirmation message
            print("Таблица 'Pet' создана!")

    @staticmethod
    def writing_to_table_pet(type_of_animal, name, date_of_birth, age, birthplace, breed):
        """
        Записывает строку в таблицу Pet.
        :param type_of_animal: Название типа животного
        :param name: Имя животного
        :param date_of_birth: Дата рождения животного
        :param age: Возраст животного
        :param birthplace: Место рождения животного (страна)
        :param breed: Порода животного
        :return: Запись строки в соответстующей таблице
        """
        with sqlite3.connect('Animal_registry.db') as connection:
            cursor = connection.cursor()

            # Insert a record into the Pet table
            insert_query = '''
            INSERT INTO Pet (type_of_animal, name, date_of_birth, age, birthplace, breed) 
            VALUES (?, ?, ?, ?, ?, ?);
            '''
            pet_data = (type_of_animal, name, date_of_birth, age, birthplace, breed)

            cursor.execute(insert_query, pet_data)

            # Commit the changes automatically
            connection.commit()

            # No need to call connection.close(); it's done automatically!
            print("Запись создана")

    @staticmethod
    def create_table_pet_commands():
        with sqlite3.connect('Animal_registry.db') as connection:
            # Create a cursor object
            cursor = connection.cursor()

            # Write the SQL command to create the Pet_commands table
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS Pet_commands (
                id INTEGER FOREIGN KEY (PetId) REFERENCES Pet (id),
                command TEXT NOT NULL
            );
            '''

            # Execute the SQL command
            cursor.execute(create_table_query)

            # Commit the changes
            connection.commit()

            # Print a confirmation message
            print("Таблица 'Pet_commands' создана!")

    @staticmethod
    def writing_to_table_pet_commands(command):
        with sqlite3.connect('Animal_registry.db') as connection:
            cursor = connection.cursor()

            # Insert a record into the Pet table
            insert_query = '''
            INSERT INTO Pet (command) 
            VALUES (?);
            '''
            pet_data = command

            cursor.execute(insert_query, pet_data)

            # Commit the changes automatically
            connection.commit()

            # No need to call connection.close(); it's done automatically!
            print("Запись создана")


    @staticmethod
    def create_table_pack_animal():
        """
        Создает базу данных и таблицу Pack_animal, если они отсутствуют.
        """
        with sqlite3.connect('Animal_registry.db') as connection:
            # Create a cursor object
            cursor = connection.cursor()

            # Write the SQL command to create the Pack_animal table
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS Pack_animal (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type_of_animal TEXT NOT NULL,
                name TEXT NOT NULL,
                date_of_birth TEXT NOT NULL,
                age INTEGER,
                birthplace TEXT NOT NULL,
                breed TEXT,
                lifting_capacity INTEGER
            );
            '''

            # Execute the SQL command
            cursor.execute(create_table_query)

            # Commit the changes
            connection.commit()

            # Print a confirmation message
            print("Таблица 'Pack_animal' создана!")

    @staticmethod
    def writing_to_table_pack_animal(type_of_animal, name, date_of_birth, age, birthplace, breed, lifting_capacity):
        """
        Записывает строку в таблицу Pack_animal.
        :param type_of_animal: Название типа животного
        :param name: Имя животного
        :param date_of_birth: Дата рождения животного
        :param age: Возраст животного
        :param birthplace: Место рождения животного (страна)
        :param breed: Порода животного
        :param lifting_capacity: Грузоподъемность вьючного животного
        :return: Запись строки в соответстующей таблице
        """
        with sqlite3.connect('Animal_registry.db') as connection:
            cursor = connection.cursor()

            # Insert a record into the Pack_animal table
            insert_query = '''
            INSERT INTO Pack_animal (type_of_animal, name, date_of_birth, age, birthplace, breed, lifting_capacity) 
            VALUES (?, ?, ?, ?, ?, ?, ?);
            '''
            pack_animal_data = (type_of_animal, name, date_of_birth, age, birthplace, breed, lifting_capacity)

            cursor.execute(insert_query, pack_animal_data)

            # Commit the changes automatically
            connection.commit()

            # No need to call connection.close(); it's done automatically!
            print("Запись создана")

    @staticmethod
    def reading_table(name_table):
        """
        Чтение таблицы.
        :param name_table: Имя таблицы
        """
        with sqlite3.connect('Animal_registry.db') as connection:
            # Write the SQL command to select all records from the table
            select_query = f"SELECT * FROM {name_table};"

            # Use pandas to read SQL query directly into a DataFrame
            df = pd.read_sql_query(select_query, connection)

        # Display the DataFrame
        print(f"Животные в таблице {name_table}")
        print(df)

    @staticmethod
    def update_table(name_table, update_animal_id, column_update, new_value):
        """
        Чтение таблицы.
        :param name_table: Имя таблицы
        :param update_animal_id: id животного в базе
        :param column_update: Название атрибута, который хотим изменить
        :param new_value: Новое значение
        """
        with sqlite3.connect('Animal_registry.db') as connection:
            cursor = connection.cursor()

            # SQL command to update
            update_query = f'''
            UPDATE {name_table} 
            SET {column_update} = ? 
            WHERE id = ?;
            '''

            # Data for the update
            new_val = new_value
            id_animal = update_animal_id

            # Execute the SQL command with the data
            cursor.execute(update_query, (new_val, id_animal))

            # Commit the changes to save the update
            connection.commit()

            # Print a confirmation message
            print(f"Значение {column_update} строки с id {update_animal_id} было изменено на {new_val}.")
