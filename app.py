import streamlit as st
from datetime import datetime
import random

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Inner Compass",
    page_icon="🏛️",
    layout="wide"
)

# =========================
# STATE
# =========================
if "history" not in st.session_state:
    st.session_state.history = []

# =========================
# LANGUAGE
# =========================
lang = st.selectbox("🌍 Language", ["Български", "English"])

def t(bg, en):
    return bg if lang == "Български" else en

# =========================
# STYLE
# =========================
st.markdown("""
<style>
html, body {
    font-family: Inter, system-ui, sans-serif;
    background: #020617;
    color: #e2e8f0;
}

.stTextInput input {
    font-size: 20px !important;
    height: 60px !important;
}

.stButton button {
    font-size: 16px !important;
}

h1 {
    text-align: center;
    font-size: 34px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("<h1>Inner Compass</h1>", unsafe_allow_html=True)

st.markdown(
    f"<p style='text-align:center; opacity:0.7;'>"
    f"⟡ {t('Продължаваме заедно... по-смирени, по-смислени, по-стоически', 'We continue together... more calm, more meaningful, more stoic')} ⟡"
    f"</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# =========================
# EMOTION DETECTION (STABLE)
# =========================
def detect(text):
    ttxt = text.lower()

    if any(x in ttxt for x in ["умор", "измор", "изтощ", "нямам сила", "капнал"]):
        return "recovery"

    if any(x in ttxt for x in ["стрес", "напрег", "претовар"]):
        return "stress"

    if any(x in ttxt for x in ["тъж", "празно", "сам"]):
        return "sad"

    if any(x in ttxt for x in ["яд", "гнев"]):
        return "anger"

    if any(x in ttxt for x in ["работа", "задачи"]):
        return "work"

    if any(x in ttxt for x in ["вдъхнов", "мотив"]):
        return "inspiration"

    return "neutral"

# =========================
# LONG RESPONSES (UNCHANGED CORE)
# =========================
RESPONSES = {
    "recovery": """⟡ Това състояние показва натрупана умора.

Тялото и умът имат нужда от възстановяване. Това не е слабост, а сигнал за баланс на ресурсите.

Понякога най-правилното действие е да намалиш темпото.""",

    "stress": """⟡ Това показва когнитивно претоварване.

Когато всичко изглежда важно едновременно, умът губи яснота. Това не е проблем на способност, а на натоварване.

Яснотата се връща чрез редукция, не чрез добавяне.""",

    "sad": """⟡ Това е емоционално натежаване.

Тези състояния често идват, когато има вътрешно напрежение. Те не трябва да бъдат насилствено променяни.

Понякога разбирането е първата промяна.""",

    "anger": """⟡ Това е повишена реактивност.

Гневът е сигнал за граници или натрупване. Не е враг, а индикатор.

Пауза преди реакция променя резултата.""",

    "work": """⟡ Това показва работно натоварване.

Прекалено много задачи намаляват яснотата. Това не е липса на способност, а на структура.

Фокусът възстановява контрол.""",

    "inspiration": """⟡ Това е ясно състояние на импулс и мотивация.

Когато умът е подреден, действията стават естествени.

Важно е да се поддържа баланс.""",

    "neutral": """⟡ Стабилно вътрешно състояние.

Няма доминираща емоция. Това е добра основа за решения."""
}

# =========================
# STOIC QUOTES (30 + GROUPED)
# =========================
STOIC_QUOTES = {
    "recovery": [
        "Почивката не е отклонение от пътя, а част от него.",
        "Силата включва и способността да спреш.",
        "Възстановяването е форма на мъдрост.",
        "Умората е сигнал, не враг.",
        "Понякога бездействието е правилното действие."
    ],
    "stress": [
        "Не събитията те смущават, а преценката ти за тях.",
        "Яснотата се ражда в намаляването.",
        "Когато всичко е важно, нищо не е под контрол.",
        "Спокойствието започва с пауза.",
        "Мисълта не е факт, а движение."
    ],
    "sad": [
        "Тежестта намалява, когато бъде разбрана.",
        "Емоциите са временни състояния.",
        "Тишината понякога лекува повече от думите.",
        "Не всичко трябва да бъде решено веднага.",
        "Приемането е първата стъпка към промяна."
    ],
    "anger": [
        "Между стимула и реакцията има пространство.",
        "Гневът иска скорост, мъдростта иска пауза.",
        "Контролът започва преди реакцията.",
        "Търпението е сила.",
        "Реакцията е избор."
    ],
    "work": [
        "Разпиляното внимание създава разпиляни резултати.",
        "Фокусът е дисциплина.",
        "Структурата намалява хаоса.",
        "Една ясна задача е повече от десет разпилени.",
        "Умът работи най-добре в ред."
    ],
    "inspiration": [
        "Ясният ум избира по-добре.",
        "Импулсът е начало, не посока.",
        "Действието следва яснота.",
        "Вдъхновението без структура се разпада.",
        "Подреденият ум създава движение."
    ],
    "neutral": [
        "Спокойствието е форма на сила.",
        "Стабилността е основа на действие.",
        "Яснотата идва в тишина.",
        "Не всяко състояние изисква реакция.",
        "Балансът е активна форма на осъзнатост."
    ]
}

# =========================
# LAYOUT
# =========================
left, center, right = st.columns([1, 3, 1.2])

# =========================
# LEFT - ANALYSIS + SUMMARY + QUOTES
# =========================
with left:
    st.markdown("### 🧠 Анализ")

    counts = {}
    for h in st.session_state.history:
        counts[h["emotion"]] = counts.get(h["emotion"], 0) + 1

    for k, v in counts.items():
        st.markdown(f"- {k}: {v}")

    st.markdown("---")

    if counts:
        dominant = max(counts, key=counts.get)

        summary_map = {
            "recovery": "Доминира умора и нужда от възстановяване.",
            "stress": "Доминира напрежение и претоварване.",
            "sad": "Доминира емоционална тежест.",
            "anger": "Доминира реактивност.",
            "work": "Доминира работно натоварване.",
            "inspiration": "Доминира яснота и мотивация.",
            "neutral": "Доминира стабилност."
        }

        st.markdown("### 📊 Обобщение")
        st.markdown(summary_map.get(dominant, ""))

        st.markdown("### 🏛️ Стоическа перспектива")
        quote = random.choice(STOIC_QUOTES.get(dominant, [""]))
        st.markdown(f"*{quote}*")

# =========================
# CENTER - CHAT
# =========================
with center:

    st.markdown(t("### Как се чувстваш?", "### How do you feel?"))

    with st.form("form", clear_on_submit=True):
        text = st.text_input(t("Сподели състояние...", "Share your state..."))
        send = st.form_submit_button(t("Изпрати", "Send"))

        if send and text:
            emo = detect(text)

            st.session_state.history.append({
                "time": datetime.now().strftime("%H:%M"),
                "text": text,
                "emotion": emo
            })

    st.markdown("---")

    for h in reversed(st.session_state.history):
        st.markdown(f"**{h['time']} · {h['text']}**")
        st.info(RESPONSES[h["emotion"]])
        st.markdown("---")

# =========================
# RIGHT - WELLBEING
# =========================
with right:

    st.markdown("### 🧘 Well-being система")

    with st.expander("⟡ Дишане"):
        st.write("Намалява стрес и стабилизира вниманието.")

    with st.expander("⟡ 20–20–20"):
        st.write("Намалява напрежението в очите.")

    with st.expander("⟡ Движение"):
        st.write("Подобрява циркулацията и яснотата.")

    with st.expander("⟡ Хидратация"):
        st.write("Поддържа концентрацията.")

    with st.expander("⟡ Фокус"):
        st.write("Един контекст = по-висока ефективност.")

    with st.expander("⟡ Почивка"):
        st.write("Почивката е продуктивност.")
