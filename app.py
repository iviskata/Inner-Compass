import streamlit as st
from datetime import datetime

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Inner Compass HR", page_icon="Compass", layout="wide")

# =========================
# DATA STORAGE
# =========================
if "data" not in st.session_state:
    st.session_state.data = []

# =========================
# SIDEBAR MENU
# =========================
menu = st.sidebar.selectbox(
    "Навигация",
    ["Въвеждане на данни", "Анализи", "AI препоръки", "HR Данни"]
)

# =========================
# EMPLOYEES + DEPARTMENTS
# =========================
employees = ["Employee A", "Employee B", "Employee C", "Employee D"]
departments = ["Разработка", "Маркетинг", "Продажби"]

# =========================================================
# 1. INPUT PAGE
# =========================================================
if menu == "Въвеждане на данни":

    st.title("Въвеждане на дневно състояние")

    employee = st.selectbox("Служител", employees)
    department = st.selectbox("Отдел", departments)

    mood = st.radio("Настроение", ["Добро", "Нормално", "Лошо"])
    energy = st.slider("Енергия (1-10)", 1, 10, 5)
    note = st.text_input("Бележка (по избор)")

    if st.button("Запази"):
        st.session_state.data.append({
            "time": datetime.now(),
            "employee": employee,
            "department": department,
            "mood": mood,
            "energy": energy,
            "note": note
        })
        st.success("Записано успешно")

    st.write("---")
    st.write("Последни записи")

    for d in st.session_state.data[-10:]:
        st.write(f"{d['time'].strftime('%Y-%m-%d %H:%M')} | {d['employee']} | {d['mood']} | {d['energy']}")

# =========================================================
# 2. ANALYTICS PAGE
# =========================================================
elif menu == "Анализи":

    st.title("Анализи на екипа")

    if len(st.session_state.data) == 0:
        st.info("Няма данни")
    else:

        moods = [d["mood"] for d in st.session_state.data]

        good = moods.count("Добро")
        neutral = moods.count("Нормално")
        bad = moods.count("Лошо")

        st.write("### Общо състояние")
        st.write(f"Добро: {good}")
        st.write(f"Нормално: {neutral}")
        st.write(f"Лошо: {bad}")

        avg_energy = sum([d["energy"] for d in st.session_state.data]) / len(st.session_state.data)
        st.write(f"Средна енергия: {avg_energy:.1f}")

        st.write("---")
        st.write("### Графика (енергия)")

        st.line_chart([d["energy"] for d in st.session_state.data])

# =========================================================
# 3. AI INSIGHTS PAGE
# =========================================================
elif menu == "AI препоръки":

    st.title("AI HR анализ")

    if len(st.session_state.data) == 0:
        st.info("Няма данни за анализ")
    else:

        bad_ratio = len([d for d in st.session_state.data if d["mood"] == "Лошо"]) / len(st.session_state.data)
        avg_energy = sum([d["energy"] for d in st.session_state.data]) / len(st.session_state.data)

        st.write("### Наблюдение")

        if bad_ratio > 0.4:
            st.warning("Засилено напрежение в екипа")
        elif avg_energy < 5:
            st.warning("Ниска енергия в екипа")
        else:
            st.success("Стабилно състояние")

        st.write("### Причина")

        if bad_ratio > 0.4:
            st.write("Вероятно има натрупване на стрес и работно напрежение.")
        elif avg_energy < 5:
            st.write("Възможна умора или претоварване.")
        else:
            st.write("Няма негативни модели в момента.")

        st.write("### Препоръка")

        if bad_ratio > 0.4:
            st.write("Намалете натоварването и добавете почивки.")
        elif avg_energy < 5:
            st.write("Оптимизирайте работния ритъм.")
        else:
            st.write("Поддържайте текущия баланс.")

# =========================================================
# 4. HR DATA PAGE
# =========================================================
elif menu == "HR Данни":

    st.title("HR данни (всички записи)")

    if len(st.session_state.data) == 0:
        st.info("Няма данни")
    else:
        st.dataframe(st.session_state.data)
