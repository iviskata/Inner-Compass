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
# LANGUAGE (RESTORED ✔)
# =========================
lang = st.selectbox("🌍 Language", ["Български", "English"])

def t(bg, en):
    return bg if lang == "Български" else en

# =========================
# STYLE (ONLY UI HIERARCHY FIX - SAFE)
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

[data-testid="column"] {
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER (LANGUAGE FIXED ✔)
# =========================
st.markdown("<h1>Inner Compass</h1>", unsafe_allow_html=True)

motto = t(
"⟡ Продължаваме заедно... по-смирени, по-смислени, по-стоически ⟡",
"⟡ We continue together... more humble, more meaningful, more stoic ⟡"
)

st.markdown(f"<p style='text-align:center; opacity:0.7;'>{motto}</p>", unsafe_allow_html=True)

st.markdown("---")

# =========================
# EMOTION ENGINE (UNCHANGED)
# =========================
def detect(text):
    t = text.lower()

    if any(x in t for x in ["умор", "изтощ"]):
        return "recovery"
    if any(x in t for x in ["стрес"]):
        return "stress"
    if any(x in t for x in ["тъж"]):
        return "sad"
    if any(x in t for x in ["яд"]):
        return "anger"
    if any(x in t for x in ["работа"]):
        return "work"
    if any(x in t for x in ["вдъхнов"]):
        return "inspiration"

    return "neutral"

RESPONSES = {
    "recovery": "⟡ Това състояние показва нужда от възстановяване.",
    "stress": "⟡ Когнитивно претоварване.",
    "sad": "⟡ Емоционална тежест.",
    "anger": "⟡ Повишена реактивност.",
    "work": "⟡ Работно напрежение.",
    "inspiration": "⟡ Висока яснота.",
    "neutral": "⟡ Баланс."
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
        st.markdown(f"<p style='font-size:12px; opacity:0.7'>{k}: {v}</p>", unsafe_allow_html=True)

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
# RIGHT - WELL-BEING (UNCHANGED STRUCTURE)
# =========================
with right:

    st.markdown(t("### 🧘 Well-being", "### 🧘 Well-being"))

    with st.expander("⟡ Дишане"):
        st.write(t(
            "Намалява стрес реакцията и стабилизира вниманието.",
            "Reduces stress response and stabilizes attention."
        ))

    with st.expander("⟡ 20–20–20"):
        st.write(t(
            "Намалява напрежението в очите.",
            "Reduces eye strain."
        ))

    with st.expander("⟡ Движение"):
        st.write(t(
            "Възстановява кръвообращението.",
            "Improves circulation."
        ))

    with st.expander("⟡ Хидратация"):
        st.write(t(
            "Поддържа концентрацията.",
            "Maintains focus."
        ))

    with st.expander("⟡ Фокус"):
        st.write(t(
            "Един контекст = по-висока ефективност.",
            "Single tasking improves performance."
        ))

    with st.expander("⟡ Почивка"):
        st.write(t(
            "Почивката е част от продуктивността.",
            "Rest is part of productivity."
        ))
