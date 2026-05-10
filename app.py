import streamlit as st
from datetime import datetime
import random

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Inner Compass HR", page_icon="🧭", layout="centered")

st.title("🧭 Inner Compass HR Platform")
st.subheader("Team Wellbeing Analytics")

# =========================
# STORAGE
# =========================
if "team_data" not in st.session_state:
    st.session_state.team_data = []

# =========================
# EMPLOYEES
# =========================
st.write("### 👤 Select Employee")

employee = st.selectbox(
    "Choose employee:",
    ["Employee A", "Employee B", "Employee C"]
)

# =========================
# CHECK-IN
# =========================
st.write("### How are you feeling today?")

mood = st.radio(
    "Mood:",
    ["😄 Good", "😐 Neutral", "😔 Bad"]
)

energy = st.slider("Energy level", 1, 10, 5)

note = st.text_input("Optional note")

if st.button("Save check-in"):
    entry = {
        "employee": employee,
        "time": datetime.now(),
        "mood": mood,
        "energy": energy
    }
    st.session_state.team_data.append(entry)
    st.success("Saved!")

# =========================
# CONVERT MOOD TO SCORE
# =========================
def mood_score(m):
    if m == "😄 Good":
        return 3
    elif m == "😐 Neutral":
        return 2
    return 1

# =========================
# FILTER EMPLOYEE DATA
# =========================
emp_data = [d for d in st.session_state.team_data if d["employee"] == employee]

# =========================
# PERSONAL VIEW
# =========================
st.write("---")
st.write(f"### 📍 {employee} History")

if len(emp_data) == 0:
    st.info("No data yet.")
else:
    for d in emp_data[-10:]:
        st.write(f"{d['time'].strftime('%Y-%m-%d %H:%M')} | {d['mood']} | ⚡ {d['energy']}")

# =========================
# WEEKLY ANALYSIS
# =========================
st.write("---")
st.write("### 📅 Weekly Emotion Trend")

if len(emp_data) >= 3:
    week_scores = [mood_score(d["mood"]) for d in emp_data[-7:]]

    st.line_chart(week_scores)
else:
    st.info("Not enough data for weekly trend (need at least 3 entries).")

# =========================
# MONTHLY ANALYSIS
# =========================
st.write("### 📆 Monthly Emotion Trend")

if len(emp_data) >= 5:
    month_scores = [mood_score(d["mood"]) for d in emp_data]

    # simulate smoothing (grouping)
    grouped = []
    step = max(1, len(month_scores)//4)

    for i in range(0, len(month_scores), step):
        grouped.append(sum(month_scores[i:i+step]) / len(month_scores[i:i+step]))

    st.line_chart(grouped)
else:
    st.info("Not enough data for monthly trend.")

# =========================
# TEAM OVERVIEW
# =========================
st.write("---")
st.write("### 📊 Team Overview")

if len(st.session_state.team_data) > 0:
    all_moods = [d["mood"] for d in st.session_state.team_data]

    good = all_moods.count("😄 Good")
    neutral = all_moods.count("😐 Neutral")
    bad = all_moods.count("😔 Bad")

    st.write(f"😄 Good: {good}")
    st.write(f"😐 Neutral: {neutral}")
    st.write(f"😔 Bad: {bad}")

    avg_energy = sum([d["energy"] for d in st.session_state.team_data]) / len(st.session_state.team_data)
    st.write(f"⚡ Avg energy: {avg_energy:.1f}")

    st.write("---")
    st.write("### 🧠 Insight Engine")

    if bad > good:
        st.warning("Increased stress detected in team. Possible burnout risk.")
    elif avg_energy < 5:
        st.warning("Low energy levels detected across team.")
    else:
        st.success("Team state is stable and balanced.")
else:
    st.info("No team data yet.")
