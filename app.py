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
# SIDEBAR BRANDING
# =========================
st.sidebar.markdown("## Inner Compass")
st.sidebar.caption("AI Wellbeing & HR Intelligence")

menu = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Check-in", "AI Insights", "Data", "Wellbeing Guide"]
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
# GLOBAL HEADER (PERSISTENT BRAND)
# =========================
st.markdown(
    """
    <h1 style='text-align:center; margin-bottom:5px;'>
    Inner Compass
    </h1>
    <h4 style='text-align:center; color:gray; margin-top:0px;'>
    AI Wellbeing & HR Intelligence Platform
    </h4>
    <hr>
    """,
    unsafe_allow_html=True
)

# =========================================================
# DASHBOARD
# =========================================================
if menu == "Dashboard":

    st.title("HR Dashboard")

    data = st.session_state.data

    if len(data) == 0:
        st.info("No data yet. System is ready for input.")

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

        col1.metric("Entries", len(data))
        col2.metric("Good Mood", good)
        col3.metric("Bad Mood", bad)
        col4.metric("Avg Energy", f"{avg_energy:.1f}")

        st.write("---")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Energy Trend")
            st.line_chart(energy)

        with col2:
            st.subheader("Mood Distribution")
            st.bar_chart({
                "Good": good,
                "Neutral": neutral,
                "Bad": bad
            })

# =========================================================
# CHECK-IN
# =========================================================
elif menu == "Check-in":

    st.title("Daily Check-in")

    employee = st.selectbox("Employee", employees)
    department = st.selectbox("Department", departments)

    mood = st.radio("Mood", ["Good", "Neutral", "Bad"])
    energy = st.slider("Energy level", 1, 10, 5)

    note = st.text_input("Note (optional)")

    if st.button("Save"):
        st.session_state.data.append({
            "time": datetime.now(),
            "employee": employee,
            "department": department,
            "mood": mood,
            "energy": energy,
            "note": note
        })
        st.success("Saved successfully")

    st.write("---")

    st.subheader("Recent Entries")

    for d in st.session_state.data[-8:]:
        st.write(f"{d['time'].strftime('%Y-%m-%d %H:%M')} | {d['employee']} | {d['mood']} | {d['energy']}")

# =========================================================
# AI INSIGHTS
# =========================================================
elif menu == "AI Insights":

    st.title("AI HR Intelligence")

    data = st.session_state.data

    if len(data) == 0:
        st.info("No data available")
    else:

        bad_ratio = len([d for d in data if d["mood"] == "Bad"]) / len(data)
        avg_energy = sum([d["energy"] for d in data]) / len(data)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Observation")

            if bad_ratio > 0.4:
                st.error("High stress detected in team")
            elif avg_energy < 5:
                st.warning("Low energy detected")
            else:
                st.success("Stable team condition")

        with col2:
            st.subheader("AI Analysis")

            if bad_ratio > 0.4:
                st.write("Likely workload stress accumulation.")
                st.write("Recommendation: reduce workload pressure.")
            elif avg_energy < 5:
                st.write("Possible fatigue or overload.")
                st.write("Recommendation: introduce recovery time.")
            else:
                st.write("No risk patterns detected.")

# =========================================================
# DATA
# =========================================================
elif menu == "Data":

    st.title("HR Data")

    if len(st.session_state.data) == 0:
        st.info("No records yet")
    else:
        st.dataframe(st.session_state.data, use_container_width=True)

# =========================================================
# WELLBEING GUIDE
# =========================================================
elif menu == "Wellbeing Guide":

    st.title("Workplace Wellbeing Guide")

    st.write("## Ergonomics")
    st.write("""
- Keep back straight  
- Take breaks every 45–60 minutes  
- Screen at eye level  
- Use proper chair support  
""")

    st.write("## Mental Health")
    st.write("""
- Avoid nonstop work without breaks  
- Focus on one task at a time  
- Communicate stress early  
""")

    st.write("## Work Balance")
    st.write("""
- 50 min work / 10 min break cycles  
- Prioritize tasks  
- Reduce distractions  
""")

    st.write("## Recovery")
    st.write("""
- Disconnect after work  
- Walk daily  
- Sleep 7–9 hours  
""")
