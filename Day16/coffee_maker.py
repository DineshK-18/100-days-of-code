import time
import random

def energize():
    actions = [
        "Splash cold water on your face 💦",
        "Do 20 jumping jacks 🏃‍♂️",
        "Blast your favorite hype song 🎶",
        "Eat a brain-boosting snack 🍫",
        "Turn on bright lights 💡",
        "Shout 'I AM UNSTOPPABLE!' 😤"
    ]
    print("⚔️ Sleep Slayer Activated ⚔️")
    for i in range(3):
        print(f"> {random.choice(actions)}")
        time.sleep(2)

def study_session():
    print("\n📚 Study Mode: ON 📚")
    for i in range(4):
        print(f"🔸 Focus for 25 minutes - Round {i+1}")
        time.sleep(1)
        print("🔹 Take a 5-minute break")
        time.sleep(1)

def victory():
    print("\n🎉 Mission Accomplished, Dinesh! You defeated Sleep and conquered your studies! 🎉")

# Run the code
energize()
study_session()
victory()
