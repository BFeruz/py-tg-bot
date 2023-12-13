from settings import get_token
from telegram.ext import (
    Updater, 
    CommandHandler,
    MessageHandler,
    Filters,
)
from handlers import (
    start,
    echo,
    ok,
    echo_photo,
)


def main():
    try:
        TOKEN = get_token()
    except ValueError:
        print('400')
        return
    
    # create udpater obj
    updater = Updater(TOKEN)
    
    # create dispatcher obj
    dispatcher = updater.dispatcher
    
    # add command handlers
    dispatcher.add_handler(
        handler=CommandHandler(
            command=['start', 'boshlash'],
            callback=start
        )
    )
    
    # add message handlers
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text('ok'),
            callback=ok
        )
    )
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text,
            callback=echo
        )
    )
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.photo,
            callback=echo_photo
        )
    )

    # start polling
    updater.start_polling()
    updater.idle()

main()
