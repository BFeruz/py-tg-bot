from settings import get_token
from telegram import Bot
import time

TOKEN = get_token()

bot = Bot(TOKEN)

last_update_id = -1

while True:
    curr_update = bot.get_updates()[-1]

    if last_update_id != curr_update.update_id:
        user = curr_update.message.from_user
        message = curr_update.message
        bot.send_message(
            chat_id=user.id,
            text=message.text
        )

        last_update_id = curr_update.update_id

    time.sleep(0.5)
