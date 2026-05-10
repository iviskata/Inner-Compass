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
        "Енергията ти е подредена и ясна.",
        "Добър баланс между фокус и спокойствие.",
        "Стабилна продуктивност без напрежение.",
        "Ден, в който нещата се случват естествено."
    ],
    "Neutral": [
        "Спокоен и равен ден.",
        "Нормален ритъм — и това е добре.",
        "Тихо, без напрежение.",
        "Баланс без крайности.",
        "Стабилна основа за работа."
    ],
    "Bad": [
        "Труден момент — но временен.",
        "Дай си пауза.",
        "Намали темпото.",
        "Не носи всичко сам.",
        "Това ще отмине."
    ]
}

# =========================
# SIDEBAR
# =========================
st.sidebar.title("Inner Compass")

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
st.markdown(
    f"""
    <h1 style='text-align:center;'>Inner Compass</h1>
    <h4 style='text-align:center; color:gray;'>
    {t("AI платформа за HR и благосъстояние", "AI HR & Wellbeing Platform")}
    </h4>
    <hr>
    """,
    unsafe_allow_html=True
)

# =========================================================
# DASHBOARD
# =========================================================
if menu == t("Табло", "Dashboard"):

    st.title(t("HR Табло", "HR Dashboard"))

    data = st.session_state.data

    if len(data) == 0:
        st.info(t("Няма данни", "No data"))
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

        st.columns(2)[0].line_chart([d["energy"] for d in data[-7:]])
        st.columns(2)[1].line_chart([d["energy"] for d in data[-30:]])

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
# AI INSIGHTS (IMPROVED FINAL LOGIC)
# =========================================================
elif menu == t("AI анализ", "AI Insights"):

    st.title("AI HR Intelligence")

    data = st.session_state.data

    if len(data) == 0:
        st.info(t("Няма данни", "No data"))

    else:

        bad_ratio = len([d for d in data if d["mood"] == "Bad"]) / len(data)
        avg_energy = sum([d["energy"] for d in data]) / len(data)

        st.subheader(t("HR интерпретация", "HR Interpretation"))

        if bad_ratio > 0.4:

            st.error(t(
                "Повишено напрежение в екипа.",
                "Increased stress detected in the team."
            ))

            st.markdown(t(
                """
### Препоръки:
- Намаляване на натоварването  
- Повече почивки  
- 1:1 разговори  
- Изчистване на приоритети  
                """,
                """
### Recommendations:
- Reduce workload  
- More breaks  
- 1:1 check-ins  
- Clarify priorities  
                """
            ))

        elif avg_energy < 5:

            st.warning(t(
                "Спад в енергията.",
                "Energy levels are declining."
            ))

            st.markdown(t(
                """
### Препоръки:
- По-лек ритъм  
- Кратки почивки  
- Фокус върху основното  
                """,
                """
### Recommendations:
- Lighter workload  
- Short breaks  
- Focus on essentials  
                """
            ))

        else:

            st.success(t(
                "Стабилно и здравословно състояние.",
                "Stable and healthy team condition."
            ))

            st.info(t(
                "Продължете текущия подход — работи добре.",
                "Continue current approach — it works well."
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
# WELLBEING (RESTORED + ENHANCED)
# =========================================================
elif menu == t("Work & Mind Balance", "Work & Mind Balance"):

    st.title(t("Баланс работа и ум", "Work & Mind Balance"))

    st.markdown(t(
        """
## 🪑 Ергономия
- Поддържай правилна стойка  
- Монитор на нивото на очите  
- Стол с добра опора  
- Не работи приведен дълго  

## ⏱ Ритъм на работа
- Почивки на 45–60 минути  
- 50/10 работен цикъл  
- Разделяй задачите на малки части  
- Не работи без пауза дълго време  

## 🧠 Ментално здраве
- Не мултитасквай постоянно  
- Дай си “тихо време” без чатове  
- Намали известията  
- Фокус върху една задача  

## 🌿 Възстановяване
- Разходки през деня  
- Достатъчен сън (7–9 часа)  
- Излизане от работната среда след работа  
- Време без екран  

## 🔥 Продуктивност без изгаряне
- По-бавно = по-качествено  
- Почивката е част от работата  
- Балансът създава резултат  
""",
        """
## 🪑 Ergonomics
- Keep correct posture  
- Screen at eye level  
- Proper chair support  
- Avoid long slouching  

## ⏱ Work rhythm
- Break every 45–60 min  
- 50/10 work cycles  
- Split tasks into small steps  
- Don’t work without pause  

## 🧠 Mental health
- Avoid constant multitasking  
- Silent focus time  
- Reduce notifications  
- Single-task focus  

## 🌿 Recovery
- Walk during the day  
- Sleep 7–9 hours  
- Disconnect after work  
- Screen-free time  

## 🔥 Sustainable productivity
- Slower = higher quality  
- Rest is part of work  
- Balance creates results  
"""
    ))
