import telebot
from telebot import types
from translate import Translator

text1 = "-"
text2 = "-"

bot = telebot.TeleBot('7166886117:AAFDhKqgZbtTfRbCBmT7d-USaHS0qpREUA4')


@bot.message_handler(commands=['start', 'newText'])
def main(message):
    markup = types.ReplyKeyboardMarkup()
    # markup.add(types.KeyboardButton("rus", callback_data='info'))
    btn1 = types.KeyboardButton("rus")
    btn2 = types.KeyboardButton("eng")
    markup.row(btn1, btn2)
    btn3 = types.KeyboardButton("chin")
    btn4 = types.KeyboardButton("span")
    markup.row(btn3, btn4)
    bot.send_message(message.chat.id,
                     f'<b>Привет {message.from_user.first_name}!</b> Сначало выберите язык, на котором написан ваш текст~ ("rus" - русский, "eng" - английский, "chin" - китайский, "span" - испанский)',
                     parse_mode="html", reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    global text1
    if message.text == "rus":
        text1 = "ru"
    elif message.text == "eng":
        text1 = "en"
    elif message.text == "chin":
        text1 = "zh-tw"
    elif message.text == "span":
        text1 = "es"
    main2(message)


def main2(message):
    markup = types.ReplyKeyboardMarkup()
    # markup.add(types.KeyboardButton("rus", callback_data='info'))
    btn1 = types.KeyboardButton("rus")
    btn2 = types.KeyboardButton("eng")
    markup.row(btn1, btn2)
    btn3 = types.KeyboardButton("chin")
    btn4 = types.KeyboardButton("span")
    markup.row(btn3, btn4)
    bot.send_message(message.chat.id,
                     f'Выберите язык, на который длжен быть переписан ваш текст~ ("rus" - русский, "eng" - английский, "chin" - китайский, "span" - испанский)',
                     parse_mode="html", reply_markup=markup)
    bot.register_next_step_handler(message, on_click2)


def on_click2(message):
    global text2
    if message.text == "rus":
        text2 = "ru"
    elif message.text == "eng":
        text2 = "en"
    elif message.text == "chin":
        text2 = "zh-tw"
    elif message.text == "span":
        text2 = "es"
    bot.send_message(message.chat.id, f'Введите текст для перевода~ ')


@bot.message_handler()
def info4(message):
    if text1 != "-" and text2 != "-":
        translator = Translator(from_lang=text1, to_lang=text2)
        result = translator.translate(message.text)
        bot.send_message(message.chat.id, result)


bot.polling(none_stop=True)
