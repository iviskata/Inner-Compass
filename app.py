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
lang = st.selectbox("Language", ["Български", "English"])

# =========================
# STYLE (clean + premium)
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
    height: 60px;
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
st.title("Inner Compass")
st.markdown("### H-TECH · DIGITAL SYSTEMS")
st.markdown("> quiet intelligence · structured reflection · stoic AI system")
st.markdown("---")

# =========================
# 🧠 INNER COMPASS BRAIN v2
# =========================

EMOTION_BANK = {
    "stress": [
        "⟡ Понякога напрежението идва от опита да носим твърде много неща едновременно. Намали до следващата стъпка.",
        "⟡ Не всичко изисква контрол сега. Кратка пауза може да върне яснота.",
        "⟡ Спокойствието не идва от липса на проблеми, а от начина, по който ги носиш.",
        "⟡ Ако всичко е тежко, избери само едно малко действие.",
        "⟡ Напрежението често означава, че умът е над капацитета си."
    ],

    "sad": [
        "— Тъгата не е враг. Тя е процес.",
        "— Някои състояния просто трябва да бъдат преживени, не поправени.",
        "— Дай време. Вътрешните състояния имат цикъл.",
        "— Тежестта не е постоянна.",
        "— Това също ще се промени."
    ],

    "tired": [
        "⟡ Умората не е слабост, а сигнал.",
        "⟡ Почивката е част от прогреса.",
        "⟡ Тялото не се противопоставя — то комуникира.",
        "⟡ Понякога най-доброто действие е да спреш.",
        "⟡ Възстановяването е процес, не пауза."
    ],

    "happy": [
        "◇ Това състояние има стойност.",
        "◇ Радостта стабилизира вътрешния свят.",
        "◇ Запомни какво я е създало.",
        "◇ Позитивните състояния са ресурс.",
        "◇ Това е момент за осъзнаване, не за бързане."
    ],

    "neutral": [
        "⟡ Състоянието е стабилно.",
        "⟡ Не всяка мисъл изисква реакция.",
        "⟡ Наблюдавай без натиск.",
        "⟡ Яснотата идва от тишината.",
        "⟡ Просто бъди в момента."
    ]
}

def detect_emotion(text):
    t = text.lower()

    if any(w in t for w in ["стрес", "напрег", "притесн", "stress", "overthinking"]):
        return "stress"

    if any(w in t for w in ["тъж", "sad", "сам", "празно"]):
        return "sad"

    if any(w in t for w in ["умор", "tired", "изтощ", "нямам енергия"]):
        return "tired"

    if any(w in t for w in ["щаст", "happy", "добре", "радост"]):
        return "happy"

    return "neutral"

def get_response(text):
    emotion = detect_emotion(text)
    return random.choice(EMOTION_BANK[emotion])

# =========================
# INPUT
# =========================
question = "Как се чувстваш?" if lang == "Български" else "How do you feel?"

with st.form("form", clear_on_submit=True):
    user_input = st.text_input(question)
    send = st.form_submit_button("Изпрати" if lang == "Български" else "Send")

    if send and user_input:
        response = get_response(user_input)

        st.session_state.history.append({
            "time": datetime.now().strftime("%H:%M"),
            "text": user_input,
            "response": response
        })

# =========================
# HISTORY
# =========================
for item in reversed(st.session_state.history):
    st.markdown(f"**{item['time']} · {item['text']}**")
    st.info(item["response"])
    st.markdown("---")

# =========================
# DAILY SUMMARY
# =========================
st.markdown("## Reflection")

if st.session_state.history:

    texts = [h["text"].lower() for h in st.session_state.history]

    stress = sum("стрес" in t or "stress" in t for t in texts)
    sad = sum("тъж" in t or "sad" in t for t in texts)
    tired = sum("умор" in t or "tired" in t for t in texts)
    happy = sum("щаст" in t or "радост" in t for t in texts)

    st.write(f"Positive: {happy}")
    st.write(f"Stress: {stress}")
    st.write(f"Sad: {sad}")
    st.write(f"Tired: {tired}")

    st.markdown("---")

    if happy >= max(stress, sad, tired):
        st.success("Balanced positive day")
    elif stress > tired:
        st.info("High stress pattern detected")
    elif tired > stress:
        st.info("Recovery needed")
    else:
        st.info("Stable mental state")

# =========================
# WELLBEING DASHBOARD
# =========================
st.markdown("---")
st.markdown("## Well-being System")

left, right = st.columns(2)

with left:
    st.markdown("### Focus")

    with st.expander("Deep Work"):
        st.write("60–90 min focused work without interruption.")

    with st.expander("Single-tasking"):
        st.write("One task at a time improves clarity.")

    with st.expander("Planning"):
        st.write("Start with 3 priorities per day.")

with right:
    st.markdown("### Recovery")

    with st.expander("Breaks"):
        st.write("Regular pauses restore focus.")

    with st.expander("Hydration"):
        st.write("Water supports cognitive function.")

    with st.expander("Shutdown"):
        st.write("End the day consciously, without work carryover.")
