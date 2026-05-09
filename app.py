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
# EMOTION RESPONSES
# =========================
EMOTION_BANK = {
"stress": t(
"⟡ Когнитивно претоварване. Намали задачите и върни фокуса върху една стъпка.",
"⟡ Cognitive overload detected. Reduce tasks and focus on one step."
),

"sad": t(
"⟡ Емоционална тежест. Това състояние е временно и ще премине.",
"⟡ Emotional heaviness. This state is temporary."
),

"anger": t(
"⟡ Повишена реактивност. Пауза преди действие ще намали напрежението.",
"⟡ High reactivity detected. Pause before action reduces tension."
),

"work_stress": t(
"⟡ Работно напрежение. Средата може да не съвпада с вътрешните ти нужди.",
"⟡ Work stress detected. Environment may not match your needs."
),

"recovery": t(
"⟡ Налице е изтощение. Това е сигнал за възстановяване, не слабост.",
"⟡ Fatigue detected. This is a signal for recovery, not weakness."
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
# 🧠 FIXED EMOTION BRAIN
# =========================
def detect_emotion(text):
    ttxt = text.lower().strip()

    # WORK STRESS
    if any(w in ttxt for w in ["работа", "офис", "шеф", "колеги"]) and any(w in ttxt for w in ["стрес", "нещаст", "зле", "не харесвам"]):
        return "work_stress"

    # SAD
    if any(w in ttxt for w in ["не ми е добре", "празно", "срив", "тъж", "разбит"]):
        return "sad"

    # STRESS
    if any(w in ttxt for w in ["стрес", "напрег", "претовар", "overwhelmed"]):
        return "stress"

    # ANGER
    if any(w in ttxt for w in ["ядос", "гнев", "драз"]):
        return "anger"

    # 🧯 RECOVERY (FIXED - IMPORTANT)
    if any(w in ttxt for w in ["уморена съм", "уморен съм", "изморена", "изморен", "изтощен", "нямам сила", "нямам енергия", "искам да спя"]):
        return "recovery"

    # INSPIRATION
    if any(w in ttxt for w in ["вдъхнов", "мотив", "енергич", "flow"]):
        return "inspiration"

    return "neutral"

def get_response(text):
    return EMOTION_BANK[detect_emotion(text)]

# =========================
# ANALYTICS
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

def label(key):
    labels = {
        "stress": "⚡ Когнитивно натоварване",
        "sad": "🌫 Емоционално напрежение",
        "anger": "🔥 Повишен натиск",
        "work_stress": "💼 Работно напрежение",
        "recovery": "🧯 Нужда от възстановяване",
        "inspiration": "🚀 Висока ангажираност",
        "neutral": "⚖ Стабилно състояние"
    }
    return labels[key]

# =========================
# LAYOUT
# =========================
left, center, right = st.columns([1, 2.3, 1.3])

# =========================
# LEFT
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
# CENTER
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
# RIGHT
# =========================
with right:
    st.markdown("## 🧘 Well-being система")

    with st.expander("🎯 Фокус"):
        st.write("Deep Work · Single-tasking · Приоритети")

    with st.expander("🧠 Възстановяване"):
        st.write("Почивки · Хидратация · Рестарт")

    with st.expander("⚖ Баланс"):
        st.write("Натоварване ↔ Почивка · Ум ↔ Енергия")
