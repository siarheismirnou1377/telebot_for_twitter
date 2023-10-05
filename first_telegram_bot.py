from time import sleep
from random import randint

import telebot
from telebot import types

from parser_twitter.parser_twi import func_return_text, reading_last_twit
from bot_config import token
from twit_curl import response


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  button1 = types.KeyboardButton("Начать")
  button2 = types.KeyboardButton("Остановить")
  markup.add(button1, button2)
  bot.send_message(message.chat.id, 
                   text="Привет, {0.first_name}! Я могу следить за пользователем в твиттере.".format(message.from_user),
                   reply_markup=markup
                  )

stop = False

@bot.message_handler(content_types=['text'])
def bot_work(message):
  global stop
  count = 0
  if(message.text == "Начать"):
    stop = False
    while True:
      if stop:
        break
      num = randint(1, 30)
      if count == 0:  # Если запрос первый раз отправляется
        count += 1
        text = func_return_text(response, reading_last_twit)
        bot.send_message(message.chat.id, text)
        sleep(num)
        continue
      elif count >= 1:  # Если запрос уже отправлялся
        count += 1
        text_2 = func_return_text(response, reading_last_twit)
        if text == text_2:  # Проверяем полученные данные из предыдущего запроса
          sleep(num)
          continue
        else:
          text = text_2  
          bot.send_message(message.chat.id, text_2)
          sleep(num)
          continue
  elif (message.text == "Остановить"):
    stop = True


bot.polling(none_stop=True, interval=0)