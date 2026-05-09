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
# STYLE (minimal fix only)
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
st.markdown("<p style='text-align:center; opacity:0.7;'>⟡ Продължаваме заедно... по-смирени, по-смислени, по-стоически ⟡</p>", unsafe_allow_html=True)

st.markdown("---")

# =========================
# SIMPLE EMOTION ENGINE (unchanged logic)
# =========================
def detect(text):
    t = text.lower()

    if any(x in t for x in ["умор", "изтощ", "нямам сила"]):
        return "recovery"
    if any(x in t for x in ["стрес", "напрег"]):
        return "stress"
    if any(x in t for x in ["тъж", "празно"]):
        return "sad"
    if any(x in t for x in ["яд", "гнев"]):
        return "anger"
    if any(x in t for x in ["работа"]):
        return "work"
    if any(x in t for x in ["вдъхнов", "мотив"]):
        return "inspiration"

    return "neutral"

RESPONSES = {
    "recovery": "⟡ Това състояние показва нужда от възстановяване, не слабост.",
    "stress": "⟡ Наблюдава се когнитивно претоварване и напрежение.",
    "sad": "⟡ Емоционална тежест — временно вътрешно състояние.",
    "anger": "⟡ Повишена реактивност — необходима е пауза.",
    "work": "⟡ Работно напрежение и натоварване.",
    "inspiration": "⟡ Висока активност и яснота.",
    "neutral": "⟡ Балансирано състояние."
}

# =========================
# LAYOUT
# =========================
left, center, right = st.columns([1, 2.5, 1.3])

# =========================
# LEFT - ANALYSIS (unchanged)
# =========================
with left:
    st.markdown("### 🧠 Анализ")

    counts = {}
    for h in st.session_state.history:
        counts[h["emotion"]] = counts.get(h["emotion"], 0) + 1

    for k, v in counts.items():
        st.markdown(f"- {k}: {v}")

# =========================
# CENTER - CHAT
# =========================
with center:

    st.markdown("### Как се чувстваш?")

    with st.form("form", clear_on_submit=True):
        text = st.text_input("...")
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
# RIGHT - WELL-BEING (FIXED AS SINGLE CLEAN SYSTEM)
# =========================
with right:

    st.markdown("### 🧘 Well-being система")
    st.markdown("<p style='opacity:0.6; font-size:12px;'>⟡ Златни правила за баланс</p>", unsafe_allow_html=True)

    with st.expander("⟡ Дишане и нервна система"):
        st.write("Бавното дишане намалява стрес реакцията и стабилизира вниманието.")

    with st.expander("⟡ 20–20–20 правило"):
        st.write("На всеки 20 мин гледай 20 сек в далечина за да намалиш напрежението в очите.")

    with st.expander("⟡ Движение"):
        st.write("Кратките паузи възстановяват кръвообращението и яснотата на мислене.")

    with st.expander("⟡ Хидратация"):
        st.write("Недостигът на вода намалява концентрацията и енергията.")

    with st.expander("⟡ Фокус (single-tasking)"):
        st.write("Една задача = по-висока ефективност и по-нисък когнитивен шум.")

    with st.expander("⟡ Възстановяване"):
        st.write("Почивките са част от продуктивността, не прекъсване.")
