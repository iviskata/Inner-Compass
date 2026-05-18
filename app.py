import streamlit as st
from datetime import datetime
import random
import pandas as pd

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Inner Compass — AI Wellbeing & HR Intelligence",
    page_icon="logo.png",
    layout="wide"
)

# =========================
# STATE
# =========================
if "data" not in st.session_state:
    st.session_state.data = []

# ✅ NEW STATE FOR CHALLENGES
if "challenge_data" not in st.session_state:
    st.session_state.challenge_data = []

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
    background: linear-gradient(135deg, #1f1f2e, #2b2b40);
    padding: 18px;
    border-radius: 16px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.25);
    text-align: center;
    color: white;
}

.small-title { font-size: 13px; color: gray; }
.big-number { font-size: 30px; font-weight: 700; margin-top: 8px; }

.challenge-card {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    padding: 22px;
    border-radius: 18px;
    color: white;
    margin-bottom: 20px;
    border: 1px solid rgba(255,255,255,0.08);
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("logo.png", width=420)

    st.markdown(
        """
        <div style='text-align:center; margin-top:10px;'>
            <p style='color:gray; font-size:14px;'>
                AI HR & Wellbeing Intelligence Platform
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<hr>", unsafe_allow_html=True)

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
        t("Work & Mind Balance", "Work & Mind Balance"),
        t("Уелнес предизвикателства", "Wellbeing Challenges")
    ]
)

# =========================
# DASHBOARD
# =========================
if menu == t("Табло", "Dashboard"):

    st.title(t("HR Табло", "HR Dashboard"))

    data = st.session_state.data

    if len(data) == 0:
        st.info(t("Няма данни", "No data yet"))

    else:
        moods = [d["mood"] for d in data]
        energy = [d["energy"] for d in data]
        avg = sum(energy) / len(energy)

        def metric(title, value, emoji):
            st.markdown(f"""
            <div class="metric-card">
                <div style="font-size: 13px; color: gray;">{emoji} {title}</div>
                <div style="font-size: 30px; font-weight: 700; margin-top: 8px;">
                    {value}
                </div>
            </div>
            """, unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            metric("Total Check-ins", len(data), "📊")

        with col2:
            metric("Positive Mood", moods.count("Good"), "😊")

        with col3:
            metric("Attention Needed", moods.count("Bad"), "⚠️")

        with col4:
            metric("Team Energy", f"{avg:.1f}", "⚡")

        st.write("---")

        # ✅ ACTIVE CHALLENGE PREVIEW
        st.markdown("""
        <div class="challenge-card">
            <h3>🏆 Active Monthly Challenge</h3>
            <p>Movement & Energy Challenge</p>
            <p>Employees collect points through steps, movement and healthy routines.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Live Team Status")

        if moods.count("Bad") / len(data) > 0.4:
            st.error("⚠️ Increased stress detected in the team.")
        elif avg < 5:
            st.warning("🔋 Team energy levels are declining.")
        else:
            st.success("🟢 Team morale is stable today.")

        st.write("---")

        st.subheader(t("Тенденции", "Trends"))

        df = pd.DataFrame(data)
        df["time"] = pd.to_datetime(df["time"])

        col1, col2 = st.columns(2)

        with col1:
            st.write(t("Седмица", "Weekly"))

            weekly = df.tail(7).sort_values("time")
            weekly_chart = weekly.set_index("time")[["energy"]]

            st.line_chart(weekly_chart)
            st.caption("Last 7 check-ins with timestamps")

        with col2:
            st.write(t("Месец", "Monthly"))

            monthly = df.copy()
            monthly["date"] = monthly["time"].dt.date
            monthly_grouped = monthly.groupby("date")["energy"].mean()

            st.line_chart(monthly_grouped)
            st.caption("Daily average energy trend")

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

    feedback = st.text_area(
        t("Предложения към ръководството", "Suggestions to Management")
    )

    if st.button(t("Запази", "Save")):

        st.session_state.data.append({
            "time": datetime.now(),
            "employee": employee,
            "department": department,
            "mood": mood,
            "energy": energy,
            "note": note,
            "feedback": feedback
        })

        st.success(t("Записано успешно", "Saved successfully"))
        st.info(random.choice(emotion_responses[mood]))

# =========================
# AI INSIGHTS
# =========================
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

# =========================
# DATA
# =========================
elif menu == t("Данни", "Data"):

    st.title(t("HR данни", "HR Data"))

    if len(st.session_state.data) == 0:
        st.info(t("Няма данни", "No data"))
    else:
        st.dataframe(st.session_state.data, use_container_width=True)

# =========================
# WELLBEING
# =========================
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

# =========================
# WELLBEING CHALLENGES
# =========================
elif menu == t("Уелнес предизвикателства", "Wellbeing Challenges"):

    st.title(t(
        "Уелнес предизвикателства",
        "Wellbeing Challenges"
    ))

    st.markdown("""
    <div class="challenge-card">
        <h2>🏆 Movement & Energy Challenge</h2>
        <p>Track movement, healthy habits and team wellbeing engagement.</p>
    </div>
    """, unsafe_allow_html=True)

    employee = st.selectbox(
        t("Служител", "Employee"),
        employees,
        key="challenge_employee"
    )

    steps = st.number_input(
        t("Днешни крачки", "Today's Steps"),
        min_value=0,
        max_value=50000,
        step=500
    )

    active_minutes = st.slider(
        t("Активни минути", "Active Minutes"),
        0,
        180,
        30
    )

    stretch_breaks = st.slider(
        t("Почивки за раздвижване", "Stretch Breaks"),
        0,
        20,
        3
    )

    if st.button(t("Запази активност", "Save Activity")):

        total_score = (
            steps // 1000 +
            active_minutes +
            (stretch_breaks * 5)
        )

        st.session_state.challenge_data.append({
            "employee": employee,
            "steps": steps,
            "active_minutes": active_minutes,
            "stretch_breaks": stretch_breaks,
            "score": total_score
        })

        st.success(
            t(
                "Активността е запазена успешно.",
                "Activity saved successfully."
            )
        )

    if len(st.session_state.challenge_data) > 0:

        st.write("---")

        st.subheader(t("Класация", "Leaderboard"))

        challenge_df = pd.DataFrame(st.session_state.challenge_data)

        leaderboard = (
            challenge_df.groupby("employee")[["score"]]
            .sum()
            .sort_values("score", ascending=False)
        )

        st.dataframe(leaderboard, use_container_width=True)

        winner = leaderboard.index[0]

        st.success(
            t(
                f"🏆 Водещ участник: {winner}",
                f"🏆 Current Leader: {winner}"
            )
        )

        st.info(
            t(
                "Целта е изграждане на по-здравословна и активна работна среда.",
                "The goal is building a healthier and more active work environment."
            )
        )
