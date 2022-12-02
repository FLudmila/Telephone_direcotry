import telebot
from telebot import types
import sys
sys.path.append('Telegram_Bot_Project\work')
from Display_Contacts import Print_contacts


def tg_bot():
    API_TOKEN = '5943741465:AAEfm9wHXbsoZnexiRpbJlrjbMwakXsDBL4'

    bot = telebot.TeleBot(API_TOKEN)

    keyboard1 = telebot.types.ReplyKeyboardMarkup()
    keyboard1.row('Добавить контакт', 'Найти контакт', 'Удалить контакт')
    keyboard1.row('Добавить контакты из файла', 'Запись справочника в файл')
    keyboard1.row('Вывод справочника на экран', 'Закончить работу')

    base = []
    @bot.message_handler(commands = ['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text == 'Добавить контакт':
            contact = bot.send_message(message.chat.id, 'Введите строку в формате\n"ИМЯ ФАМИЛИЯ ТЕЛЕФОН ОПИСАНИЕ":', reply_markup=keyboard1)
            bot.register_next_step_handler(contact, add_contact_to_base)
        elif message.text == 'Закончить работу':
            Print_contacts(base)

    def add_contact_to_base(string):
        contact = string.text.split()
        contact.insert(0, len(base) + 1)
        print(contact)
        base.append(contact)
        return base

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