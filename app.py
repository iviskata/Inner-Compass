import streamlit as st
from datetime import datetime

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Inner Compass HR", layout="wide")

# =========================
# DATA STORAGE
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
# SIDEBAR NAVIGATION
# =========================
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
employees = ["Employee A", "Employee B", "Employee C"]
departments = ["Development", "Marketing", "Sales"]

# =========================
# DASHBOARD
# =========================
if menu == t("Табло", "Dashboard"):

    st.title(t("HR Табло за управление", "HR Dashboard"))

    data = st.session_state.data

    if len(data) == 0:
        st.info(t("Няма данни още, но структурата на системата е активна.", "No data yet, but system is active."))

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total", "0")
        col2.metric("Good", "0")
        col3.metric("Bad", "0")
        col4.metric("Avg Energy", "0")

    else:

        moods = [d["mood"] for d in data]
        energy = [d["energy"] for d in data]

        good = moods.count("Good")
        neutral = moods.count("Neutral")
        bad = moods.count("Bad")

        avg_energy = sum(energy) / len(energy)

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(t("Записи", "Entries"), len(data))
        col2.metric(t("Добро", "Good"), good)
        col3.metric(t("Лошо", "Bad"), bad)
        col4.metric(t("Енергия", "Energy"), f"{avg_energy:.1f}")

        st.write("---")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader(t("Енергийна тенденция", "Energy Trend"))
            st.line_chart(energy)

        with col2:
            st.subheader(t("Настроение", "Mood"))
            st.bar_chart({
                "Good": good,
                "Neutral": neutral,
                "Bad": bad
            })

# =========================
# CHECK-IN
# =========================
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
        st.success(t("Записано", "Saved"))

    st.write("---")
    st.subheader(t("Последни записи", "Recent entries"))

    for d in st.session_state.data[-8:]:
        st.write(f"{d['time'].strftime('%Y-%m-%d %H:%M')} | {d['employee']} | {d['mood']} | {d['energy']}")

# =========================
# AI INSIGHTS
# =========================
elif menu == t("AI анализ", "AI Insights"):

    st.title(t("AI HR анализ", "AI HR Analysis"))

    data = st.session_state.data

    if len(data) == 0:
        st.info(t("Няма данни за анализ", "No data to analyze"))
    else:

        bad_ratio = len([d for d in data if d["mood"] == "Bad"]) / len(data)
        avg_energy = sum([d["energy"] for d in data]) / len(data)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader(t("Наблюдение", "Observation"))

            if bad_ratio > 0.4:
                st.error(t("Повишено напрежение", "High stress detected"))
            elif avg_energy < 5:
                st.warning(t("Ниска енергия", "Low energy detected"))
            else:
                st.success(t("Стабилно състояние", "Stable condition"))

        with col2:
            st.subheader(t("Анализ", "Insight"))

            if bad_ratio > 0.4:
                st.write(t(
                    "Вероятно има натрупване на стрес.",
                    "Likely accumulated stress in team."
                ))
                st.write(t(
                    "Препоръка: намаляване на натоварването.",
                    "Recommendation: reduce workload."
                ))
            elif avg_energy < 5:
                st.write(t(
                    "Възможна умора.",
                    "Possible fatigue."
                ))
                st.write(t(
                    "Препоръка: повече почивки.",
                    "Recommendation: more breaks."
                ))
            else:
                st.write(t(
                    "Няма проблемни модели.",
                    "No risk patterns detected."
                ))

# =========================
# DATA VIEW
# =========================
elif menu == t("Данни", "Data"):

    st.title(t("HR данни", "HR Data"))

    if len(st.session_state.data) == 0:
        st.info(t("Няма данни", "No data"))
    else:
        st.dataframe(st.session_state.data, use_container_width=True)

# =========================
# WELLBEING GUIDE
# =========================
elif menu == t("Здравословна работа", "Wellbeing Guide"):

    st.title(t("Златни правила за здравословна работа", "Healthy Work Guidelines"))

    st.write(t("## 🪑 Ергономия", "## 🪑 Ergonomics"))

    st.write(t("""
- Дръж гърба изправен  
- Почивка на всеки 45–60 минути  
- Екран на нивото на очите  
- Удобен стол е задължителен  
""",
"""
- Keep back straight  
- Break every 45–60 min  
- Screen at eye level  
- Use ergonomic chair  
"""))

    st.write("---")

    st.write(t("## 🧠 Психично здраве", "## 🧠 Mental Health"))

    st.write(t("""
- Не работи без почивки  
- Фокус върху една задача  
- Не трупай стрес  
- Говори с екипа  
""",
"""
- Take regular breaks  
- Focus on one task  
- Do not accumulate stress  
- Communicate with team  
"""))

    st.write("---")

    st.write(t("## ⏱ Работа и фокус", "## ⏱ Focus & Work"))

    st.write(t("""
- 50 мин работа / 10 мин почивка  
- Най-важната задача първо  
- Минимизирай разсейването  
""",
"""
- 50 min work / 10 min break  
- Do important task first  
- Reduce distractions  
"""))

    st.write("---")

    st.write(t("## 🌿 Баланс", "## 🌿 Balance"))

    st.write(t("""
- Почивка след работа  
- Разходки  
- 7–9 часа сън  
""",
"""
- Disconnect after work  
- Walks and movement  
- 7–9 hours sleep  
"""))
