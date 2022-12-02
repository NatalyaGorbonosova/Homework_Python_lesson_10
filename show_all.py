import sqlite3

def show_all():
    try:
        sqlite_connection = sqlite3.connect('phone_book.db')
        cursor = sqlite_connection.cursor()
        sqlite_select_query = """SELECT name, number_phone, birthday, comment FROM people INNER JOIN phones ON people.id_people = phones.id_people ORDER BY name"""
        cursor.execute(sqlite_select_query)
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
            

