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
    max-width: 1150px;
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
st.markdown("<h1 style='text-align:center;'>Inner Compass</h1>", unsafe_allow_html=True)

motto = t(
    "Продължаваме заедно... по-смирени, по-смислени, по-стоически.",
    "We continue together... more humble, more meaningful, more stoic."
)

st.markdown(f"<p style='text-align:center;'>⟡ {motto}</p>", unsafe_allow_html=True)
st.markdown("---")

# =========================
# 🧠 EMOTION ENGINE
# =========================
EMOTION_BANK = {
"stress": t(
"⟡ Това показва когнитивно претоварване. Фокус върху една задача възстановява яснота.",
"⟡ Cognitive overload detected. Focus restores clarity."
),

"sad": t(
"⟡ Емоционална тежест. Това състояние е временно и преходно.",
"⟡ Emotional heaviness. This state is temporary."
),

"anger": t(
"⟡ Повишена емоционална реакция. Пауза преди действие е ключова.",
"⟡ Elevated emotional response. Pause before action is key."
),

"work_stress": t(
"⟡ Работно напрежение или неудовлетворение от средата.",
"⟡ Work-related stress or dissatisfaction."
),

"inspiration": t(
"⟡ Повишена яснота и мотивация. Подходящ момент за действие.",
"⟡ High clarity and motivation. Good moment for action."
),

"neutral": t(
"⟡ Стабилно състояние без доминираща емоция.",
"⟡ Stable state with no dominant emotion."
)
}

# =========================
# FIXED DETECTION (IMPORTANT)
# =========================
def detect_emotion(text):
    ttxt = text.lower().strip()

    if any(p in ttxt for p in ["нещастна съм в работата", "не съм щастлив в работата", "работата ме напряга"]):
        return "work_stress"

    if any(p in ttxt for p in ["не ми е добре", "зле съм", "тъжна съм", "тъжен съм"]):
        return "sad"

    if any(p in ttxt for p in ["ядосвам", "гнев", "раздраз"]):
        return "anger"

    if any(p in ttxt for p in ["стрес", "напрег", "претовар"]):
        return "stress"

    if any(p in ttxt for p in ["вдъхнов", "мотив", "енерг"]):
        return "inspiration"

    return "neutral"

def get_response(text):
    return EMOTION_BANK[detect_emotion(text)]

# =========================
# 🧠 ANALYSIS (NEW PROFESSIONAL MODEL - BG)
# =========================
def analyze():
    counts = {
        "cognitive_load": 0,
        "pressure": 0,
        "emotional_strain": 0,
        "stable": 0,
        "engagement": 0,
        "recovery": 0
    }

    for h in st.session_state.history:
        e = h["emotion"]

        if e in ["stress"]:
            counts["cognitive_load"] += 1

        elif e in ["anger"]:
            counts["pressure"] += 1

        elif e in ["sad", "work_stress"]:
            counts["emotional_strain"] += 1

        elif e in ["neutral"]:
            counts["stable"] += 1

        elif e in ["inspiration"]:
            counts["engagement"] += 1

        else:
            counts["recovery"] += 1

    dominant = max(counts, key=counts.get)
    return counts, dominant


def label(key):
    labels = {
        "cognitive_load": "🧠 Когнитивно натоварване",
        "pressure": "⚡ Повишен натиск",
        "emotional_strain": "🌫 Емоционално напрежение",
        "stable": "⚖ Стабилно състояние",
        "engagement": "🚀 Висока ангажираност",
        "recovery": "🧯 Нужда от възстановяване"
    }
    return labels[key]

# =========================
# LAYOUT
# =========================
left, center, right = st.columns([1, 2.3, 1.3])

# =========================
# LEFT → ANALYSIS (FIXED)
# =========================
with left:
    st.markdown("## 🧠 Работен профил")

    if st.session_state.history:
        counts, dominant = analyze()

        for k, v in counts.items():
            st.metric(label(k), v)

        st.markdown("---")

        st.info(f"⟡ Доминиращо състояние:\n\n{label(dominant)}")

    else:
        st.write("Няма данни.")

# =========================
# CENTER → CHAT
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
# RIGHT → WELLBEING SYSTEM
# =========================
with right:
    st.markdown("## 🧘 Система за баланс и продуктивност")

    with st.expander("🎯 Система за фокус"):
        st.write("Deep Work · Single-tasking · Приоритети")

    with st.expander("🧠 Система за възстановяване"):
        st.write("Почивки · Хидратация · Рестарт на вниманието")

    with st.expander("⚖ Система за баланс"):
        st.write("Ум ↔ Тяло ↔ Енергия · Натоварване ↔ Почивка")
