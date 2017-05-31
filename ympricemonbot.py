import logging
import time
from telegram.ext import Updater, CommandHandler

from ymparser import parse_ym

token = '383016959:AAF491dge5g5Fm7bRrnz2gFn-uACyUBK2dY'


def start(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Monitoring GTX1070 for price <= 24500 every 20 minutes"
    )
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Current prices:\n%s" % '\n'.join(str(p) for p in parse_ym())
    )

    while True:
        prices = list(parse_ym())
        if prices[0] <= 24500:
            bot.send_message(chat_id=update.message.chat_id, text="Gotcha!")
        time.sleep(20 * 60)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    updater = Updater(token=token)
    start_handler = CommandHandler('start', start)
    updater.dispatcher.add_handler(start_handler)
    updater.start_polling()
