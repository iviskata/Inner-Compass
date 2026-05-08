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
# MEMORY
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
    color: white;
    font-size: 44px;
    margin-bottom: 0px;
}

/* SUBTITLE */
.subtitle {
    text-align: center;
    color: #94a3b8;
    margin-bottom: 30px;
    font-size: 13px;
    letter-spacing: 2px;
}

/* LANGUAGE ICON */
.lang {
    text-align: center;
    margin-bottom: -5px;
    font-size: 17px;
}

/* SELECT */
div[data-baseweb="select"] {
    max-width: 130px;
    margin: auto;
    margin-bottom: 20px;
}

/* INPUT */
.stTextInput input {
    height: 62px;
    border-radius: 16px;
    font-size: 18px;

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

    background: linear-gradient(
        90deg,
        #2563eb,
        #7c3aed
    );

    color: white;
    font-size: 16px;
}

/* USER */
.user {
    color: #60a5fa;
    margin-top: 25px;
    margin-bottom: 8px;
    font-weight: 500;
}

/* CARD */
.card {
    padding: 20px;

    border-radius: 18px;

    background: rgba(15,23,42,0.72);

    border: 1px solid rgba(255,255,255,0.06);

    line-height: 1.8;

    box-shadow: 0 4px 30px rgba(0,0,0,0.25);
}

/* QUOTE */
.quote {
    margin-top: 15px;
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
# LANGUAGE
# =================================
st.markdown("<div class='lang'>🌍</div>", unsafe_allow_html=True)

lang = st.selectbox(
    "",
    ["Български", "English"],
    label_visibility="collapsed"
)

# =================================
# HEADER
# =================================
st.markdown(
    "<h1>Inner Compass 🏛️</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>◉ calm stoic reflection engine ◉</div>",
    unsafe_allow_html=True
)

# =================================
# DATABASE
# =================================
quotes = {

    "sad": [

        (
            "💭 Това чувство няма да остане завинаги.",
            "Не страдаме от събитията, а от представите си за тях.",
            "Епиктет"
        ),

        (
            "💭 Дори тежките дни преминават.",
            "Душата става по-силна чрез трудностите.",
            "Сенека"
        )
    ],

    "stress": [

        (
            "💭 Не носи целия свят наведнъж.",
            "Имаш власт над ума си — не над външните събития.",
            "Марк Аврелий"
        ),

        (
            "💭 Спокойствието е сила.",
            "Спокойният ум носи яснота.",
            "Сенека"
        )
    ],

    "tired": [

        (
            "💭 Възстановяването също е прогрес.",
            "Природата работи в ритъм.",
            "Епиктет"
        ),

        (
            "💭 Забавянето не означава провал.",
            "Силният ум знае кога да спре.",
            "Марк Аврелий"
        )
    ]
}

# =================================
# DETECT EMOTION
# =================================
def detect(text):

    t = text.lower()

    if any(x in t for x in [
        "тъжен","тъжна","sad","сам"
    ]):
        return "sad"

    if any(x in t for x in [
        "стрес","stress","паника"
    ]):
        return "stress"

    if any(x in t for x in [
        "изморен","изморена","tired"
    ]):
        return "tired"

    return "default"

# =================================
# RESPONSE
# =================================
def answer(user_text):

    emotion = detect(user_text)

    if emotion == "default":

        if lang == "English":
            return (
                "💭 Stay present with the feeling.",
                "The soul becomes dyed with the color of its thoughts.",
                "Marcus Aurelius"
            )

        return (
            "💭 Остани спокоен в настоящия момент.",
            "Душата приема цвета на мислите си.",
            "Марк Аврелий"
        )

    return random.choice(quotes[emotion])

# =================================
# FORM
# =================================
with st.form("form", clear_on_submit=True):

    question = (
        "Как се чувстваш?"
        if lang == "Български"
        else "How do you feel?"
    )

    button = (
        "Изпрати"
        if lang == "Български"
        else "Send"
    )

    user_input = st.text_input(question)

    submit = st.form_submit_button(button)

    if submit and user_input:

        reflection, quote, author = answer(user_input)

        st.session_state.history.append({
            "user": user_input,
            "reflection": reflection,
            "quote": quote,
            "author": author
        })

# =================================
# SHOW HISTORY
# =================================
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
