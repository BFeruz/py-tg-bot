from telegram.ext import CallbackContext
from telegram import Update


def start(update: Update, context: CallbackContext):
    user = update.message.from_user

    welcome_msg = f'Assalomu alaykum, {user.full_name}'

    bot = context.bot
    bot.send_message(chat_id=user.id, text=welcome_msg)

def ok(update: Update, context: CallbackContext):
    user = update.message.from_user

    bot = context.bot
    bot.send_message(chat_id=user.id, text='okay')

def echo(update: Update, context: CallbackContext):
    user = update.message.from_user
    message = update.message

    bot = context.bot
    bot.send_message(chat_id=user.id, text=message.text)

def echo_photo(update: Update, context: CallbackContext):
    user = update.message.from_user
    message = update.message

    bot = context.bot
    bot.send_photo(chat_id=user.id, photo=message.photo[-1])
