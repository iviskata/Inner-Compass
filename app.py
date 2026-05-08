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
# STYLE
# =========================
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

/* TOP BRAND */
.brand {
    text-align: center;
    font-size: 12px;
    letter-spacing: 3px;
    color: #94a3b8;
    margin-top: 10px;
}

/* TITLE */
h1 {
    text-align: center;
    font-size: 44px;
    color: white;
    margin-bottom: 0px;
}

/* MOTTO */
.motto {
    text-align: center;
    font-size: 14px;
    color: #cbd5e1;
    margin-top: -5px;
    margin-bottom: 20px;
    font-style: italic;
}

/* SUBTITLE */
.subtitle {
    text-align: center;
    color: #94a3b8;
    font-size: 12px;
    letter-spacing: 2px;
    margin-bottom: 25px;
}

/* INPUT */
.stTextInput input {
    height: 62px;
    font-size: 18px;
    border-radius: 16px;

    background: rgba(15,23,42,0.9);
    color: white;

    border: 1px solid rgba(255,255,255,0.08);

    padding-left: 18px;
}

/* BUTTON */
.stButton button {
    width: 100%;
    height: 50px;
    border-radius: 14px;
    border: none;

    background: linear-gradient(90deg,#2563eb,#7c3aed);
    color: white;
    font-size: 16px;
}

/* USER */
.user {
    color: #60a5fa;
    margin-top: 20px;
    margin-bottom: 8px;
    font-weight: 500;
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

# =========================
# HEADER
# =========================
st.markdown("<div class='brand'>H-TECH DIGITAL SYSTEMS</div>", unsafe_allow_html=True)

st.markdown("<h1>Inner Compass 🏛️</h1>", unsafe_allow_html=True)

st.markdown(
    "<div class='motto'>Продължаваме заедно... по-смирени, по-смислени, по-стоически.</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>◉ stoic emotional reflection system ◉</div>",
    unsafe_allow_html=True
)

# =========================
# STOIC RESPONSES
# =========================
responses = [
    ("💭 Това ще премине.", "Не страдаме от събитията, а от нашата интерпретация.", "Епиктет"),
    ("💭 Спокойствието е сила.", "Контролирай това, което зависи от теб.", "Марк Аврелий"),
    ("💭 Почивката е прогрес.", "Понякога спирането е движение напред.", "Сенека"),
    ("💭 Бъди тук и сега.", "Животът се случва в настоящия момент.", "Стоицизъм")
]

# =========================
# RESPONSE ENGINE
# =========================
def generate_response(text):

    t = text.lower()

    if any(x in t for x in ["тъжен","sad","болка","pain"]):
        return responses[0]

    if any(x in t for x in ["стрес","stress","паника"]):
        return responses[1]

    if any(x in t for x in ["изморен","tired","burnout"]):
        return responses[2]

    return random.choice(responses)

# =========================
# INPUT
# =========================
with st.form("form", clear_on_submit=True):

    user_input = st.text_input("Как се чувстваш?")

    submit = st.form_submit_button("Изпрати")

    if submit and user_input:

        reflection, quote, author = generate_response(user_input)

        st.session_state.history.append({
            "user": user_input,
            "r": reflection,
            "q": quote,
            "a": author
        })

# =========================
# OUTPUT
# =========================
for item in reversed(st.session_state.history):

    st.markdown(f"<div class='user'>🧠 {item['user']}</div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class='card'>

        {item['r']}

        <div class='quote'>
        “{item['q']}”
        </div>

        <div class='author'>
        — {item['a']}
        </div>

    </div>
    """, unsafe_allow_html=True)
