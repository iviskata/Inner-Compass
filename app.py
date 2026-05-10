import streamlit as st
from datetime import datetime

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Inner Compass HR", page_icon="🧭", layout="centered")

st.title("🧭 Inner Compass HR Platform")
st.subheader("Team Wellbeing System (MVP)")

# =========================
# TEAM DATA STORAGE
# =========================
if "team_data" not in st.session_state:
    st.session_state.team_data = []

# =========================
# EMPLOYEE IDENTIFIER (SIMULATION)
# =========================
st.write("### 👤 Кой си днес (симулация на служител)")

user = st.selectbox(
    "Избери потребител:",
    ["Иван", "Мария", "Георги", "Ани"]
)

# =========================
# CHECK-IN
# =========================
st.write("### Как се чувстваш днес?")

mood = st.radio(
    "Настроение:",
    ["😄 Добре", "😐 Нормално", "😔 Зле"]
)

energy = st.slider("Енергия (1–10)", 1, 10, 5)

note = st.text_input("Коментар (по желание)")

if st.button("Запази"):
    entry = {
        "user": user,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "mood": mood,
        "energy": energy,
        "note": note
    }
    st.session_state.team_data.append(entry)
    st.success("Запазено!")

# =========================
# PERSONAL HISTORY
# =========================
st.write("---")
st.write(f"### 📍 История на {user}")

user_entries = [x for x in st.session_state.team_data if x["user"] == user]

if len(user_entries) == 0:
    st.info("Още няма данни за този човек.")
else:
    for item in reversed(user_entries[-10:]):
        st.write(f"{item['time']} | {item['mood']} | ⚡ {item['energy']}")
        if item["note"]:
            st.write(f"👉 {item['note']}")

# =========================
# TEAM OVERVIEW (HR VIEW)
# =========================
st.write("---")
st.write("### 📊 Екипна картина")

if len(st.session_state.team_data) > 0:

    moods = [m["mood"] for m in st.session_state.team_data]

    happy = moods.count("😄 Добре")
    neutral = moods.count("😐 Нормално")
    sad = moods.count("😔 Зле")

    total = len(moods)

    st.write(f"😄 Добре: {happy}/{total}")
    st.write(f"😐 Нормално: {neutral}/{total}")
    st.write(f"😔 Зле: {sad}/{total}")

    avg_energy = sum([m["energy"] for m in st.session_state.team_data]) / total
    st.write(f"⚡ Средна енергия на екипа: {avg_energy:.1f}")

    # =========================
    # SIMPLE HR INSIGHT ENGINE
    # =========================
    st.write("---")
    st.write("### 🧠 HR Insight")

    if sad > happy:
        st.warning("Внимание: Повишено напрежение в екипа. Възможен риск от burnout.")
    elif avg_energy < 5:
        st.warning("Екипът е с ниска енергия. Възможно е претоварване.")
    else:
        st.success("Екипът е в стабилно състояние.")

else:
    st.info("Още няма екипни данни.")
