import streamlit as st

st.title("Inner Compass 🏛️")

user = st.text_input("Как се чувстваш?")

if user:
    st.write("Стоически отговор: приеми ситуацията и действай спокойно.")
