import telebot
import os
import threading
from flask import Flask

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "أهلاً! البوت شغال تمام ✅")

if __name__ == '__main__':
    threading.Thread(target=run_flask).start()
    bot.infinity_polling()
