import streamlit as st

# Title
st.title("🧮 BMI Calculator")
st.write("Calculate your Body Mass Index (BMI) easily.")

# Input
weight = st.number_input("Enter your weight (kg)", min_value=1.0)
height_cm = st.number_input("Enter your height (cm)", min_value=1.0)

# Calculate Button
if st.button("Calculate BMI"):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)

    st.success(f"Your BMI is: {bmi:.2f}")

    # Interpretation
    if bmi < 18.5:
        st.warning("You are Underweight 😟")
    elif 18.5 <= bmi < 25:
        st.info("You have a Normal weight 😊")
    elif 25 <= bmi < 30:
        st.warning("You are Overweight 😐")
    else:
        st.error("You are Obese 😟")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
