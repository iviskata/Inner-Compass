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

st.markdown(f"<p style='text-align:center;'>⟡ {t('Продължаваме заедно... по-смирени, по-смислени, по-стоически.',
'We continue together... more humble, more meaningful, more stoic.')}</p>", unsafe_allow_html=True)

st.markdown("---")

# =========================
# 🧠 EMOTION DATASET (BRAIN)
# =========================

RECOVERY = [
"уморена съм","уморен съм","изморена съм","изморен съм","изтощена съм","изтощен съм",
"нямам енергия","нямам сила","срината съм","изцедена съм","не мога повече",
"празна съм","искам да спя","burnout","не издържам","психически изтощена"
]

STRESS = [
"стресирана съм","стресиран съм","напрегната съм","напрегнат съм","претоварена съм",
"претоварен съм","overwhelmed","твърде много ми е","хаос","не смогвам",
"не ми стига времето","под напрежение съм"
]

SAD = [
"не ми е добре","тъжна съм","тъжен съм","празнота","разбита съм","разбит съм",
"вътрешно тежко","самотна съм","изгубена съм","няма смисъл","сривам се"
]

ANGER = [
"ядосана съм","ядосан съм","бесна съм","бесен съм","дразня се","кипя",
"не издържам","изнервена съм","изнервен съм","всичко ме дразни"
]

FOCUS_OVERLOAD = [
"не мога да мисля","твърде много мисли","хаос в главата","не мога да се фокусирам",
"объркана съм","объркан съм","mental fog","блокирана съм","блокиран съм"
]

INSPIRATION = [
"вдъхновена съм","вдъхновен съм","мотивирана съм","мотивиран съм","flow",
"ясно ми е","имам енергия","готов съм","готова съм","искам да действам"
]

# =========================
# 🧠 EMOTION ENGINE (SMART MATCH)
# =========================
def detect_emotion(text):
    ttxt = text.lower()

    def match(group):
        return any(p in ttxt for p in group)

    if match(RECOVERY):
        return "recovery"
    if match(STRESS):
        return "stress"
    if match(SAD):
        return "sad"
    if match(ANGER):
        return "anger"
    if match(FOCUS_OVERLOAD):
        return "focus"
    if match(INSPIRATION):
        return "inspiration"

    return "neutral"

# =========================
# RESPONSES
# =========================
RESPONSES = {
"recovery": t(
"⟡ Наблюдава се ясно изтощение. Това е сигнал за възстановяване, не слабост.",
"⟡ Clear fatigue detected. This is a signal for recovery, not weakness."
),

"stress": t(
"⟡ Налице е натрупано напрежение. Намаляването на задачите ще върне контрол.",
"⟡ Accumulated stress detected. Reducing tasks restores control."
),

"sad": t(
"⟡ Емоционална тежест. Това състояние е временно и не определя посоката ти.",
"⟡ Emotional heaviness. This state is temporary."
),

"anger": t(
"⟡ Повишена реактивност. Пауза ще намали интензитета на реакцията.",
"⟡ High reactivity detected. Pause reduces intensity."
),

"focus": t(
"⟡ Когнитивен хаос. Нужно е опростяване на задачите и фокус.",
"⟡ Cognitive chaos detected. Simplification and focus needed."
),

"inspiration": t(
"⟡ Висока яснота и енергия. Подходящ момент за действие.",
"⟡ High clarity and energy. Good moment for action."
),

"neutral": t(
"⟡ Стабилно състояние без доминираща емоция.",
"⟡ Stable state with no dominant emotion."
)
}

# =========================
# ANALYSIS
# =========================
def analyze():
    counts = {
        "recovery": 0,
        "stress": 0,
        "sad": 0,
        "anger": 0,
        "focus": 0,
        "inspiration": 0,
        "neutral": 0
    }

    for h in st.session_state.history:
        counts[h["emotion"]] += 1

    dominant = max(counts, key=counts.get)
    return counts, dominant

# =========================
# UI LAYOUT
# =========================
left, center, right = st.columns([1, 2.3, 1.3])

# =========================
# LEFT - ANALYSIS
# =========================
with left:
    st.markdown("## 🧠 Анализ")

    if st.session_state.history:
        counts, dominant = analyze()

        for k, v in counts.items():
            st.metric(k, v)

        st.markdown("---")
        st.info(f"⟡ Доминиращо състояние:\n\n{dominant}")
    else:
        st.write("Няма данни.")

# =========================
# CENTER - CHAT
# =========================
with center:

    q = t("Как се чувстваш?", "How do you feel?")

    with st.form("form", clear_on_submit=True):
        user_input = st.text_input(q)
        send = st.form_submit_button(t("Изпрати", "Send"))

        if send and user_input:
            emotion = detect_emotion(user_input)

            st.session_state.history.append({
                "time": datetime.now().strftime("%H:%M"),
                "text": user_input,
                "emotion": emotion,
                "response": RESPONSES[emotion]
            })

    st.markdown("---")

    for h in reversed(st.session_state.history):
        st.markdown(f"**{h['time']} · {h['text']}**")
        st.info(h["response"])
        st.markdown("---")

# =========================
# RIGHT - WELLBEING
# =========================
with right:
    st.markdown("## 🧘 Well-being система")

    with st.expander("🎯 Фокус"):
        st.write("Deep Work · Single-tasking · Приоритети")

    with st.expander("🧠 Възстановяване"):
        st.write("Почивки · Хидратация · Рестарт")

    with st.expander("⚖ Баланс"):
        st.write("Натоварване ↔ Почивка · Ум ↔ Енергия")
