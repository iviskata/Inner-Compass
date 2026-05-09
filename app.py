import streamlit as st
import random
from datetime import datetime

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="H-Tech · Inner Compass",
    page_icon="🏛️",
    layout="centered"
)

# =========================
# SESSION STATE
# =========================
if "history" not in st.session_state:
    st.session_state.history = []

# =========================
# LANGUAGE
# =========================
lang = st.selectbox("Language", ["Български", "English"])

# =========================
# MOTTO (FIXED — YOUR ORIGINAL IDEA RESTORED)
# =========================
motto_bg = "Продължаваме заедно... по-смирени, по-смислени, по-стоически."
motto_en = "We continue together... more humble, more meaningful, more stoic."

motto = motto_bg if lang == "Български" else motto_en

# =========================
# STYLE (CENTERED + CLEAN PREMIUM)
# =========================
st.markdown("""
<style>

.stApp {
    background:
    radial-gradient(circle at top, rgba(59,130,246,0.18), transparent 35%),
    radial-gradient(circle at bottom, rgba(168,85,247,0.12), transparent 30%),
    #020617;
    color: #e2e8f0;
    text-align: center;
}

h1, h2, h3, p {
    text-align: center;
}

.stTextInput, .stButton {
    display: flex;
    justify-content: center;
}

.stTextInput input {
    width: 100%;
    max-width: 520px;
    height: 60px;
    border-radius: 16px;
    font-size: 18px;
    text-align: center;
}

.stButton button {
    width: 100%;
    max-width: 520px;
    height: 48px;
    border-radius: 14px;
    background: linear-gradient(90deg,#2563eb,#7c3aed);
    color: white;
    border: none;
}

.block-container {
    padding-top: 2rem;
    max-width: 800px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.title("Inner Compass")
st.markdown("### H-TECH · DIGITAL SYSTEMS")
st.markdown(f"> {motto}")
st.markdown("---")

# =========================
# 🧠 EMOTION ENGINE v2.1 (LONGER RESPONSES)
# =========================

EMOTION_BANK = {
    "stress": [
        "⟡ Понякога напрежението се появява не защото има твърде много проблеми, а защото умът се опитва да ги държи всички едновременно. В такива моменти най-ефективният подход не е контрол върху всичко, а съзнателно ограничаване на фокуса до една малка и реална следваща стъпка.",
        "⟡ Стресът често не е външно събитие, а вътрешно натрупване на мисли, които се опитват да се случат наведнъж. Ако забавиш ритъма на реакция, ще откриеш, че ситуацията е по-управляема, отколкото изглежда в момента.",
        "⟡ Не е нужно да решаваш целия си живот в това състояние. Достатъчно е да върнеш вниманието към следващото ясно действие. Всичко останало може да изчака без да се губи контрол.",
    ],

    "sad": [
        "— Тъгата не е грешка в системата, а естествен процес на вътрешна обработка. Тя идва, когато нещо има нужда да бъде осъзнато, а не бързо поправено.",
        "— Понякога най-здравословният подход не е да се противопоставяш на това състояние, а да му позволиш да премине със свое собствено темпо, без натиск и без оценка.",
        "— Вътрешната тежест не е постоянна. Дори когато изглежда стабилна, тя се променя постепенно, когато не бъде насилвана."
    ],

    "tired": [
        "⟡ Умората не е знак за слабост, а директен сигнал от системата, че ресурсите са изчерпани. В този момент най-рационалното действие не е усилие, а възстановяване.",
        "⟡ Почивката не прекъсва прогреса — тя го поддържа. Без нея всяко следващо усилие става по-малко ефективно и по-тежко.",
        "⟡ Тялото и умът работят като единна система. Когато единият компонент се изтощи, другият не може да компенсира безкрайно."
    ],

    "happy": [
        "◇ Това състояние има стойност, която често се подценява. Спокойната яснота или радост не са просто емоции, а вътрешен ресурс, който може да стабилизира следващите по-трудни моменти.",
        "◇ Когато се появи лекота, тя не е случайна. Тя е резултат от множество малки вътрешни баланси. Осъзнаването на това я прави по-устойчива.",
        "◇ Тези моменти не трябва да се ускоряват. Те се запомнят най-добре, когато не се бърза през тях."
    ],

    "neutral": [
        "⟡ Състоянието е балансирано. Това означава, че няма вътрешен конфликт, който да изисква незабавна реакция.",
        "⟡ Не всяка мисъл изисква действие. Понякога наблюдението е достатъчно, за да се поддържа яснота.",
        "⟡ Тишината между мислите често съдържа повече информация, отколкото самите мисли."
    ]
}

def detect_emotion(text):
    t = text.lower()

    if any(w in t for w in ["стрес", "напрег", "stress", "overthinking"]):
        return "stress"

    if any(w in t for w in ["тъж", "sad", "сам", "празно"]):
        return "sad"

    if any(w in t for w in ["умор", "tired", "изтощ"]):
        return "tired"

    if any(w in t for w in ["щаст", "happy", "радост", "добре"]):
        return "happy"

    return "neutral"

def get_response(text):
    emotion = detect_emotion(text)
    return random.choice(EMOTION_BANK[emotion])

# =========================
# INPUT (CENTERED)
# =========================
question = "Как се чувстваш?" if lang == "Български" else "How do you feel?"

with st.form("form", clear_on_submit=True):
    user_input = st.text_input(question)
    send = st.form_submit_button("Изпрати" if lang == "Български" else "Send")

    if send and user_input:
        response = get_response(user_input)

        st.session_state.history.append({
            "time": datetime.now().strftime("%H:%M"),
            "text": user_input,
            "response": response
        })

# =========================
# HISTORY (CLEAN + CENTERED)
# =========================
for item in reversed(st.session_state.history):
    st.markdown(f"**{item['time']} · {item['text']}**")
    st.info(item["response"])
    st.markdown("---")

# =========================
# DAILY SUMMARY
# =========================
st.markdown("## 📊 Reflection")

if st.session_state.history:

    texts = [h["text"].lower() for h in st.session_state.history]

    stress = sum("стрес" in t or "stress" in t for t in texts)
    sad = sum("тъж" in t or "sad" in t for t in texts)
    tired = sum("умор" in t or "tired" in t for t in texts)
    happy = sum("щаст" in t or "радост" in t for t in texts)

    st.write(f"• Positive: {happy}")
    st.write(f"• Stress: {stress}")
    st.write(f"• Sad: {sad}")
    st.write(f"• Tired: {tired}")

    st.markdown("---")

    if happy >= max(stress, sad, tired):
        st.success("Баланс и позитивна динамика през деня.")
    elif stress > tired:
        st.info("Повишено напрежение — нужда от редуциране на фокуса.")
    elif tired > stress:
        st.info("Доминираща умора — необходима е регенерация.")
    else:
        st.info("Стабилно вътрешно състояние.")

# =========================
# WELL-BEING SYSTEM (IMPROVED UI)
# =========================
st.markdown("---")
st.markdown("## 🧠 Well-being System")

left, right = st.columns(2)

with left:
    st.markdown("### 🎯 Focus System")

    with st.expander("💻 Deep Work"):
        st.write("60–90 минути фокусирана работа без разсейване върху една задача.")

    with st.expander("🎯 Single-tasking"):
        st.write("Една задача в един момент увеличава яснота и ефективност.")

    with st.expander("📌 Planning"):
        st.write("Започни деня с 3 ясни приоритета, не повече.")

with right:
    st.markdown("### 🧘 Recovery System")

    with st.expander("⟡ Break Protocol"):
        st.write("Кратки паузи през деня възстановяват когнитивния капацитет.")

    with st.expander("💧 Hydration"):
        st.write("Хидратацията влияе директно върху концентрацията.")

    with st.expander("🌙 Shutdown Ritual"):
        st.write("Затваряне на деня без работа подобрява възстановяването.")
