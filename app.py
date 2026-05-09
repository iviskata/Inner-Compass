import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Inner Compass", layout="wide")

if "history" not in st.session_state:
    st.session_state.history = []

lang = st.selectbox("Language", ["Български", "English"])

def t(bg, en):
    return bg if lang == "Български" else en

# =========================
# GLOBAL STYLE (minimal but stable)
# =========================
st.markdown("""
<style>
html, body {
    font-family: Inter, system-ui, sans-serif;
    background: #020617;
    color: #e2e8f0;
}

.block-container {
    max-width: 1100px;
}

h1 {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("<h1>Inner Compass</h1>", unsafe_allow_html=True)

motto = t(
"⟡ Продължаваме заедно... по-смирени, по-смислени, по-стоически. ⟡",
"⟡ We continue together... more humble, more meaningful, more stoic. ⟡"
)

st.markdown(f"""
<p style="text-align:center; font-size:13px; opacity:0.65;">
{motto}
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# =========================
# SIMPLE EMOTION ENGINE
# =========================
def detect(text):
    ttxt = text.lower()

    if any(w in ttxt for w in ["умор", "измор", "изтощ", "нямам сила"]):
        return "recovery"

    if any(w in ttxt for w in ["стрес", "напрег", "over"]):
        return "stress"

    if any(w in ttxt for w in ["тъж", "празно", "разбит"]):
        return "sad"

    if any(w in ttxt for w in ["яд", "гнев", "драз"]):
        return "anger"

    return "neutral"

RESP = {
"recovery": "⟡ Изтощение — сигнал за нужда от възстановяване, не слабост.",
"stress": "⟡ Натрупано напрежение — системата е претоварена.",
"sad": "⟡ Емоционална тежест — временно състояние.",
"anger": "⟡ Повишена реактивност — пауза преди действие.",
"neutral": "⟡ Стабилно състояние."
}

# =========================
# LAYOUT
# =========================
left, center, right = st.columns([1, 2.6, 1.2])

# =========================
# LEFT ANALYSIS (SMALL TEXT)
# =========================
with left:
    st.markdown("### 🧠 Анализ")

    counts = {}
    for h in st.session_state.history:
        counts[h["emotion"]] = counts.get(h["emotion"], 0) + 1

    for k, v in counts.items():
        st.markdown(f"<p style='font-size:13px; opacity:0.75'>{k}: {v}</p>", unsafe_allow_html=True)

# =========================
# CENTER CHAT (BIGGEST PRIORITY)
# =========================
with center:

    q = t("Как се чувстваш?", "How do you feel?")

    with st.form("f", clear_on_submit=True):
        text = st.text_input(q)
        send = st.form_submit_button("Send")

        if send and text:
            emo = detect(text)

            st.session_state.history.append({
                "time": datetime.now().strftime("%H:%M"),
                "text": text,
                "emotion": emo
            })

    st.markdown("---")

    for h in reversed(st.session_state.history):

        # BIG TEXT (IMPORTANT FIX)
        st.markdown(f"""
        <div style="font-size:18px; font-weight:500;">
        {h['time']} · {h['text']}
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style="font-size:15px; opacity:0.85; margin-top:5px;">
        {RESP[h['emotion']]}
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

# =========================
# RIGHT WELLBEING (SMALL + SUBTLE)
# =========================
with right:
    st.markdown("### 🧘 Well-being")

    with st.expander("Фокус"):
        st.markdown("<p style='font-size:13px; opacity:0.7'>Deep Work · Single-tasking</p>", unsafe_allow_html=True)

    with st.expander("Състояние"):
        st.markdown("<p style='font-size:13px; opacity:0.7'>Стрес · Яснота · Натоварване</p>", unsafe_allow_html=True)

    with st.expander("Възстановяване"):
        st.markdown("<p style='font-size:13px; opacity:0.7'>Почивка · Рестарт · Баланс</p>", unsafe_allow_html=True)
