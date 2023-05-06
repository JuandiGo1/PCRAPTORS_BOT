import telebot
import matplotlib
from PIL import Image
bot = telebot.TeleBot("6298746467:AAEIgk1m-VVMFAp8wNcFtS8qXuUbAoZIcw0")

@bot.message_handler(commands=["start"])
def enviar(msg):
    bot.reply_to(msg, "Bienvenidos al Himalaya")

@bot.message_handler(commands=["ver_estrellas"])
def verEst(msg):
    bot.reply_to(msg, "A continuación el grafico donde se muestran todas las estrellas: ")
    bot.send_photo(msg.chat.id, Image.open("universo.jpg"))

@bot.message_handler(commands=["ver_constelacion"])
def enviar(msg):
    bot.reply_to(msg, "☄️ Elija una constelación a continuación:\n 💫 Boyero\n 🌟 Casiopea\n 💫 Cazo\n 🌟 Cygnet\n 💫 Geminis\n 🌟 Hydra\n 💫 Osamayor\n 🌟 Osamenor")
    @bot.message_handler(func=lambda message: True, content_types=['text'])
    def enviarCons(msg):
        try:
            bot.reply_to(msg, "Generando gráfico...📈")
            cons= msg.text.lower()+".jpg"
            bot.send_photo(msg.chat.id, Image.open(cons))
        except:
            bot.send_message(msg.chat.id, 'Nombre invalido, intenta nuevamente por favor :)')

@bot.message_handler(commands=["constelaciones"])
def todas(msg):
    bot.reply_to(msg, "A continuación el grafico donde se muestran todas las constelaciones: ")
    bot.send_photo(msg.chat.id, Image.open("todas.jpg"))


bot.polling()