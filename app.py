import streamlit as st
import random
from datetime import datetime

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="H-Tech · Inner Compass",
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
lang = st.selectbox("🌍 Language", ["Български", "English"])

# =========================
# STYLE
# =========================
st.markdown("""
<style>

.stApp {
    text-align: center;
    background:
    radial-gradient(circle at top, rgba(59,130,246,0.18), transparent 35%),
    radial-gradient(circle at bottom, rgba(168,85,247,0.12), transparent 30%),
    #020617;
    color: #e2e8f0;
}

.stTextInput, .stButton {
    display: flex;
    justify-content: center;
}

.stTextInput input {
    width: 100%;
    max-width: 520px;
    height: 60px;
    border-radius: 16px;
    font-size: 18px;
}

.stButton button {
    width: 100%;
    max-width: 520px;
    height: 48px;
    border-radius: 14px;
    background: linear-gradient(90deg,#2563eb,#7c3aed);
    color: white;
    border: none;
}

h1, h3, p {
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.title("Inner Compass 🏛️")
st.markdown("### H-TECH · DIGITAL SYSTEMS")
st.markdown("> Продължаваме заедно... по-смирени, по-смислени, по-стоически.")
st.markdown("---")

# =========================
# STOIC RESPONSES
# =========================
responses = [
    ("💭 Това ще премине.", "Не страдаме от събитията, а от интерпретацията им.", "Епиктет"),
    ("💭 Спокойствието е сила.", "Контролирай това, което зависи от теб.", "Марк Аврелий"),
    ("💭 Почивката също е прогрес.", "Понякога спирането е напредък.", "Сенека"),
    ("💭 Бъди тук и сега.", "Животът се случва в настоящия момент.", "Стоицизъм"),
    ("💭 Всичко е наред.", "Балансът е истинската сила.", "Стоицизъм")
]

# =========================
# SMART ENGINE (NOW WITH POSITIVE MOOD)
# =========================
def get_response(text):

    t = text.lower()

    # Negative moods
    if any(x in t for x in ["стрес", "stress", "panic"]):
        return responses[1]

    if any(x in t for x in ["тъж", "sad"]):
        return responses[0]

    if any(x in t for x in ["умор", "tired", "burnout"]):
        return responses[2]

    # Positive moods
    if any(x in t for x in ["щаст", "happy", "радост", "добре", "ок", "great", "good"]):
        return responses[4]

    # Default
    return random.choice(responses)

# =========================
# INPUT
# =========================
question = "Как се чувстваш?" if lang == "Български" else "How do you feel?"

with st.form("form", clear_on_submit=True):

    user_input = st.text_input(question)

    send = st.form_submit_button("Изпрати" if lang == "Български" else "Send")

    if send and user_input:

        r, q, a = get_response(user_input)

        st.session_state.history.append({
            "time": datetime.now().strftime("%H:%M"),
            "text": user_input,
            "r": r,
            "q": q,
            "a": a
        })

# =========================
# HISTORY
# =========================
for item in reversed(st.session_state.history):

    st.markdown(f"**🧠 {item['time']} · {item['text']}**")
    st.info(item["r"])
    st.markdown(f"💭 {item['q']}")
    st.caption(f"— {item['a']}")
    st.markdown("---")

# =========================
# DAILY SUMMARY (BALANCED)
# =========================
st.markdown("## 📊 End of Day Reflection")

if st.session_state.history:

    texts = [h["text"].lower() for h in st.session_state.history]

    stress = sum("стрес" in t or "stress" in t for t in texts)
    sad = sum("тъж" in t or "sad" in t for t in texts)
    tired = sum("умор" in t or "tired" in t for t in texts)

    positive = sum(
        any(x in t for x in ["щаст", "happy", "добре", "ок", "радост", "good"])
        for t in texts
    )

    st.markdown("### 🧠 Баланс на деня")

    st.write(f"😊 Позитивни моменти: {positive}")
    st.write(f"😣 Стрес моменти: {stress}")
    st.write(f"😔 Тъга моменти: {sad}")
    st.write(f"😴 Умора моменти: {tired}")

    st.markdown("---")

    # Summary logic
    if positive >= max(stress, sad, tired):
        st.success("💭 Денят е бил позитивен. Добър баланс и добра енергия.")
        st.caption("— Стоицизъм")

    elif stress > sad and stress > tired:
        st.info("💭 Денят беше напрегнат. Помни: контролирай реакцията си.")
        st.caption("— Марк Аврелий")
st.markdown("---")

st.markdown("## 🧠 Well-being Guide for Developers")

st.markdown("""
### 💻 Продуктивни навици за по-добър фокус и здрав ум

#### 🧠 Deep Work
Работи 60–90 мин без прекъсване върху една задача.

#### 👁️ Правило 20-20-20
На всеки 20 мин гледай 20 секунди в далечината.

#### 🚶 Movement Breaks
Ставай на всеки час за кратко движение.

#### 💧 Хидратация
Пий вода редовно – влияе на концентрацията.

#### 🧘 Мини reset
1–2 мин дълбоко дишане при стрес.

#### 🎯 Single-tasking
Една задача = по-добър резултат.

#### 🌙 Shutdown ritual
Затвори работния ден осъзнато, без мисли за задачи.
""")
    elif tired > stress:
        st.info("💭 Умората показва нужда от почивка.")
        st.caption("— Сенека")

    else:
        st.info("💭 Денят е бил балансиран. Продължавай така.")
        st.caption("— Стоицизъм")

else:
    st.write("Още няма данни за деня.")
