import telebot

# bot = telebot.TeleBot('6572448028:AAFF3TFXGys7rCYc8ZGG6UsyeH0ryh8Ftiw')
bot = telebot.TeleBot('6937908458:AAHKH6ou_aubJDw9M3hwcd0UTXNtZ86aY0c')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Сообщение')


@bot.message_handler(commands=['run'])
def main(message):
    bot.send_message(message.chat.id, 'БЕГИ!!! \nБЕГИ!!!')


bot.infinity_polling()