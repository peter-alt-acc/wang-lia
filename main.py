import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from google import genai

# Load environment variables from a .env file (useful for securely storing your bot token)
load_dotenv()

# Retrieve the bot's unique token from the environment variables
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Setup Gemini
gemini_client = genai.Client(api_key=GEMINI_API_KEY)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text

    try:
        response = gemini_client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=user_message
        )

        await update.message.reply_text(response.text)

    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")

# This function is triggered when a user sends the /start command to the bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("New Bot")

# The main function that initializes and runs the bot
def main():
    # Check if the TOKEN was successfully loaded; if not, show an error and stop
    if not TOKEN:
        print("Error: TELEGRAM_BOT_TOKEN not found. Please set it in the .env file.")
        return
    if not GEMINI_API_KEY:
        print("Error: GEMINI_API_KEY not found. Please set it in the .env file.")
        return
    
    # Create the application object that will manage the bot
    application = Application.builder().token(TOKEN).build()

    # Add a "handler" that tells the bot to run the 'start' function when it sees '/start'
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("Bot Started (Polling)...")

    # Start the bot and make it constantly check Telegram for new messages
    application.run_polling()

# This part ensures the main function only runs if this script is executed directly
if __name__ == "__main__":
    main()