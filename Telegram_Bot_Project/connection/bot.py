# from bot_commands import *

# app = ApplicationBuilder().token("5765171209:AAE9j_s90u8L9IUxhK4EukyEuI0nHM04o3A").build()

# app.add_handler(CommandHandler("add", add))
# # app.add_handler(CommandHandler("import", read_con))
# # app.add_handler(CommandHandler("delet", Delete_contact))
# # app.add_handler(CommandHandler("export", write_con))
# app.add_handler(CommandHandler("help", help))
# print("Server start")

# app.run_polling()
# print('Server stoped')

import telebot
from telebot import types

def tg_bot():
    API_TOKEN = '5943741465:AAEfm9wHXbsoZnexiRpbJlrjbMwakXsDBL4'

    bot = telebot.TeleBot(API_TOKEN)

    keyboard1 = telebot.types.ReplyKeyboardMarkup()
    keyboard1.row('Добавить контакт', 'Найти контакт', 'Удалить контакт')
    keyboard1.row('Добавить контакты из файла', 'Запись справочника в файл')
    keyboard1.row('Вывод справочника на экран')

    @bot.message_handler(commands = ['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text == 'Добавить контакт':
            name = bot.send_message(message.chat.id, 'Введите имя:')
            bot.register_next_step_handler(name, test)
    
    def test(message):
        print(message.text)
        bot.send_message(message.chat.id, message.text)
            # def get_text_messages(message):
            #     f=open('db.txt', 'a')
            #     f.write(message.text)
            #     f.close

            # surname = bot.send_message(message.chat.id, 'Введите фамилию:')
            # number = bot.send_message(message.chat.id, 'Введите телефон:')
        # elif message.text == 'Пока':
        #     bot.send_message(message.chat.id, 'Прощай, создатель')

    bot.infinity_polling()