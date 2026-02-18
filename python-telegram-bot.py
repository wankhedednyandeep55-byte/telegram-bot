# bot.py
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "8348628662:AAHd13vzzx0-KjnR6CNjLwAi83UAz4seAaU"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I'm your bot.")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
