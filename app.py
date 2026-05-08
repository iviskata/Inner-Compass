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
# STATE INIT (for auto-clear input)
# =======================
if "history" not in st.session_state:
    st.session_state.history = []

if "input_key" not in st.session_state:
    st.session_state.input_key = 0

# =======================
# LANGUAGE
# =======================
lang = st.selectbox(
    "🌍",
    ["Български", "English"],
    label_visibility="collapsed"
)

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
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #94a3b8;
        font-size: 12px;
        margin-bottom: 20px;
        letter-spacing: 1px;
    }

    /* BIGGER INPUT */
    .stTextInput input {
        height: 55px;
        font-size: 18px;
        border-radius: 14px;
        background-color: #1e293b;
        color: white;
        border: 1px solid rgba(255,255,255,0.12);
    }

    /* SMALLER SELECTBOX */
    div[data-baseweb="select"] {
        font-size: 12px;
        max-width: 120px;
        margin: 0 auto 10px auto;
    }

    .card {
        margin-top: 12px;
        padding: 18px;
        border-radius: 16px;
        background: rgba(17, 24, 39, 0.65);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255,255,255,0.08);
        line-height: 1.6;
    }

    .user {
        color: #60a5fa;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =======================
# HEADER
# =======================
st.markdown("<h1>Inner Compass 🏛️</h1>", unsafe_allow_html=True)

subtitle = "calm stoic reflection engine"
if lang == "English":
    subtitle = "calm stoic reflection engine"

st.markdown(f"<div class='subtitle'>◉ {subtitle} ◉</div>", unsafe_allow_html=True)

# =======================
# SMART ENGINE (more natural variation)
# =======================
def inner_compass(text):
    t = text.lower()

    if any(w in t for w in ["тъжен","sad","lonely","болка","pain"]):
        return random.choice([
            "💭 Това е временно.\n🏛️ Епиктет: Не събитията, а възприятието ни за тях.",
            "💭 Разбирам те.\n🏛️ Това ще премине.",
            "💭 Болката не е постоянна.\n🏛️ Всичко се движи."
        ])

    if any(w in t for w in ["стрес","stress","anxiety","паника"]):
        return random.choice([
            "💭 Върни се към настоящия момент.\n🏛️ Контролирай това, което можеш.",
            "💭 Умът ти е натоварен.\n🏛️ Спокойствието е избор.",
            "💭 Една стъпка е достатъчна.\n🏛️ Не всичко е спешно."
        ])

    if any(w in t for w in ["изморен","tired","exhausted"]):
        return random.choice([
            "💭 Почивката е сила.\n🏛️ Сенека: Дори силният ум има нужда от покой.",
            "💭 Тялото ти има нужда от пауза.\n🏛️ Това е нормално.",
            "💭 Забави темпото.\n🏛️ Възстановяването е прогрес."
        ])

    return "💭 Разбирам.\n🏛️ Наблюдавай това чувство спокойно."

# =======================
# INPUT
# =======================
placeholder = "Как се чувстваш?" if lang == "Български" else "How do you feel?"

user = st.text_input(
    placeholder,
    key=f"input_{st.session_state.input_key}",
    label_visibility="collapsed"
)

# =======================
# SUBMIT LOGIC
# =======================
if user:
    response = inner_compass(user)
    st.session_state.history.append((user, response))

    # 🔥 RESET INPUT (key trick)
    st.session_state.input_key += 1

# =======================
# DISPLAY HISTORY
# =======================
for u, r in reversed(st.session_state.history):
    st.markdown(f"<div class='user'>🧠 {u}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='card'>{r.replace('\n','<br>')}</div>", unsafe_allow_html=True)
