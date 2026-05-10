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
# CALM AESTHETIC STYLE 🌿
# =========================
st.markdown("""
<style>

/* soft gradient background */
.stApp {
    background: linear-gradient(135deg, #e8f5f0 0%, #f4f7ff 50%, #eef9f2 100%);
}

/* glass-like cards */
div[data-testid="stMetric"] {
    background: rgba(255, 255, 255, 0.7);
    border-radius: 16px;
    padding: 12px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.05);
    backdrop-filter: blur(8px);
}

/* sidebar soft */
section[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.6);
}

/* text soft */
h1, h2, h3 {
    color: #2c3e50;
}

</style>
""", unsafe_allow_html=True)

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
# EMOTIONS
# =========================
emotion_responses = {
    "Good": [
        "Днес си в стабилен и лек ритъм.",
        "Енергията ти е подредена.",
        "Спокоен и продуктивен ден.",
        "Балансът ти работи добре.",
        "Добър поток на мисли и работа."
    ],
    "Neutral": [
        "Спокоен, равен ден.",
        "Баланс без крайности.",
        "Тих работен ритъм.",
        "Стабилно състояние.",
        "Нормален ден — и това е окей."
    ],
    "Bad": [
        "Труден момент — но временен.",
        "Дишай и забави темпото.",
        "Почивката е правилният ход.",
        "Не носи всичко сам.",
        "Това ще премине."
    ]
}

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

# =========================
# HEADER
# =========================
st.markdown("""
<div style='text-align:center; padding:10px 0 20px 0;'>
    <h1>Inner Compass</h1>
    <p style='color:#5f6f81;'>AI HR & Wellbeing Intelligence Platform</p>
</div>
<hr style='opacity:0.3'>
""", unsafe_allow_html=True)

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

        col1.metric("Entries", len(data))
        col2.metric("Good", moods.count("Good"))
        col3.metric("Bad", moods.count("Bad"))
        col4.metric("Energy", f"{sum(energy)/len(energy):.1f}")

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

            st.error(t(
                "Повишено напрежение в екипа.",
                "Increased stress detected."
            ))

            st.write(t(
                "Препоръка: повече почивки и по-ниско натоварване.",
                "Recommendation: more breaks and reduced workload."
            ))

        elif avg_energy < 5:

            st.warning(t(
                "Спад в енергията.",
                "Energy levels are declining."
            ))

            st.write(t(
                "Препоръка: по-лек ритъм.",
                "Recommendation: lighter pace."
            ))

        else:

            st.success(t(
                "Стабилно състояние на екипа.",
                "Stable team condition."
            ))

            st.info(t(
                "Продължете текущия баланс.",
                "Continue current balance."
            ))

# =========================================================
# DATA
# =========================================================
elif menu == t("Данни", "Data"):

    st.title(t("HR данни", "HR Data"))

    if len(st.session_state.data) == 0:
        st.info(t("Няма данни", "No data"))
    else:
        st.dataframe(st.session_state.data, use_container_width=True)

# =========================================================
# WELLBEING
# =========================================================
elif menu == t("Work & Mind Balance", "Work & Mind Balance"):

    st.title(t("Баланс ум и работа", "Work & Mind Balance"))

    st.markdown(t("""
## 🪑 Ергономия
- Правилна стойка  
- Монитор на нивото на очите  
- Удобен стол  

## ⏱ Ритъм
- Почивки на 45–60 мин  
- Баланс работа/почивка  

## 🧠 Ментално здраве
- Фокус върху една задача  
- Без излишни известия  

## 🌿 Възстановяване
- Разходки  
- Сън 7–9 часа  
""",
"""
## 🪑 Ergonomics
- Correct posture  
- Eye-level monitor  
- Comfortable chair  

## ⏱ Rhythm
- Break every 45–60 min  
- Work/rest balance  

## 🧠 Mental health
- Single task focus  
- Reduce notifications  

## 🌿 Recovery
- Walks  
- 7–9h sleep  
"""))
