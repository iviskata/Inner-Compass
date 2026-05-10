import streamlit as st
from datetime import datetime
import random

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Inner Compass HR", page_icon="Compass", layout="centered")

st.title("Inner Compass HR Platform")
st.subheader("Система за анализ на благосъстоянието в екипа")

# =========================
# DATA STORAGE
# =========================
if "data" not in st.session_state:
    st.session_state.data = []

# =========================
# ORGANIZATIONAL STRUCTURE
# =========================
st.write("## Служител и отдел")

department = st.selectbox(
    "Избери отдел:",
    ["Разработка", "Маркетинг", "Продажби"]
)

employee = st.selectbox(
    "Избери служител:",
    ["Служител A", "Служител B", "Служител C", "Служител D"]
)

# =========================
# CHECK-IN
# =========================
st.write("## Дневно състояние")

mood = st.radio(
    "Настроение:",
    ["Добро", "Нормално", "Лошо"]
)

energy = st.slider("Енергия (1–10)", 1, 10, 5)

note = st.text_input("Коментар (по избор)")

if st.button("Запази данни"):
    entry = {
        "time": datetime.now(),
        "department": department,
        "employee": employee,
        "mood": mood,
        "energy": energy,
        "note": note
    }
    st.session_state.data.append(entry)
    st.success("Данните са записани успешно")

# =========================
# FILTER DATA
# =========================
dept_data = [d for d in st.session_state.data if d["department"] == department]
emp_data = [d for d in dept_data if d["employee"] == employee]

# =========================
# PERSONAL VIEW
# =========================
st.write("## Лична история")

if len(emp_data) == 0:
    st.info("Няма данни за този служител.")
else:
    for d in emp_data[-10:]:
        st.write(f"{d['time'].strftime('%Y-%m-%d %H:%M')} | {d['mood']} | Енергия: {d['energy']}")
        if d["note"]:
            st.write(f"Бележка: {d['note']}")

# =========================
# WEEKLY ANALYSIS
# =========================
st.write("## Седмичен анализ")

weekly_scores = {"Добро": 3, "Нормално": 2, "Лошо": 1}

if len(emp_data) >= 3:
    values = [weekly_scores[d["mood"]] for d in emp_data[-7:]]
    st.line_chart(values)
else:
    st.info("Няма достатъчно данни за седмичен анализ")

# =========================
# MONTHLY ANALYSIS
# =========================
st.write("## Месечен анализ")

if len(emp_data) >= 5:
    values = [weekly_scores[d["mood"]] for d in emp_data]
    st.line_chart(values)
else:
    st.info("Няма достатъчно данни за месечен анализ")

# =========================
# TEAM OVERVIEW
# =========================
st.write("## Преглед на екипа")

if len(dept_data) > 0:
    moods = [d["mood"] for d in dept_data]

    good = moods.count("Добро")
    neutral = moods.count("Нормално")
    bad = moods.count("Лошо")

    total = len(moods)

    st.write(f"Добро: {good}")
    st.write(f"Нормално: {neutral}")
    st.write(f"Лошо: {bad}")

    avg_energy = sum([d["energy"] for d in dept_data]) / total
    st.write(f"Средна енергия: {avg_energy:.1f}")

# =========================
# AI ANALYSIS ENGINE
# =========================
st.write("## AI анализ на състоянието")

if len(dept_data) > 0:
    bad_ratio = sum([1 for d in dept_data if d["mood"] == "Лошо"]) / len(dept_data)
    avg_energy = sum([d["energy"] for d in dept_data]) / len(dept_data)

    st.write("### Наблюдение")

    if bad_ratio > 0.4:
        st.warning("Засилено напрежение в отдела.")
    elif avg_energy < 5:
        st.warning("Ниска енергия в екипа.")
    else:
        st.success("Стабилно състояние в отдела.")

    st.write("### Причина (AI анализ)")

    if bad_ratio > 0.4:
        st.write("Вероятно има натрупване на работно напрежение или стресови периоди.")
    elif avg_energy < 5:
        st.write("Възможно е умора или недостатъчна почивка.")
    else:
        st.write("Няма видими проблемни модели в момента.")

    st.write("### Препоръка")

    if bad_ratio > 0.4:
        st.write("Препоръчва се намаляване на натоварването и кратки почивки.")
    elif avg_energy < 5:
        st.write("Препоръчва се оптимизация на работния ритъм.")
    else:
        st.write("Поддържайте текущия баланс.")
else:
    st.info("Няма достатъчно данни за анализ")

# =========================
# RAW DATA (HR VIEW)
# =========================
st.write("## Данни (HR достъп)")

st.dataframe(st.session_state.data)
