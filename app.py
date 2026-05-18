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
# MONTHLY CHALLENGES
# =========================
monthly_challenges = [
    t("Movement & Energy Challenge", "Movement & Energy Challenge"),
    t("Stretch & Recover Challenge", "Stretch & Recover Challenge"),
    t("Mind & Motion Challenge", "Mind & Motion Challenge"),
    t("Hydration & Balance Challenge", "Hydration & Balance Challenge")
]

active_challenge = monthly_challenges[
    datetime.now().month % len(monthly_challenges)
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

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            metric("Total Check-ins", len(data), "📊")

        with col2:
            metric("Positive Mood", moods.count("Good"), "😊")

        with col3:
            metric("Attention Needed", moods.count("Bad"), "⚠️")

        with col4:
            metric("Team Energy", f"{avg:.1f}", "⚡")

        with col5:

            participation = 0

            if len(st.session_state.challenge_data) > 0:
                unique_users = len(
                    set([
                        x["employee"]
                        for x in st.session_state.challenge_data
                    ])
                )

                participation = int(
                    (unique_users / len(employees)) * 100
                )

            metric(
                t("Уелнес участие", "Wellness Participation"),
                f"{participation}%",
                "🏆"
            )

        st.write("---")

        # ✅ ACTIVE CHALLENGE PREVIEW
        st.markdown(f"""
        <div class="challenge-card">
            <h3>🏆 {t("Активно месечно предизвикателство", "Active Monthly Challenge")}</h3>
            <p>{active_challenge}</p>
            <p>{t(
                "Служителите събират точки чрез движение и здравословни навици.",
                "Employees collect points through movement and healthy habits."
            )}</p>
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

            st.info(t(
                "🤖 AI предложение: Recovery & Movement Challenge",
                "🤖 AI Suggestion: Recovery & Movement Challenge"
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

            st.info(t(
                "🤖 AI предложение: Mind & Motion Challenge",
                "🤖 AI Suggestion: Mind & Motion Challenge"
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

            st.info(t(
                "🤖 AI предложение: Team Energy Challenge",
                "🤖 AI Suggestion: Team Energy Challenge"
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

    st.markdown(f"""
    <div class="challenge-card">
        <h2>🏆 {active_challenge}</h2>
        <p>{t(
            "Проследяване на движение, активност и уелнес навици.",
            "Track movement, activity and healthy wellbeing habits."
        )}</p>
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # TEAM GOAL
    # =========================
    team_goal = 500000

    total_steps = 0

    if len(st.session_state.challenge_data) > 0:
        total_steps = sum(
            item["steps"]
            for item in st.session_state.challenge_data
        )

    progress = min(total_steps / team_goal, 1.0)

    st.subheader(t("Отборна цел", "Team Goal"))

    st.progress(progress)

    st.caption(
        t(
            f"{total_steps:,} / {team_goal:,} крачки",
            f"{total_steps:,} / {team_goal:,} steps"
        )
    )

    st.write("---")

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

        # ✅ HUMAN FEEDBACK
        if total_score >= 120:

            st.success(t(
                "🔥 Страхотна последователност днес.",
                "🔥 Amazing consistency today."
            ))

        elif total_score >= 60:

            st.info(t(
                "🌿 Всяка малка стъпка подкрепя дългосрочното благополучие.",
                "🌿 Every small step supports long-term wellbeing."
            ))

        else:

            st.warning(t(
                "💙 Дори кратките моменти на движение имат значение.",
                "💙 Even short movement breaks matter."
            ))

    # =========================
    # WELLBEING PROGRESS
    # =========================
    if len(st.session_state.challenge_data) > 0:

        st.write("---")

        st.subheader(t(
            "Уелнес прогрес",
            "Wellbeing Progress"
        ))

        challenge_df = pd.DataFrame(st.session_state.challenge_data)

        leaderboard = (
            challenge_df.groupby("employee")[["score"]]
            .sum()
            .sort_values("score", ascending=False)
        )

        medals = ["🥇", "🥈", "🥉"]

        for index, (employee_name, row) in enumerate(leaderboard.iterrows()):

            medal = medals[index] if index < 3 else "🏅"

            st.markdown(f"""
            <div class="metric-card" style="margin-bottom:15px;">
                <div style="font-size:20px;">
                    {medal} {employee_name}
                </div>
                <div style="font-size:32px; margin-top:10px;">
                    {int(row["score"])} pts
                </div>
            </div>
            """, unsafe_allow_html=True)

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

        # =========================
        # WELLBEING INSIGHTS
        # =========================
        st.write("---")

        st.subheader(t(
            "Уелнес прозрения",
            "Wellbeing Insights"
        ))

        st.info(t(
            "📈 Екипите с по-висока физическа активност показват по-добри нива на енергия и настроение.",
            "📈 Teams with higher movement engagement show stronger mood and energy trends."
        ))

        st.info(t(
            "🌿 Редовните почивки за раздвижване подпомагат по-балансиран работен ритъм.",
            "🌿 Regular stretch breaks support a more balanced work rhythm."
        ))
