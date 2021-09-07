from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from algorithm import ask
from dotenv import load_dotenv
import logging 
import os
import sys

def setup():
    load_dotenv()
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
    return { 'token': os.environ['TOKEN'] }

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Selamat datang di Tanyahukum(dev)!')
    context.bot.send_message(chat_id=update.effective_chat.id, text='Silahkan bertanya :)')

def answer(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=ask(update.message.text))


def main():
    TOKEN = setup()['token']
    if TOKEN is None:
        sys.exit('token not provided')
    updater = Updater(token=TOKEN, use_context=True)
    start_handler = CommandHandler('start', start)
    answer_handler = MessageHandler(Filters.text & (~Filters.command), answer)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(answer_handler)
    updater.start_polling()

if __name__ == '__main__':
    main()