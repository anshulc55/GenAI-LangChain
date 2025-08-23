# Learning StreamLit Basic Funcations and uses 

# import module
import streamlit as st

# WebPage Title
st.title("This is My first Streamlit App")

# Write on Page
st.write("This is your first Streamlit app.")

# Text: st.title(), st.header(), st.subheader(), st.write() st.text()

# Header
st.header("This is a header") 

# # Subheader
st.subheader("This is a subheader")

st.text("This is Sample Text")

# Success, Info, Warning, Error, Exception:
st.success("Success")
st.info("Information")
st.warning("Warning")
st.error("Error")
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)


# checkbox
if st.checkbox("Show/Hide"):
    # display the text if the checkbox returns True value
    st.text("Showing the widget")


# radio button
status = st.radio("Select Gender : ", ("Male", "Female", "Trans", "Don't want to Disclose"))
if status == "Male":
    st.success("Male")
elif status == "Female":
    st.success("Female")
elif status == "Trans":
    st.success("Trans")
else:
    st.success("Don't want to Disclose")


# Selection box
hobby = st.selectbox("Hobbies : ", ['Dancing', 'Reading', 'Sports'])
st.write("Your hobby is: ", hobby)


# multi select box
hobbies = st.multiselect("Hobbies : ", ['Dancing', 'Reading', 'Sports'])
st.write("Your hobbies are: ", len(hobbies), 'hobbies')


# Create a simple button
st.button("Click me!")

if st.button("See More..."):
    st.text("Button Click Operation is Done...")


# Text Input
name = st.text_input("Enter Your name", "Type here...")
if st.button("Submit"):
    st.success(name.title())


# Slidebar
level = st.slider("Select the Level", 1, 10)
st.text("Selected : {}".format(level))
