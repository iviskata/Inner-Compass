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
# LANGUAGE SYSTEM
# =========================
lang = st.sidebar.selectbox("Language / Език", ["Български", "English"])

def t(bg, en):
    return bg if lang == "Български" else en

# =========================
# SIDEBAR
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
# EMPLOYEES / DEPARTMENTS
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
# HEADER
# =========================
st.markdown(
    """
    <h1 style='text-align:center;'>Inner Compass</h1>
    <h4 style='text-align:center; color:gray;'>
    AI Wellbeing & HR Intelligence Platform
    </h4>
    <hr>
    """,
    unsafe_allow_html=True
)

# =========================================================
# DASHBOARD (UPGRADED: WEEKLY + MONTHLY + TEAM SCORE)
# =========================================================
if menu == t("Табло", "Dashboard"):

    st.title(t("HR Табло", "HR Dashboard"))

    data = st.session_state.data

    if len(data) == 0:
        st.info(t("Няма данни още", "No data yet"))

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
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Entries", len(data))
        col2.metric("Good", good)
        col3.metric("Bad", bad)
        col4.metric("Avg Energy", f"{avg_energy:.1f}")

        st.write("---")

        # =========================
        # WEEK / MONTH VIEW (SIMPLIFIED)
        # =========================
        st.subheader(t("Тенденции", "Trends"))

        last_7 = data[-7:] if len(data) >= 7 else data
        last_30 = data[-30:] if len(data) >= 30 else data

        col1, col2 = st.columns(2)

        with col1:
            st.write(t("Седмица", "Weekly"))
            if len(last_7) > 0:
                st.line_chart([d["energy"] for d in last_7])
            else:
                st.info("-")

        with col2:
            st.write(t("Месец", "Monthly"))
            if len(last_30) > 0:
                st.line_chart([d["energy"] for d in last_30])
            else:
                st.info("-")

        st.write("---")

        # =========================
        # TEAM HEALTH SCORE (NEW)
        # =========================
        st.subheader("Team Health Score")

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
# CHECK-IN (UNCHANGED LOGIC)
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

        # small emotional feedback (safe minimal)
        st.info(t(
            "Благодарим ти за споделянето.",
            "Thank you for sharing."
        ))

    st.write("---")
    st.subheader(t("Последни записи", "Recent entries"))

    for d in st.session_state.data[-8:]:
        st.write(f"{d['time'].strftime('%Y-%m-%d %H:%M')} | {d['employee']} | {d['mood']} | {d['energy']}")

# =========================================================
# AI INSIGHTS (UPGRADED HUMAN HR STYLE)
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

        # HUMAN HR STYLE (NEW)
        if bad_ratio > 0.4:
            st.error(t(
                "В екипа се наблюдава повишено напрежение и емоционално натоварване.",
                "The team shows increased stress and emotional load."
            ))
            st.write(t(
                "Препоръка: облекчаване на натоварването и повече почивки.",
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
                "Екипът показва стабилно психо-емоционално състояние.",
                "The team shows stable emotional state."
            ))
            st.write(t(
                "Продължете текущия ритъм на работа.",
                "Maintain current workflow."
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

    st.title(t("Златни правила", "Wellbeing Guide"))

    st.write("## 🪑 Ergonomics")
    st.write("""
- Straight posture  
- Break every 45–60 min  
- Eye-level screen  
- Comfortable chair  
""")

    st.write("## 🧠 Mental Health")
    st.write("""
- Take breaks  
- Single-task focus  
- Avoid overload  
""")

    st.write("## ⏱ Work Balance")
    st.write("""
- 50/10 cycles  
- Prioritize tasks  
- Reduce distractions  
""")

    st.write("## 🌿 Recovery")
    st.write("""
- Walks  
- 7–9h sleep  
- Disconnect after work  
""")
