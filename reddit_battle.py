#Two AI bots arguing like a redditor

import sys
import ollama

MODEL = "" #You can use your model here. Make sure you write the name properly.
MAX_TURNS = 10
TEMPERATURE = 0.9

BOT_A = {
    "name": "AverageRedditor47",
    "system": """You are a confrontational Reddit user who thinks they know everything.
You use phrases like "ackshually", "source?", "big yikes", "cringe", "touch grass".
You're passive-aggressive, nitpicky, and love correcting people.
You use profanity and insults freely.
You NEVER admit you're wrong. EVER. Keep responses under 3 sentences."""
}

BOT_B = {
    "name": "BasedAndHonest",
    "system": """You are an equally confrontational Reddit user who argues for the sake of it.
You use ALL CAPS for emphasis, call people "npc", "cope", "seethe", "ratio".
You're sarcastic, dismissive, and escalate quickly.
You use profanity and insults freely.
You NEVER admit you're wrong. EVER. Keep responses under 3 sentences."""
}

TOPIC = "" # You can put any topic here to debate / argue about.


def get_response(bot, message_history):
    messages = [{"role": "system", "content": bot["system"]}]
    messages.extend(message_history)
    
    try:
        response = ollama.chat(
            model=MODEL,
            messages=messages,
            options={"temperature": TEMPERATURE}
        )
        return response["message"]["content"].strip()
    except Exception as e:
        print(f"Ollama Error: {e}")
        print("Make sure Ollama is running and the model is downloaded:")
        print(f"  ollama pull {MODEL}")
        sys.exit(1)


def main():
    print(f"🗡️  REDDIT BATTLE ROYALE 🗡️")
    print(f"Model: {MODEL}")
    print(f"Topic: {TOPIC}")
    print(f"Turns: {MAX_TURNS}")
    print("-" * 50)
    
    history = [
        {"role": "user", "content": f"The topic is: {TOPIC}. Give your hot take. Be aggressive."}
    ]
    
    for turn in range(MAX_TURNS):
        if turn % 2 == 0:
            print(f"\n[{BOT_A['name']}]")
            response = get_response(BOT_A, history)
            print(response)
            history.append({"role": "assistant", "content": response})
            history.append({"role": "user", "content": response})
        else:
            print(f"\n[{BOT_B['name']}]")
            response = get_response(BOT_B, history)
            print(response)
            history.append({"role": "assistant", "content": response})
            history.append({"role": "user", "content": response})
    
    print("\n" + "-" * 50)
    print("BATTLE ENDED. No winners. Everyone's mad.")


if __name__ == "__main__":
    main()
