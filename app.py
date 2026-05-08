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
# SESSION STATE
# =======================
if "history" not in st.session_state:
    st.session_state.history = []

# =======================
# LANGUAGE
# =======================
lang = st.selectbox(
    "🌍 Language",
    ["Български", "English"]
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
        margin-bottom: 0px;
    }

    .subtitle {
        text-align: center;
        color: #94a3b8;
        margin-bottom: 20px;
        font-size: 13px;
        letter-spacing: 1px;
    }

    div[data-baseweb="select"] {
        max-width: 140px;
        margin: auto;
        margin-bottom: 15px;
        font-size: 12px;
    }

    .stTextInput input {
        height: 58px;
        font-size: 18px;
        border-radius: 14px;
        background-color: #1e293b;
        color: white;
        border: 1px solid rgba(255,255,255,0.1);
    }

    .card {
        margin-top: 10px;
        padding: 18px;
        border-radius: 16px;
        background: rgba(17, 24, 39, 0.65);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255,255,255,0.08);
        line-height: 1.7;
    }

    .user {
        color: #60a5fa;
        margin-top: 18px;
        font-weight: 500;
    }

    .stButton button {
        width: 100%;
        border-radius: 12px;
        height: 45px;
        background-color: #2563eb;
        color: white;
        border: none;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =======================
# HEADER
# =======================
st.markdown("<h1>Inner Compass 🏛️</h1>", unsafe_allow_html=True)

subtitle = "◉ calm stoic reflection engine ◉"

st.markdown(
    f"<div class='subtitle'>{subtitle}</div>",
    unsafe_allow_html=True
)

# =======================
# SMART ENGINE
# =======================
def inner_compass(text):
    t = text.lower()

    # sadness
    if any(w in t for w in ["тъжен", "sad", "сам", "lonely", "болка", "pain"]):
        return random.choice([
            "💭 Това е временно.\n🏛️ Епиктет: Не събитията, а възприятието ни за тях.",
            "💭 Разбирам те.\n🏛️ Всичко се променя.",
            "💭 Болката не е постоянна.\n🏛️ И това ще премине."
        ])

    # stress
    if any(w in t for w in ["стрес", "stress", "anxiety", "паника"]):
        return random.choice([
            "💭 Върни се към настоящия момент.\n🏛️ Контролирай това, което можеш.",
            "💭 Не всичко трябва да бъде решено днес.\n🏛️ Спокойствието е сила.",
            "💭 Една малка стъпка е достатъчна.\n🏛️ Дишай по-бавно."
        ])

    # fatigue
    if any(w in t for w in ["изморен", "изморена", "tired", "exhausted"]):
        return random.choice([
            "💭 Почивката е част от напредъка.\n🏛️ Дори силният ум има нужда от покой.",
            "💭 Тялото ти сигнализира.\n🏛️ Слушай го.",
            "💭 Забави темпото.\n🏛️ Възстановяването е сила."
        ])

    # anger
    if any(w in t for w in ["ядосан", "angry", "гняв"]):
        return random.choice([
            "💭 Емоцията е временна.\n🏛️ Реакцията е избор.",
            "💭 Спокойствието е контрол.\n🏛️ Не позволявай на момента да те управлява.",
            "💭 Направи пауза.\n🏛️ Ясният ум вижда по-добре."
        ])

    # default
    if lang == "English":
        return "💭 I hear you.\n🏛️ Observe the feeling without judgment."
    else:
        return "💭 Разбирам.\n🏛️ Наблюдавай чувството спокойно."

# =======================
# FORM (REAL FIX FOR CLEAR INPUT)
# =======================
with st.form("feeling_form", clear_on_submit=True):

    question = "Как се чувстваш?"
    button_text = "Изпрати"

    if lang == "English":
        question = "How do you feel?"
        button_text = "Send"

    user_input = st.text_input(question)

    submitted = st.form_submit_button(button_text)

    if submitted and user_input:
        response = inner_compass(user_input)
        st.session_state.history.append((user_input, response))

# =======================
# DISPLAY HISTORY
# =======================
for u, r in reversed(st.session_state.history):

    st.markdown(
        f"<div class='user'>🧠 {u}</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<div class='card'>{r.replace(chr(10), '<br>')}</div>",
        unsafe_allow_html=True
    )
