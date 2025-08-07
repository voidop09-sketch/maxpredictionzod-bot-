
import random
import datetime

dialogues = [
    "💥 Big Boom Ahead — Trust Your Luck!",
    "🧠 Brain says yes... but heart says hell yeah!",
    "⚡ 90% Accuracy — Follow the signal!",
    "🔥 High Confidence Call — Use it wisely!",
    "😈 Secret Insider Vibes Detected.",
    "🤑 Use this one. Then thank me later.",
    "👑 Boss Move — Only for legends.",
    "😂 Bhaiya lagao warna regret hoga!",
    "🎯 Lag gaya to rocket 🚀, nahi to next round pakka!",
    "🥷 Silent entry, loud profit.",
    "Boss... ye wala to pura game changer hai! 💰",
    "Mat soch bhai... lagao seedha! 🔥",
    "Yeh system ka crack version hai. 😈"
]

choices = ['🔴 SMALL', '🟢 BIG']

def get_time():
    now = datetime.datetime.now()
    return now.strftime("⏱ %I:%M %p | %d %b %Y")

def get_period():
    return random.randint(100, 999)

def generate_prediction():
    lines = ["🎯 WINGO 1 MINUTE\n"]
    for _ in range(5):
        period = get_period()
        color = random.choice(choices)
        multiplier = f"X{random.randint(1, 3)}"
        line = f"🌈 PERIOD: {period} — {color} {multiplier}"
        lines.append(line)
    goku = f'\n🧠 GOKU: "{random.choice(dialogues)}"'
    timestamp = f"{get_time()}"
    return "\n".join(lines) + goku + f"\n{timestamp}"
