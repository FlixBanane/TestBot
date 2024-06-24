import telebot
import os
from flask import Flask, request

TOKEN = "6931696104:AAGDpRB0S1Bbt6rH77BNKFpOwEUttIZ56aE"
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

# Commande /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Bonjour {message.from_user.first_name}, bienvenue sur le bot Telegram!")

# Gestion des messages texte
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

# Route de base
@app.route('/')
def index():
    return 'Bot is running!'

# Route pour le webhook
@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '!', 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=f"https://test-bot-r67u.vercel.app/{TOKEN}")
    # app.run(host="0.0.0.0", port=int(5000))
