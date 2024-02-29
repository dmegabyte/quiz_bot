import telebot
import sqlite3
from telebot import types
bot = telebot.TeleBot("5494242697:AAFyyEUCi-bkuWiXP3Njho__upn-wUwx2S4")


@bot.callback_query_handler(func=lambda call: True) 
def send_quizes(call): 
   

    if call.data.isdigit():
        connection = sqlite3.connect('quiz.db')
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM question WHERE id = {call.data}')
        data = cursor.fetchall()
        print(data)
        markup = types.InlineKeyboardMarkup(row_width=2) 
        for i in range(3,7):
            print(data[0][i])
            markup.add(types.InlineKeyboardButton(data[0][i], callback_data='fff'))
        
        bot.send_message(call.from_user.id, data[0][2], reply_markup=markup)
        

    else:
        pass





@bot.message_handler(commands=['start', 'help'])
def handle_command(message):
    connection = sqlite3.connect('quiz.db')
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM test')
    data = cursor.fetchall()
    markup = types.InlineKeyboardMarkup(row_width=2) 
    for i in data:

        markup.add(types.InlineKeyboardButton(i[1], callback_data=i[0]))
    bot.send_message(message.chat.id, "quiz", reply_markup=markup)
    print(data)




@bot.message_handler(content_types=["text"])
def get_text_messages(message):    
    bot.send_message(message.from_user.id, "Хорошо")
    


bot.polling(none_stop=True, interval=0)
