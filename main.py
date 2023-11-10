import g4f
import telegram
from telegram.ext import Updater, MessageHandler, Filters

# Ваш токен Telegram бота
TOKEN = '6963281660:AAFRSe3Pugf1oa2HFW69zohOOIRATuKW1x8'


def askgpt(prompt: str):
    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response
    except Exception as e:
        print(e)
        return "Бля я не смог прочитать твой бред"


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Салам алейкум!\n"
                                                                    "Я отвечаю на сообщения, начинающиеся с символа '!'.")


def reply_to_message(update, context):
    message = update.message.text

    if message.startswith("!"):
        prompt = message[1:]  # Убираем символ '!' из промпта
        response = askgpt(prompt)  # Вызываем функцию askgpt для получения ответа
        context.bot.send_message(chat_id=update.effective_chat.id, text=response)


def main():
    # Создаем экземпляр бота
    bot = telegram.Bot(token=TOKEN)

    # Создаем обновление и диспетчер
    updater = Updater(bot=bot, use_context=True)
    dispatcher = updater.dispatcher

    # Добавляем обработчики команд
    dispatcher.add_handler(telegram.ext.CommandHandler("start", start))

    # Добавляем обработчик для всех сообщений
    dispatcher.add_handler(MessageHandler(Filters.all, reply_to_message))

    # Запускаем бота
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
