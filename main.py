import telebot

TOKEN = '7833826047:AAH1VlBGgyTmLkIwMc9UIO61WvDTOZmXcFU'
bot =  telebot.TeleBot(TOKEN)


#Creación de comandos simples como `/start` y `/help`

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, 'Hola! Soy tu primer bot creado con Telebot')


@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, 'Puedes interactuar conmigo usando comandos. Por ahora, solo respondo a /start y /help.')


@bot.message_handler(func=lambda m:True)
def echo_all(message):
	bot.reply_to(message, message.text)


if __name__ == '__main__':
	bot.polling(none_stop=True)