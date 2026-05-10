import streamlit as st
from datetime import datetime
import random

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Inner Compass — AI Wellbeing & HR Intelligence",
    layout="wide"
)

# =========================
# STATE
# =========================
if "data" not in st.session_state:
    st.session_state.data = []

# =========================
# LANGUAGE SYSTEM
# =========================
lang = st.sidebar.selectbox("Language / Език", ["Български", "English"])

def t(bg, en):
    return bg if lang == "Български" else en

# =========================
# DATA
# =========================
employees = ["Employee A", "Employee B", "Employee C", "Employee D"]

departments = [
    t("Човешки ресурси", "Human Resources"),
    t("Разработка", "Development"),
    t("Операции", "Operations"),
    t("Поддръжка", "Support"),
    t("Управление", "Management")
]

# =========================
# EMOTIONAL ENGINE
# =========================
emotion_responses = {
    "Good": [
        "Днес си в стабилен и лек ритъм.",
        "Енергията ти е подредена.",
        "Добър баланс между фокус и спокойствие.",
        "Стабилна продуктивност без напрежение.",
        "Всичко ти е на място днес."
    ],
    "Neutral": [
        "Спокоен и равен ден.",
        "Нищо крайно — и това е окей.",
        "Балансът е стабилен.",
        "Тих работен ритъм.",
        "Неутрално състояние."
    ],
    "Bad": [
        "Труден момент — но временен.",
        "Дишай и забави темпото.",
        "Не си сам в това.",
        "Това ще премине.",
        "Почивката е правилният ход."
    ]
}

# =========================
# 🔥 FIXED DARK MODE (ONLY ADDITION)
# =========================
st.markdown("""
<style>

/* FULL DARK BACKGROUND (FOR ALL DEVICES) */
html, body, .stApp {
    background-color: #0e1117 !important;
    color: #ffffff !important;
}

/* FORCE ALL TEXT WHITE */
* {
    color: #ffffff !important;
}

/* MAIN CONTAINER */
.block-container {
    background-color: #0e1117 !important;
}

/* HEADER LINES */
hr {
    border-color: #2a2f3a !important;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #0b0f19 !important;
}

/* CARDS */
.metric-card {
    background: #1a1f2e;
    padding: 18px;
    border-radius: 14px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.6);
    text-align: center;
}

/* CARD TEXT */
.small-title {
    font-size: 13px;
    color: #a0a0a0 !important;
}

.big-number {
    font-size: 28px;
    font-weight: 600;
    color: #ffffff !important;
}

/* INPUTS */
input, textarea, select {
    background-color: #1a1f2e !important;
    color: #ffffff !important;
    border: 1px solid #333 !important;
}

/* DATAFRAME */
div[data-testid="stDataFrame"] {
    background-color: #0e1117 !important;
    color: #ffffff !important;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("""
<div style='text-align:center; padding:20px 0;'>
    <h1>Inner Compass</h1>
    <p style='color:gray;'>AI HR & Wellbeing Intelligence Platform</p>
</div>
<hr>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
menu = st.sidebar.radio(
    t("Навигация", "Navigation"),
    [
        t("Табло", "Dashboard"),
        t("Въвеждане", "Check-in"),
        t("AI анализ", "AI Insights"),
        t("Данни", "Data"),
        t("Work & Mind Balance", "Work & Mind Balance")
    ]
)

# =========================================================
# DASHBOARD
# =========================================================
if menu == t("Табло", "Dashboard"):

    st.title(t("HR Табло", "HR Dashboard"))

    data = st.session_state.data

    if len(data) == 0:
        st.info(t("Няма данни", "No data yet"))

    else:
        moods = [d["mood"] for d in data]
        energy = [d["energy"] for d in data]

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown(f"<div class='metric-card'><div class='small-title'>Entries</div><div class='big-number'>{len(data)}</div></div>", unsafe_allow_html=True)

        with col2:
            st.markdown(f"<div class='metric-card'><div class='small-title'>Good</div><div class='big-number'>{moods.count('Good')}</div></div>", unsafe_allow_html=True)

        with col3:
            st.markdown(f"<div class='metric-card'><div class='small-title'>Bad</div><div class='big-number'>{moods.count('Bad')}</div></div>", unsafe_allow_html=True)

        with col4:
            avg = sum(energy)/len(energy)
            st.markdown(f"<div class='metric-card'><div class='small-title'>Energy</div><div class='big-number'>{avg:.1f}</div></div>", unsafe_allow_html=True)

        st.write("---")

        st.subheader(t("Тенденции", "Trends"))

        col1, col2 = st.columns(2)

        with col1:
            st.write(t("Седмица", "Weekly"))
            st.line_chart([d["energy"] for d in data[-7:]])

        with col2:
            st.write(t("Месец", "Monthly"))
            st.line_chart([d["energy"] for d in data[-30:]])

# =========================================================
# CHECK-IN
# =========================================================
elif menu == t("Въвеждане", "Check-in"):

    st.title(t("Дневно въвеждане", "Daily Check-in"))

    employee = st.selectbox(t("Служител", "Employee"), employees)
    department = st.selectbox(t("Отдел", "Department"), departments)

    mood = st.radio(t("Настроение", "Mood"), ["Good", "Neutral", "Bad"])
    energy = st.slider(t("Енергия", "Energy"), 1, 10, 5)
    note = st.text_input(t("Бележка", "Note"))

    if st.button(t("Запази", "Save")):

        st.session_state.data.append({
            "time": datetime.now(),
            "employee": employee,
            "department": department,
            "mood": mood,
            "energy": energy,
            "note": note
        })

        st.success(t("Записано успешно", "Saved successfully"))
        st.info(random.choice(emotion_responses[mood]))

# =========================================================
# AI INSIGHTS
# =========================================================
elif menu == t("AI анализ", "AI Insights"):

    st.title("AI HR Intelligence")

    data = st.session_state.data

    if len(data) == 0:
        st.info(t("Няма данни", "No data"))
    else:

        bad_ratio = len([d for d in data if d["mood"] == "Bad"]) / len(data)
        avg_energy = sum([d["energy"] for d in data]) / len(data)

        if bad_ratio > 0.4:
            st.error("Повишено напрежение в екипа.")
        elif avg_energy < 5:
            st.warning("Спад в енергията.")
        else:
            st.success("Стабилно състояние на екипа.")

# =========================================================
# DATA
# =========================================================
elif menu == t("Данни", "Data"):

    st.title("HR Data")

    if len(st.session_state.data) == 0:
        st.info("No data")
    else:
        st.dataframe(st.session_state.data, use_container_width=True)

# =========================================================
# WELLBEING
# =========================================================
elif menu == t("Work & Mind Balance", "Work & Mind Balance"):

    st.title("Work & Mind Balance")

    st.markdown("""
## 🪑 Ергономия
- Правилна стойка  
- Монитор на нивото на очите  

## ⏱ Ритъм
- Почивки  

## 🧠 Фокус
- Една задача  

## 🌿 Възстановяване
- Сън и разходки  
""")
