# import module
import streamlit as st

# Application Title
st.title("Welcome to BMI Calculator! Your own Health Monitor!!!")

# TAKE WEIGHT
weight = st.number_input("Enter your weight (in kgs)")

# TAKE HEIGHT
height_unit = st.radio("Select your height format:", ('cms', 'meters', 'feet'))

if height_unit == "cms":
    height = st.number_input('Centimeters')
    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text("Enter some value of height")
elif height_unit == "meters":
    height = st.number_input('Meters')
    try:
        bmi = weight / (height**2)
    except:
        st.text("Enter some value of height")
else:
    height = st.number_input('Feets')
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("Enter some value of height")


# check if the button is pressed or not
if st.button('Calculate BMI'):

    # print the BMI INDEX
    st.subheader("Your BMI Index is {}.".format(bmi))

    if(bmi < 16):
        st.error("You are Extremely Underweight")
    elif(bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("Healthy")
    elif(bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    elif(bmi >= 30):
        st.error("Extremely Overweight")

