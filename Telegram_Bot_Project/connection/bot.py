from bot_commands import *

app = ApplicationBuilder().token("5765171209:AAE9j_s90u8L9IUxhK4EukyEuI0nHM04o3A").build()

app.add_handler(CommandHandler("add", add))
# app.add_handler(CommandHandler("import", read_con))
# app.add_handler(CommandHandler("delet", Delete_contact))
# app.add_handler(CommandHandler("export", write_con))
app.add_handler(CommandHandler("help", help))
print("Server start")

app.run_polling()
print('Server stoped')