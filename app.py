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
# LANGUAGE SYSTEM
# =========================
lang = st.selectbox("Language", ["Български", "English"])

def t(bg, en):
    return bg if lang == "Български" else en

# =========================
# STYLE FIX (CENTER HEADER)
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

h1, h2, h3, p {
    text-align: center;
}

.block-container {
    padding-top: 2rem;
    max-width: 1100px;
    margin: auto;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER (FIXED CENTER)
# =========================
st.markdown("<h1 style='text-align:center;'>Inner Compass</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>H-TECH · DIGITAL SYSTEMS</h3>", unsafe_allow_html=True)

motto = t(
    "Продължаваме заедно... по-смирени, по-смислени, по-стоически.",
    "We continue together... more humble, more meaningful, more stoic."
)

st.markdown(f"<p style='text-align:center;'>⟡ {motto}</p>", unsafe_allow_html=True)
st.markdown("---")

# =========================
# 🧠 EMOTION ENGINE (FIXED REAL WORLD INPUTS)
# =========================

EMOTION_BANK = {
"stress": t(
"⟡ Това напрежение показва претоварване. Не е нужно да решиш всичко наведнъж — само следващата стъпка.",
"⟡ This tension indicates overload. You don't need to solve everything, only the next step."
),

"sad": t(
"⟡ Това състояние показва вътрешна тежест. То не е постоянно и не определя посоката ти.",
"⟡ This state reflects internal heaviness. It is temporary and does not define your direction."
),

"anger": t(
"⟡ Силната емоция показва натрупан вътрешен натиск. Пауза преди реакция променя всичко.",
"⟡ Strong emotion indicates internal pressure. A pause before reaction changes everything."
),

"work_stress": t(
"⟡ Работната неудовлетвореност често идва от несъответствие между среда и вътрешни нужди.",
"⟡ Work dissatisfaction often comes from mismatch between environment and internal needs."
),

"inspiration": t(
"⟡ Това състояние показва яснота и разширено мислене. Добър момент за създаване.",
"⟡ This state reflects clarity and expanded thinking. A good moment for creation."
),

"neutral": t(
"⟡ Стабилно вътрешно състояние без доминиращо напрежение.",
"⟡ Stable internal state without dominant tension."
)
}

# =========================
# DETECTION (FIXED - REAL PHRASES)
# =========================
def detect_emotion(text):
    ttxt = text.lower()

    # STRONG NEGATIVE STATES
    if any(w in ttxt for w in ["не ми е добре", "зле съм", "not well", "feeling bad"]):
        return "sad"

    if any(w in ttxt for w in ["нещастна съм", "нещастен съм", "не съм щастлив", "unhappy"]):
        return "work_stress"

    # STANDARD STATES
    if any(w in ttxt for w in ["стрес", "напрег", "stress"]):
        return "stress"

    if any(w in ttxt for w in ["яд", "гнев", "раздраз"]):
        return "anger"

    if any(w in ttxt for w in ["вдъхнов", "мотив", "енерг"]):
        return "inspiration"

    return "neutral"

def get_response(text):
    return EMOTION_BANK[detect_emotion(text)]

# =========================
# ANALYSIS ENGINE (FIXED LOGIC)
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

    # weighted dominance (IMPORTANT FIX)
    weighted_score = {
        "stress": counts["stress"] * 2,
        "sad": counts["sad"] * 2,
        "anger": counts["anger"] * 3,
        "work_stress": counts["work_stress"] * 3,
        "inspiration": counts["inspiration"] * 1,
        "neutral": counts["neutral"] * 0.5
    }

    dominant = max(weighted_score, key=weighted_score.get)

    return counts, dominant

def stoic_insight(dominant):
    return t(
        {
            "stress": "⟡ Стоически поглед: напрежението идва от разпилено внимание.",
            "sad": "⟡ Това е временно състояние, не крайна реалност.",
            "anger": "⟡ Контролът започва с пауза преди реакция.",
            "work_stress": "⟡ Несъответствието между среда и вътрешни нужди създава напрежение.",
            "inspiration": "⟡ Яснотата е момент на подредено съзнание.",
            "neutral": "⟡ Балансът е стабилност, не липса на емоции."
        }.get(dominant, "⟡ Наблюдение без интерпретация."),
        {
            "stress": "⟡ Stoic view: tension comes from divided attention.",
            "sad": "⟡ Temporary state, not reality.",
            "anger": "⟡ Control begins with pause.",
            "work_stress": "⟡ Mismatch creates internal tension.",
            "inspiration": "⟡ Clarity is ordered mind.",
            "neutral": "⟡ Balance is stability, not absence."
        }.get(dominant, "⟡ Neutral observation.")
    )

# =========================
# LAYOUT (FIXED BALANCE)
# =========================
left, center, right = st.columns([0.9, 2.2, 1.3])

# =========================
# LEFT → SMALL ANALYSIS (FIXED VISUAL WEIGHT)
# =========================
with left:
    st.markdown("## 🧠 " + t("Анализ", "Analysis"))

    if st.session_state.history:
        counts, dominant = analyze()

        st.metric(t("Стрес", "Stress"), counts["stress"])
        st.metric(t("Тъга", "Sad"), counts["sad"])
        st.metric(t("Яд", "Anger"), counts["anger"])
        st.metric(t("Работа", "Work"), counts["work_stress"])

        st.markdown("---")

        st.markdown("### ⟡")
        st.info(t("Доминиращо:", "Dominant: ") + dominant)

        st.markdown("### 🏛️")
        st.write(stoic_insight(dominant))

    else:
        st.write(t("Няма данни", "No data yet"))

# =========================
# CENTER → CHAT (MAIN FOCUS)
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
# RIGHT → WELLBEING (FULL BG FIXED + EXPANDED)
# =========================
with right:
    st.markdown("## 🧘 " + t("Система", "System"))

    with st.expander(t("Фокус", "Focus")):
        st.write(t(
            "Deep Work – дълбока концентрация\nSingle-tasking – една задача\n3 приоритета на ден",
            "Deep Work – deep focus\nSingle-tasking – one task\n3 priorities per day"
        ))

    with st.expander(t("Възстановяване", "Recovery")):
        st.write(t(
            "Почивки между цикли\nХидратация и движение\nОсъзнат край на деня",
            "Break cycles\nHydration and movement\nConscious shutdown"
        ))

    with st.expander(t("Баланс", "Balance")):
        st.write(t(
            "Ум ↔ Тяло ↔ Енергия\nНатоварване ↔ Почивка",
            "Mind ↔ Body ↔ Energy\nLoad ↔ Rest"
        ))
