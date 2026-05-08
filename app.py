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
    ("💭 Балансът е сила.", "Спокойният ум вижда ясно.", "Стоицизъм")
]

def get_response(text):
    t = text.lower()

    if "стрес" in t or "stress" in t:
        return responses[1]
    if "тъж" in t or "sad" in t:
        return responses[0]
    if "умор" in t or "tired" in t:
        return responses[2]
    if "добре" in t or "happy" in t or "ok" in t:
        return responses[4]

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
# DAILY SUMMARY (BOTTOM)
# =========================
st.markdown("## 📊 End of Day Reflection")

if st.session_state.history:

    texts = [h["text"].lower() for h in st.session_state.history]

    stress = sum("стрес" in t or "stress" in t for t in texts)
    sad = sum("тъж" in t or "sad" in t for t in texts)
    tired = sum("умор" in t or "tired" in t for t in texts)
    positive = sum("добре" in t or "ok" in t or "happy" in t for t in texts)

    st.write(f"😊 Позитивни: {positive}")
    st.write(f"😣 Стрес: {stress}")
    st.write(f"😔 Тъга: {sad}")
    st.write(f"😴 Умора: {tired}")

    st.markdown("---")

    if positive >= max(stress, sad, tired):
        st.success("💭 Балансиран и позитивен ден.")
    elif stress > sad and stress > tired:
        st.info("💭 Напрегнат ден — контролирай реакцията.")
    elif tired > stress:
        st.info("💭 Умора — време за почивка.")
    else:
        st.info("💭 Балансиран ден.")

# =========================
# WELL-BEING DASHBOARD (TWO COLUMNS)
# =========================
st.markdown("---")
st.markdown("## 🧠 Developer Well-being Dashboard")

left, right = st.columns(2)

with left:
    st.markdown("### 🎯 Focus & Productivity")

    with st.expander("💻 Deep Work"):
        st.write("60–90 мин фокус без прекъсване върху една задача.")

    with st.expander("🎯 Single-tasking"):
        st.write("Една задача наведнъж = по-висока продуктивност.")

    with st.expander("📵 Digital silence"):
        st.write("Изключи нотификации по време на фокус.")

    with st.expander("🧠 Planning"):
        st.write("Започни деня с 3 ясни приоритета.")

with right:
    st.markdown("### 🧘 Health & Recovery")

    with st.expander("👁️ 20-20-20 rule"):
        st.write("На всеки 20 мин гледай 20 сек в далечината.")

    with st.expander("🚶 Movement breaks"):
        st.write("Ставай на всеки час и се движи.")

    with st.expander("💧 Hydration"):
        st.write("Водата влияе директно на концентрацията.")

    with st.expander("🌙 Shutdown ritual"):
        st.write("Затвори деня осъзнато и без работа след това.")
