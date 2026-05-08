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
# STYLE (CALM AESTHETIC UI)
# =======================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

    .stApp {
        background: radial-gradient(circle at top, #0f172a, #020617);
        color: #e2e8f0;
        font-family: 'Inter', sans-serif;
        letter-spacing: 0.2px;
    }

    h1 {
        text-align: center;
        color: #f8fafc;
        font-weight: 600;
        letter-spacing: 1px;
        margin-bottom: 0px;
    }

    .subtitle {
        text-align: center;
        color: #94a3b8;
        font-size: 13px;
        margin-bottom: 25px;
        font-weight: 300;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    .stTextInput > div > div > input {
        background-color: #1e293b;
        color: white;
        border-radius: 12px;
        padding: 12px;
        border: 1px solid rgba(255,255,255,0.1);
    }

    .card {
        margin-top: 22px;
        padding: 24px;
        border-radius: 20px;
        background: rgba(17, 24, 39, 0.65);
        backdrop-filter: blur(14px);
        border: 1px solid rgba(255,255,255,0.08);
        color: #e2e8f0;
        line-height: 1.7;
        box-shadow: 0px 10px 35px rgba(0,0,0,0.45);
    }

    .circle {
        text-align: center;
        font-size: 18px;
        color: #60a5fa;
        margin: 10px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =======================
# HEADER
# =======================
st.markdown("<h1>INNER COMPASS 🏛️</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>◉ calm stoic reflection engine ◉</div>", unsafe_allow_html=True)

# =======================
# MORE INTELLIGENT STOIC ENGINE
# =======================
def inner_compass(text):
    t = text.lower()

    # sadness / emotional pain
    if any(w in t for w in [
        "тъжен","sad","болка","pain","сам","lonely","разбит","empty","празно","отчаян"
    ]):
        return (
            "💭 Разбирам те.\n\n"
            "🧭 Това, което чувстваш, е човешко и временно.\n\n"
            "🏛️ „Не ни тревожат нещата, а нашето мнение за тях.“ – Епиктет"
        )

    # anxiety / overthinking
    if any(w in t for w in [
        "стрес","stress","anxiety","претоварен","overthinking","panic","паника","напрежение"
    ]):
        return (
            "💭 Умът ти е претоварен.\n\n"
            "🧭 Върни се към настоящия момент.\n\n"
            "🏛️ „Ако нещо не зависи от теб, не го носи в ума си.“ – Стоицизъм"
        )

    # fatigue / burnout
    if any(w in t for w in [
        "изморен","tired","exhausted","нямам сили","burnout","прегорял","изтощен"
    ]):
        return (
            "💭 Тялото ти говори.\n\n"
            "🧭 Почивката е част от силата.\n\n"
            "🏛️ „Дори и най-силният ум има нужда от покой.“ – Сенека"
        )

    # anger / conflict
    if any(w in t for w in [
        "гняв","anger","ядосан","angry","обиден","hurt","нарани"
    ]):
        return (
            "💭 Емоцията е силна, но временна.\n\n"
            "🧭 Ти избираш реакцията си.\n\n"
            "🏛️ „Който владее себе си, владее света си.“ – Марк Аврелий"
        )

    # default
    return (
        "💭 Това е валидно чувство.\n\n"
        "🧭 Опитай да го наблюдаваш, без да се отъждествяваш с него.\n\n"
        "🏛️ „Животът е такъв, какъвто го правят мислите ни.“ – Марк Аврелий"
    )

# =======================
# INPUT
# =======================
user = st.text_input("Как се чувстваш?")

# =======================
# OUTPUT
# =======================
if user:
    response = inner_compass(user)

    st.markdown("<div class='circle'>◉</div>", unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="card">
        {response.replace('\n', '<br>')}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div class='circle'>◉</div>", unsafe_allow_html=True)
