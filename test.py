> D.:
import requests 
import random 
import telebot 
import os 
from telebot import types 
quiz_question = 'Выберите викторину' 
bot = telebot.TeleBot('5494242697:AAFa-ilkjrE_aqQr_elGWFxVrFAvVquqR8U') 
try: 
    url = 'http://intgr.twin24.io:60061/get_data?spreadsheet_url=https://docs.google.com/spreadsheets/d/1SeVC9-sfWFaFEQUCtYM7mpWbJVdt_sJ7rRsxz0OZi3c/edit%23gid=0&worksheet_name=Лист1' 
    response = requests.get(url) 
    response = response.json() 
except: 
    print('ОШИБКА RESPONE') 
    response = None 
 
 
r = random.randint(0,2) 
quistion = response['data'][0]['quistion'] 
right_answer = response['data'][0]['a'] 
quiz_name = 'Общие вопросы' 
 
# клавиатаура 
def inline(name_button_0, name_button_1=None, name_button_2=None, name_button_3=None, callback_prefix = ''): 
     
    markup = types.InlineKeyboardMarkup(row_width=2) 
    markup.add(types.InlineKeyboardButton(name_button_0, callback_data=callback_prefix+name_button_0)) 
    if name_button_1 is not None: 
        markup.add(types.InlineKeyboardButton(name_button_1, callback_data=callback_prefix+name_button_1)) 
    elif name_button_2 is not None: 
        markup.add(types.InlineKeyboardButton(name_button_2, callback_data=callback_prefix+name_button_2)) 
    elif name_button_3 is not None: 
        markup.add(types.InlineKeyboardButton(name_button_3, callback_data=callback_prefix+name_button_3)) 
    return markup 
 
 
 
@bot.message_handler(commands=['help', 'start']) 
def send_welcome(message): 
 
    markup = inline('тест выбора', callback_prefix='choice') 
 
    bot.send_message(message.chat.id, quiz_question, reply_markup=markup) 
    markup = inline('тест ответов', callback_prefix='answer') 
    bot.send_message(message.chat.id, quiz_question, reply_markup=markup) 
 
     
@bot.callback_query_handler(func=lambda call: call.data.startswith('choice')) 
def send_quizes(call): 
    answer = call.data 
    print('00') 
    # if not answer.startswith('choice'): 
    #     return 
    # if answer[6::] == quiz_name: 
    #     name_button = 'test' 
    #     markup = inline(name_button,name_button,name_button,name_button) 
    #     bot.send_message(call.from_user.id, quiz_question, reply_markup=markup) 
    # else: 
    #     print('1111') 
 
 
 
         
@bot.callback_query_handler(func=lambda call: call.data.startswith('answer')) 
def send_quiz_question(call): 
    answer = call.data 
    quiz_name = response['data'][0]['quistion'] 
    print('0') 
    # print(quiz_name) 
    # if not answer.startswith('answer'): 
    #     print('1') 
    #     return 
    # if answer[6::] == quiz_name: 
    #     print('2') 
    #     quiz_question = response['data'][0]['a'] 
    #     name_button = 'test' 
    #     markup = inline(name_button,name_button,name_button,name_button) 
    #     bot.send_message(call.from_user.id, quiz_question, reply_markup=markup) 
    # else: 
    #     print('2222') 
 
 
 
 
bot.infinity_polling()
