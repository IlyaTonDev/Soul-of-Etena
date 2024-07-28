import time
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram import Update, Bot

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
CHAT_ID = None

def start(update: Update, context):
    global CHAT_ID
    CHAT_ID = update.effective_chat.id
    context.bot.send_message(chat_id=CHAT_ID, text='Загрузка...')
    time.sleep(2)  # имитируем загрузку
    context.bot.send_message(chat_id=CHAT_ID, text='Готово!')
    context.bot.send_photo(chat_id=CHAT_ID, photo='https://example.com/background_image.jpg')  # отправляем фоновую картинку
    context.bot.send_animation(chat_id=CHAT_ID, animation='https://example.com/animation.gif')  # отправляем анимацию

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()