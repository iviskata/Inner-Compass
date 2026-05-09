# =========================
# 🧠 АНАЛИЗ НА РАБОТНО СЪСТОЯНИЕ (БЪЛГАРСКИ МОДЕЛ)
# =========================

def analyze():
    counts = {
        "cognitive_load": 0,
        "pressure": 0,
        "emotional_strain": 0,
        "stable": 0,
        "engagement": 0,
        "recovery": 0
    }

    for h in st.session_state.history:
        e = h["emotion"]

        if e in ["stress"]:
            counts["cognitive_load"] += 1

        elif e in ["anger"]:
            counts["pressure"] += 1

        elif e in ["sad", "work_stress"]:
            counts["emotional_strain"] += 1

        elif e in ["neutral"]:
            counts["stable"] += 1

        elif e in ["inspiration"]:
            counts["engagement"] += 1

        else:
            counts["recovery"] += 1

    dominant = max(counts, key=counts.get)
    return counts, dominant


def pretty_label(key):
    labels = {
        "cognitive_load": "🧠 Когнитивно натоварване",
        "pressure": "⚡ Повишен натиск",
        "emotional_strain": "🌫 Емоционално напрежение",
        "stable": "⚖ Стабилно състояние",
        "engagement": "🚀 Висока ангажираност",
        "recovery": "🧯 Нужда от възстановяване"
    }

    return labels[key]
