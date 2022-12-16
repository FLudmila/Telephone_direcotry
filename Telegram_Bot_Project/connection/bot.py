import telebot
import logging
import os
from telebot import types
import sys

from get_base import get_base
from Telegram_Bot_Project.work.Display_Contacts import Print_contacts
from Telegram_Bot_Project.work.Contact_Processing import Search_cont, Add_contact, Delete_contact, Sort_base_id


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
    global res

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
            contact = bot.send_message(message.chat.id, 'Введите кто будет удалён',
                                       reply_markup=keyboard1)
            bot.register_next_step_handler(contact, Delete_contacts)
        elif message.text == 'Вывод справочника на экран':
            dictionary = base_to_tg_text()
            bot.send_message(message.chat.id, dictionary)
        elif message.text == 'Закончить работу':
            bot.send_message(message.chat.id, "Работа завершена")

    def Delete_contacts(message):
        contact_base = get_base()
        delete_contact = message.text
        contact = []
        for elem in contact_base:
            for i in elem:
                if delete_contact.lower() in i.lower():
                    contact.append(elem)
                    break

        print(len(contact))
        if len(contact) == 1:
            print(contact)
            Delete_contact(contact[0][0])
            bot.send_message(message.chat.id, f'Контакт {contact} удалён')
        elif len(contact) == 0:
            bot.send_message(message.chat.id, 'Такого контакта нет')
        else:
            print(contact)
            res = list_to_tg_text(contact)
            print(res)
            bot.send_message(message.chat.id, f'Найдено несколько контактов, какой ID удалить?\n\n{res}')
            bot.register_next_step_handler(message.text, Delete_contact)

    def Delete_contact(id_from_user):
        new_id = str(id_from_user)
        print(new_id)
        contact_base = get_base()
        contact_base.pop(int(new_id) - 1)
        sorted_contact_base = Sort_base_id(contact_base)
        with open('base.txt', 'w', encoding='utf-8') as base:
            for line in sorted_contact_base:
                for elem in line:
                    base.write(str(elem) + ' ')
                base.write('\n')

    def Contact_search(message):
        contact_base = get_base()
        search_contact = message.text
        contact = []
        for elem in contact_base:
            for i in elem:
                if search_contact.lower() in i.lower():
                    contact.append(elem)
                    break
        res = list_to_tg_text(contact)
        print(res)
        bot.send_message(message.chat.id, res)

    def list_to_tg_text(input_list):
        contacts = ''
        for line in input_list:
            for elem in line:
                contacts = contacts + elem + ' '
            contacts = contacts + '\n'
        return contacts


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
