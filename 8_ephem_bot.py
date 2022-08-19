"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')



def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text("Привет! Чтобы узнать больше о планетах, жми /planet")


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(get_planet)

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

def get_planet(update, context):
    pt = "Вызван /planet"
    print(pt)
    message = update.message.reply.split()[planets]
    print(message)
    if message == "Mercury":
      update.message.reply.split(ephem.constellation.Mercury("2022/08/14"))
    elif message == "Venus":
      update.message.reply.split(ephem.constellation.Venus("2022/08/14"))
    elif message == "Earth":
      update.message.reply.split(ephem.constellation.Earth("2022/08/14"))
    elif message == "Mars":
      update.message.reply.split(ephem.constellation.Mars("2022/08/14"))
    elif message == "Jupiter":
      update.message.reply.split(ephem.constellation.Jupiter("2022/08/14"))
    elif message == "Saturn":
      update.message.reply.split(ephem.constellation.Saturn("2022/08/14"))
    elif message =="Uranus":
      update.message.reply.split(ephem.constellation.Uranus("2022/08/14"))
    elif message =="Neptune":
      update.message.reply.split(ephem.constellation.Neptune("2022/08/14"))
    else:
      print("Я знаю только планеты солнечной системы")


def main():
    mybot = Updater("5799760258:AAEXkQC-Th6qvY_rgAEyF2bSUBduKS99w5M", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", get_planet))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
