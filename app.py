import streamlit as st
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
# STYLE (TYPOGRAPHY SYSTEM v2)
# =========================
st.markdown("""
<style>

/* BASE */
html, body {
    font-family: Inter, system-ui, sans-serif;
    background: #020617;
    color: #e2e8f0;
}

/* LAYOUT */
.block-container {
    max-width: 1100px;
    padding-top: 2rem;
}

/* =========================
   TYPOGRAPHY SYSTEM
========================= */

/* PRIMARY (CHAT) */
.primary-text {
    font-size: 18px;
    font-weight: 500;
    line-height: 1.5;
}

/* SECONDARY (ANALYSIS) */
.secondary-text {
    font-size: 15px;
    font-weight: 400;
    opacity: 0.85;
    line-height: 1.4;
}

/* TERTIARY (WELLBEING) */
.tertiary-text {
    font-size: 13px;
    font-weight: 400;
    opacity: 0.75;
    line-height: 1.4;
}

/* META (MOTTO / SMALL UI TEXT) */
.meta-text {
    font-size: 13px;
    font-weight: 300;
    opacity: 0.6;
    letter-spacing: 0.3px;
}

/* INPUT EMPHASIS */
.stTextInput input {
    font-size: 18px !important;
    height: 55px;
    font-weight: 500;
}

/* CENTER TITLE */
h1 {
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("<h1>Inner Compass</h1>", unsafe_allow_html=True)

motto = t(
    "⟡ Продължаваме заедно... по-смирени, по-смислени, по-стоически. ⟡",
    "⟡ We continue together... more humble, more meaningful, more stoic. ⟡"
)

st.markdown(f"<p class='meta-text' style='text-align:center;'>{motto}</p>", unsafe_allow_html=True)

st.markdown("---")

# =========================
# EMOTION RESPONSES
# =========================
RESPONSES = {
"stress": t(
"⟡ Когнитивно претоварване. Намаляването на задачите ще върне яснота.",
"⟡ Cognitive overload detected. Reducing tasks restores clarity."
),

"sad": t(
"⟡ Емоционална тежест. Това състояние е временно.",
"⟡ Emotional heaviness. This is temporary."
),

"anger": t(
"⟡ Повишена реактивност. Пауза преди действие намалява интензитета.",
"⟡ High reactivity detected. Pause reduces intensity."
),

"work_stress": t(
"⟡ Работно напрежение. Средата може да не съвпада с вътрешните ти нужди.",
"⟡ Work stress detected. Environment mismatch possible."
),

"recovery": t(
"⟡ Изтощение. Това е сигнал за нужда от възстановяване, не слабост.",
"⟡ Fatigue detected. Signal for need of recovery, not weakness."
),

"inspiration": t(
"⟡ Висока яснота и мотивация. Подходящ момент за действие.",
"⟡ High clarity and motivation. Good moment for action."
),

"neutral": t(
"⟡ Стабилно състояние без доминираща емоция.",
"⟡ Stable state with no dominant emotion."
)
}

# =========================
# EMOTION ENGINE
# =========================
def detect_emotion(text):
    ttxt = text.lower()

    if any(w in ttxt for w in ["уморена съм","уморен съм","изморена","изморен","изтощен","нямам сила","нямам енергия"]):
        return "recovery"

    if any(w in ttxt for w in ["стрес","напрег","претовар","overwhelmed"]):
        return "stress"

    if any(w in ttxt for w in ["не ми е добре","тъж","празно","разбит"]):
        return "sad"

    if any(w in ttxt for w in ["ядос","гнев","драз"]):
        return "anger"

    if any(w in ttxt for w in ["работа","офис","колеги","шеф"]):
        if any(w in ttxt for w in ["зле","стрес","не харесвам","тежко"]):
            return "work_stress"

    if any(w in ttxt for w in ["вдъхнов","мотив","flow","енергич"]):
        return "inspiration"

    return "neutral"

def get_response(text):
    return RESPONSES[detect_emotion(text)]

# =========================
# ANALYSIS
# =========================
def analyze():
    counts = {
        "stress": 0,
        "sad": 0,
        "anger": 0,
        "work_stress": 0,
        "recovery": 0,
        "inspiration": 0,
        "neutral": 0
    }

    for h in st.session_state.history:
        counts[h["emotion"]] += 1

    dominant = max(counts, key=counts.get)
    return counts, dominant

# =========================
# LAYOUT
# =========================
left, center, right = st.columns([1, 2.5, 1.2])

# =========================
# LEFT - ANALYSIS
# =========================
with left:
    st.markdown("### 🧠 Анализ")

    if st.session_state.history:
        counts, dominant = analyze()

        for k, v in counts.items():
            st.markdown(f"<p class='secondary-text'>{k}: {v}</p>", unsafe_allow_html=True)

        st.markdown("---")
        st.markdown(f"<p class='secondary-text'>Доминиращо: {dominant}</p>", unsafe_allow_html=True)

    else:
        st.markdown("<p class='secondary-text'>Няма данни</p>", unsafe_allow_html=True)

# =========================
# CENTER - CHAT (PRIORITY)
# =========================
with center:

    question = t("Как се чувстваш?", "How do you feel?")

    with st.form("form", clear_on_submit=True):
        user_input = st.text_input(question)
        send = st.form_submit_button(t("Изпрати", "Send"))

        if send and user_input:
            emotion = detect_emotion(user_input)

            st.session_state.history.append({
                "time": datetime.now().strftime("%H:%M"),
                "text": user_input,
                "emotion": emotion,
                "response": get_response(user_input)
            })

    st.markdown("---")

    for h in reversed(st.session_state.history):
        st.markdown(f"<p class='primary-text'><b>{h['time']} · {h['text']}</b></p>", unsafe_allow_html=True)
        st.info(h["response"])
        st.markdown("---")

# =========================
# RIGHT - WELLBEING (SECONDARY COLLAPSIBLE STYLE)
# =========================
with right:
    st.markdown("### 🧘 Well-being система")

    with st.expander("🎯 Фокус"):
        st.markdown("<p class='tertiary-text'>Deep Work · Single-tasking · Приоритети</p>", unsafe_allow_html=True)

    with st.expander("🧠 Ментално състояние"):
        st.markdown("<p class='tertiary-text'>Когнитивно натоварване · Стрес модели · Яснота</p>", unsafe_allow_html=True)

    with st.expander("🧯 Възстановяване"):
        st.markdown("<p class='tertiary-text'>Почивки · Хидратация · Рестарт на вниманието</p>", unsafe_allow_html=True)

    with st.expander("⚖ Баланс"):
        st.markdown("<p class='tertiary-text'>Натоварване ↔ Почивка · Устойчив ритъм</p>", unsafe_allow_html=True)
