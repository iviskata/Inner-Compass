# =======================
# PAGE CONFIG
# =======================
st.set_page_config(page_title="Inner Compass", page_icon="🏛️", layout="centered")

# =======================
# STYLES (AESTHETIC UI)
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
        font-weight: 600;
        margin-bottom: 0px;
    }

    .subtitle {
        text-align: center;
        color: #94a3b8;
        margin-bottom: 25px;
        font-size: 14px;
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

    .quote {
        margin-top: 10px;
        color: #93c5fd;
        font-style: italic;
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
# STOIC ENGINE (MORE INTELLIGENT)
# =======================
def inner_compass(text):
    t = text.lower()

    # sadness / emotional pain
    if any(w in t for w in ["тъжен", "сам", "болка", "празно", "отчаян", "разбит"]):
        return (
            "💭 Разбирам те. Това, което чувстваш, е тежко и истинско.\n\n"
            "🧭 Това състояние няма да остане постоянно — то е в движение, като всичко друго.\n\n"
            "🏛️ „Не ни тревожат нещата, а нашето мнение за тях.“ – Епиктет"
        )

    # fatigue / burnout
    if any(w in t for w in ["изморен", "изморена", "нямам сили", "изтощен", "прегорял"]):
        return (
            "💭 Умората ти е сигнал, не слабост.\n\n"
            "🧭 Почивката е част от растежа, не отклонение от него.\n\n"
            "🏛️ „Трудностите укрепват ума.“ – Сенека"
        )

    # stress / overwhelm
    if any(w in t for w in ["стрес", "претоварен", "напрежение", "паника"]):
        return (
            "💭 Носиш повече, отколкото е нужно в този момент.\n\n"
            "🧭 Върни се към една малка следваща стъпка.\n\n"
            "🏛️ „Фокусирай се върху това, което зависи от теб.“ – Епиктет"
        )

    # anger / conflict
    if any(w in t for w in ["ядосан", "гняв", "обиден", "нарани", "яд ме"]):
        return (
            "💭 Емоцията ти е силна — но не трябва да я управляваш теб.\n\n"
            "🧭 Реакцията ти е избор, не автоматичен процес.\n\n"
            "🏛️ „Който побеждава себе си, е най-силен.“ – Марк Аврелий"
        )

    # default
    return (
        "💭 Това, което споделяш, е важно.\n\n"
        "🧭 Опитай да го погледнеш от по-спокойна перспектива.\n\n"
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
