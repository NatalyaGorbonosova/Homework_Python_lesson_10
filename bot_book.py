import telebot
import re
import logger as lg
import show_all as sa
import find_name as fn
import find_comment as fc
import find_phone as fp
import delete as dl
import add_contact as ac

API_TOKEN = '5754862285:AAF1AEqLUxqmn1w1tQfEVRNg3Rt6q1T9pVM'

bot = telebot.TeleBot(API_TOKEN)

                # Формирует строку на вывод в чат
def for_print(list):
    str = ''
    for row in list:
        for e in row: str += e.center(10, ' ') + ' | '
        str += f'\n'
    return str

                # Начало работы
@bot.message_handler(commands=['start'])
def start_message(message):
    lg.log(message)
    mess = f'Привет, {message.from_user.first_name}! \n Готов к работе! Чтобы узнать возможности вызовите команду /help'
    bot.send_message(message.chat.id, mess)
                # Список команд
@bot.message_handler(commands=['help'])
def show_help(message):
    lg.log(message)
    mess_list = ['/all - показывает весь список контактов', 
                '/find_nam "Имя контакта" - найти контакт по имени',
                '/find_comment "Название группы (семья, друзья, работа)" - все контакты выбранной группы',
                '/find_phone "Номер телефона" - найти контакт по номеру телефона',
                '/delete "Имя контакта" - удаляет контакт с данным имененм',
                '/add name; phone; birthday; group - добавляет контакт с введенными данными именно в этом порядке и через ";"']
    mess = ''
    for el in mess_list:
        mess += f'{el} \n'
    bot.send_message(message.chat.id, mess)               
                # Показывает весь список контактов
@bot.message_handler(commands=['all'])
def show_all(message):
    lg.log(message)
    mess = for_print(sa.show_all())
    bot.send_message(message.chat.id, mess)
                # Ищет по имени в БД выводит на экран все данные контакта
@bot.message_handler(commands=['find_name'])
def find_name(message):
    lg.log(message)
    mess_list = message.text.split()[1:]
    mess = ' '.join(mess_list)
    mess_answer = for_print(fn.find_name(mess))
    bot.send_message(message.chat.id, mess_answer)
                # Выводит на экран все контаткты группы
@bot.message_handler(commands=['find_comment'])
def find_comment(message):
    lg.log(message)
    mess_list = message.text.split()[1:]
    mess = ' '.join(mess_list)
    mess_answer = for_print(fc.find_comment(mess))
    bot.send_message(message.chat.id, mess_answer)
                # Ищет данные по номеру телефона
@bot.message_handler(commands=['find_phone'])
def find_phone(message):
    lg.log(message)
    mess_list = message.text.split()[1:]
    mess = ' '.join(mess_list)
    mess_answer = for_print(fp.find_phone(mess))
    bot.send_message(message.chat.id, mess_answer)
                # Удаление контакта по имени
@bot.message_handler(commands=['delete'])
def delete(message):
    lg.log(message)
    mess_list = message.text.split()[1:]
    mess = ' '.join(mess_list)
    dl.delete_contact(mess)
    bot.send_message(message.chat.id, 'Контакт удален. Можете проверить список контактов')
                # Добавление контакта
@bot.message_handler(commands=['add'])
def add_contact(message):
    lg.log(message)
    mess_list = message.text.split()[1:]
    mess = ''.join(mess_list)
    list_info = mess.split(';')
    if len(list_info) == 4:
        ac.add_contact(list_info)
        bot.send_message(message.chat.id, f'Контакт {list_info} добавлен, для просмотра введите команду /all')
    else: bot.send_message(message.chat.id, 'Что-то пошло не так')

bot.polling()