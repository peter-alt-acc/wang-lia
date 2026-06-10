import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("New Bot")

def main():
    if not TOKEN:
        print("Error: TELEGRAM_BOT_TOKEN not found. Please set it in the .env file.")
        return
    
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    
    print("Bot Started (Polling)...")
    application.run_polling()

if __name__ == "__main__":
    main()