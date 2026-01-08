import streamlit as st

st.set_page_config(page_title="Aura – Crisis Clarity Engine")

st.title("Aura – Crisis Clarity Engine")
st.write("Describe your situation below. Aura will help you understand the risk and the next step.")

user_input = st.text_area("What happened?")

if st.button("Get Guidance"):
    if user_input.strip() == "":
        st.warning("Please describe your situation.")
    else:
        text = user_input.lower()

        # SCAM / FRAUD
        if any(word in text for word in ["otp", "bank", "account", "payment", "link", "scam"]):
            category = "Immediate Risk (Scam / Fraud)"
            risk = "High"
            insight = "The situation shows signs of urgency and information requests commonly used in scams."
            action = "Pause immediately. Do not share details or click links. Verify through official sources."
            why = (
                "Scammers rely on panic to bypass careful thinking. "
                "Stopping and verifying protects you from irreversible financial loss."
            )

        # HEALTH
        elif any(word in text for word in ["fever", "pain", "headache", "injury", "bleeding"]):
            category = "Health Concern"
            risk = "Medium"
            insight = "Your description suggests a health issue that may need attention but is not clearly an emergency."
            action = "Monitor symptoms, rest if possible, and seek medical advice if conditions worsen."
            why = (
                "Early observation helps you act at the right time without unnecessary panic."
            )

        # EDUCATION (STUDENTS)
        elif any(word in text for word in ["exam", "college", "degree", "study", "education", "higher studies"]):
            category = "Education Decision"
            risk = "Medium"
            insight = "You are facing pressure to make an important decision without full clarity or experience."
            action = "Break the decision into a small step, such as exploring one option through research or short courses."
            why = (
                "Large decisions become easier when tested through small, low-risk experiments."
            )

        # CAREER / JOB
        elif any(word in text for word in ["job", "career", "work", "office", "promotion", "resign"]):
            category = "Career Stagnation"
            risk = "Medium"
            insight = "You feel stuck because dissatisfaction and fear of uncertainty are both present."
            action = "Identify one skill or role you can explore without immediately changing your job."
            why = (
                "Progress without immediate risk restores confidence and helps clarify long-term direction."
            )

        # EMOTIONAL / LIFE CONFUSION
        elif any(word in text for word in ["confused", "overwhelmed", "stressed", "relationship", "pressure"]):
            category = "Emotional Overload"
            risk = "Low to Medium"
            insight = "Strong emotions may be clouding your ability to think clearly right now."
            action = "Pause major decisions and write down what you need versus what you fear losing."
            why = (
                "Separating emotions from decisions prevents regret-driven choices."
            )

        # DEFAULT
        else:
            category = "General Situation"
            risk = "Low"
            insight = "No immediate danger indicators were detected."
            action = "Remain calm and observe the situation before acting."
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
