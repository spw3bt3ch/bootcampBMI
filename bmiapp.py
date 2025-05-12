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
tab1, tab2, tab3 = st.tabs(['About BMI', 'Calculate BMI', 'Facts About BMI'])
with tab1:
    st.title("Welcome to BMI Calculator")
    st.subheader("Body Mass Index")
    st.write("""BMI stands for Body Mass Index. 
    It's a number derived from a person’s weight and height. 
    It's used as a general indicator to categorize a person's 
    body weight relative to their height — and helps assess 
    if a person is underweight, healthy, overweight, or obese.
    
    ⚠️ Important Notes
    BMI does not measure fat directly – It’s a rough indicator. 
    Someone muscular may show as “overweight” on BMI but have low body fat.
    It doesn’t consider age, gender, bone structure, or muscle mass.
    
    For children, pregnant women, and athletes, BMI might not be accurate.
    """)
with tab2:
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

with tab3:
    st.title("10 Facts About BMI")
    st.write("""📌 Facts About BMI (Body Mass Index)
1. BMI was invented in the 1830s
It was developed by a Belgian mathematician named Adolphe Quetelet — way before modern fitness culture. It was originally called the "Quetelet Index."

2. BMI is not a measure of fat
BMI just compares your weight to your height — it doesn't directly measure body fat, muscle mass, or bone density.

3. Muscular people may have a high BMI
Athletes or bodybuilders often fall into the “overweight” or even “obese” category on the BMI scale, even though they have low body fat. It’s because muscle is denser than fat.

4. BMI doesn’t consider gender or age
Men and women have different fat distribution and body composition, but BMI uses the same formula for all adults. Also, older people naturally carry weight differently.

5. It's a quick screening tool
BMI is popular because it's fast, simple, and requires no special equipment — just weight and height. But it’s only the starting point, not a diagnosis.

6. A BMI of 25+ increases health risks
Studies link BMIs over 25 with higher chances of heart disease, diabetes, high blood pressure, and stroke — though individual factors matter too.

7. BMI standards vary globally
Some countries, like those in Asia, use lower BMI thresholds to define overweight and obesity, due to differences in body composition and disease risk.

8. Children use a different BMI system
Kids and teens use percentile charts based on age and sex — because their bodies grow and change rapidly.

9. BMI can be misleading during pregnancy
Pregnant women naturally gain weight, so BMI isn't a useful health indicator during pregnancy.

10. There are alternatives to BMI
Other health indicators like waist-to-hip ratio, body fat percentage, waist circumference, and DEXA scans can give a more accurate picture of health.


    """)