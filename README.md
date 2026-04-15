# 🗡️ Reddit Battle Royale

An interactive AI debate simulator where two LLM agents with distinct Reddit-inspired personas argue against each other on any topic, with a third AI judge deciding the winner.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLMs-green)

## 🎯 What It Does

- **Two AI bots** with opposing personalities debate any topic you choose
- **Live battle** unfolds turn-by-turn with typing animations
- **AI Judge** analyzes the argument and declares a winner
- **Customizable** number of turns and typing speed

## 🤖 The Bots

| Bot | Name | Personality |
|-----|------|-------------|
| **Bot A** | AverageRedditor47 | Passive-aggressive know-it-all who "ackshually" corrects everyone |
| **Bot B** | BasedAndHonest | Chaotic shitposter who uses ALL CAPS and calls people NPCs |
| **Judge** | NeutralObserver69 | Unbiased lurker who delivers brutal but fair verdicts |

## 🚀 Quick Start

### Prerequisites

1. [Install Ollama](https://ollama.com/download) and pull the model:
   ```bash
   ollama pull qwen2.5:3b
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/reddit-battle-royale.git
   cd reddit-battle-royale
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   streamlit run reddit_battle_streamlit.py
   ```

## 📸 Screenshot

<img width="1919" height="796" alt="image" src="https://github.com/user-attachments/assets/8dbba997-fbd9-4b41-bbb3-b3e944a8d9b3" />


## 🛠️ Tech Stack

- **Streamlit** - Interactive web UI
- **Ollama** - Local LLM inference
- **Python** - Backend logic

## 📝 Features

- ✅ Custom CSS styling matching Reddit's aesthetic
- ✅ Real-time chat interface with avatars
- ✅ Session state management for battle control
- ✅ Adjustable battle settings (turns, speed)
- ✅ Dynamic winner celebration effects

## 🔧 Customization

You can easily modify the bots by editing their system prompts in the code:

```python
BOT_A = {
    "name": "YourBotName",
    "system": "Your custom personality prompt here..."
}
```

## 📄 License

MIT License - feel free to use and modify!

---

Built with ❤️ by [Fatin Ilham](https://github.com/fatin-ilham)
