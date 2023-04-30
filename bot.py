import telebot
import matplotlib

bot = telebot.TeleBot("6298746467:AAEIgk1m-VVMFAp8wNcFtS8qXuUbAoZIcw0")
@bot.message_handler(commands=["ayuda", "start"])

def enviar(msg):
    bot.reply_to(msg, "Bienvenidos al Himalaya")

bot.polling()