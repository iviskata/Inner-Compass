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
# SESSION
# =========================
if "history" not in st.session_state:
    st.session_state.history = []

# =========================
# STYLE (CENTER FIX)
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

/* INPUT CENTER FIX */
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

/* TEXT CENTER */
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

st.markdown(
    "> Продължаваме заедно... по-смирени, по-смислени, по-стоически."
)

st.markdown("---")

# =========================
# STOIC RESPONSES
# =========================
responses = [
    ("💭 Това ще премине.", "Не страдаме от събитията, а от интерпретацията им.", "Епиктет"),
    ("💭 Спокойствието е сила.", "Контролирай това, което зависи от теб.", "Марк Аврелий"),
    ("💭 Почивката е прогрес.", "Понякога спирането е напредък.", "Сенека"),
    ("💭 Бъди тук и сега.", "Животът се случва в настоящия момент.", "Стоицизъм")
]

# =========================
# ENGINE
# =========================
def get_response(text):

    t = text.lower()

    if "тъж" in t or "sad" in t:
        return responses[0]

    if "стрес" in t or "stress" in t:
        return responses[1]

    if "умор" in t or "tired" in t:
        return responses[2]

    return random.choice(responses)

# =========================
# INPUT (ENTER WORKS)
# =========================
with st.form("form", clear_on_submit=True):

    user_input = st.text_input("Как се чувстваш?")

    submitted = st.form_submit_button("Изпрати")

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
