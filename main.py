import subprocess
import telebot
import os

TOKEN = os.getenv('API_KEY')
tb = telebot.TeleBot(TOKEN) #TODO: make sure that TOKEN is correct

@tb.message_handler(commands=['ttyd'])
def restart_tor(message):
    tb.send_message(message.chat.id, "running...")

    result = subprocess.call('./scripts/ttyd.sh')

    tb.send_message(message.chat.id, f"{result}")

@tb.message_handler(commands=['nottyd'])
def restart_tor(message):
    tb.send_message(message.chat.id, "running...")

    result = subprocess.call('./scripts/nottyd.sh')

    tb.send_message(message.chat.id, f"{result}")

tb.polling()

while True: # Don't end the main thread.
    pass
