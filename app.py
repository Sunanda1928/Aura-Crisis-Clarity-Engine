import streamlit as st

st.set_page_config(
    page_title="Aura – Crisis Clarity Engine",
    page_icon="🧠",
    layout="centered"
)

st.title("Aura – Crisis Clarity Engine")
st.write(
    "Describe your situation below. Aura will help you understand what’s going on "
    "and suggest a safe next step."
)

user_input = st.text_area("What happened?")

if st.button("Get Guidance"):
    if user_input.strip() == "":
        st.warning("Please describe your situation.")
    else:
        text = user_input.lower()

        # 🚨 SCAM / FRAUD
        if any(word in text for word in ["otp", "bank", "account", "payment", "link", "scam"]):
            category = "Immediate Risk (Scam / Fraud)"
            risk = "High"
            insight = "The situation shows patterns commonly used in financial scams."
            action = "Do not share any information or click links. Verify directly using official bank contact details."
            why = (
                "Scammers rely on urgency and fear to force quick action. "
                "Pausing and verifying prevents irreversible financial loss."
            )

        # 🏥 HEALTH CONCERN
        elif any(word in text for word in ["fever", "pain", "headache", "injury", "bleeding"]):
            category = "Health Concern"
            risk = "Medium"
            insight = "Your description suggests a health issue that may need attention but is not clearly an emergency."
            action = "Monitor symptoms, rest if possible, and seek medical advice if the condition worsens."
            why = (
                "Early observation helps you respond at the right time without unnecessary panic."
            )

        # 🎓 EDUCATION (STUDENTS)
        elif any(word in text for word in ["exam", "college", "degree", "study", "education", "higher studies"]):
            category = "Education Decision"
            risk = "Medium"
            insight = "You are facing pressure to make an important academic decision without full clarity."
            action = "Break the decision into a small step, such as researching one option or speaking to a mentor."
            why = (
                "Large academic decisions become easier when explored through small, low-risk actions."
            )

        # 💼 CAREER / JOB
        elif any(word in text for word in ["job", "career", "work", "office", "promotion", "resign"]):
            category = "Career Stagnation"
            risk = "Medium"
            insight = "You feel stuck due to dissatisfaction combined with fear of uncertainty."
            action = "Explore one new skill, role, or internal opportunity without making immediate job changes."
            why = (
                "Progress without immediate risk restores confidence and helps clarify long-term direction."
            )

        # 🧠 BEHAVIORAL / HABIT CONCERN
        elif any(word in text for word in ["cant stop", "cannot stop", "addicted", "habit", "craving", "eating"]):
            category = "Behavioral Concern"
            risk = "Medium"
            insight = "The situation suggests a repetitive behavior that may be linked to habit, stress, or routine."
            action = "Reflect on when this behavior started and what triggers it. Consider discussing it with someone you trust."
            why = (
                "Recognizing patterns early helps prevent escalation and supports healthier choices."
            )

        # ❤️ EMOTIONAL / LIFE CONFUSION
        elif any(word in text for word in ["confused", "overwhelmed", "stressed", "pressure", "relationship"]):
            category = "Emotional Overload"
            risk = "Low to Medium"
            insight = "Strong emotions may be making it difficult to think clearly right now."
            action = "Pause major decisions and write down what you need versus what you fear losing."
            why = (
                "Separating emotions from decisions reduces regret-driven choices."
            )

        # 🟢 DEFAULT / GENERAL
        else:
            category = "General Situation"
            risk = "Low"
            insight = "No immediate danger indicators were detected in the situation."
            action = "Remain calm and observe the situation before taking further action."
            why = (
                "Clarity often improves with time and careful observation."
            )

        st.subheader("Aura Assessment")
        st.write(f"**Situation Type:** {category}")
        st.write(f"**Risk Level:** {risk}")
        st.write(f"**What’s Going On:** {insight}")
        st.write(f"**Recommended Next Step:** {action}")

        st.markdown("### Why this helps")
        st.write(why)
