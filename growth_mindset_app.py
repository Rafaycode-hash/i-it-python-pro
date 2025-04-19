import streamlit as st
import random

# Title
st.title("🚀 Growth Mindset Challenge")
st.subheader("Empower Yourself to Learn, Grow, and Succeed")

# Section: What is Growth Mindset?
st.markdown("""
A **growth mindset** means you believe your abilities and intelligence can improve with effort, learning, and persistence.

> “In a growth mindset, challenges are exciting rather than threatening.” – Carol Dweck
""")

# Section: Why Growth Mindset
st.header("🌱 Why Adopt a Growth Mindset?")
points = [
    "💡 Embrace Challenges",
    "❌ Learn from Mistakes",
    "💪 Persist Through Difficulties",
    "🎉 Celebrate Effort",
    "🧠 Keep an Open Mind"
]
for point in points:
    st.write(point)

# Section: Random Quote
quotes = [
    "Mistakes are proof that you are trying.",
    "Every expert was once a beginner.",
    "Your potential is endless.",
    "Doubt kills more dreams than failure ever will."
]
st.subheader("💬 Motivational Quote of the Day")
st.success(random.choice(quotes))

# Section: Self Checklist
st.header("✅ Self-Check: Are You Growing?")
st.checkbox("I learned something new recently.")
st.checkbox("I failed at something and reflected on it.")
st.checkbox("I helped someone else improve.")
st.checkbox("I asked for feedback.")
st.checkbox("I stayed positive during tough times.")

# Feedback box
st.header("📬 Share Your Thoughts")
feedback = st.text_area("How do you feel about your growth journey?")
if st.button("Submit Feedback"):
    st.success("Thanks for sharing! Keep growing. 🌟")

# Footer
st.markdown("---")
st.caption("Created as part of the Growth Mindset Challenge using Streamlit 💖")
