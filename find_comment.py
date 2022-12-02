import sqlite3

def find_comment(data):
    try:
        sqlite_connection = sqlite3.connect('phone_book.db')
        cursor = sqlite_connection.cursor()
           
        split_select_query = """SELECT name, number_phone, birthday, comment from people INNER JOIN phones ON people.id_people = phones.id_people where comment = ?"""
        cursor.execute(split_select_query, (data, ))
        
        records = cursor.fetchall()
        list_phone = []
        for row in records:
            list_phone.append(row)
        cursor.close()
        return list_phone

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()