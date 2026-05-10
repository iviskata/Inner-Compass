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
# LANGUAGE
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
# EMOTIONS
# =========================
emotion_responses = {
    "Good": [
        "Днес си в стабилен ритъм.",
        "Енергията ти е балансирана.",
        "Спокоен и продуктивен ден.",
        "Добър поток на работа.",
        "Всичко е под контрол."
    ],
    "Neutral": [
        "Спокоен, равен ден.",
        "Нормален ритъм.",
        "Баланс без крайности.",
        "Тих работен ден.",
        "Стабилно състояние."
    ],
    "Bad": [
        "Труден момент — ще отмине.",
        "Забави темпото.",
        "Почивката е важна.",
        "Не си сам.",
        "Дишай спокойно."
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
# HEADER (CLEAN)
# =========================
st.title("Inner Compass")
st.caption("AI HR & Wellbeing Intelligence Platform")

st.write("---")

# =========================================================
# DASHBOARD
# =========================================================
if menu == t("Табло", "Dashboard"):

    st.header(t("HR Табло", "HR Dashboard"))

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

    st.header(t("Дневно въвеждане", "Daily Check-in"))

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

    st.header("AI HR Intelligence")

    data = st.session_state.data

    if len(data) == 0:
        st.info(t("Няма данни", "No data"))
    else:

        bad_ratio = len([d for d in data if d["mood"] == "Bad"]) / len(data)
        avg_energy = sum([d["energy"] for d in data]) / len(data)

        if bad_ratio > 0.4:

            st.error(t(
                "Повишено напрежение в екипа.",
                "Increased stress detected in the team."
            ))

            st.write(t(
                "Препоръка: намаляване на натоварването и повече почивки.",
                "Recommendation: reduce workload and increase breaks."
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

    st.header(t("HR данни", "HR Data"))

    if len(st.session_state.data) == 0:
        st.info(t("Няма данни", "No data"))
    else:
        st.dataframe(st.session_state.data, use_container_width=True)

# =========================================================
# WELLBEING
# =========================================================
elif menu == t("Work & Mind Balance", "Work & Mind Balance"):

    st.header(t("Баланс работа и ум", "Work & Mind Balance"))

    st.markdown(t("""
## Ергономия
- Правилна стойка  
- Монитор на нивото на очите  
- Удобен стол  

## Ритъм на работа
- Почивки на 45–60 мин  
- Баланс работа/почивка  

## Ментално здраве
- Фокус върху една задача  
- Намаляване на известия  

## Възстановяване
- Разходки  
- Сън 7–9 часа  
""",
"""
## Ergonomics
- Correct posture  
- Eye-level monitor  
- Comfortable chair  

## Work rhythm
- Break every 45–60 min  
- Work-life balance  

## Mental health
- Single task focus  
- Reduce notifications  

## Recovery
- Walks  
- 7–9h sleep  
"""))
