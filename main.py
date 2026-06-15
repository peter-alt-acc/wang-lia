import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Load environment variables from a .env file (useful for securely storing your bot token)
load_dotenv()

# Retrieve the bot's unique token from the environment variables
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# This function is triggered when a user sends the /start command to the bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Send a simple reply message to the user who sent the command
    await update.message.reply_text("New Bot")

# The main function that initializes and runs the bot
def main():
    # Check if the TOKEN was successfully loaded; if not, show an error and stop
    if not TOKEN:
        print("Error: TELEGRAM_BOT_TOKEN not found. Please set it in the .env file.")
        return
    
    # Create the application object that will manage the bot
    application = Application.builder().token(TOKEN).build()

    # Add a "handler" that tells the bot to run the 'start' function when it sees '/start'
    application.add_handler(CommandHandler("start", start))
    
    print("Bot Started (Polling)...")

    # Start the bot and make it constantly check Telegram for new messages
    application.run_polling()

# This part ensures the main function only runs if this script is executed directly
if __name__ == "__main__":
    main()