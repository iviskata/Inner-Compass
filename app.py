import streamlit as st
import random
from datetime import datetime

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Inner Compass",
    page_icon="🏛️",
    layout="centered"
)

# =========================
# SESSION STATE
# =========================
if "history" not in st.session_state:
    st.session_state.history = []

# =========================
# LANGUAGE
# =========================
lang = st.selectbox("Language", ["Български", "English"])

motto = "Продължаваме заедно... по-смирени, по-смислени, по-стоически." if lang == "Български" \
        else "We continue together... more humble, more meaningful, more stoic."

# =========================
# STYLE (clean + centered)
# =========================
st.markdown("""
<style>

.stApp {
    background:
    radial-gradient(circle at top, rgba(59,130,246,0.18), transparent 35%),
    radial-gradient(circle at bottom, rgba(168,85,247,0.12), transparent 30%),
    #020617;
    color: #e2e8f0;
    text-align: center;
}

.block-container {
    max-width: 850px;
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
# 🧠 EMOTION ENGINE (KEEPED - CLEAN)
# =========================
EMOTION_BANK = {

"fatigue": [
"⟡ Умората показва, че системата е достигнала граница на капацитет. Това не е сигнал за натиск, а за възстановяване.",
"⟡ Когато енергията спадне, ефективността пада експоненциално. Почивката е част от продуктивността, не нейна противоположност.",
"⟡ Възстановяването стабилизира цялата система и позволява по-ясно мислене след това."
],

"stress": [
"⟡ Стресът идва от разпределено внимание върху твърде много посоки. Фокусът върху една задача възстановява реда.",
"⟡ Напрежението не е реалността, а интерпретация на сложност. Намаляването на скоростта връща яснота.",
"⟡ Умът създава спешност, която не винаги съществува."
],

"sad": [
"⟡ Тъгата е естествен процес на вътрешна обработка. Тя не изисква бързо решение.",
"⟡ Това е временен емоционален цикъл, не постоянна характеристика.",
"⟡ Най-добрият подход е позволяване, не съпротива."
],

"anxiety": [
"⟡ Тревожността идва от бъдещи сценарии, които не съществуват в момента.",
"⟡ Връщането в настоящето намалява вътрешния шум.",
"⟡ Не е нужно да предвиждаш всичко, за да действаш правилно."
],

"anger": [
"⟡ Гневът е интензивен импулс, който изпреварва логическата обработка.",
"⟡ Пауза между импулс и действие променя резултата.",
"⟡ Емоцията не е проблем, реакцията към нея е ключът."
],

"neutral": [
"⟡ Системата е в балансирано състояние.",
"⟡ Няма доминиращ емоционален натиск.",
"⟡ Това е оптимално състояние за ясно мислене."
]
}

# =========================
# DETECTOR
# =========================
def detect_emotion(text):
    t = text.lower()

    if any(w in t for w in ["умор", "измор", "tired"]):
        return "fatigue"
    if any(w in t for w in ["стрес", "stress"]):
        return "stress"
    if any(w in t for w in ["тъж", "sad"]):
        return "sad"
    if any(w in t for w in ["тревож", "страх"]):
        return "anxiety"
    if any(w in t for w in ["гнев", "яд"]):
        return "anger"

    return "neutral"

def get_response(text):
    return random.choice(EMOTION_BANK[detect_emotion(text)])

# =========================
# INPUT
# =========================
question = "Как се чувстваш?" if lang == "Български" else "How do you feel?"

with st.form("form", clear_on_submit=True):
    user_input = st.text_input(question)
    send = st.form_submit_button("Изпрати" if lang == "Български" else "Send")

    if send and user_input:
        response = get_response(user_input)

        st.session_state.history.append({
            "time": datetime.now().strftime("%H:%M"),
            "text": user_input,
            "response": response,
            "emotion": detect_emotion(user_input)
        })

# =========================
# HISTORY
# =========================
for item in reversed(st.session_state.history):
    st.markdown(f"**{item['time']} · {item['text']}**")
    st.info(item["response"])
    st.markdown("---")

# =========================
# 🧠 EMOTION ANALYTICS (RETURNED FIXED)
# =========================
st.markdown("## 🧠 Emotional System Analysis")

if st.session_state.history:

    counts = {
        "fatigue": 0,
        "stress": 0,
        "sad": 0,
        "anxiety": 0,
        "anger": 0,
        "neutral": 0
    }

    for h in st.session_state.history:
        counts[h["emotion"]] += 1

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("⟡ Fatigue", counts["fatigue"])
        st.metric("⟡ Stress", counts["stress"])

    with col2:
        st.metric("⟡ Sad", counts["sad"])
        st.metric("⟡ Anxiety", counts["anxiety"])

    with col3:
        st.metric("⟡ Anger", counts["anger"])
        st.metric("⟡ Neutral", counts["neutral"])

    dominant = max(counts, key=counts.get)

    st.markdown("---")

    st.info(f"⟡ Dominant emotional state: {dominant}")

# =========================
# 🧘 WELLBEING SYSTEM (FIXED UI + COLLAPSIBLE)
# =========================
st.markdown("## 🧘 Well-being System")

col1, col2 = st.columns(2)

with col1:
    with st.expander("🎯 Focus System"):
        st.markdown("""
        ⟡ Deep Work  
        Поддържане на дълги периоди на концентрация без прекъсване.

        ⟡ Single-tasking  
        Една задача = една ясна когнитивна линия.

        ⟡ Planning  
        Ограничаване до 3 основни приоритета на деня.
        """)

with col2:
    with st.expander("🧠 Recovery System"):
        st.markdown("""
        ⟡ Break cycles  
        Редовни паузи за възстановяване на вниманието.

        ⟡ Hydration  
        Поддържа когнитивна яснота и стабилност.

        ⟡ Shutdown ritual  
        Осъзнат край на работния ден без натоварване.
        """)
