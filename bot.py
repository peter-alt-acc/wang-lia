import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, MessageHandler, filters

from gemini import command_ch

async def handle(update, context):
    msg = update.message or update.business_message
    if not msg or not getattr(msg, "text", None):
        return

    text = msg.text or ""
    text = text.strip()

    parts = text.split()
    if not parts:
        return
    cmd = parts[0]
    
    
    if cmd == "/ch":
        content = text[3:].strip()

        if not content:
            await msg.reply_text("🤖 Usage: /ch <text>")
            return
        
        thinking = await context.bot.send_message(
            chat_id=update.effective_chat.id, 
            text="🤔 Thinking...",
            parse_mode="HTML"
        )
        
        result = command_ch(content)

        await thinking.edit_text(result, parse_mode="HTML")
        return



load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    print("Error: TELEGRAM_BOT_TOKEN not found. Please set it in the .env file.")

app = (
    ApplicationBuilder()
    .token(TOKEN)
    .concurrent_updates(True)
    .connection_pool_size(20)
    .pool_timeout(30)
    .build()
)

app.add_handler(MessageHandler(filters.ALL, handle))

print("Bot Started (Polling)...")

app.run_polling()