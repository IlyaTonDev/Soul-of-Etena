import sqlite3
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram import Update, Bot

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
DB_NAME = 'referrals.db'
CHAT_ID = None

def start(update: Update, context):
    global CHAT_ID
    CHAT_ID = update.effective_chat.id
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS referrals (id INTEGER PRIMARY KEY, user_id INTEGER, referrer_id INTEGER)')
    conn.commit()
    conn.close()

    context.bot.send_message(chat_id=CHAT_ID, text='Привет! Введите код приглашения, если у вас есть один.')

def referral(update: Update, context):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM referrals WHERE user_id = ?', (update.effective_user.id,))
    if cursor.fetchone():
        context.bot.send_message(chat_id=CHAT_ID, text='Вы уже зарегистрированы!')
    else:
        referrer_id = int(context.args[0])
        cursor.execute('INSERT INTO referrals (user_id, referrer_id) VALUES (?, ?)', (update.effective_user.id, referrer_id))
        conn.commit()
        conn.close()
        context.bot.send_message(chat_id=CHAT_ID, text='Вы успешно зарегистрированы!')
        context.bot.send_message(chat_id=CHAT_ID, text='Ваш код приглашения: {}'.format(update.effective_user.id))

def check_referral(update: Update, context):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM referrals WHERE referrer_id = ?', (update.effective_user.id,))
    referrals = cursor.fetchall()
    conn.close()
    if referrals:
        context.bot.send_message(chat_id=CHAT_ID, text='Ваши рефералы:')
        for referral in referrals:
            context.bot.send_message(chat_id=CHAT_ID, text='{}'.format(referral[1]))
    else:
        context.bot.send_message(chat_id=CHAT_ID, text='У вас нет рефералов.')

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('referral', referral))
    dp.add_handler(CommandHandler('check_referral', check_referral))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()