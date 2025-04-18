import sqlite3
import pandas as pd

# 11.Создать новую таблицу “молодые животные” в которую попадут все
# животные старше 1 года, но младше 3 лет и в отдельном столбце с точностью
# до месяца подсчитать возраст животных в новой таблице
# 12. Объединить все таблицы в одну, при этом сохраняя поля, указывающие на
# прошлую принадлежность к старым таблицам.

# Все остальные задания реализованы в меню (main) посредством вызова функций из AnimalRegistry и AnimalFactory

with sqlite3.connect('Animal_registry.db') as connection:
    # Write the SQL command to select all records from the table
    select_query = ('''
                    SELECT id, type_of_animal, name, date_of_birth, 'bird' AS from_table FROM Bird
                    WHERE age < 3 
                    UNION
                    SELECT id, type_of_animal, name, date_of_birth, 'pack_animal' AS from_table FROM Pack_animal
                    WHERE age < 3
                    UNION
                    SELECT id, type_of_animal, name, date_of_birth, 'pet' AS from_table FROM Pet
                    WHERE age < 3
                    UNION
                    SELECT id, type_of_animal, name, date_of_birth, 'mammal' AS from_table FROM Mammal
                    WHERE age < 3
                    ;
                    ''')
    pd.options.display.max_columns = None
    # Use pandas to read SQL query directly into a DataFrame
    df = pd.read_sql_query(select_query, connection)

print(df)
