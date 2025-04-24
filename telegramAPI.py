from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

BOT_TOKEN = 'seu_token_aqui'

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text
    print(f"Usuário: {user_msg}")

    # Aqui você insere sua chamada à OpenAI (com o system_message da Chama)
    resposta = "Estou aqui com você, respira... 🌱"  # placeholder

    await update.message.reply_text(resposta)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

print("🔥 Chama está escutando com alma...")
app.run_polling()

