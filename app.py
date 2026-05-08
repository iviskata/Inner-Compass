import streamlit as st

# =======================
# PAGE CONFIG (must be first Streamlit call)
# =======================
st.set_page_config(
    page_title="Inner Compass",
    page_icon="🏛️",
    layout="centered"
)

# =======================
# STYLE (aesthetic calm UI)
# =======================
st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at top, #0f172a, #020617);
        color: #e2e8f0;
    }

    h1 {
        text-align: center;
        color: #f8fafc;
        margin-bottom: 0px;
    }

    .subtitle {
        text-align: center;
        color: #94a3b8;
        margin-bottom: 20px;
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
st.markdown("<div class='subtitle'>A calm stoic reflection space</div>", unsafe_allow_html=True)

# =======================
# STOIC ENGINE
# =======================
def inner_compass(text):
    t = text.lower()

    if any(w in t for w in ["тъжен", "сам", "болка", "празно", "отчаян"]):
        return (
            "💭 Разбирам те. Това, което чувстваш, е тежко.\n\n"
            "🧭 Това няма да остане завинаги.\n\n"
            "🏛️ „Не ни тревожат нещата, а нашето мнение за тях.“ – Епиктет"
        )

    if any(w in t for w in ["изморен", "изморена", "нямам сили", "изтощен"]):
        return (
            "💭 Умората ти е сигнал, не слабост.\n\n"
            "🧭 Почивката е част от растежа.\n\n"
            "🏛️ „Трудностите укрепват ума.“ – Сенека"
        )

    if any(w in t for w in ["стрес", "претоварен", "напрежение", "паника"]):
        return (
            "💭 В момента е твърде много.\n\n"
            "🧭 Върни се към една малка стъпка.\n\n"
            "🏛️ „Фокусирай се върху това, което зависи от теб.“ – Епиктет"
        )

    if any(w in t for w in ["ядосан", "гняв", "обиден", "нарани"]):
        return (
            "💭 Емоцията е силна, но временна.\n\n"
            "🧭 Реакцията ти е избор.\n\n"
            "🏛️ „Който побеждава себе си, е най-силен.“ – Марк Аврелий"
        )

    return (
        "💭 Добре е, че споделяш това.\n\n"
        "🧭 Погледни ситуацията по-спокойно.\n\n"
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

    st.markdown(
        f"""
        <div class="card">
        {response.replace('\n', '<br>')}
        </div>
        """,
        unsafe_allow_html=True
    )
