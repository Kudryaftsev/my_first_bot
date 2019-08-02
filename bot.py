# импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# импортируем лщгирование
import logging
# импортируем настройки
import settings

# конфигурируем логгирование
#                        имя файла      уровень события     само сообщение
#                       asсtime - если хотим дату, name - если хотим имя
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s",
                    level=logging.INFO, # error - получаем только ошибки; warning - получаем потенциальные ошибки
                    filename="bot.log"  # создается файл, где всё будет прописано
                    )
# и что это такое вообще?
# Ну, по-первых, по структуре: сверху вниз - импорты, глобальные настройки, функции, главная функция. 
# ВАЖНО ВАЖНО ВАЖНО ВАЖНО ВАЖНО
# В случаях, когда нам не нужно знать, от кого пришло сообщение, можно заменить имя на дату
# 

# Настройки proxy


def greet_user(bot, update):    #   обязательные аргументы функции - bot, update
    text = "Вызван /start"
    logging.info(text)                 #   чтобы знать, что бот работает
    # мы можем даже не принтировать текст, а выводить его в .log
    update.message.reply_text(text) #   отвечает пользователю в телеграмме

    #   Чтобы изменения работали - нужно перезапустить

    #   update - это всё, что приходит от платформы

def talk_to_me(bot, update):
    user_text =f"Привет, {update.message.chat.first_name}. Ты написал {update.message.text}." # текст от пользователя
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.first_name, update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)    #   ДА он отправляет то же самое, что мы ему пишм

# функция, которая соединяется с телеграм
def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)    # идентификация

    logging.info("Бот запускается") # при старте программы будет попадать в .log

    #   mybot.dispatcher.add_handler(CommandHandler("start", start)) # первый аргумент - команда, которая обрабатывается; второй аргумент - что будет сделано, когда эта команда поступит
    #   дело в том, что таких функций может быть очень много
    #   поэтому, немногим проще будет определять его в переменную

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    #                           какой тип обрабатывать
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()                                               # начинает подключаться
    mybot.idle()                                                        # будет работать, 
                                                                        # пока не остановят
# вызываем функцию
main()

# Это и есть самая базовая структура для бота.
# Дальше - больше.