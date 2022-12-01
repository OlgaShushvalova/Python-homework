from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

bot = Bot(token='')
updater = Updater(token='')
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id,
                             'Привет, \n напиши выражение')
    get_id_user(update.effective_chat.id)


id_user = None
input_data = None
result = None


def get_id_user(id):
    global id_user
    id_user = id


def get_input_data(data):
    global input_data
    input_data = data


def get_result(res):
    global result
    result = res


def operations_data(update, context):
    data = update.message.text
    get_input_data(data)
    list_data = parse_data(data)
    result = calculate(list_data)
    get_result(result)
    save_log()
    context.bot.send_message(update.effective_chat.id, f'Результат: {result}')


def parse_data(data):
    s = data
    result = []
    digit = ""
    for symbol in s:
        if symbol.isdigit():
            digit += symbol
        else:
            result.append(int(digit))
            digit = ""
            result.append(symbol)
    else:
        if digit:
            result.append(int(digit))
    return result


def calculate(lst):
    result = 0
    for s in lst:
        if s == '*' or s == '/':
            if s == '*':
                index = lst.index(s)
                result = lst[index - 1] * lst[index + 1]
                lst = lst[:index - 1] + [result] + lst[index + 2:]
            else:
                index = lst.index(s)
                result = lst[index - 1] / lst[index + 1]
                lst = lst[:index - 1] + [result] + lst[index + 2:]
    for s in lst:
        if s == '+' or s == '-':
            if s == '+':
                index = lst.index(s)
                result = lst[index - 1] + lst[index + 1]
                lst = lst[:index - 1] + [result] + lst[index + 2:]
            else:
                index = lst.index(s)
                result = lst[index - 1] - lst[index + 1]
                lst = lst[:index - 1] + [result] + lst[index + 2:]
    return result


def save_log():
    with open('data_file.txt', 'a', encoding='utf-8') as f:
        f.writelines(
            f'Id пользователя: {id_user}, Выражение: {input_data}, Результат: {result}\n')


def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'До встречи')
    return ConversationHandler.END


start_handler = CommandHandler('start', start)
operations_data_handler = MessageHandler(Filters.text, operations_data)
cancel_handler = CommandHandler('end', cancel)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(operations_data_handler)
dispatcher.add_handler(cancel_handler)

updater.start_polling()
updater.idle()
