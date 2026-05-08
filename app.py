import streamlit as st
<div style="
    margin-top:20px;
    padding:22px;
    border-radius:18px;
    background: rgba(17, 24, 39, 0.6);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.08);
    color:#e2e8f0;
    line-height:1.6;
">
# ===== PAGE SETTINGS =====
st.set_page_config(page_title="Inner Compass", page_icon="🏛️")

# ===== CUSTOM STYLE =====
st.markdown(
    """
    <style>
    .main {
        background-color: #0f172a;
        color: #e2e8f0;
    }

    h1 {
        text-align: center;
        color: #f8fafc;
        font-weight: 600;
    }

    .stTextInput > div > div > input {
        background-color: #1e293b;
        color: white;
        border-radius: 10px;
        padding: 10px;
    }

    .card {
        background-color: #111827;
        padding: 20px;
        border-radius: 16px;
        margin-top: 20px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.4);
        color: #e2e8f0;
        line-height: 1.6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ===== STOIC LOGIC =====
def inner_compass(text):
    text = text.lower()

    if any(w in text for w in ["тъжен", "сам", "болка", "празно", "отчаян"]):
        return "💭 Разбирам те. Това, което чувстваш, е тежко.\n\n🧭 Това състояние няма да остане вечно.\n\n🏛️ „Не ни тревожат нещата, а нашето мнение за тях.“ – Епиктет"

    if any(w in text for w in ["изморен", "изморена", "нямам сили", "изтощен"]):
        return "💭 Чувстваш се изтощен — това е сигнал, не слабост.\n\n🧭 Почивката е част от напредъка.\n\n🏛️ „Трудностите укрепват ума.“ – Сенека"

    if any(w in text for w in ["стрес", "претоварен", "напрежение"]):
        return "💭 В момента носиш твърде много.\n\n🧭 Сведи мисълта до една следваща стъпка.\n\n🏛️ „Фокусирай се само върху това, което зависи от теб.“ – Епиктет"

    if any(w in text for w in ["ядосан", "нарани", "хора"]):
        return "💭 Разбирам реакцията ти.\n\n🧭 Спокойствието ти зависи от теб, не от другите.\n\n🏛️ „Избери да не бъдеш наранен от действията на другите.“ – Марк Аврелий"

    return "💭 Добре е, че споделяш това.\n\n🧭 Опитай да погледнеш ситуацията по-спокойно.\n\n🏛️ „Животът е такъв, какъвто го правят мислите ни.“ – Марк Аврелий"


# ===== UI =====
st.markdown("<h1>Inner Compass 🏛️</h1>", unsafe_allow_html=True)

user = st.text_input("Как се чувстваш?")

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
