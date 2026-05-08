import streamlit as st
import random

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

/* INPUT CENTER */
.stTextInput {
    display: flex;
    justify-content: center;
}

.stTextInput input {
    width: 100%;
    max-width: 500px;
    height: 60px;
    border-radius: 16px;
    font-size: 18px;
}

/* BUTTON CENTER */
.stButton {
    display: flex;
    justify-content: center;
}

.stButton button {
    width: 100%;
    max-width: 500px;
    height: 48px;
    border-radius: 14px;
    background: linear-gradient(90deg,#2563eb,#7c3aed);
    color: white;
    border: none;
}

/* CENTER TEXT */
h1, h3, p {
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER (LANGUAGE AWARE)
# =========================
if lang == "Български":
    st.title("Inner Compass 🏛️")
    st.markdown("### H-TECH · DIGITAL SYSTEMS")
    st.markdown("> Продължаваме заедно... по-смирени, по-смислени, по-стоически.")
    question = "Как се чувстваш?"
    button = "Изпрати"
else:
    st.title("Inner Compass 🏛️")
    st.markdown("### H-TECH · DIGITAL SYSTEMS")
    st.markdown("> We continue together... more humble, more meaningful, more stoic.")
    question = "How do you feel?"
    button = "Send"

st.markdown("---")

# =========================
# STOIC RESPONSES
# =========================
responses_bg = [
    ("💭 Това ще премине.", "Не страдаме от събитията, а от интерпретацията им.", "Епиктет"),
    ("💭 Спокойствието е сила.", "Контролирай това, което зависи от теб.", "Марк Аврелий"),
    ("💭 Почивката е прогрес.", "Понякога спирането е напредък.", "Сенека"),
    ("💭 Бъди тук и сега.", "Животът се случва в настоящия момент.", "Стоицизъм")
]

responses_en = [
    ("💭 This will pass.", "We suffer not from events, but from our interpretation of them.", "Epictetus"),
    ("💭 Calm is strength.", "Control what is within your power.", "Marcus Aurelius"),
    ("💭 Rest is progress.", "Sometimes stopping is moving forward.", "Seneca"),
    ("💭 Be present.", "Life happens in the present moment.", "Stoicism")
]

def get_response(text):

    t = text.lower()

    pool = responses_bg if lang == "Български" else responses_en

    if any(x in t for x in ["sad", "тъж"]):
        return pool[0]

    if any(x in t for x in ["stress", "стрес"]):
        return pool[1]

    if any(x in t for x in ["tired", "умор"]):
        return pool[2]

    return random.choice(pool)

# =========================
# INPUT (ENTER WORKS)
# =========================
with st.form("form", clear_on_submit=True):

    user_input = st.text_input(question)

    submitted = st.form_submit_button(button)

    if submitted and user_input:

        r, q, a = get_response(user_input)

        st.session_state.history.append({
            "user": user_input,
            "r": r,
            "q": q,
            "a": a
        })

# =========================
# OUTPUT
# =========================
for item in reversed(st.session_state.history):

    st.markdown(f"**🧠 {item['user']}**")

    st.info(item["r"])

    st.markdown(f"💭 {item['q']}")

    st.caption(f"— {item['a']}")

    st.markdown("---")
