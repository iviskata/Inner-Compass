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
# GLOBAL STYLE (UI HIERARCHY FIX)
# =========================
st.markdown("""
<style>
html, body {
    font-family: Inter, system-ui, sans-serif;
    background: #020617;
    color: #e2e8f0;
}

/* CENTER CHAT - MAKE IT DOMINANT */
textarea, input {
    font-size: 18px !important;
}

/* INPUT FIELD BIGGER */
.stTextInput input {
    font-size: 20px !important;
    height: 60px !important;
}

/* BUTTON */
.stButton button {
    font-size: 16px !important;
    padding: 10px 20px !important;
}

/* HEADINGS */
h1 {
    text-align: center;
    font-size: 34px;
}

h3 {
    font-size: 20px;
}

/* MAKE SIDE PANELS SMALLER VISUALLY */
[data-testid="column"] {
    font-size: 13px;
}

/* WELLBEING MORE COMPACT */
.stExpander {
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("<h1>Inner Compass</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; opacity:0.7;'>⟡ Продължаваме заедно... по-смирени, по-смислени, по-стоически ⟡</p>", unsafe_allow_html=True)

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
# LAYOUT (CHAT = MAIN FOCUS)
# =========================
left, center, right = st.columns([1, 3, 1.2])

# =========================
# LEFT - ANALYSIS (SMALLER)
# =========================
with left:
    st.markdown("### 🧠 Анализ")

    counts = {}
    for h in st.session_state.history:
        counts[h["emotion"]] = counts.get(h["emotion"], 0) + 1

    for k, v in counts.items():
        st.markdown(f"<p style='font-size:12px; opacity:0.7'>{k}: {v}</p>", unsafe_allow_html=True)

# =========================
# CENTER - CHAT (MADE BIGGER + PRIORITY)
# =========================
with center:

    st.markdown("### Как се чувстваш?")

    with st.form("form", clear_on_submit=True):
        text = st.text_input(
            "Сподели състояние...",
            placeholder="напр. изморена съм, стресиран съм...",
        )
        send = st.form_submit_button("Изпрати")

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
# RIGHT - WELL-BEING (SMALLER VISUAL WEIGHT)
# =========================
with right:

    st.markdown("### 🧘 Well-being")

    with st.expander("⟡ Дишане"):
        st.write("Намалява стрес реакцията и стабилизира вниманието.")

    with st.expander("⟡ 20–20–20"):
        st.write("Намалява напрежението в очите.")

    with st.expander("⟡ Движение"):
        st.write("Възстановява кръвообращението.")

    with st.expander("⟡ Хидратация"):
        st.write("Поддържа концентрацията.")

    with st.expander("⟡ Фокус"):
        st.write("Един контекст = по-висока ефективност.")

    with st.expander("⟡ Почивка"):
        st.write("Почивката е част от продуктивността.")
