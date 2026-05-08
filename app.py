import streamlit as st
import random
from datetime import datetime

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="H-Tech · Inner Compass",
    page_icon="🏛️",
    layout="centered"
)

# =========================
# SESSION STATE
# =========================
if "history" not in st.session_state:
    st.session_state.history = []

# =========================
# LANGUAGE
# =========================
lang = st.selectbox("🌍 Language", ["Български", "English"])

# =========================
# STYLE (clean + centered)
# =========================
st.markdown("""
<style>

.stApp {
    text-align: center;
    background:
    radial-gradient(circle at top, rgba(59,130,246,0.18), transparent 35%),
    radial-gradient(circle at bottom, rgba(168,85,247,0.12), transparent 30%),
    #020617;
    color: #e2e8f0;
}

.stTextInput, .stButton {
    display: flex;
    justify-content: center;
}

.stTextInput input {
    width: 100%;
    max-width: 520px;
    height: 62px;
    border-radius: 16px;
    font-size: 18px;
}

.stButton button {
    width: 100%;
    max-width: 520px;
    height: 48px;
    border-radius: 14px;
    background: linear-gradient(90deg,#2563eb,#7c3aed);
    color: white;
    border: none;
}

h1, h3, p {
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.title("Inner Compass 🏛️")

st.markdown("### H-TECH · DIGITAL SYSTEMS")

st.markdown(
    "> Продължаваме заедно... по-смирени, по-смислени, по-стоически."
)

st.markdown("---")

# =========================
# STOIC ENGINE (SMART)
# =========================
def smart_response(text):

    t = text.lower()

    if any(x in t for x in ["sad", "тъж"]):
        return (
            "💭 Изглежда тежък момент. Това чувство е временно.",
            "Не страдаме от събитията, а от нашата интерпретация.",
            "Епиктет"
        )

    if any(x in t for x in ["stress", "стрес", "panic"]):
        return (
            "💭 Спри за момент. Дишай.",
            "Контролирай това, което зависи от теб.",
            "Марк Аврелий"
        )

    if any(x in t for x in ["tired", "умор", "burnout"]):
        return (
            "💭 Тялото ти иска пауза.",
            "Почивката също е част от движението напред.",
            "Сенека"
        )

    return random.choice([
        ("💭 Бъди тук и сега.", "Животът се случва в настоящия момент.", "Стоицизъм"),
        ("💭 Спокойствието е сила.", "Ясният ум вижда правилно.", "Марк Аврелий")
    ])

# =========================
# INPUT (ENTER ENABLED)
# =========================
with st.form("form", clear_on_submit=True):

    question = "Как се чувстваш?" if lang == "Български" else "How do you feel?"

    user_input = st.text_input(question)

    send = st.form_submit_button("Изпрати" if lang == "Български" else "Send")

    if send and user_input:

        reflection, quote, author = smart_response(user_input)

        st.session_state.history.append({
            "time": datetime.now().strftime("%H:%M"),
            "user": user_input,
            "r": reflection,
            "q": quote,
            "a": author
        })

# =========================
# DAILY MIND HISTORY (NEW FEATURE)
# =========================
if st.session_state.history:

    st.markdown("## 🧠 Дневна емоционална история" if lang == "Български" else "## 🧠 Daily Emotional Log")

# =========================
# OUTPUT
# =========================
for item in reversed(st.session_state.history):

    st.markdown(f"**{item['time']} · 🧠 {item['user']}**")

    st.info(item["r"])

    st.markdown(f"💭 *{item['q']}*")

    st.caption(f"— {item['a']}")

    st.markdown("---")
