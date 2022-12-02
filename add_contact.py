import sqlite3

def add_contact(list):
    try:
        sqlite_connection = sqlite3.connect('phone_book.db')
        cursor = sqlite_connection.cursor()
           
        sqlite_insert_with_param = """INSERT INTO people
                              (name, birthday, comment)
                              VALUES (?, ?, ?);"""

        data_tuple = (list[0], list[2], list[3])
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqlite_connection.commit()

        split_select_query = """SELECT id_people from people where name = ?"""
        cursor.execute(split_select_query, (list[0], ))
        records = cursor.fetchall()
        id = records[0][0]

        sqlite_insert_with_param = """INSERT INTO phones
                              (id_people, number_phone)
                              VALUES (?, ?);"""

        data_tuple = (id, list[1])
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqlite_connection.commit()

        cursor.close()
 
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        
    finally:
        if sqlite_connection:
            sqlite_connection.close()
