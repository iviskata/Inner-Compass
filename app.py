import streamlit as st
from datetime import datetime

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
# LANGUAGE SYSTEM (RESTORED)
# =========================
lang = st.sidebar.selectbox("Language / Език", ["Български", "English"])

def t(bg, en):
    return bg if lang == "Български" else en

# =========================
# SIDEBAR BRANDING (SAFE ADDITION)
# =========================
st.sidebar.markdown("## Inner Compass")
st.sidebar.caption("AI Wellbeing & HR Intelligence")

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
# EMPLOYEES / DEPARTMENTS (IMPROVED STRUCTURE)
# =========================
employees = ["Employee A", "Employee B", "Employee C", "Employee D"]

departments = [
    "Human Resources (HR)",
    "Development",
    "Operations",
    "Support",
    "Management"
]

# =========================
# GLOBAL HEADER (BRAND - FIXED TOP)
# =========================
st.markdown(
    f"""
    <h1 style='text-align:center; margin-bottom:5px;'>
    Inner Compass
    </h1>
    <h4 style='text-align:center; color:gray; margin-top:0px;'>
    {t("AI Wellbeing & HR Intelligence Платформа", "AI Wellbeing & HR Intelligence Platform")}
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
        st.info(t("Няма данни все още", "No data yet"))

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Entries", "0")
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
            st.subheader(t("Енергия", "Energy Trend"))
            st.line_chart(energy)

        with col2:
            st.subheader(t("Настроение", "Mood Distribution"))
            st.bar_chart({
                "Good": good,
                "Neutral": neutral,
                "Bad": bad
            })

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

    st.write("---")
    st.subheader(t("Последни записи", "Recent entries"))

    for d in st.session_state.data[-8:]:
        st.write(f"{d['time'].strftime('%Y-%m-%d %H:%M')} | {d['employee']} | {d['mood']} | {d['energy']}")

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

        col1, col2 = st.columns(2)

        with col1:
            st.subheader(t("Наблюдение", "Observation"))

            if bad_ratio > 0.4:
                st.error(t("Висок стрес", "High stress"))
            elif avg_energy < 5:
                st.warning(t("Ниска енергия", "Low energy"))
            else:
                st.success(t("Стабилно", "Stable"))

        with col2:
            st.subheader(t("Анализ", "Insight"))

            if bad_ratio > 0.4:
                st.write(t("Натрупан стрес.", "Accumulated stress."))
                st.write(t("Намалете натоварването.", "Reduce workload."))
            elif avg_energy < 5:
                st.write(t("Умора.", "Fatigue."))
                st.write(t("Повече почивки.", "More breaks."))
            else:
                st.write(t("Без рискови модели.", "No risk patterns."))

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
# WELLBEING GUIDE (NEW MODULE - SAFE ADDITION)
# =========================================================
elif menu == t("Здравословна работа", "Wellbeing Guide"):

    st.title(t("Златни правила за здравословна работа", "Healthy Work Guidelines"))

    st.write(t("## 🪑 Ергономия", "## 🪑 Ergonomics"))
    st.write(t("""
- Прав гръб  
- Почивка на 45–60 мин  
- Екран на нивото на очите  
- Удобен стол  
""",
"""
- Straight posture  
- Break every 45–60 min  
- Eye-level screen  
- Ergonomic chair  
"""))

    st.write(t("## 🧠 Психично здраве", "## 🧠 Mental Health"))
    st.write(t("""
- Почивки са задължителни  
- Фокус върху една задача  
- Не трупай стрес  
""",
"""
- Take breaks  
- Single-task focus  
- Avoid stress buildup  
"""))

    st.write(t("## ⏱ Баланс", "## ⏱ Balance"))
    st.write(t("""
- 50/10 работен цикъл  
- Приоритети  
- Минимални разсейвания  
""",
"""
- 50/10 work cycle  
- Prioritize tasks  
- Reduce distractions  
"""))

    st.write(t("## 🌿 Възстановяване", "## 🌿 Recovery"))
    st.write(t("""
- Разходки  
- Сън 7–9 часа  
- Изключване след работа  
""",
"""
- Walks  
- 7–9h sleep  
- Disconnect after work  
"""))
