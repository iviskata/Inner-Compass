import streamlit as st
import random

# =================================
# PAGE
# =================================
st.set_page_config(
    page_title="Inner Compass",
    page_icon="🏛️",
    layout="centered"
)

# =================================
# SESSION
# =================================
if "history" not in st.session_state:
    st.session_state.history = []

# =================================
# STYLE
# =================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
    radial-gradient(circle at top, rgba(59,130,246,0.18), transparent 35%),
    radial-gradient(circle at bottom, rgba(168,85,247,0.12), transparent 30%),
    #020617;

    color: #e2e8f0;
}

/* TITLE */
h1 {
    text-align: center;
    font-size: 44px;
    color: white;
    margin-bottom: 0px;
}

/* SUBTITLE */
.subtitle {
    text-align: center;
    color: #94a3b8;
    margin-bottom: 25px;
    font-size: 13px;
    letter-spacing: 2px;
}

/* LANGUAGE */
.lang {
    text-align: center;
    font-size: 17px;
    margin-bottom: -5px;
}

/* SELECT */
div[data-baseweb="select"] {
    max-width: 130px;
    margin: auto;
    margin-bottom: 20px;
}

/* INPUT FIX (CENTER CURSOR + TEXT) */
.stTextInput input {
    height: 62px;
    border-radius: 16px;
    font-size: 18px;

    background: rgba(15,23,42,0.9);
    color: white;

    border: 1px solid rgba(255,255,255,0.08);

    padding-left: 18px;

    /* 🔥 FIX */
    line-height: 62px;
    padding-top: 0px;
    padding-bottom: 0px;
}

/* BUTTON */
.stButton button {
    width: 100%;
    height: 50px;
    border-radius: 14px;

    background: linear-gradient(90deg,#2563eb,#7c3aed);
    color: white;
    border: none;
    font-size: 16px;
}

/* USER */
.user {
    color: #60a5fa;
    margin-top: 25px;
    margin-bottom: 8px;
}

/* CARD */
.card {
    padding: 20px;
    border-radius: 18px;
    background: rgba(15,23,42,0.72);
    border: 1px solid rgba(255,255,255,0.06);
    line-height: 1.7;
}

/* QUOTE */
.quote {
    margin-top: 12px;
    color: #cbd5e1;
    font-style: italic;
}

/* AUTHOR */
.author {
    margin-top: 8px;
    color: #94a3b8;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# =================================
# HEADER
# =================================
st.markdown("<h1>Inner Compass 🏛️</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>◉ calm stoic reflection engine ◉</div>", unsafe_allow_html=True)

# =================================
# LANGUAGE
# =================================
st.markdown("<div class='lang'>🌍</div>", unsafe_allow_html=True)

lang = st.selectbox("", ["Български", "English"], label_visibility="collapsed")

# =================================
# STOIC DATA
# =================================
data = {
    "sad": [
        ("💭 Това ще мине.", "Не страдаме от събитията, а от представите си.", "Епиктет"),
        ("💭 Тъгата не е вечна.", "Всичко се променя.", "Марк Аврелий")
    ],
    "stress": [
        ("💭 Спри за момент.", "Имаш контрол само над ума си.", "Марк Аврелий"),
        ("💭 Дишай.", "Спокойният ум вижда ясно.", "Сенека")
    ],
    "tired": [
        ("💭 Почивката е сила.", "Понякога спирането е напредък.", "Сенека"),
        ("💭 Не бързай.", "Природата не бърза.", "Епиктет")
    ]
}

def detect(text):
    t = text.lower()

    if "тъж" in t or "sad" in t:
        return "sad"
    if "стрес" in t or "stress" in t:
        return "stress"
    if "умор" in t or "tired" in t:
        return "tired"

    return "default"

def respond(text):

    e = detect(text)

    if e == "default":

        if lang == "English":
            return ("💭 Stay present.", "Your mind shapes your world.", "Marcus Aurelius")

        return ("💭 Бъди тук.", "Мислите оформят реалността.", "Марк Аврелий")

    return random.choice(data[e])

# =================================
# INPUT
# =================================
with st.form("form", clear_on_submit=True):

    q = "Как се чувстваш?" if lang == "Български" else "How do you feel?"

    text = st.text_input(q)

    send = st.form_submit_button("Изпрати" if lang == "Български" else "Send")

    if send and text:

        r, c, a = respond(text)

        st.session_state.history.append({
            "user": text,
            "r": r,
            "c": c,
            "a": a
        })

# =================================
# OUTPUT
# =================================
for item in reversed(st.session_state.history):

    st.markdown(f"<div class='user'>🧠 {item['user']}</div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class='card'>
        {item['r']}
        <div class='quote'>“{item['c']}”</div>
        <div class='author'>— {item['a']}</div>
    </div>
    """, unsafe_allow_html=True)
