import telebot
import logging
from telebot import types
import sys
from Telegram_Bot_Project.work.Display_Contacts import Print_contacts
from Telegram_Bot_Project.work.Contact_Processing import Search_cont, Add_contact, Delete_contact

sys.path.append('Telegram_Bot_Project\work')


def tg_bot():
    # API_TOKEN = '5943741465:AAEfm9wHXbsoZnexiRpbJlrjbMwakXsDBL4'
    API_TOKEN = '5765171209:AAE9j_s90u8L9IUxhK4EukyEuI0nHM04o3A'

    bot = telebot.TeleBot(API_TOKEN)

    keyboard1 = telebot.types.ReplyKeyboardMarkup()
    keyboard1.row('Добавить контакт', 'Найти контакт', 'Удалить контакт')
    keyboard1.row('Добавить контакты из файла', 'Запись справочника в файл')
    keyboard1.row('Вывод справочника на экран', 'Закончить работу')

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text == 'Добавить контакт':
            contact = bot.send_message(message.chat.id, 'Введите строку в формате\n"ИМЯ ФАМИЛИЯ ТЕЛЕФОН ОПИСАНИЕ":',
                                       reply_markup=keyboard1)
            bot.register_next_step_handler(contact, add_contact_to_base)
        elif message.text == 'Найти контакт':
            source_Messege = bot.send_message(message.chat.id, 'Что хотим найти?', reply_markup=keyboard1)
            bot.register_next_step_handler(source_Messege, Search_cont)
            bot.send_message(message.chat.id, Search_cont())
            # bot.send_message(message.chat.id,' Контакт')
            # bot.send_message(message.from_user.id,f' Контакт{name},{surname},{number_phone},{info}')
        elif message.text == 'Удалить контакт':
            bot.send_message(message.chat.id, "Напиши привет")
        elif message.text == 'Вывод справочника на экран':
            bot.send_message(message.chat.id, f'Вывод телонного справочника{Print_contacts()}')
        elif message.text == 'Закончить работу':
            pass  # Print_contacts(base)

    def add_contact_to_base(string):
        base = []
        contact = string.text.split()
        contact.insert(0, len(base) + 1)
        base.append(contact)
        file = open('file_name.txt', 'a', encoding='utf-8')
        for contact in base:
            for elem in contact:
                file.write(str(elem))
                file.write('\n')
            file.close()
        return base


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

        # bot.send_message(message.chat.id, message.text)
        # def get_text_messages(message):
        #     f=open('db.txt', 'a')
        #     f.write(message.text)
        #     f.close

        # surname = bot.send_message(message.chat.id, 'Введите фамилию:')
        # number = bot.send_message(message.chat.id, 'Введите телефон:')
        # elif message.text == 'Пока':
        #     bot.send_message(message.chat.id, 'Прощай, создатель')

    bot.infinity_polling()
