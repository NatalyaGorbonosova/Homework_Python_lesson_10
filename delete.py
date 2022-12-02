import sqlite3

def delete_contact(data):
    try:
        sqlite_connection = sqlite3.connect('phone_book.db')
        cursor = sqlite_connection.cursor()
           
        split_select_query = """SELECT id_people from people where name = ?"""
        cursor.execute(split_select_query, (data, ))
        records = cursor.fetchall()
        id = records[0][0]
        
        split_select_query = """DELETE from people where id_people = ?"""
        cursor.execute(split_select_query, (id, ))
        sqlite_connection.commit()

        split_select_query = """DELETE from phones where id_people = ?"""
        cursor.execute(split_select_query, (id, ))
        sqlite_connection.commit()

        cursor.close()
 
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        
    finally:
        if sqlite_connection:
            sqlite_connection.close()
