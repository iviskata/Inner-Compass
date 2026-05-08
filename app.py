import streamlit as st
import random

# =======================
# PAGE CONFIG
# =======================
st.set_page_config(
    page_title="Inner Compass",
    page_icon="🏛️",
    layout="centered"
)

# =======================
# SESSION STATE
# =======================
if "history" not in st.session_state:
    st.session_state.history = []

# =======================
# LANGUAGE
# =======================
st.markdown("<div class='lang-wrap'>🌍</div>", unsafe_allow_html=True)

lang = st.selectbox(
    "",
    ["Български", "English"],
    label_visibility="collapsed"
)

# =======================
# STYLE
# =======================
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

/* HEADER */
h1 {
    text-align: center;
    color: #f8fafc;
    margin-bottom: 0px;
    font-size: 44px;
    letter-spacing: -1px;
}

.subtitle {
    text-align: center;
    color: #94a3b8;
    margin-bottom: 28px;
    font-size: 13px;
    letter-spacing: 2px;
    text-transform: uppercase;
}

/* LANGUAGE */
.lang-wrap {
    text-align: center;
    font-size: 18px;
    margin-bottom: -8px;
    opacity: 0.85;
}

div[data-baseweb="select"] {
    max-width: 130px;
    margin: auto;
    margin-bottom: 18px;
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
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    color: white;
    font-size: 16px;
    font-weight: 500;
    margin-top: 6px;
}

/* USER */
.user {
    color: #60a5fa;
    margin-top: 22px;
    margin-bottom: 8px;
    font-weight: 500;
    font-size: 15px;
}

/* RESPONSE CARD */
.card {
    padding: 20px;
    border-radius: 18px;
    background: rgba(15,23,42,0.72);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255,255,255,0.06);
    line-height: 1.8;
    color: #e2e8f0;
    font-size: 16px;
    box-shadow: 0 4px 30px rgba(0,0,0,0.25);
}

.quote {
    margin-top: 14px;
    color: #cbd5e1;
    font-style: italic;
    opacity: 0.92;
}

.author {
    margin-top: 8px;
    color: #94a3b8;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# =======================
# HEADER
# =======================
st.markdown("<h1>Inner Compass 🏛️</h1>", unsafe_allow_html=True)

subtitle = "◉ calm stoic reflection engine ◉"

st.markdown(
    f"<div class='subtitle'>{subtitle}</div>",
    unsafe_allow_html=True
)

# =======================
# STOIC DATABASE
# =======================
stoic_db = {

    "sadness": [
        (
            "💭 Болката не е вечна. Това, което чувстваш сега, ще се промени.",
            "Не страдаме от събитията, а от представите си за тях.",
            "Епиктет"
        ),
        (
            "💭 Тъгата не те определя. Тя е момент, не самоличност.",
            "Душата става по-силна чрез трудностите.",
            "Сенека"
        ),
        (
            "💭 Дори тежките дни преминават.",
            "Всичко, което се случва, е част от природата.",
            "Марк Аврелий"
        )
    ],

    "stress": [
        (
            "💭 Върни се към настоящия момент. Не носи целия свят наведнъж.",
            "Имаш власт над ума си — не над външните събития.",
            "Марк Аврелий"
        ),
        (
            "💭 Не всичко изисква незабавен отговор.",
            "Спокойният ум носи сила.",
            "Сенека"
        ),
        (
            "💭 Една малка стъпка е достатъчна за сега.",
            "Контролирай това, което зависи от теб.",
            "Епиктет"
        )
    ],

    "fatigue": [
        (
            "💭 Тялото ти има нужда от покой, не от вина.",
            "Понякога почивката е най-мъдрото действие.",
            "Сенека"
        ),
        (
            "💭 Забавянето не означава провал.",
            "Силният ум знае кога да спре.",
            "Марк Аврелий"
        ),
        (
            "💭 Възстановяването също е прогрес.",
            "Природата работи в ритъм, не в бързане.",
            "Епиктет"
        )
    ],

    "anger": [
        (
            "💭 Реакцията ти е по-важна от самата ситуация.",
            "Най-доброто отмъщение е да не приличаш на този, който те е наранил.",
            "Марк Аврелий"
        ),
        (
            "💭 Гневът замъглява ясната мисъл.",
            "Този, който владее себе си, е истински силен.",
            "Сенека"
        ),
        (
            "💭 Направи пауза преди действие.",
            "Свободата започва с контрол над реакциите.",
            "Епиктет"
        )
    ],

    "fear": [
        (
            "💭 Бъдещето не е тук още. Остани в настоящето.",
            "Често страдаме повече във въображението си, отколкото в реалността.",
            "Сенека"
        ),
        (
            "💭 Страхът не означава слабост.",
            "Пречката по пътя се превръща в самия път.",
            "Марк Аврелий"
        ),
        (
            "💭 Не позволявай на неизвестното да отнеме спокойствието ти.",
            "Не можеш да контролираш всичко — и това е нормално.",
            "Епиктет"
        )
    ]
}

# =======================
# SMART MATCHING
# =======================
def detect_emotion(text):

    t = text.lower()

    if any(w in t for w in [
        "тъжен","тъжна","sad","lonely","болка","pain","сам"
    ]):
        return "sadness"

    if any(w in t for w in [
        "стрес","stress","anxiety","паника","overthinking"
    ]):
        return "stress"

    if any(w in t for w in [
        "изморен","изморена","tired","burnout","exhausted"
    ]):
        return "fatigue"

    if any(w in t for w in [
        "яд","гняв","angry","anger","ядосан"
    ]):
        return "anger"

    if any(w in t for w in [
        "страх","fear","scared","worried","притеснен"
    ]):
        return "fear"

    return "default"

# =======================
# RESPONSE ENGINE
# =======================
def inner_compass(user_text):

    emotion = detect_emotion(user_text)

    if emotion == "default":

        if lang == "English":
            return (
                "💭 I hear you. Stay present with the feeling.",
                "The soul becomes dyed with the color of its thoughts.",
                "Marcus Aurelius"
            )

        return (
            "💭 Разбирам те. Остани спокоен в настоящия момент.",
            "Душата приема цвета на мислите си.",
            "Марк Аврелий"
        )

    return random.choice(stoic_db[emotion])

# =======================
# FORM
# =======================
with st.form("emotion_form", clear_on_submit=True):

    question = (
        "Как се чувстваш?"
        if lang == "Български"
        else "How do you feel?"
    )

    button_text = (
        "Изпрати"
        if lang == "Български"
        else "Send"
    )

    user_input = st.text_input(question)

    submitted = st.form_submit_button(button_text)

    if submitted and user_input:

        reflection, quote, author = inner_compass(user_input)

        st.session_state.history.append({
            "user": user_input,
            "reflection": reflection,
            "quote": quote,
            "author": author
        })

# =======================
# DISPLAY HISTORY
# =======================
for item in reversed(st.session_state.history):

    st.markdown(
        f"<div class='user'>🧠 {item['user']}</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class='card'>
            {item['reflection']}

            <div class='quote'>
            “{item['quote']}”
            </div>

            <div class='author'>
            — {item['author']}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
