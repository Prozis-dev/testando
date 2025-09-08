import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TELEGRAM_TOKEN") 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Sou o bot jurídico em construção 🚀")

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pergunta = update.message.text
    await update.message.reply_text(f"Recebi sua pergunta: {pergunta}")

def main():
    if not TOKEN:
        raise ValueError("⚠️ Variável de ambiente TELEGRAM_TOKEN não configurada!")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))
    app.run_polling()

if __name__ == "__main__":
    main()

# Para rodar o bot no Telegram, use:
    # t.me/chatbot_juridico_bot
    # Token: 8304485718:AAFeqEuONC6pR8lsNsHZvcGYX5UVMoGk9P4
    # Na pasta raiz do projeto, execute: pip install python-telegram-bot==20.3
    # Depois, execute: set TELEGRAM_TOKEN=8304485718:AAFeqEuONC6pR8lsNsHZvcGYX5UVMoGk9P4
    # Depois, execute: python app/bot.py