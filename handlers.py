from telegram.ext import CallbackContext
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def start(update: Update, context: CallbackContext):
    user = update.message.from_user

    welcome_msg = f'Assalomu alaykum, {user.full_name}'
    update.message.reply_text(text=welcome_msg)

def ok(update: Update, context: CallbackContext):
    user = update.message.from_user

    bot = context.bot
    bot.send_message(
        chat_id=user.id, text='okay',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(
                        text='btn1',
                        request_contact=True
                    ),
                    KeyboardButton(
                        text='btn2',
                        request_location=True
                    )
                ]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )

def echo(update: Update, context: CallbackContext):
    user = update.message.from_user
    message = update.message

    bot = context.bot
    bot.send_message(
        chat_id=user.id, text=message.text,
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text='google',
                        url='http://google.com'
                    ),
                    InlineKeyboardButton(
                        text='some',
                        callback_data='some'
                    )
                ]
            ]
        )
    )

def echo_photo(update: Update, context: CallbackContext):
    user = update.message.from_user
    message = update.message

