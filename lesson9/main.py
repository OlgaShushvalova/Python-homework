from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = Bot(token='5609667013:AAE7l8TwHbAK2FPCPvcSLww8ll8i5-Olj5A')
updater = Updater(token='5609667013:AAE7l8TwHbAK2FPCPvcSLww8ll8i5-Olj5A')
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id,
                             'Привет, \n Напиши текст, из которого нужно удалить слова, содержащие "абв"')


def del_some_words(update, context):
    text = update.message.text.split()
    list = []
    for elem in text:
        if 'абв' not in elem:
            list.append(elem)
        context.bot.send_message(
            update.effective_chat.id, ' '.join(list))


start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text, del_some_words)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)


updater.start_polling()
updater.idle()
