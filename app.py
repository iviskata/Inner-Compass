import streamlit as st
import random

# =========================
# CONFIG
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
# HEADER
# =========================
st.title("Inner Compass 🏛️")

st.markdown(
    "### H-TECH · DIGITAL SYSTEMS"
)

st.markdown(
    "> *Продължаваме заедно... по-смирени, по-смислени, по-стоически.*"
)

st.markdown("---")

# =========================
# STOIC RESPONSES
# =========================
responses = [
    ("💭 Това ще премине.", "Не страдаме от събитията, а от нашата интерпретация.", "Епиктет"),
    ("💭 Спокойствието е сила.", "Контролирай това, което зависи от теб.", "Марк Аврелий"),
    ("💭 Почивката също е прогрес.", "Понякога спирането е напредък.", "Сенека"),
    ("💭 Бъди тук и сега.", "Животът се случва в настоящия момент.", "Стоицизъм")
]

# =========================
# SIMPLE AI LOGIC
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
# INPUT
# =========================
user_input = st.text_input("Как се чувстваш?")

if st.button("Изпрати") and user_input:

    r, q, a = get_response(user_input)

    st.session_state.history.append({
        "user": user_input,
        "r": r,
        "q": q,
        "a": a
    })

# =========================
# OUTPUT (CARDS)
# =========================
for item in reversed(st.session_state.history):

    st.markdown(f"**🧠 {item['user']}**")

    st.info(item["r"])

    st.markdown(f"💭 *{item['q']}*")

    st.caption(f"— {item['a']}")

    st.markdown("---")
