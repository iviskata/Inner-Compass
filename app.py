import streamlit as st
from datetime import datetime

# =========================
# PAGE CONFIG (clean SaaS style)
# =========================
st.set_page_config(
    page_title="Inner Compass HR",
    layout="wide"
)

# =========================
# DATA STORAGE
# =========================
if "data" not in st.session_state:
    st.session_state.data = []

# =========================
# SIDEBAR NAVIGATION
# =========================
menu = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Check-in", "AI Insights", "Data"]
)

# =========================
# BASE DATA
# =========================
employees = ["Employee A", "Employee B", "Employee C"]
departments = ["Development", "Marketing", "Sales"]

# =========================================================
# DASHBOARD (PREMIUM VIEW)
# =========================================================
if menu == "Dashboard":

    st.markdown("# Inner Compass HR")

    st.caption("Team wellbeing analytics platform")

    if len(st.session_state.data) == 0:
        st.info("No data available yet.")
    else:

        data = st.session_state.data
        total = len(data)

        moods = [d["mood"] for d in data]
        energy = [d["energy"] for d in data]

        good = moods.count("Good")
        neutral = moods.count("Neutral")
        bad = moods.count("Bad")

        avg_energy = sum(energy) / total

        # =========================
        # KPI CARDS (premium layout)
        # =========================
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown("### Total Entries")
            st.markdown(f"## {total}")

        with col2:
            st.markdown("### Positive Mood")
            st.markdown(f"## {good}")

        with col3:
            st.markdown("### Negative Mood")
            st.markdown(f"## {bad}")

        with col4:
            st.markdown("### Avg Energy")
            st.markdown(f"## {avg_energy:.1f}")

        st.write("---")

        # =========================
        # CHARTS (clean layout)
        # =========================
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Energy Trend")
            st.line_chart(energy)

        with col2:
            st.markdown("### Mood Distribution")
            st.bar_chart({
                "Good": good,
                "Neutral": neutral,
                "Bad": bad
            })

# =========================================================
# CHECK-IN PAGE
# =========================================================
elif menu == "Check-in":

    st.markdown("# Daily Check-in")
    st.caption("Log employee wellbeing data")

    employee = st.selectbox("Employee", employees)
    department = st.selectbox("Department", departments)

    mood = st.radio("Mood", ["Good", "Neutral", "Bad"])
    energy = st.slider("Energy level", 1, 10, 5)

    note = st.text_input("Optional note")

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

    st.markdown("### Recent entries")

    for d in st.session_state.data[-8:]:
        st.write(
            f"{d['time'].strftime('%Y-%m-%d %H:%M')} | "
            f"{d['employee']} | {d['mood']} | Energy: {d['energy']}"
        )

# =========================================================
# AI INSIGHTS (clean consulting style)
# =========================================================
elif menu == "AI Insights":

    st.markdown("# AI Insights")
    st.caption("System-generated wellbeing analysis")

    if len(st.session_state.data) == 0:
        st.info("No data to analyze.")
    else:

        data = st.session_state.data
        total = len(data)

        bad_ratio = len([d for d in data if d["mood"] == "Bad"]) / total
        avg_energy = sum([d["energy"] for d in data]) / total

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Observation")

            if bad_ratio > 0.4:
                st.error("Elevated stress levels detected")
            elif avg_energy < 5:
                st.warning("Low energy levels detected")
            else:
                st.success("Stable team condition")

        with col2:
            st.markdown("### Interpretation")

            if bad_ratio > 0.4:
                st.write("Likely workload accumulation or pressure increase.")
                st.write("Recommended action: redistribute workload.")
            elif avg_energy < 5:
                st.write("Possible fatigue or insufficient recovery.")
                st.write("Recommended action: introduce recovery periods.")
            else:
                st.write("No significant risk patterns detected.")

# =========================================================
# DATA PAGE (clean table view)
# =========================================================
elif menu == "Data":

    st.markdown("# HR Data")

    if len(st.session_state.data) == 0:
        st.info("No records available.")
    else:
        st.dataframe(st.session_state.data, use_container_width=True)
