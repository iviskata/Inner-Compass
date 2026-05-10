import streamlit as st
from datetime import datetime
import random

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Inner Compass — AI Wellbeing & HR Intelligence",
    layout="wide"
)

# =========================
# DATA STORAGE
# =========================
if "data" not in st.session_state:
    st.session_state.data = []

# =========================
# LANGUAGE SYSTEM (GLOBAL FIX)
# =========================
lang = st.sidebar.selectbox("Language / Език", ["Български", "English"])

def t(bg, en):
    return bg if lang == "Български" else en

# =========================
# SIDEBAR
# =========================
st.sidebar.markdown("## Inner Compass")
st.sidebar.caption(t("AI Wellbeing & HR Intelligence", "AI Wellbeing & HR Intelligence"))

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
# EMPLOYEES / DEPARTMENTS
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
# HEADER (FULL TRANSLATED)
# =========================
st.markdown(
    f"""
    <h1 style='text-align:center;'>Inner Compass</h1>
    <h4 style='text-align:center; color:gray;'>
    {t("AI Платформа за благосъстояние и HR анализ", "AI Wellbeing & HR Intelligence Platform")}
    </h4>
    <hr>
    """,
    unsafe_allow_html=True
)

# =========================================================
# DASHBOARD (UPGRADED UI + FULL TRANSLATION)
# =========================================================
if menu == t("Табло", "Dashboard"):

    st.title(t("HR Табло", "HR Dashboard"))

    data = st.session_state.data

    if len(data) == 0:
        st.info(t("Няма данни все още", "No data yet"))

    else:

        moods = [d["mood"] for d in data]
        energy = [d["energy"] for d in data]

        good = moods.count("Good")
        neutral = moods.count("Neutral")
        bad = moods.count("Bad")

        avg_energy = sum(energy) / len(energy)

        # =========================
        # KPI CARDS
        # =========================
        c1, c2, c3, c4 = st.columns(4)

        c1.metric(t("Записи", "Entries"), len(data))
        c2.metric(t("Добро", "Good"), good)
        c3.metric(t("Лошо", "Bad"), bad)
        c4.metric(t("Енергия", "Energy"), f"{avg_energy:.1f}")

        st.write("---")

        # =========================
        # TRENDS (FULL TRANSLATED)
        # =========================
        st.subheader(t("Тенденции", "Trends"))

        last_7 = data[-7:]
        last_30 = data[-30:]

        col1, col2 = st.columns(2)

        with col1:
            st.write(t("Седмична енергия", "Weekly Energy"))
            if len(last_7) > 0:
                st.line_chart([d["energy"] for d in last_7])
            else:
                st.info("-")

        with col2:
            st.write(t("Месечна енергия", "Monthly Energy"))
            if len(last_30) > 0:
                st.line_chart([d["energy"] for d in last_30])
            else:
                st.info("-")

        st.write("---")

        # =========================
        # TEAM HEALTH SCORE (TRANSLATED LABELS)
        # =========================
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
# CHECK-IN (UNCHANGED LOGIC, FIXED TEXTS)
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

        st.info(t(
            "Благодарим за споделянето.",
            "Thank you for sharing."
        ))

    st.write("---")
    st.subheader(t("Последни записи", "Recent entries"))

    for d in st.session_state.data[-8:]:
        st.write(f"{d['time'].strftime('%Y-%m-%d %H:%M')} | {d['employee']} | {d['mood']} | {d['energy']}")

# =========================================================
# AI INSIGHTS (FULL HUMAN HR STYLE + TRANSLATION FIX)
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
                "Наблюдава се повишено натоварване и напрежение в екипа.",
                "Increased stress and workload detected in the team."
            ))
            st.write(t(
                "Препоръка: намаляване на натоварването и повече възстановяване.",
                "Recommendation: reduce workload and increase recovery time."
            ))

        elif avg_energy < 5:
            st.warning(t(
                "Наблюдава се спад в енергията на екипа.",
                "Team energy levels are declining."
            ))
            st.write(t(
                "Препоръка: оптимизация на работния ритъм.",
                "Recommendation: optimize work rhythm."
            ))

        else:
            st.success(t(
                "Екипът показва стабилно състояние.",
                "The team shows stable performance and emotional balance."
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

    st.title(t("Здравословна работа", "Workplace Wellbeing"))

    st.write("## 🪑 " + t("Ергономия", "Ergonomics"))
    st.write(t("""
- Правилна стойка  
- Почивки на 45–60 мин  
- Удобен стол  
""",
"""
- Correct posture  
- Break every 45–60 min  
- Ergonomic chair  
"""))

    st.write("## 🧠 " + t("Психично здраве", "Mental Health"))
    st.write(t("""
- Почивки  
- Фокус  
- Без пренатоварване  
""",
"""
- Take breaks  
- Focus  
- Avoid overload  
"""))
