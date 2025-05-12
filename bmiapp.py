import streamlit as st

# st.title("Title widget")
#
# st.header("Header widget")
#
# st.subheader("SubHeader widget")
#
# st.write("Write widget")
#
# st.success("Success")
#
# st.error("Error")
#
# st.warning("Warning")

try:
    st.title("BMI CALCULATOR")
    st.write("Get to know your Body Mass Index")
    weight = st.number_input("WEIGHT (Kg) xx")
    height = st.number_input("HEIGHT (m) x.xx")
    bmi = weight / (height * height)

    st.header(f"BMI: {bmi:.2f}")

    if bmi < 18.5:
        st.error("You are underweight")
    elif 18.5 <= bmi < 25:
        st.success("Your BMI is normal")
    elif 25 <= bmi < 30:
        st.warning("You are Overweight")
    elif bmi >= 30:
        st.error("You are Obese")
except ZeroDivisionError:
    st.info("Enter a valid input")