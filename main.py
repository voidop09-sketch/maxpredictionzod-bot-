
import logging
import asyncio
import nest_asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from scheduler.auto_predict import start_auto_prediction

nest_asyncio.apply()

BOT_TOKEN = "7467409659:AAECM2gp_2LQfgDYVO9fh5NKCJkucUBXAzk"

logging.basicConfig(
    filename='logs/bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    print(f"✅ /start used in Chat ID: {chat_id}")
    await update.message.reply_text("👋 Welcome to MaxPredictionZod!")

async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from scheduler.prediction_engine import generate_prediction
    prediction = generate_prediction()
    await update.message.reply_text(prediction)

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("predict", predict))
    asyncio.create_task(start_auto_prediction(app))
    print("🤖 Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
