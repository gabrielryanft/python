import telebot

bot = telebot.TeleBot('token')
@bot.message_handler(commands=['start'])

def start(msg):
    bot.reply_to(msg, 'Opa! Digite uma operação matematica:')

@bot.message_handler(commands=['calc'])
def calc(msg):
    separado = msg.text.split(' ')
    bot.reply_to(msg, eval(' '.join(separado[1])))

bot.polling()