import telebot

bot = telebot.TeleBot('6041534816:AAG1y_sAhm-8bt1EF3h3Mo6CxHkT_d6Pssw')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello, I’m Alko_Sale_Support_bot!", parse_mode='html')


bot.polling(non_stop=True)