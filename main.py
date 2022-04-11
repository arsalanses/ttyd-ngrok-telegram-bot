from telebot import types
import subprocess
import telebot
import os

TOKEN = os.getenv('API_KEY')
tb = telebot.TeleBot(TOKEN) #TODO: make sure that TOKEN is correct

@tb.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('/salam')
    markup.add(itembtn1)
    tb.send_message(message.chat.id, "Choose:", reply_markup=markup)

@tb.message_handler(commands=['htop'])
def start_htop(message):
    tb.send_message(message.chat.id, "running...")

    result = subprocess.call('./scripts/ttyd.sh')

    tb.send_message(message.chat.id, f"{result}")

@tb.message_handler(commands=['nohtop'])
def stop_htop(message):
    tb.send_message(message.chat.id, "running...")

    result = subprocess.call('./scripts/nottyd.sh')

    tb.send_message(message.chat.id, f"{result}")

@tb.message_handler(commands=['salam'])
def is_up(message):
    tb.send_message(message.chat.id, "Bede bezanim!")

# tb.polling()
tb.infinity_polling(timeout=10, long_polling_timeout=5)

while True: # Don't end the main thread.
    pass
