from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from algorithm import ask
from dotenv import load_dotenv
import logging 
import os
import sys

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger(__name__)

def setup():
    load_dotenv()
    try:
        config = { 'token': os.environ['TOKEN'], 'port': int(os.environ.get('PORT', 5000)) }
        logger.info('Token ditemukan!')
        return config
    except KeyError:
        logger.warning('Token tidak ditemukan!')
        sys.exit()

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Selamat datang di Tanyahukum(dev)!')

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Untuk mencari, kirim kata kunci atau pertanyaan')

def answer(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=ask(update.message.text))

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    config = setup()
    TOKEN = config['token']
    PORT = config['port']

    updater = Updater(token=TOKEN, use_context=True)
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    answer_handler = MessageHandler(Filters.text & (~Filters.command), answer)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(answer_handler)

    dispatcher.add_error_handler(error)

    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN,
                          webhook_url='https://tanyahukumbotsrv.herokuapp.com/' + TOKEN)
    
    updater.idle()

if __name__ == '__main__':
    main()