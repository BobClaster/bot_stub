from telegram.ext import Updater, MessageHandler, Filters
import settings
import logging

updater = Updater(token=settings.BOT_TOKEN)
dispatcher = updater.dispatcher


def reply_message(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text=settings.MESSAGE, parse_mode="HTML")


reply_message_hand = MessageHandler(Filters.all, reply_message)
dispatcher.add_handler(reply_message_hand)


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


dispatcher.add_error_handler(error)

updater.start_polling()
updater.idle()