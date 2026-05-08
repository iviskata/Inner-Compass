import streamlit as st
import random
from collections import Counter

# =========================
# SESSION
# =========================
if "history" not in st.session_state:
    st.session_state.history = []

# =========================
# STOIC RESPONSES
# =========================
responses = [
    ("💭 Това ще премине.", "Не страдаме от събитията, а от нашата интерпретация.", "Епиктет"),
    ("💭 Спокойствието е сила.", "Контролирай това, което зависи от теб.", "Марк Аврелий"),
    ("💭 Почивката също е прогрес.", "Понякога спирането е напредък.", "Сенека"),
    ("💭 Бъди тук и сега.", "Животът се случва в настоящия момент.", "Стоицизъм")
]

def get_response(text):
    t = text.lower()

    if "стрес" in t or "stress" in t:
        return responses[1]
    if "тъж" in t or "sad" in t:
        return responses[0]
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
        "text": user_input,
        "r": r,
        "q": q,
        "a": a
    })

# =========================
# MAIN OUTPUT
# =========================
for item in reversed(st.session_state.history):

    st.markdown(f"**🧠 {item['text']}**")
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

    st.markdown("### 🧠 Емоционален баланс за деня")

    st.write(f"Стрес моменти: {stress}")
    st.write(f"Тъга моменти: {sad}")
    st.write(fУмора моменти: {tired}")

    st.markdown("---")

    # Stoic summary logic
    if stress > sad and stress > tired:
        st.info("💭 Денят беше напрегнат. Помни: не всичко зависи от теб.")
        st.caption("— Марк Аврелий")

    elif tired > stress:
        st.info("💭 Денят показва умора. Почивката е част от силата.")
        st.caption("— Сенека")

    else:
        st.info("💭 Денят е бил балансиран. Продължавай така.")
        st.caption("— Стоицизъм")

else:
    st.write("Още няма данни за деня.")
