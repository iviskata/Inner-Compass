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
# EMPLOYEES & DEPARTMENTS
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
# EMOTIONAL RESPONSE ENGINE
# =========================
emotion_responses = {
    "Good": [
        "Ти днес си в много добър баланс.",
        "Лек и стабилен ден — това е сила.",
        "Продължавай в този ритъм.",
        "Енергията ти е подредена и ясна.",
        "Добър ден за продуктивност без напрежение.",
        "Изглежда всичко ти е на място.",
        "Спокойна ефективност — най-добрият тип ден.",
        "Днес работиш с лекота.",
        "Хармония между фокус и спокойствие.",
        "Стабилен и чист работен поток."
    ],
    "Neutral": [
        "Спокоен ден — и това е окей.",
        "Балансът понякога е най-доброто състояние.",
        "Нищо крайно, просто ритъм.",
        "Ден за подреждане на мисли.",
        "Стабилност без напрежение.",
        "Добър момент за кратка пауза.",
        "Рутинен, но полезен ден.",
        "Тих и равен поток.",
        "Неутралното също е прогрес.",
        "Спокойна основа за утре."
    ],
    "Bad": [
        "Тежък момент — но ще мине.",
        "Не си сам в това състояние.",
        "Спри за момент и дишай.",
        "Това е само фаза.",
        "Не трябва да носиш всичко сам.",
        "Почивката е правилният ход.",
        "Днес е трудно, но временно.",
        "Намали темпото.",
        "Не си този момент.",
        "Всичко тежко отминава."
    ]
}

# =========================
# SIDEBAR MENU
# =========================
st.sidebar.title("Inner Compass")

menu = st.sidebar.radio(
    t("Навигация", "Navigation"),
    [
        t("Табло", "Dashboard"),
        t("Въвеждане", "Check-in"),
        t("AI анализ", "AI Insights"),
        t("Данни", "Data"),
        t("Здравословна работа", "Wellbeing Guide")
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
        st.info(t("Няма данни", "No data yet"))
    else:

        moods = [d["mood"] for d in data]
        energy = [d["energy"] for d in data]

        good = moods.count("Good")
        neutral = moods.count("Neutral")
        bad = moods.count("Bad")

        avg_energy = sum(energy) / len(energy)

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Entries", len(data))
        col2.metric("Good", good)
        col3.metric("Bad", bad)
        col4.metric("Energy", f"{avg_energy:.1f}")

        st.write("---")

        st.subheader(t("Тенденции", "Trends"))

        last_7 = data[-7:]
        last_30 = data[-30:]

        col1, col2 = st.columns(2)

        with col1:
            st.write(t("Седмица", "Weekly"))
            st.line_chart([d["energy"] for d in last_7] if last_7 else [])

        with col2:
            st.write(t("Месец", "Monthly"))
            st.line_chart([d["energy"] for d in last_30] if last_30 else [])

        st.write("---")

        st.subheader(t("Здраве на екипите", "Team Health Score"))

        dept_scores = {}

        for dept in departments:
            dept_data = [d for d in data if d["department"] == dept]

            if len(dept_data) == 0:
                score = 50
            else:
                avg = sum([d["energy"] for d in dept_data]) / len(dept_data)
                bad_ratio = len([d for d in dept_data if d["mood"] == "Bad"]) / len(dept_data)
                score = int((avg * 10) - (bad_ratio * 40))

            dept_scores[dept] = score

        st.bar_chart(dept_scores)

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

    st.write("---")

    st.subheader(t("Последни записи", "Recent entries"))

    for d in st.session_state.data[-8:]:
        st.write(f"{d['time'].strftime('%Y-%m-%d %H:%M')} | {d['employee']} | {d['mood']} | {d['energy']}")

# =========================================================
# AI INSIGHTS (HR STYLE)
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
                "Наблюдава се повишено напрежение в екипа.",
                "Increased stress detected in the team."
            ))
            st.write(t(
                "Препоръка: намаляване на натоварването.",
                "Recommendation: reduce workload."
            ))

        elif avg_energy < 5:
            st.warning(t(
                "Наблюдава се спад в енергията.",
                "Energy levels are declining."
            ))
            st.write(t(
                "Препоръка: повече почивки.",
                "Recommendation: more breaks."
            ))

        else:
            st.success(t(
                "Стабилно състояние на екипа.",
                "Stable team condition."
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
# WELLBEING GUIDE
# =========================================================
elif menu == t("Здравословна работа", "Wellbeing Guide"):

    st.title(t("Здравословна работа", "Wellbeing Guide"))

    st.write(t(
        """
- Почивки на 45–60 мин  
- Правилна стойка  
- Баланс работа/почивка  
""",
        """
- Break every 45–60 min  
- Proper posture  
- Work-life balance  
"""
    ))
