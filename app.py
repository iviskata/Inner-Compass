import streamlit as st
from datetime import datetime

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
# LANGUAGE SYSTEM
# =========================
lang = st.selectbox("🌍 Language", ["Български", "English"])

def t(bg, en):
    return bg if lang == "Български" else en

# =========================
# STYLE (SAFE + STABLE)
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
# EMOTION DETECTION (FIXED LOGIC)
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
# LONG, HUMAN RESPONSES (FIXED — NO MORE "BALANCE")
# =========================
RESPONSES = {
    "recovery": """⟡ Това състояние показва натрупана умора.

Когато се появява такова усещане, това не е сигнал за слабост, а за изчерпване на текущите ресурси. Тялото и умът работят в режим на натоварване и имат нужда от пауза.

Най-важното в този момент не е да се “натискаш”, а да намалиш темпото и да дадеш време за възстановяване.""",

    "stress": """⟡ Това показва натрупано напрежение и когнитивно претоварване.

Когато мислите се ускоряват и всичко изглежда едновременно важно, умът влиза в режим на стрес. Това е естествена реакция на прекалено много стимули.

Яснотата не идва от още усилие, а от намаляване на натоварването.""",

    "sad": """⟡ Това изглежда като емоционално натежаване.

Такива състояния често се появяват, когато има вътрешно напрежение или неизразени чувства. Това не е проблем, който трябва да се поправя веднага, а състояние, което има нужда от пространство.

Позволяването му да бъде там често е първата стъпка към промяна.""",

    "anger": """⟡ Това е повишена емоционална реактивност.

Ядът често се появява, когато граници са преминати или когато напрежението се натрупва. Това не е нещо негативно само по себе си — това е сигнал.

Пауза преди реакция може да промени целия резултат.""",

    "work": """⟡ Това показва работно натоварване и умствено напрежение.

Когато задачите се увеличат, вниманието започва да се разпилява. Това не означава, че не се справяш, а че системата е натоварена.

Структурата и приоритизацията връщат контрола.""",

    "inspiration": """⟡ Това е състояние на повишена яснота и вътрешен импулс.

В такива моменти мисленето е по-свързано и естествено насочено към действие. Това е добър момент за фокусирана работа, без излишно разпиляване.""",

    "neutral": """⟡ Това е стабилно и балансирано състояние.

Няма доминираща емоция, което често означава вътрешна стабилност и яснота. Това е добра база за вземане на решения."""
}

# =========================
# LAYOUT
# =========================
left, center, right = st.columns([1, 3, 1.2])

# =========================
# LEFT - ANALYSIS
# =========================
with left:
    st.markdown("### 🧠 Анализ")

    counts = {}
    for h in st.session_state.history:
        counts[h["emotion"]] = counts.get(h["emotion"], 0) + 1

    for k, v in counts.items():
        st.markdown(f"- {k}: {v}")

# =========================
# CENTER - CHAT (MAIN FOCUS)
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
# RIGHT - WELL-BEING (CLEAN ACCORDION SYSTEM)
# =========================
with right:

    st.markdown("### 🧘 Well-being система")
    st.markdown("<p style='opacity:0.6; font-size:12px;'>⟡ Златни правила за баланс</p>", unsafe_allow_html=True)

    with st.expander("⟡ Дишане"):
        st.write("Намалява стрес реакцията и стабилизира вниманието.")

    with st.expander("⟡ 20–20–20 правило"):
        st.write("Намалява напрежението в очите при работа с екран.")

    with st.expander("⟡ Движение"):
        st.write("Подобрява кръвообращението и яснотата на мислене.")

    with st.expander("⟡ Хидратация"):
        st.write("Поддържа концентрацията и енергията.")

    with st.expander("⟡ Фокус"):
        st.write("Един контекст = по-висока ефективност.")

    with st.expander("⟡ Почивка"):
        st.write("Почивката е част от продуктивността, не прекъсване.")
