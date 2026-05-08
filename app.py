import streamlit as st
import random

# =======================
# PAGE CONFIG
# =======================
st.set_page_config(
    page_title="Inner Compass",
    page_icon="🏛️",
    layout="centered"
)

# =======================
# LANGUAGE TOGGLE
# =======================
lang = st.selectbox("Language / Език", ["Български", "English"])

# =======================
# STYLE
# =======================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');

    .stApp {
        background: radial-gradient(circle at top, #0f172a, #020617);
        color: #e2e8f0;
        font-family: 'Inter', sans-serif;
    }

    h1 {
        text-align: center;
        color: #f8fafc;
        margin-bottom: 0px;
    }

    .subtitle {
        text-align: center;
        color: #94a3b8;
        margin-bottom: 20px;
        font-size: 13px;
        letter-spacing: 1px;
    }

    .card {
        margin-top: 10px;
        padding: 18px;
        border-radius: 16px;
        background: rgba(17, 24, 39, 0.65);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255,255,255,0.08);
        color: #e2e8f0;
        line-height: 1.6;
    }

    .user {
        color: #60a5fa;
        margin-top: 10px;
        font-weight: 500;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =======================
# HEADER
# =======================
title = "Inner Compass 🏛️"
subtitle = "calm stoic reflection engine"

if lang == "English":
    subtitle = "calm stoic reflection engine"

st.markdown(f"<h1>{title}</h1>", unsafe_allow_html=True)
st.markdown(f"<div class='subtitle'>◉ {subtitle} ◉</div>", unsafe_allow_html=True)

# =======================
# CHAT HISTORY
# =======================
if "history" not in st.session_state:
    st.session_state.history = []

# =======================
# SMART RESPONSE ENGINE
# =======================
def inner_compass(text):
    t = text.lower()

    # sadness
    if any(w in t for w in ["тъжен","sad","болка","pain","сам","lonely","empty"]):
        return random.choice([
            "💭 Това, което чувстваш, е временно.\n🏛️ Епиктет: Не нещата, а мнението ни за тях ни тревожи.",
            "💭 Разбирам те.\n🏛️ Това състояние няма да остане завинаги.",
            "💭 Болката е сигнал, не присъда.\n🏛️ Всичко се променя."
        ])

    # stress
    if any(w in t for w in ["стрес","stress","anxiety","паника","overthinking"]):
        return random.choice([
            "💭 Върни се към една малка стъпка.\n🏛️ Фокусът е върху това, което контролираш.",
            "💭 Умът ти е претоварен.\n🏛️ Спокойствието е избор.",
            "💭 Спри за момент.\n🏛️ Не всичко трябва да се реши веднага."
        ])

    # fatigue
    if any(w in t for w in ["изморен","tired","exhausted","burnout"]):
        return random.choice([
            "💭 Почивката е сила.\n🏛️ Сенека: Дори силният ум има нужда от покой.",
            "💭 Тялото ти говори.\n🏛️ Слушай го.",
            "💭 Забави темпото.\n🏛️ Възстановяването е част от напредъка."
        ])

    # anger
    if any(w in t for w in ["гняв","angry","anger","ядосан"]):
        return random.choice([
            "💭 Емоцията е временна.\n🏛️ Ти избираш реакцията си.",
            "💭 Спри преди реакция.\n🏛️ Контролът е сила.",
            "💭 Гневът замъглява мисълта.\n🏛️ Спокойствието я изяснява."
        ])

    # default
    if lang == "English":
        return "💭 I hear you.\n🏛️ Try to observe this feeling without judgment."
    else:
        return "💭 Разбирам те.\n🏛️ Опитай да наблюдаваш това чувство спокойно."

# =======================
# INPUT
# =======================
prompt = "Как се чувстваш?"
if lang == "English":
    prompt = "How do you feel?"

user = st.text_input(prompt)

# =======================
# ADD MESSAGE
# =======================
if user:
    response = inner_compass(user)
    st.session_state.history.append((user, response))

# =======================
# DISPLAY CHAT
# =======================
for u, r in reversed(st.session_state.history):
    st.markdown(f"<div class='user'>🧠 {u}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='card'>{r.replace('\n','<br>')}</div>", unsafe_allow_html=True)
