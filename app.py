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
# LANGUAGE
# =========================
lang = st.selectbox("Language", ["Български", "English"])

def t(bg, en):
    return bg if lang == "Български" else en

# =========================
# GLOBAL STYLE (UNCHANGED CORE)
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

st.markdown(f"<p style='text-align:center; opacity:0.7; font-size:13px;'>{motto}</p>", unsafe_allow_html=True)

st.markdown("---")

# =========================
# EMOTION RESPONSES (UNCHANGED)
# =========================
RESPONSES = {
"recovery": "⟡ Изтощение. Това е сигнал за нужда от възстановяване, не слабост.",
"stress": "⟡ Когнитивно претоварване. Намаляването на задачите ще върне яснота.",
"sad": "⟡ Емоционална тежест. Това състояние е временно.",
"anger": "⟡ Повишена реактивност. Пауза намалява интензитета.",
"work_stress": "⟡ Работно напрежение. Средата може да не съвпада с нуждите ти.",
"inspiration": "⟡ Висока яснота и мотивация. Подходящ момент за действие.",
"neutral": "⟡ Стабилно състояние без доминираща емоция."
}

# =========================
# EMOTION ENGINE (UNCHANGED)
# =========================
def detect(text):
    ttxt = text.lower()

    if any(w in ttxt for w in ["умор", "измор", "изтощ", "нямам сила"]):
        return "recovery"
    if any(w in ttxt for w in ["стрес", "напрег"]):
        return "stress"
    if any(w in ttxt for w in ["тъж", "празно"]):
        return "sad"
    if any(w in ttxt for w in ["яд", "гнев"]):
        return "anger"
    if any(w in ttxt for w in ["работа", "офис"]):
        return "work_stress"
    if any(w in ttxt for w in ["вдъхнов", "мотив"]):
        return "inspiration"

    return "neutral"

# =========================
# LAYOUT
# =========================
left, center, right = st.columns([1, 2.6, 1.2])

# =========================
# LEFT - ANALYSIS (UNCHANGED)
# =========================
with left:
    st.markdown("### 🧠 Анализ")

    counts = {}
    for h in st.session_state.history:
        counts[h["emotion"]] = counts.get(h["emotion"], 0) + 1

    for k, v in counts.items():
        st.markdown(f"<p style='font-size:13px; opacity:0.7'>{k}: {v}</p>", unsafe_allow_html=True)

# =========================
# CENTER - CHAT (UNCHANGED)
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
        st.markdown(f"**{h['time']} · {h['text']}**")
        st.info(RESPONSES[h["emotion"]])
        st.markdown("---")

# =========================
# RIGHT - WELL-BEING (ONLY VISUAL UPGRADE)
# =========================
with right:

    st.markdown("### 🧘 Well-being система")

    # =========================
    # QUICK RULES (SYSTEM DASHBOARD STYLE)
    # =========================
    st.markdown("""
    <div style="
        font-family: Inter, system-ui, sans-serif;
        font-size:13px;
        line-height:1.9;
        opacity:0.85;
        padding:12px;
        border:1px solid rgba(255,255,255,0.08);
        border-radius:10px;
        background: rgba(255,255,255,0.02);
    ">

    <b>⟡ Дишане</b> — 3 дълбоки вдишвания при напрежение<br>
    <b>⟡ Очна почивка</b> — 20 сек на 20 м на всеки ~20 мин<br>
    <b>⟡ Движение</b> — кратка активност на всеки 60 мин<br>
    <b>⟡ Хидратация</b> — вода през целия ден<br>
    <b>⟡ Фокус</b> — една задача = един контекст

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # =========================
    # EXPANDED (GUIDE / SERIF STYLE ONLY CHANGE HERE)
    # =========================
    with st.expander("📘 Обяснение на златните правила"):

        st.markdown("""
        <div style="
            font-family: Georgia, 'Times New Roman', serif;
            font-size:14px;
            line-height:1.85;
            letter-spacing:0.2px;
            opacity:0.9;
        ">

        <b>⟡ Дишане и нервна система</b><br>
        Дълбокото и бавно дишане активира парасимпатиковата нервна система и намалява стрес реакцията.

        <br><br>

        <b>⟡ 20–20–20 правило</b><br>
        Намалява напрежението в очите при екранна работа и възстановява вниманието.

        <br><br>

        <b>⟡ Движение</b><br>
        Кратките паузи подобряват кръвообращението и когнитивната яснота.

        <br><br>

        <b>⟡ Хидратация</b><br>
        Поддържа концентрация и умствена скорост.

        <br><br>

        <b>⟡ Фокус правило</b><br>
        Един контекст = по-ниско когнитивно натоварване.

        </div>
        """, unsafe_allow_html=True)
