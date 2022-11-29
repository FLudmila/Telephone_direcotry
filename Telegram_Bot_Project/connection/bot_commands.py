from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    item = msg.split()
    name = item[1]
    surname = item[2]
    number_phone = item[3]
    await update.message.reply_text(f'{name},{surname},{number_phone}')


# async def read_con(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(f'He {update.effective_user.first_name}')-
#
# async def Delete_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(f'H {update.effective_user.first_name}')
#
# async def write_con(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(f'o {update.effective_user.first_name}')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/add\n/import\n/delet\n/export\n/help')
