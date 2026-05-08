import streamlit as st

# =======================
# PAGE CONFIG
# =======================
st.set_page_config(
    page_title="Inner Compass",
    page_icon="🏛️",
    layout="centered"
)

# =======================
# STYLE (AESTHETIC UI)
# =======================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');

    .stApp {
        background: radial-gradient(circle at top, #0f172a, #020617);
        color: #e2e8f0;
        font-family: 'Inter', sans-serif;
    }

    h1 {
        text-align: center;
        color: #f8fafc;
        margin-bottom: 0px;
        font-weight: 600;
        letter-spacing: 0.5px;
    }

    .subtitle {
        text-align: center;
        color: #94a3b8;
        margin-bottom: 25px;
        font-size: 14px;
        font-weight: 300;
        letter-spacing: 0.3px;
    }

    .stTextInput > div > div > input {
        background-color: #1e293b;
        color: white;
        border-radius: 12px;
        padding: 12px;
        border: 1px solid rgba(255,255,255,0.1);
    }

    .card {
        margin-top: 20px;
        padding: 22px;
        border-radius: 18px;
        background: rgba(17, 24, 39, 0.65);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255,255,255,0.08);
        color: #e2e8f0;
        line-height: 1.6;
        box-shadow: 0px 8px 30px rgba(0,0,0,0.4);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =======================
# HEADER
# =======================
st.markdown("<h1>Inner Compass 🏛️</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>A calm stoic reflection space.</div>", unsafe_allow_html=True)

# =======================
# STOIC ENGINE (BG + EN)
# =======================
def inner_compass(text):
    t = text.lower()

    # sadness
    if any(w in t for w in ["тъжен", "sad", "сам", "lonely", "болка", "pain"]):
        return (
            "💭 Разбирам те. / I understand you.\n\n"
            "🧭 Това ще премине. / This will pass.\n\n"
            "🏛️ „Не ни тревожат нещата, а нашето мнение за тях.“ – Епиктет"
        )

    # fatigue
    if any(w in t for w in ["изморен", "tired", "exhausted", "нямам сили"]):
        return (
            "💭 Умората е сигнал, не слабост. / Fatigue is a signal, not weakness.\n\n"
            "🧭 Почивката е част от напредъка. / Rest is part of progress.\n\n"
            "🏛️ „Трудностите укрепват ума.“ – Сенека"
        )

    # stress
    if any(w in t for w in ["стрес", "stress", "anxiety", "претоварен"]):
        return (
            "💭 Твърде много наведнъж. / Too much at once.\n\n"
            "🧭 Една стъпка е достатъчна. / One step is enough.\n\n"
            "🏛️ „Фокусирай се върху това, което зависи от теб.“ – Епиктет"
        )

    # anger
    if any(w in t for w in ["гняв", "anger", "ядосан", "angry"]):
        return (
            "💭 Емоцията е временна. / Emotion is temporary.\n\n"
            "🧭 Ти избираш реакцията си. / You choose your response.\n\n"
            "🏛️ „Който побеждава себе си, е най-силен.“ – Марк Аврелий"
        )

    return (
        "💭 Добре е, че споделяш. / It's good that you share this.\n\n"
        "🧭 Погледни спокойно. / Look at it calmly.\n\n"
        "🏛️ „Животът е такъв, какъвто го правят мислите ни.“ – Марк Аврелий"
    )

# =======================
# INPUT
# =======================
user = st.text_input("Как се чувстваш? / How do you feel?")

# =======================
# OUTPUT
# =======================
if user:
    response = inner_compass(user)

    st.markdown(
        f"""
        <div class="card">
        {response.replace('\n', '<br>')}
        </div>
        """,
        unsafe_allow_html=True
    )
