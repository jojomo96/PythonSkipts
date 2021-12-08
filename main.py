import telebot
import os

API_KEY = os.environ["API_KEY"]
chatId = '1154921572'
BOT = telebot.TeleBot(API_KEY)


def initBot():
    BOT.send_message(chatId, "Test Nachricht")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    initBot()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
