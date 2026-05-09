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
# 🧠 EMOTION RESPONSES
# =========================
EMOTION_BANK = {
"stress": t(
"⟡ Налице е когнитивно претоварване. Фокус върху една задача ще върне яснота и контрол.",
"⟡ Cognitive overload detected. Focusing on one task restores clarity and control."
),

"sad": t(
"⟡ Това е състояние на емоционална тежест. То е временно и не определя посоката ти.",
"⟡ This is an emotional heaviness state. Temporary and not defining your direction."
),

"anger": t(
"⟡ Засечена е повишена реактивност. Пауза преди действие ще намали напрежението.",
"⟡ Elevated reactivity detected. A pause before action reduces tension."
),

"work_stress": t(
"⟡ Работен дисбаланс или напрежение. Средата може да не съответства на нуждите ти.",
"⟡ Work imbalance or tension detected. Environment may not match your needs."
),

"inspiration": t(
"⟡ Повишена яснота и мотивация. Подходящ момент за действие и създаване.",
"⟡ High clarity and motivation. A good moment for action and creation."
),

"neutral": t(
"⟡ Стабилно състояние без доминираща емоция.",
"⟡ Stable state with no dominant emotion."
)
}

# =========================
# 🧠 SMART EMOTION BRAIN (FIXED VERSION)
# =========================
def detect_emotion(text):
    ttxt = text.lower().strip()

    # WORK CONTEXT
    if any(w in ttxt for w in ["работа", "офис", "колеги", "шеф"]) and any(w in ttxt for w in ["нещаст", "зле", "стрес", "тежко", "не ми харесва"]):
        return "work_stress"

    # EMOTIONAL HEAVINESS
    if any(w in ttxt for w in ["не ми е добре", "празно", "срив", "тъж", "разбит", "нещаст"]):
        return "sad"

    # STRESS / OVERLOAD
    if any(w in ttxt for w in ["стрес", "напрег", "претовар", "overwhelmed", "много ми е"]):
        return "stress"

    # ANGER
    if any(w in ttxt for w in ["ядос", "гнев", "драз", "не мога да понасям"]):
        return "anger"

    # RECOVERY / FATIGUE (IMPORTANT FIX)
    if any(w in ttxt for w in ["умор", "изтощен", "нямам сила", "искам да спя", "нямам енергия"]):
        return "stress"

    # INSPIRATION
    if any(w in ttxt for w in ["вдъхнов", "мотив", "енергич", "flow", "ясно ми е"]):
        return "inspiration"

    return "neutral"

def get_response(text):
    return EMOTION_BANK[detect_emotion(text)]

# =========================
# ANALYTICS (CLEAN VERSION)
# =========================
def analyze():
    counts = {
        "stress": 0,
        "sad": 0,
        "anger": 0,
        "work_stress": 0,
        "inspiration": 0,
        "neutral": 0
    }

    for h in st.session_state.history:
        e = h["emotion"]
        counts[e] += 1

    dominant = max(counts, key=counts.get)
    return counts, dominant

def label(key):
    labels = {
        "stress": "⚡ Когнитивно натоварване",
        "sad": "🌫 Емоционално напрежение",
        "anger": "🔥 Повишен натиск",
        "work_stress": "💼 Работно напрежение",
        "inspiration": "🚀 Висока ангажираност",
        "neutral": "⚖ Стабилно състояние"
    }
    return labels[key]

# =========================
# LAYOUT
# =========================
left, center, right = st.columns([1, 2.3, 1.3])

# =========================
# LEFT (ANALYSIS)
# =========================
with left:
    st.markdown("## 🧠 Анализ")

    if st.session_state.history:
        counts, dominant = analyze()

        for k, v in counts.items():
            st.metric(label(k), v)

        st.markdown("---")
        st.info(f"⟡ Доминиращо:\n\n{label(dominant)}")
    else:
        st.write("Няма данни.")

# =========================
# CENTER (CHAT)
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
# RIGHT (WELLBEING)
# =========================
with right:
    st.markdown("## 🧘 Well-being система")

    with st.expander("🎯 Фокус"):
        st.write("Deep Work · Single-tasking · Приоритети")

    with st.expander("🧠 Възстановяване"):
        st.write("Паузи · Хидратация · Рестарт на вниманието")

    with st.expander("⚖ Баланс"):
        st.write("Натоварване ↔ Почивка · Ум ↔ Енергия")
