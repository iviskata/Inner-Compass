import streamlit as st
from datetime import datetime

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Inner Compass HR", layout="wide")

# =========================
# DATA STORAGE
# =========================
if "data" not in st.session_state:
    st.session_state.data = []

# =========================
# SIDEBAR
# =========================
menu = st.sidebar.radio(
    "Навигация",
    ["Dashboard", "Въвеждане", "AI анализ", "HR данни"]
)

employees = ["Employee A", "Employee B", "Employee C"]
departments = ["Разработка", "Маркетинг", "Продажби"]

# =========================
# DASHBOARD PAGE (MAIN VIEW)
# =========================
if menu == "Dashboard":

    st.title("Inner Compass HR Dashboard")

    if len(st.session_state.data) == 0:
        st.info("Няма данни за показване")
    else:

        total = len(st.session_state.data)

        moods = [d["mood"] for d in st.session_state.data]
        energy_values = [d["energy"] for d in st.session_state.data]

        good = moods.count("Добро")
        neutral = moods.count("Нормално")
        bad = moods.count("Лошо")

        avg_energy = sum(energy_values) / total

        # =========================
        # KPI CARDS
        # =========================
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Общо записи", total)
        col2.metric("Добро настроение", good)
        col3.metric("Лошо настроение", bad)
        col4.metric("Средна енергия", f"{avg_energy:.1f}")

        st.write("---")

        # =========================
        # CHARTS
        # =========================
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Енергия (тенденция)")
            st.line_chart(energy_values)

        with col2:
            st.subheader("Разпределение на настроение")
            st.bar_chart({
                "Добро": good,
                "Нормално": neutral,
                "Лошо": bad
            })

# =========================
# INPUT PAGE
# =========================
elif menu == "Въвеждане":

    st.title("Дневно въвеждане")

    employee = st.selectbox("Служител", employees)
    department = st.selectbox("Отдел", departments)

    mood = st.radio("Настроение", ["Добро", "Нормално", "Лошо"])
    energy = st.slider("Енергия", 1, 10, 5)

    note = st.text_input("Бележка")

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
    st.subheader("Последни записи")

    for d in st.session_state.data[-8:]:
        st.write(f"{d['time'].strftime('%Y-%m-%d %H:%M')} | {d['employee']} | {d['mood']} | {d['energy']}")

# =========================
# AI ANALYSIS PAGE
# =========================
elif menu == "AI анализ":

    st.title("AI HR анализ")

    if len(st.session_state.data) == 0:
        st.info("Няма данни")
    else:

        total = len(st.session_state.data)
        bad_ratio = len([d for d in st.session_state.data if d["mood"] == "Лошо"]) / total
        avg_energy = sum([d["energy"] for d in st.session_state.data]) / total

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Наблюдение")

            if bad_ratio > 0.4:
                st.error("Повишено напрежение в екипа")
            elif avg_energy < 5:
                st.warning("Ниска енергия в екипа")
            else:
                st.success("Стабилно състояние")

        with col2:
            st.subheader("AI интерпретация")

            if bad_ratio > 0.4:
                st.write("Вероятно има натрупан стрес и претоварване.")
                st.write("Препоръка: намаляване на натоварването.")
            elif avg_energy < 5:
                st.write("Възможна умора в екипа.")
                st.write("Препоръка: оптимизация на работния ритъм.")
            else:
                st.write("Няма негативни модели в момента.")
                st.write("Поддържайте текущия баланс.")

# =========================
# HR DATA PAGE
# =========================
elif menu == "HR данни":

    st.title("HR база данни")

    if len(st.session_state.data) == 0:
        st.info("Няма данни")
    else:
        st.dataframe(st.session_state.data)
