import telebot
import logging
import os
from telebot import types
import sys

from get_base import get_base
=======
from Telegram_Bot_Project.work.Display_Contacts import Print_contacts
from Telegram_Bot_Project.work.Contact_Processing import Search_cont, Add_contact, Delete_contact
from get_base import get_base


sys.path.append('Telegram_Bot_Project\work')


def tg_bot():
    # API_TOKEN = '5943741465:AAEfm9wHXbsoZnexiRpbJlrjbMwakXsDBL4'
    API_TOKEN = '5765171209:AAE9j_s90u8L9IUxhK4EukyEuI0nHM04o3A'

    bot = telebot.TeleBot(API_TOKEN)

    keyboard1 = telebot.types.ReplyKeyboardMarkup()
    keyboard1.row('Добавить контакт', 'Найти контакт', 'Удалить контакт')
    keyboard1.row('Добавить контакты из файла', 'Запись справочника в файл')
    keyboard1.row('Вывод справочника на экран', 'Закончить работу')

    base = []

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text == 'Добавить контакт':
            contact = bot.send_message(message.chat.id, 'Введите строку в формате\n"ИМЯ ФАМИЛИЯ ТЕЛЕФОН ОПИСАНИЕ":',
                                       reply_markup=keyboard1)
            bot.register_next_step_handler(contact, add_contact_to_base)


        elif message.text == 'Найти контакт':
            contact = bot.send_message(message.chat.id, 'Введите кого надо найти',
                                       reply_markup=keyboard1)
            bot.register_next_step_handler(contact, Contact_search)

        elif message.text == 'Удалить контакт':
            bot.send_message(message.chat.id, "Напиши привет")


        elif message.text == 'Вывод справочника на экран':
            dictionary = base_to_tg_text()
            bot.send_message(message.chat.id, dictionary)



        elif message.text == 'Закончить работу':
            bot.send_message(message.chat.id, "Работа завершена")

    def Contact_search(messageChat):
        contact_base = get_base()
        search_contact = messageChat.text
        contacT = []
        for elem in contact_base:
            for i in elem:
                if i == search_contact:
                    contacT.append(elem)
        return contacT


        elif message.text == 'Закончить работу':
            pass  # Print_contacts(base)


    def base_to_tg_text():
        contacts = ''
        if os.stat('base.txt').st_size == 0:
            contacts = 'Ваша база пуста'
            return contacts
        else:
            with open('base.txt', 'r', encoding='utf-8') as base:
                while True:
                    line = base.readline().rstrip()
                    if not line:
                        break
                    contacts = contacts + line + '\n'
            return contacts


    def add_contact_to_base(message):
        base = get_base()
        contact = message.text.split()


    def add_contact_to_base(string):
        base = get_base()
        contact = string.text.split()

        contact.insert(0, len(base) + 1)
        base.append(contact)
        file = open('base.txt', 'a', encoding='utf-8')
        for elem in contact:
            file.write(str(elem))
            file.write(' ')
        file.write('\n')
        file.close()



    def Print_contacts():
         Base = []
         read_file = open('file_name.txt', 'r')
         for line in read_file:
            Base.append(line).split()
            read_file.close()
            return Base
        #
        # @bot.message_handler(content_types=['text'])
        # def Search_cont(base):
        #     contacts = add_contact_to_base()
        #     name = contacts[1]
        #     surname = contacts[2]
        #     number_phone = contacts[3]
        #     info = contacts[4]
        #     bot.send_message(contacts.chat.id,f' Контакт{name},{surname},{number_phone},{info}')
        #
        #       return base

        # def Search_cont(contacts):
        #     base = []
        #     for items in contacts:
        #          base.append(items)
        #
        #      return base



        # def add_logging():
        #  logging.basicConfig(
        #     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        #     level=logging.INFO
        # )

    bot.infinity_polling()
