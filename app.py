import streamlit as st
from datetime import datetime
import random

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Inner Compass",
    page_icon="🏛️",
    layout="wide"
)

# =========================
# STATE
# =========================
if "history" not in st.session_state:
    st.session_state.history = []

# =========================
# LANGUAGE
# =========================
lang = st.selectbox("Language", ["Български", "English"])

def t(bg, en):
    return bg if lang == "Български" else en

# =========================
# STYLE
# =========================
st.markdown("""
<style>
html, body {
    font-family: Inter, system-ui, sans-serif;
    background: #020617;
    color: #e2e8f0;
}

.stTextInput input {
    font-size: 20px !important;
    height: 60px !important;
}

h1 { text-align: center; }
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER (FIXED - NOT REMOVED)
# =========================
st.markdown("<h1>Inner Compass</h1>", unsafe_allow_html=True)

st.markdown(
    f"<p style='text-align:center; opacity:0.7;'>"
    f"⟡ {t('Продължаваме заедно... по-смирени, по-смислени, по-стоически', 'We continue together... more calm, more meaningful, more stoic')} ⟡"
    f"</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# =========================
# EMOTION KEYWORDS (unchanged logic, stable)
# =========================
RECOVERY = ["уморен","изморен","изтощен","капнал","изчерпан","нямам сила","прегорял"]
STRESS = ["стрес","напрежение","хаос","паника","натиск","притеснен","пренатоварен"]
SAD = ["тъжен","сам","болка","разбит","отчаян","потиснат"]
ANGER = ["ядосан","гневен","бесен","раздразнен","кипя"]
WORK = ["работа","deadline","задачи","график","натоварен"]
INSPO = ["щастлив","радост","вдъхновен","усмихнат","добре ми е"]
NEUTRAL = ["ок","нормално","спокойно","баланс","без промяна"]

def match(words, text):
    return any(w in text for w in words)

def detect(text):
    ttxt = text.lower()

    if match(RECOVERY, ttxt): return "recovery"
    if match(STRESS, ttxt): return "stress"
    if match(SAD, ttxt): return "sad"
    if match(ANGER, ttxt): return "anger"
    if match(WORK, ttxt): return "work"
    if match(INSPO, ttxt): return "inspiration"
    return "neutral"

# =========================
# RESPONSES (kept strong, not reduced)
# =========================
RESPONSES = {
"recovery":[
"Тялото ти показва ясна нужда от възстановяване. Това не е слабост, а естествена реакция на натрупано натоварване.",
"Изтощението е сигнал за прекомерно използване на ресурс. Възстановяването е част от процеса, не пауза от него.",
"Когато системата е уморена, правилният отговор е намаляване на натоварването, не натиск.",
"Понякога напредъкът изглежда като спиране, но всъщност е рестарт.",
"Това състояние показва, че е време да върнеш внимание към себе си."
],

"stress":[
"Напрежението показва претоварване на мисловния капацитет. Това е въпрос на количество, не на способност.",
"Когато всичко е важно, нищо не е ясно. Фокусът е решението.",
"Стресът често идва от едновременното обработване на твърде много посоки.",
"Не е нужно да реагираш на всичко веднага.",
"Пауза възстановява повече яснота от усилие."
],

"sad":[
"Това е състояние на вътрешна тежест, което изисква разбиране.",
"Емоционалната болка е процес, не момент.",
"Приемането намалява напрежението.",
"Това състояние е валидно и временно.",
"Разбирането е първата стъпка към облекчение."
],

"anger":[
"Гневът е висока енергия, която търси посока.",
"Между реакция и действие има пространство.",
"Това състояние показва натрупано напрежение.",
"Пауза променя резултата.",
"Гневът е сигнал, не решение."
],

"work":[
"Работното натоварване влияе на яснотата при липса на структура.",
"Фокусът е по-важен от обема задачи.",
"Това състояние показва нужда от приоритизация.",
"Прекалено много задачи разпиляват вниманието.",
"Редът създава ефективност."
],

"inspiration":[
"Това е състояние на яснота и вътрешен импулс.",
"Вдъхновението трябва да бъде насочено.",
"Когато умът е подреден, действията са естествени.",
"Това е добра вътрешна синхронизация.",
"Импулсът е начало, структурата е резултат."
],

"neutral":[
"Стабилно състояние без доминираща емоция.",
"Това е баланс между вътрешни процеси.",
"Яснота без емоционален шум.",
"Добра основа за решения.",
"Неутралността е стабилност."
]
}

# =========================
# ANALYSIS (FIXED - MEANINGFUL CATEGORIES)
# =========================
CATEGORY_LABELS = {
"recovery":"Възстановяване",
"stress":"Напрежение",
"sad":"Емоционална тежест",
"anger":"Реактивност",
"work":"Работно натоварване",
"inspiration":"Мотивация",
"neutral":"Баланс"
}

CATEGORY_DESC = {
"recovery":"Намалена енергия и нужда от почивка.",
"stress":"Ментално претоварване и натиск.",
"sad":"Вътрешна емоционална тежест.",
"anger":"Висока реактивност и напрежение.",
"work":"Претоварване от задачи и ангажименти.",
"inspiration":"Яснота и вътрешен импулс.",
"neutral":"Стабилно и балансирано състояние."
}

STOIC = {
"recovery":"„Почивката е част от пътя.“",
"stress":"„Не събитията, а интерпретацията им.“ – Епиктет",
"sad":"„Приемането носи спокойствие.“",
"anger":"„Между реакция и действие има свобода.“",
"work":"„Фокусът създава ред.“ – Сенека",
"inspiration":"„Ясният ум създава движение.“",
"neutral":"„Стабилността е основа на действие.“"
}

# =========================
# LAYOUT
# =========================
left, center, right = st.columns([1,3,1.2])

# =========================
# LEFT ANALYSIS
# =========================
with left:
    st.markdown("### 🧠 Анализ")

    counts = {}
    for h in st.session_state.history:
        counts[h["emotion"]] = counts.get(h["emotion"],0)+1

    for k,v in counts.items():
        st.write(f"{CATEGORY_LABELS[k]}: {v}")

    st.markdown("---")

    if counts:
        dom = max(counts, key=counts.get)

        st.markdown("### 📊 Обобщение")
        st.write(CATEGORY_DESC[dom])

        st.markdown("### 🏛️ Стоическа перспектива")
        st.write(STOIC[dom])

# =========================
# CENTER CHAT
# =========================
with center:

    st.markdown("### Как се чувстваш?")

    with st.form("form", clear_on_submit=True):
        text = st.text_input("Сподели състояние...")
        send = st.form_submit_button("Изпрати")

        if send and text:
            emo = detect(text)
            st.session_state.history.append({
                "time": datetime.now().strftime("%H:%M"),
                "text": text,
                "emotion": emo
            })

    st.markdown("---")

    for h in reversed(st.session_state.history):
        st.markdown(f"**{h['time']} · {h['text']}**")
        st.info(random.choice(RESPONSES[h["emotion"]]))

# =========================
# WELLBEING
# =========================
with right:
    st.markdown("### 🧘 Well-being")

    st.write("⟡ Дишане")
    st.write("⟡ Фокус")
    st.write("⟡ Движение")
    st.write("⟡ Хидратация")
    st.write("⟡ Почивка")
