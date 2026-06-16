import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import google.generativeai as genai

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Setup Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("🤖 Bot started! Send any message dan Gemini akan jawab.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    
    try:
        # Send ke Gemini
        response = model.generate_content(user_message)
        reply = response.text
        await update.message.reply_text(reply)
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")

def main():
    if not TOKEN:
        print("Error: TELEGRAM_BOT_TOKEN not found. Please set it in the .env file.")
        return
    if not GEMINI_API_KEY:
        print("Error: GEMINI_API_KEY not found. Please set it in the .env file.")
        return
    
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("Bot Started (Polling)...")
    application.run_polling()

if __name__ == "__main__":
    main()