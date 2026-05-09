import streamlit as st
import random
from datetime import datetime

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Inner Compass",
    page_icon="🏛️",
    layout="wide"
)

# =========================
# STATE
# =========================
if "history" not in st.session_state:
    st.session_state.history = []

# =========================
# LANGUAGE
# =========================
lang = st.selectbox("Language", ["Български", "English"])

def t(bg, en):
    return bg if lang == "Български" else en

# =========================
# MOTTO
# =========================
motto = t(
    "Продължаваме заедно... по-смирени, по-смислени, по-стоически.",
    "We continue together... more humble, more meaningful, more stoic."
)

# =========================
# STYLE
# =========================
st.markdown("""
<style>

.stApp {
    background:
    radial-gradient(circle at top, rgba(59,130,246,0.18), transparent 35%),
    radial-gradient(circle at bottom, rgba(168,85,247,0.12), transparent 30%),
    #020617;
    color: #e2e8f0;
}

.block-container {
    padding-top: 2rem;
}

h1,h2,h3,p {
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.title("Inner Compass")
st.markdown("### H-TECH · DIGITAL SYSTEMS")
st.markdown(f"> {motto}")
st.markdown("---")

# =========================
# 🧠 EMOTION ENGINE
# =========================
EMOTION_BANK = {

"fatigue": [
t(
"⟡ Умората е сигнал за нужда от възстановяване.",
"⟡ Fatigue is a signal that recovery is needed."
),
t(
"⟡ Натискът в това състояние намалява ефективността.",
"⟡ Pushing in this state reduces efficiency."
),
t(
"⟡ Почивката е част от прогреса.",
"⟡ Rest is part of progress."
)
],

"stress": [
t(
"⟡ Стресът идва от разпределено внимание.",
"⟡ Stress comes from divided attention."
),
t(
"⟡ Фокусът върху една задача възстановява яснота.",
"⟡ Focus restores clarity."
),
t(
"⟡ Забавянето намалява напрежението.",
"⟡ Slowing down reduces tension."
)
],

"neutral": [
t("⟡ Баланс.", "⟡ Balance."),
t("⟡ Стабилност.", "⟡ Stability."),
t("⟡ Няма напрежение.", "⟡ No tension.")
]
}

# =========================
# DETECTOR
# =========================
def detect_emotion(text):
    ttxt = text.lower()

    if any(w in ttxt for w in ["умор", "tired"]):
        return "fatigue"
    if any(w in ttxt for w in ["стрес", "stress"]):
        return "stress"

    return "neutral"

def get_response(text):
    return random.choice(EMOTION_BANK[detect_emotion(text)])

# =========================
# EMOTION ANALYTICS (LIVE)
# =========================
def analyze():
    counts = {"fatigue":0, "stress":0, "neutral":0}

    for h in st.session_state.history:
        counts[h["emotion"]] += 1

    dominant = max(counts, key=counts.get)

    return counts, dominant

# =========================
# LAYOUT (3 COLUMNS)
# =========================
left, center, right = st.columns([1.2, 2, 1.2])

# =========================
# LEFT PANEL → EMOTION SUMMARY
# =========================
with left:
    st.markdown("## 🧠 " + t("Анализ", "Analysis"))

    if st.session_state.history:
        counts, dominant = analyze()

        st.metric(t("Умора", "Fatigue"), counts["fatigue"])
        st.metric(t("Стрес", "Stress"), counts["stress"])
        st.metric(t("Баланс", "Neutral"), counts["neutral"])

        st.markdown("---")
        st.info(t(
            f"⟡ Доминиращо състояние: {dominant}",
            f"⟡ Dominant state: {dominant}"
        ))
    else:
        st.write(t("Няма данни още.", "No data yet."))

# =========================
# CENTER → INPUT + HISTORY
# =========================
with center:

    question = t("Как се чувстваш?", "How do you feel?")

    with st.form("form", clear_on_submit=True):
        user_input = st.text_input(question)
        send = st.form_submit_button(t("Изпрати", "Send"))

        if send and user_input:
            emotion = detect_emotion(user_input)
            response = get_response(user_input)

            st.session_state.history.append({
                "time": datetime.now().strftime("%H:%M"),
                "text": user_input,
                "response": response,
                "emotion": emotion
            })

    st.markdown("---")

    for item in reversed(st.session_state.history):
        st.markdown(f"**{item['time']} · {item['text']}**")
        st.info(item["response"])
        st.markdown("---")

# =========================
# RIGHT PANEL → WELLBEING
# =========================
with right:
    st.markdown("## 🧘 " + t("Система", "System"))

    with st.expander(t("Фокус", "Focus")):
        st.markdown(t(
            "⟡ Deep Work\n⟡ Single-tasking\n⟡ 3 приоритета на ден",
            "⟡ Deep Work\n⟡ Single-tasking\n⟡ 3 priorities per day"
        ))

    with st.expander(t("Възстановяване", "Recovery")):
        st.markdown(t(
            "⟡ Почивки\n⟡ Хидратация\n⟡ Край на деня ритуал",
            "⟡ Breaks\n⟡ Hydration\n⟡ Shutdown ritual"
        ))

    with st.expander(t("Баланс", "Balance")):
        st.markdown(t(
            "⟡ Натоварване ↔ Почивка\n⟡ Тяло ↔ Ум",
            "⟡ Load ↔ Rest\n⟡ Body ↔ Mind"
        ))
