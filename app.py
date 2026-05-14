import streamlit as st
from datetime import datetime
import random

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Inner Compass — AI Wellbeing & HR Intelligence",
    page_icon="logo.png.png",   # ✅ FAVICON
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
# STYLE
# =========================
st.markdown("""
<style>
.block-container { padding-top: 2rem; }
.metric-card {
    background: #ffffff;
    padding: 18px;
    border-radius: 14px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    text-align: center;
}
.small-title { font-size: 13px; color: gray; }
.big-number { font-size: 28px; font-weight: 600; }
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER (LOGO INSTEAD OF TEXT)
# =========================
st.markdown("<div style='text-align:center; padding-top:10px;'>", unsafe_allow_html=True)
st.image("logo.png", width=180)   # ✅ LOGO HEADER
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center;'>
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
# CHECK-IN (UPDATED)
# =========================================================
elif menu == t("Въвеждане", "Check-in"):

    st.title(t("Дневно въвеждане", "Daily Check-in"))

    employee = st.selectbox(t("Служител", "Employee"), employees)
    department = st.selectbox(t("Отдел", "Department"), departments)

    mood = st.radio(t("Настроение", "Mood"), ["Good", "Neutral", "Bad"])
    energy = st.slider(t("Енергия", "Energy"), 1, 10, 5)
    note = st.text_input(t("Бележка", "Note"))

    # ✅ NEW: Management feedback
    feedback = st.text_area(
        t("Suggestions to Management", "Suggestions to Management")
    )

    if st.button(t("Запази", "Save")):

        st.session_state.data.append({
            "time": datetime.now(),
            "employee": employee,
            "department": department,
            "mood": mood,
            "energy": energy,
            "note": note,
            "feedback": feedback   # ✅ NEW FIELD
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
                "Recommendation: lighter workload."
            ))

        else:

            st.success(t(
                "Стабилно състояние на екипа.",
                "Stable team condition."
            ))

            st.info(t(
                "Продължете текущия подход.",
                "Continue current approach."
            ))

# =========================================================
# DATA (UPDATED TABLE)
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

    st.title(t("Баланс работа и ум", "Work & Mind Balance"))

    st.markdown(t("""
## 🪑 Ергономия
- Правилна стойка  
- Монитор на нивото на очите  
- Удобен стол  
- Без прегърбване  

## ⏱ Ритъм
- Почивки на 45–60 мин  
- 50/10 цикъл  
- Разделяй задачите  

## 🧠 Ментално здраве
- Без мултитаскинг  
- Фокус върху 1 задача  
- Намаляване на известия  

## 🌿 Възстановяване
- Разходки  
- 7–9 часа сън  
- Почивка след работа  
""",
"""
## 🪑 Ergonomics
- Correct posture  
- Eye-level monitor  
- Comfortable chair  
- No slouching  

## ⏱ Rhythm
- Break every 45–60 min  
- 50/10 cycles  
- Task splitting  

## 🧠 Mental health
- No multitasking  
- Single focus  
- Reduce notifications  

## 🌿 Recovery
- Walks  
- 7–9h sleep  
- Rest after work  
"""))
