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

st.markdown(f"""
<p style='text-align:center;'>
⟡ {t(
"Продължаваме заедно... по-смирени, по-смислени, по-стоически.",
"We continue together... more humble, more meaningful, more stoic."
)}
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# =========================
# EMOTION RESPONSES
# =========================
RESPONSES = {
"stress": t(
"⟡ Налице е когнитивно претоварване. Намаляването на задачите ще възстанови яснотата.",
"⟡ Cognitive overload detected. Reducing tasks restores clarity."
),

"sad": t(
"⟡ Емоционална тежест. Това състояние е временно и не определя посоката ти.",
"⟡ Emotional heaviness. This state is temporary."
),

"anger": t(
"⟡ Повишена реактивност. Пауза преди действие намалява интензитета.",
"⟡ High reactivity detected. Pause reduces intensity."
),

"work_stress": t(
"⟡ Работно напрежение. Средата може да не съвпада с вътрешните ти нужди.",
"⟡ Work stress detected. Environment may not match your needs."
),

"recovery": t(
"⟡ Налице е изтощение. Това е сигнал за нужда от възстановяване, не слабост.",
"⟡ Fatigue detected. This is a signal for need of recovery, not weakness."
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
# 🧠 EMOTION ENGINE
# =========================
def detect_emotion(text):
    ttxt = text.lower()

    if any(w in ttxt for w in ["работа", "офис", "шеф", "колеги"]) and any(w in ttxt for w in ["стрес", "не харесвам", "зле"]):
        return "work_stress"

    if any(w in ttxt for w in ["не ми е добре", "тъж", "празно", "разбит"]):
        return "sad"

    if any(w in ttxt for w in ["стрес", "напрег", "претовар", "overwhelmed"]):
        return "stress"

    if any(w in ttxt for w in ["ядос", "гнев", "драз"]):
        return "anger"

    # ✅ FIXED: recovery is ONLY state, not solution
    if any(w in ttxt for w in [
        "уморена съм", "уморен съм", "изморена съм", "изморен съм",
        "изтощена съм", "изтощен съм", "нямам сила", "нямам енергия",
        "искам да спя"
    ]):
        return "recovery"

    if any(w in ttxt for w in ["вдъхнов", "мотив", "енергич", "flow"]):
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
left, center, right = st.columns([1, 2.3, 1.3])

# =========================
# LEFT - ANALYSIS
# =========================
with left:
    st.markdown("## 🧠 Анализ")

    if st.session_state.history:
        counts, dominant = analyze()

        for k, v in counts.items():
            st.metric(label=k, value=v)

        st.markdown("---")
        st.info(f"⟡ Доминиращо състояние:\n\n{dominant}")
    else:
        st.write("Няма данни.")

# =========================
# CENTER - CHAT
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
        st.markdown(f"**{h['time']} · {h['text']}**")
        st.info(h["response"])
        st.markdown("---")

# =========================
# RIGHT - WELL-BEING SYSTEM (IMPROVED)
# =========================
with right:
    st.markdown("## 🧘 Well-being система")

    st.markdown("""
### 🎯 Фокус и продуктивност
⟡ Поддържане на ясни приоритети  
⟡ Работа на блокове (deep work)  
⟡ Избягване на мултитаскинг  

---

### 🧠 Ментално състояние
⟡ Следене на когнитивно натоварване  
⟡ Разпознаване на умора и претоварване  
⟡ Ранно откриване на стрес модели  

---

### 🧯 Възстановяване
⟡ Планирани паузи и рестарт на вниманието  
⟡ Намаляване на входяща информация  
⟡ Подобряване на енергийния баланс  

---

### ⚖ Общ баланс
⟡ Баланс между натоварване и почивка  
⟡ Устойчив ритъм на работа  
⟡ Поддържане на стабилност в дългосрочен план  
""")
