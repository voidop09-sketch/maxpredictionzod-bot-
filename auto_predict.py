
import asyncio
from telegram.ext import Application
from scheduler.prediction_engine import generate_prediction

GROUP_ID = -1002423219557

async def send_prediction(app: Application):
    prediction = generate_prediction()
    try:
        await app.bot.send_message(
            chat_id=GROUP_ID,
            text=prediction,
            parse_mode="HTML"
        )
        print("✅ Auto Prediction Sent!")
    except Exception as e:
        print(f"❌ Failed to send prediction: {e}")

async def start_auto_prediction(app: Application):
    while True:
        await send_prediction(app)
        await asyncio.sleep(60)
