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
# 🧠 EMOTION ENGINE (IMPROVED DETECTION)
# =========================

EMOTION_BANK = {
"stress": "⟡ Усещането за напрежение идва от претоварен фокус. Най-ясният път е да се върнеш към една стъпка.",
"anger": "⟡ Гневът е силен импулс, който изисква пауза преди действие.",
"sad": "⟡ Тъгата е процес, не състояние за решение.",
"inspiration": "⟡ Това е момент на разширено възприятие и вътрешна яснота.",
"neutral": "⟡ Стабилно състояние без доминираща емоция."
}

def detect_emotion(text):
    ttxt = text.lower()

    # ANGER (expanded)
    if any(w in ttxt for w in ["яд", "ядос", "гнев", "разяр", "раздраз"]):
        return "anger"

    # SAD (expanded)
    if any(w in ttxt for w in ["тъж", "плача", "самот", "болка"]):
        return "sad"

    # STRESS (expanded)
    if any(w in ttxt for w in ["стрес", "напрег", "претовар", "pressure"]):
        return "stress"

    # INSPIRATION
    if any(w in ttxt for w in ["вдъхнов", "мотив", "силен съм", "енерг"]):
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
        "anger": 0,
        "sad": 0,
        "inspiration": 0,
        "neutral": 0
    }

    for h in st.session_state.history:
        counts[h["emotion"]] += 1

    # real dominant logic (NOT fake balance)
    dominant = max(counts, key=counts.get)

    return counts, dominant

def stoic_insight(dominant, counts):
    if dominant == "stress":
        return "⟡ Стоическа перспектива: напрежението не е проблемът — разпиленият фокус е."
    if dominant == "anger":
        return "⟡ Стоиците биха казали: паузата преди реакция е мястото на свободата."
    if dominant == "sad":
        return "⟡ Това е временно вътрешно движение, не дефиниция на реалността."
    if dominant == "inspiration":
        return "⟡ Яснотата идва, когато умът е свободен от вътрешен шум."
    return "⟡ Балансът не е липса на емоции, а стабилност въпреки тях."

# =========================
# LAYOUT (FIXED RATIO)
# =========================
left, center, right = st.columns([1, 2.2, 1])

# =========================
# LEFT → ANALYSIS (SMALLER)
# =========================
with left:
    st.markdown("## 🧠 " + t("Анализ", "Analysis"))

    if st.session_state.history:
        counts, dominant = analyze()

        st.metric(t("Стрес", "Stress"), counts["stress"])
        st.metric(t("Яд", "Anger"), counts["anger"])
        st.metric(t("Тъга", "Sad"), counts["sad"])
        st.metric(t("Вдъхнов", "Inspiration"), counts["inspiration"])

        st.markdown("---")

        st.markdown("### ⟡ Dominant")
        st.info(dominant)

        st.markdown("### 🏛️ Insight")
        st.write(stoic_insight(dominant, counts))

    else:
        st.write(t("Няма данни", "No data yet"))

# =========================
# CENTER → CHAT (BIGGEST)
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
# RIGHT → WELLBEING (CLEAN)
# =========================
with right:
    st.markdown("## 🧘 " + t("Система", "System"))

    with st.expander(t("Фокус", "Focus")):
        st.write(t(
            "Deep Work, Single-tasking, 3 приоритета",
            "Deep Work, Single-tasking, 3 priorities"
        ))

    with st.expander(t("Възстановяване", "Recovery")):
        st.write(t(
            "Почивки, вода, край на деня",
            "Breaks, hydration, shutdown"
        ))

    with st.expander(t("Баланс", "Balance")):
        st.write(t(
            "Ум ↔ Тяло ↔ Време",
            "Mind ↔ Body ↔ Time"
        ))
