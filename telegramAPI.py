import os
from dotenv import load_dotenv
load_dotenv()
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

#Assistente Chama t.me/assistente_chama_bot
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Função para o comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(welcomingText)

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text
    print(f"Usuário: {user_msg}")

    # Aqui você insere sua chamada à OpenAI (com o system_message da Chama)
    resposta = "Estou aqui com você, respira... 🌱"  # placeholder

    await update.message.reply_text(resposta)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

print("🔥 Chama está escutando com alma...")
app.run_polling()

