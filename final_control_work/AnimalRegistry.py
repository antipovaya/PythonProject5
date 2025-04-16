import sqlite3


class AnimalRegistry:

    @staticmethod
    def create_table_mammal():
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

    # class PackAnimal(Pet):
    #     def __init__(self, type_of_animal, name, date_of_birth, birthplace, breed, lifting_capacity):
    #         super().__init__(type_of_animal, name, date_of_birth, birthplace, breed)
    #         self.lifting_capacity = lifting_capacity  # грузоподъемность вьючного животного
    @staticmethod
    def create_table_pack_animal():
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
        with sqlite3.connect('Animal_registry.db') as connection:
            cursor = connection.cursor()

            # Insert a record into the Pet table
            insert_query = '''
            INSERT INTO Pet (type_of_animal, name, date_of_birth, age, birthplace, breed, lifting_capacity) 
            VALUES (?, ?, ?, ?, ?, ?, ?);
            '''
            pet_data = (type_of_animal, name, date_of_birth, age, birthplace, breed, lifting_capacity)

            cursor.execute(insert_query, pet_data)

            # Commit the changes automatically
            connection.commit()

            # No need to call connection.close(); it's done automatically!
            print("Запись создана")