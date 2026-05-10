import streamlit as st
from datetime import datetime

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Inner Compass HR", page_icon="🧭", layout="centered")

st.title("🧭 Inner Compass")
st.subheader("HR Wellbeing Check-in")

# =========================
# DATA STORAGE (simple in memory)
# =========================
if "mood_history" not in st.session_state:
    st.session_state.mood_history = []

# =========================
# USER INPUT (EMPLOYEE CHECK-IN)
# =========================
st.write("### Как се чувстваш днес?")

mood = st.radio(
    "Избери настроение:",
    ["😄 Добре", "😐 Нормално", "😔 Зле"]
)

energy = st.slider("Енергия (1 = ниска, 10 = висока)", 1, 10, 5)

note = st.text_input("(по желание) Какво влияе на настроението ти?")

if st.button("Запази"):
    entry = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "mood": mood,
        "energy": energy,
        "note": note
    }
    st.session_state.mood_history.append(entry)
    st.success("Запазено успешно!")

# =========================
# HISTORY VIEW (EMPLOYEE)
# =========================
st.write("---")
st.write("### Твоята история")

if len(st.session_state.mood_history) == 0:
    st.info("Още няма данни.")
else:
    for item in reversed(st.session_state.mood_history[-10:]):
        st.write(f"{item['time']} | {item['mood']} | Енергия: {item['energy']}")
        if item["note"]:
            st.write(f"👉 {item['note']}")

# =========================
# SIMPLE HR ANALYTICS (TEAM VIEW SIMULATION)
# =========================
st.write("---")
st.write("### 📊 Общо състояние (симулация)")

if len(st.session_state.mood_history) > 0:
    moods = [m["mood"] for m in st.session_state.mood_history]

    happy = moods.count("😄 Добре")
    neutral = moods.count("😐 Нормално")
    sad = moods.count("😔 Зле")

    total = len(moods)

    st.write(f"😄 Добре: {happy}/{total}")
    st.write(f"😐 Нормално: {neutral}/{total}")
    st.write(f"😔 Зле: {sad}/{total}")

    avg_energy = sum([m["energy"] for m in st.session_state.mood_history]) / total
    st.write(f"⚡ Средна енергия: {avg_energy:.1f}")

    # simple AI-like insight
    st.write("---")
    st.write("### 🧠 AI Insight")

    if sad > happy:
        st.warning("Забелязва се по-високо напрежение в данните. Възможен риск от натоварване.")
    elif avg_energy < 5:
        st.warning("Енергията е ниска. Възможно е екипът да е уморен.")
    else:
        st.success("Състоянието изглежда стабилно и балансирано.")
else:
    st.info("Няма достатъчно данни за анализ.")
