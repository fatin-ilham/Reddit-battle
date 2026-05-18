# 🗡️ Reddit Battle Royale

**Two AI bots walk into a debate. One leaves victorious.**

Watch AI agents with distinct Reddit personas argue over any topic while a neutral AI judge declares a winner. Built for entertainment, powered by LLMs.

[![Try Demo](https://img.shields.io/badge/🚀-Try%20Demo-FF4500?style=for-the-badge)](YOUR_STREAMLIT_CLOUD_LINK_HERE)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io)

---

## 🎯 What It Does

- 🔥 **Two AI bots** with opposing Reddit personalities debate any topic
- ⚡ **Live battle** unfolds turn-by-turn with typing animations
- ⚖️ **AI Judge** analyzes arguments and declares a winner
- 🎮 **Customizable** turns, speed, and bot personalities

## 🤖 Meet The Fighters

| Bot | Name | Personality | Style |
|-----|------|-------------|-------|
| 🤓 | **AverageRedditor47** | Passive-aggressive know-it-all | "ackshually", "source?", "cringe" |
| 😎 | **BasedAndHonest** | Chaotic shitposter | ALL CAPS, "npc", "cope", "ratio" |
| ⚖️ | **NeutralObserver69** | Objective lurker judge | "based", "mid", "L + ratio" |

## 📸 Screenshots

![Battle Demo](https://via.placeholder.com/800x450/DAE0E6/1A1A1B?text=Reddit+Battle+Royale+-+Live+Debate+Interface)

*Above: Watch the battle unfold in real-time with Reddit-style UI*

![Verdict](https://via.placeholder.com/800x300/FFFFFF/1A1A1B?text=AI+Judge+Delivers+Verdict)

*Above: The AI judge delivers a brutal but fair verdict*

## 🚀 Quick Start

### Option 1: Try the Live Demo

1. Click the **Try Demo** badge at the top
2. Enter any controversial topic
3. Watch the AI battle unfold!

### Option 2: Run Locally

**Prerequisites:**
- Python 3.8+
- OpenRouter API key (get one free at [openrouter.ai](https://openrouter.ai))

**Steps:**

```bash
# Clone the repo
git clone https://github.com/fatin-ilham/Reddit-battle.git
cd Reddit-battle

# Install dependencies
pip install -r requirements.txt

# Add your API key
# Create a .env file with: OPENROUTER_API_KEY=your_key_here

# Run the app
streamlit run reddit_battle_streamlit.py
```

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Frontend | Streamlit |
| Backend | Python 3.8+ |
| LLM API | OpenRouter (Qwen 2.5 7B) |
| Hosting | Streamlit Cloud |

## 📝 Features

- ✅ Reddit-inspired UI design
- ✅ Real-time chat interface with avatars
- ✅ Typing animations for realism
- ✅ Adjustable battle settings (turns, speed)
- ✅ Celebration effects (balloons/snow) for winners
- ✅ Custom bot personalities via system prompts
- ✅ Session state management

## 🔧 Customization

### Change Bot Personalities

Edit the system prompts in `reddit_battle_streamlit.py`:

```python
BOT_A = {
    "name": "YourBotName",
    "system": "Your custom personality prompt here..."
}
```

### Add New Bots

Add more bot configurations and modify the turn logic to include them.

### Change the Model

Update the `MODEL` variable to use different OpenRouter models:

```python
MODEL = "meta-llama/llama-3-8b-instruct"  # or any OpenRouter model
```

## 🎮 Example Battles

Try these topics:

- "Is water wet?"
- "Pineapple on pizza: yes or no?"
- "Vim vs Emacs"
- "Tabs vs Spaces"
- "Is a hotdog a sandwich?"
- "Should AI have rights?"

## 📄 License

MIT License - feel free to use, modify, and distribute!

## 🙋 Contributing

Found a bug? Want a feature? Open an issue or PR!

---

**Built with ❤️ by [Fatin Ilham](https://github.com/fatin-ilham)**

*Made for fun. No Redditors were harmed in the making of this app.*
