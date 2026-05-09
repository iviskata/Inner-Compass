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
# 🧠 FIXED EMOTION ENGINE (STRICT MATCHING)
# =========================
EMOTION_BANK = {
"stress": t(
"⟡ Присъства напрежение, свързано с претоварване на вниманието. Фокус върху една задача възстановява яснота.",
"⟡ Tension detected due to overloaded attention. Single focus restores clarity."
),

"sad": t(
"⟡ Наблюдава се емоционална тежест. Това е временно състояние на вътрешна обработка.",
"⟡ Emotional heaviness detected. This is a temporary processing state."
),

"anger": t(
"⟡ Засечена е висока емоционална реакция. Пауза преди действие е препоръчителна.",
"⟡ High emotional reaction detected. Pause before response is recommended."
),

"work_stress": t(
"⟡ Установено е професионално неудовлетворение или напрежение в работна среда.",
"⟡ Work-related dissatisfaction or tension detected."
),

"inspiration": t(
"⟡ Налице е повишена яснота и когнитивна активност. Подходящ момент за действие.",
"⟡ Elevated clarity and cognitive activation detected."
),

"neutral": t(
"⟡ Балансирано вътрешно състояние без доминираща емоция.",
"⟡ Balanced internal state with no dominant emotion."
)
}

# =========================
# FIXED DETECTION (VERY IMPORTANT)
# =========================
def detect_emotion(text):
    ttxt = text.lower().strip()

    # WORK STRESS (priority first)
    if any(p in ttxt for p in [
        "нещастна съм в работата",
        "не съм щастлив в работата",
        "не ми харесва работата",
        "работата ме натоварва",
        "work unhappy"
    ]):
        return "work_stress"

    # ANGER
    if any(p in ttxt for p in [
        "ядосвам се",
        "яд ме",
        "гнев",
        "раздраз",
        "very angry"
    ]):
        return "anger"

    # SAD / LOW STATE
    if any(p in ttxt for p in [
        "не ми е добре",
        "зле съм",
        "тъжна съм",
        "тъжен съм",
        "not well",
        "feeling bad"
    ]):
        return "sad"

    # STRESS
    if any(p in ttxt for p in [
        "стрес",
        "напрег",
        "претовар",
        "stress"
    ]):
        return "stress"

    # INSPIRATION
    if any(p in ttxt for p in [
        "вдъхнов",
        "мотив",
        "енергич",
        "inspired"
    ]):
        return "inspiration"

    return "neutral"

def get_response(text):
    return EMOTION_BANK[detect_emotion(text)]

# =========================
# ANALYTICS ENGINE
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
        counts[h["emotion"]] += 1

    dominant = max(counts, key=counts.get)
    return counts, dominant

# =========================
# LAYOUT
# =========================
left, center, right = st.columns([1, 2.3, 1.3])

# =========================
# LEFT → ANALYSIS (SMALL + CLEAN)
# =========================
with left:
    st.markdown("## 🧠 " + t("Анализ на състоянието", "State Analysis"))

    if st.session_state.history:
        counts, dominant = analyze()

        st.metric(t("Стрес", "Stress"), counts["stress"])
        st.metric(t("Тъга", "Sad"), counts["sad"])
        st.metric(t("Яд", "Anger"), counts["anger"])
        st.metric(t("Работа", "Work"), counts["work_stress"])

        st.markdown("---")

        st.info(t("Доминиращо състояние:", "Dominant state:") + f" {dominant}")

    else:
        st.write(t("Няма данни.", "No data yet."))

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
# RIGHT → PROFESSIONAL WELLBEING MODULE
# =========================
with right:
    st.markdown("## 🧘 Well-being & Cognitive Support System")

    st.markdown(t(
        "Система за поддържане на психична устойчивост и баланс между натоварване и възстановяване.",
        "A system for maintaining mental resilience and balance between load and recovery."
    ))

    with st.expander(t("🎯 Система за фокус", "Focus System")):
        st.write(t(
            "• Deep Work – дълбока концентрация без прекъсване\n"
            "• Single-tasking – една ясна когнитивна линия\n"
            "• Приоритизация – максимум 3 задачи дневно",
            "• Deep Work – uninterrupted focus\n"
            "• Single-tasking – one cognitive stream\n"
            "• Prioritization – max 3 tasks per day"
        ))

    with st.expander(t("🧠 Система за възстановяване", "Recovery System")):
        st.write(t(
            "• Пауза цикли – редовно разтоварване на вниманието\n"
            "• Физическа регулация – вода и движение\n"
            "• Осъзнат край на деня – отделяне от работа",
            "• Break cycles – attention reset\n"
            "• Physical regulation – hydration & movement\n"
            "• Conscious shutdown – separation from work"
        ))

    with st.expander(t("⚖️ Система за баланс", "Balance System")):
        st.write(t(
            "• Баланс между натоварване и възстановяване\n"
            "• Баланс между мислене и действие\n"
            "• Баланс между външни и вътрешни фактори",
            "• Balance between load and recovery\n"
            "• Balance between thinking and action\n"
            "• Balance between external and internal input"
        ))
