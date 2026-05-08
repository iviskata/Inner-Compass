import streamlit as st

# ===== PAGE CONFIG =====
st.set_page_config(page_title="Inner Compass", page_icon="🏛️")

# ===== DARK CALM BACKGROUND =====
st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at top, #0f172a, #020617);
    }

    .block-container {
        padding-top: 2rem;
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
    </style>
    """,
    unsafe_allow_html=True
)

# ===== STOIC CORE =====
def inner_compass(text):
    text = text.lower()

    if any(w in text for w in ["тъжен", "сам", "болка", "празно", "отчаян"]):
        return "💭 Разбирам те. Това, което чувстваш, е тежко.\n\n🧭 Това няма да остане вечно.\n\n🏛️ „Не ни тревожат нещата, а нашето мнение за тях.“ – Епиктет"

    if any(w in text for w in ["изморен", "изморена", "нямам сили", "изтощен"]):
        return "💭 Тялото ти има нужда от почивка.\n\n🧭 Това не е слабост, а сигнал.\n\n🏛️ „Трудностите укрепват ума.“ – Сенека"

    if any(w in text for w in ["стрес", "претоварен", "напрежение"]):
        return "💭 Носи се твърде много наведнъж.\n\n🧭 Само следващата стъпка има значение.\n\n🏛️ „Фокусирай се върху това, което зависи от теб.“ – Епиктет"

    return "💭 Добре е, че споделяш това.\n\n🧭 Погледни ситуацията по-спокойно.\n\n🏛️ „Животът е такъв, какъвто го правят мислите ни.“ – Марк Аврелий"


# ===== UI =====
st.markdown("<h1>Inner Compass 🏛️</h1>", unsafe_allow_html=True)

user = st.text_input("Как се чувстваш?")

if user:
    response = inner_compass(user)

    st.markdown(
        f"""
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
        {response.replace('\n', '<br>')}
        </div>
        """,
        unsafe_allow_html=True
    )
