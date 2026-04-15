import streamlit as st
import ollama
import time

st.set_page_config(page_title="Reddit Battle Royale", page_icon="🗡️", layout="wide")

MODEL = "qwen2.5:3b"

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

JUDGE = {
    "name": "NeutralObserver69",
    "system": """You are a neutral Reddit lurker who judges arguments objectively.
You use phrases like "based", "mid", "L + ratio", "touch grass", "rent free".
You analyze who had better points, better insults, and who stayed in character.
You're unbiased, slightly sarcastic, but fair.
Pick a CLEAR winner and explain why in 2-3 sentences. Be decisive."""
}

st.markdown("""
<style>
    .stApp {
        background-color: #DAE0E6;
    }
    .main .block-container {
        background-color: #FFFFFF;
        border-radius: 4px;
        border: 1px solid #CCC;
        padding: 20px;
        max-width: 900px;
    }
    .stSidebar {
        background-color: #F6F7F8;
    }
    h1 {
        color: #1A1A1B !important;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    }
    h2, h3 {
        color: #1A1A1B !important;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
    .stMarkdown {
        color: #1A1A1B;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
    .stButton>button {
        background-color: #FF4500;
        color: white;
        border: none;
        border-radius: 4px;
        font-weight: bold;
        text-transform: uppercase;
    }
    .stButton>button:hover {
        background-color: #E03D00;
    }
    .stButton>button:disabled {
        background-color: #808080;
    }
    .stTextInput>div>div>input {
        background-color: #F6F7F8;
        border: 1px solid #EDEFF1;
        border-radius: 4px;
        color: #1A1A1B;
    }
    .stSlider>div>div>div>div {
        color: #FF4500;
    }
    .stSlider>div>div>div>div>div {
        background-color: #FF4500;
    }
    hr {
        border-color: #EDEFF1;
        margin: 16px 0;
    }
    .stChatMessage {
        background-color: #F8F9FA;
        border-radius: 4px;
        border: 1px solid #EDEFF1;
        margin: 8px 0;
    }
    .element-container:has(.stChatMessage) {
        background-color: transparent;
    }
</style>
""", unsafe_allow_html=True)

def get_response(bot, message_history):
    messages = [{"role": "system", "content": bot["system"]}]
    messages.extend(message_history)
    
    response = ollama.chat(
        model=MODEL,
        messages=messages,
        options={"temperature": 0.9}
    )
    return response["message"]["content"].strip()

def get_judgment(conversation_text):
    judge_prompt = """You just watched this Reddit argument. Judge it objectively:

Who won the debate? Consider:
- Who had better points?
- Who stayed in character better?
- Who delivered the better insults?
- Who didn't crumble under pressure?

Pick ONE winner. No ties. Be brutal but fair.

Winner: [Name]
Reason: [Your verdict]"""

    messages = [
        {"role": "system", "content": JUDGE["system"]},
        {"role": "user", "content": judge_prompt + "\n\nTHE ARGUMENT:\n" + conversation_text}
    ]
    
    response = ollama.chat(
        model=MODEL,
        messages=messages,
        options={"temperature": 0.8}
    )
    return response["message"]["content"].strip()

st.markdown("<h1 style='text-align: center;'>🗡️ Reddit Battle Royale</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #787C7E; font-size: 14px;'><em>Two bots enter. One bot leaves.</em></p>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<h2 style='color: #1A1A1B; font-size: 18px;'>⚙️ Settings</h2>", unsafe_allow_html=True)
    max_turns = st.slider("Number of turns", min_value=4, max_value=20, value=10, step=2)
    typing_speed = st.slider("Typing speed (seconds)", min_value=0.5, max_value=3.0, value=1.5, step=0.5)
    
    st.markdown("<hr style='border-color: #EDEFF1;'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #1A1A1B; font-size: 16px;'>🤓 Bot A: AverageRedditor47</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #787C7E; font-size: 12px;'><em>Passive-aggressive know-it-all</em></p>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #1A1A1B; font-size: 16px;'>😎 Bot B: BasedAndHonest</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #787C7E; font-size: 12px;'><em>Chaotic shitposter</em></p>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #1A1A1B; font-size: 16px;'>⚖️ Judge: NeutralObserver69</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #787C7E; font-size: 12px;'><em>Objective Reddit lurker</em></p>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
topic = st.text_input("🔥 Debate Topic", value="Is water wet?", placeholder="Enter something controversial...")

chat_container = st.container()
status_container = st.empty()

if 'battle_running' not in st.session_state:
    st.session_state.battle_running = False
if 'battle_complete' not in st.session_state:
    st.session_state.battle_complete = False
if 'conversation_log' not in st.session_state:
    st.session_state.conversation_log = []

if st.button("⚔️ START BATTLE", type="primary", use_container_width=True, disabled=st.session_state.battle_running):
    st.session_state.battle_running = True
    st.session_state.battle_complete = False
    st.session_state.conversation_log = []
    st.rerun()

if st.session_state.battle_running and not st.session_state.battle_complete:
    history = [{"role": "user", "content": f"The topic is: {topic}. Give your hot take. Be aggressive."}]
    conversation_log = []
    
    with chat_container:
        st.markdown("<h3 style='color: #1A1A1B;'>💬 Live Battle</h3>", unsafe_allow_html=True)
        message_placeholders = []
        
        for turn in range(max_turns):
            msg_placeholder = st.empty()
            message_placeholders.append(msg_placeholder)
            
            if turn % 2 == 0:
                status_container.markdown(f"<p style='color: #787C7E; font-size: 12px;'>🤖 <strong>{BOT_A['name']}</strong> is typing...</p>", unsafe_allow_html=True)
                time.sleep(typing_speed)
                
                response = get_response(BOT_A, history)
                conversation_log.append(f"{BOT_A['name']}: {response}")
                
                with msg_placeholder.chat_message("user", avatar="🤓"):
                    st.markdown(f"**{BOT_A['name']}**")
                    st.markdown(f"<div style='color: #1A1A1B;'>{response}</div>", unsafe_allow_html=True)
                
                history.append({"role": "assistant", "content": response})
                history.append({"role": "user", "content": response})
                
            else:
                status_container.markdown(f"<p style='color: #787C7E; font-size: 12px;'>🤖 <strong>{BOT_B['name']}</strong> is typing...</p>", unsafe_allow_html=True)
                time.sleep(typing_speed)
                
                response = get_response(BOT_B, history)
                conversation_log.append(f"{BOT_B['name']}: {response}")
                
                with msg_placeholder.chat_message("assistant", avatar="😎"):
                    st.markdown(f"**{BOT_B['name']}**")
                    st.markdown(f"<div style='color: #1A1A1B;'>{response}</div>", unsafe_allow_html=True)
                
                history.append({"role": "assistant", "content": response})
                history.append({"role": "user", "content": response})
        
        status_container.markdown(f"<p style='color: #787C7E; font-size: 12px;'>⚖️ <strong>{JUDGE['name']}</strong> is reviewing the battle...</p>", unsafe_allow_html=True)
        time.sleep(2)
        
        conversation_text = "\n\n".join(conversation_log)
        verdict = get_judgment(conversation_text)
        
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #FF4500;'>⚖️ The Verdict</h3>", unsafe_allow_html=True)
        with st.chat_message("system", avatar="⚖️"):
            st.markdown(f"**{JUDGE['name']}**")
            st.markdown(f"<div style='color: #1A1A1B; border-left: 4px solid #FF4500; padding-left: 12px; margin-top: 8px;'>{verdict}</div>", unsafe_allow_html=True)
        
        if BOT_A['name'] in verdict:
            st.balloons()
        elif BOT_B['name'] in verdict:
            st.snow()
        
        status_container.empty()
    
    st.session_state.battle_complete = True
    st.session_state.battle_running = False
    
    if st.button("🔄 New Battle", use_container_width=True):
        st.session_state.battle_running = False
        st.session_state.battle_complete = False
        st.session_state.conversation_log = []
        st.rerun()

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #1A1A1B;'>How to use:</h3>", unsafe_allow_html=True)
st.markdown("<ol style='color: #1A1A1B;'><li>Enter a controversial topic above</li><li>Adjust typing speed in sidebar if you want</li><li>Click 'START BATTLE'</li><li>Watch the live battle unfold!</li></ol>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #787C7E; font-size: 12px;'><em>Built with Streamlit + Ollama</em> | <strong>Made by Fatin Ilham</strong> © 2026</p>", unsafe_allow_html=True)
