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
# MOTTO
# =========================
motto_bg = "Продължаваме заедно... по-смирени, по-смислени, по-стоически."
motto_en = "We continue together... more humble, more meaningful, more stoic."
motto = motto_bg if lang == "Български" else motto_en

# =========================
# STYLE (CENTERED PREMIUM FIXED)
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

.block-container {
    max-width: 820px;
    padding-top: 2rem;
}

.stTextInput input {
    text-align: center;
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
# 🧠 IMPROVED EMOTION ENGINE v3.1 (2–3 SENTENCES EACH)
# =========================

EMOTION_BANK = {

"stress": [
"⟡ Напрежението често се появява, когато умът се опитва да обработи твърде много неща едновременно. В този момент най-ефективното действие не е контрол върху всичко, а ограничаване на фокуса до една ясна стъпка.",
"⟡ Стресът не означава, че ситуацията е непоносима, а че вниманието ти е разпиляно между твърде много посоки. Когато го върнеш към настоящето, усещането за тежест намалява.",
"⟡ Не е необходимо да решаваш целия проблем наведнъж. Достатъчно е да се фокусираш върху следващото малко действие, което реално можеш да направиш сега."
],

"fatigue": [
"⟡ Умората не е слабост, а ясен сигнал, че системата има нужда от възстановяване. Ако я игнорираш, тя се натрупва и намалява ефективността ти още повече.",
"⟡ Тялото и умът работят като една система и когато енергията спадне, това означава, че балансът е нарушен. Почивката не е пауза от напредъка, а част от него.",
"⟡ В този момент усилието няма да даде по-добър резултат. Най-рационалното действие е да намалиш натоварването и да позволиш възстановяване."
],

"sadness": [
"— Тъгата не е нещо, което трябва да бъде премахнато веднага. Тя е естествен процес на вътрешна обработка и има нужда от време, за да премине.",
"— Това състояние не определя кой си, нито посоката ти. То е временно вътрешно движение, което постепенно отслабва, когато не бъде притискано.",
"— Понякога най-здравословното действие не е решение, а позволяване на процеса да се случи без натиск."
],

"anxiety": [
"⟡ Тревожността често идва от бъдещи сценарии, които умът създава, но които все още не съществуват. Това създава напрежение без реална основа в момента.",
"⟡ Когато върнеш вниманието към настоящето, мисловният шум постепенно отслабва. Реалността винаги е по-ясна от прогнозите за нея.",
"⟡ Не е нужно да имаш всички отговори сега. Достатъчно е да останеш в настоящия момент без да ускоряваш мисловните процеси."
],

"anger": [
"⟡ Гневът често е реакция на усещане за загуба на контрол или несправедливост. В този момент емоцията е по-бърза от осмислянето.",
"⟡ Ако дадеш време между импулса и действието, интензитетът намалява и ситуацията става по-ясна. Това променя крайния резултат значително.",
"⟡ Емоцията сама по себе си не е проблем. Важното е как я управляваш преди да се превърне в действие."
],

"neutral": [
"⟡ В момента няма вътрешен конфликт или напрежение. Това е стабилно базово състояние, което позволява ясно мислене.",
"⟡ Не всяка мисъл изисква анализ или реакция. Понякога наблюдението е напълно достатъчно.",
"⟡ Тишината между мислите също е част от вътрешния процес и носи информация."
]
}

# =========================
# EMOTION DETECTOR (FIXED PRIORITY)
# =========================

def detect_emotion(text):
    t = text.lower()

    if any(w in t for w in ["умор", "измор", "tired"]):
        return "fatigue"

    if any(w in t for w in ["стрес", "stress", "напрег"]):
        return "stress"

    if any(w in t for w in ["тъж", "sad"]):
        return "sadness"

    if any(w in t for w in ["страх", "тревож"]):
        return "anxiety"

    if any(w in t for w in ["яд", "гнев"]):
        return "anger"

    return "neutral"

def get_response(text):
    emotion = detect_emotion(text)
    return random.choice(EMOTION_BANK[emotion])

# =========================
# INPUT
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
# HISTORY
# =========================
for item in reversed(st.session_state.history):
    st.markdown(f"**{item['time']} · {item['text']}**")
    st.info(item["response"])
    st.markdown("---")

# =========================
# 🧠 WELLBEING SYSTEM (RESTORED + IMPROVED)
# =========================
st.markdown("## 🧠 Well-being System")

left, right = st.columns(2)

with left:
    st.markdown("### 🎯 Focus")

    st.write("⟡ Deep Work: 60–90 минути фокус без прекъсване върху една задача.")
    st.write("⟡ Single-tasking: една задача в един момент за по-ясен ум.")
    st.write("⟡ Planning: започни деня с 3 ясни приоритета.")

with right:
    st.markdown("### 🧘 Recovery")

    st.write("⟡ Breaks: кратки паузи възстановяват концентрацията.")
    st.write("⟡ Hydration: влияе директно върху когнитивната яснота.")
    st.write("⟡ Shutdown: осъзнат край на деня без работа след това.")
