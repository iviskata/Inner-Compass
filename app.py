# =========================
# DAILY SUMMARY (BOTTOM)
# =========================
st.markdown("## 📊 End of Day Reflection")

if st.session_state.history:

    texts = [h["text"].lower() for h in st.session_state.history]

    stress = sum("стрес" in t or "stress" in t for t in texts)
    sad = sum("тъж" in t or "sad" in t for t in texts)
    tired = sum("умор" in t or "tired" in t for t in texts)

    st.markdown("### 🧠 Емоционален баланс за деня")

    st.write(f"Стрес моменти: {stress}")
    st.write(f"Тъга моменти: {sad}")
    st.write(f"Умора моменти: {tired}")

    st.markdown("---")

    # Stoic summary logic
    if stress > sad and stress > tired:
        st.info("💭 Денят беше напрегнат. Помни: не всичко зависи от теб.")
        st.caption("— Марк Аврелий")

    elif tired > stress:
        st.info("💭 Денят показва умора. Почивката е част от силата.")
        st.caption("— Сенека")

    else:
        st.info("💭 Денят е бил балансиран. Продължавай така.")
        st.caption("— Стоицизъм")

else:
    st.write("Още няма данни за деня.")
