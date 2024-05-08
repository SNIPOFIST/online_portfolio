import streamlit as st


# PAGE CONFG
st.set_page_config(page_title="Hari Ram Selvaraj's Portfolio", page_icon="sun", layout="wide", initial_sidebar_state="expanded")

col_1 , col_2, col_3 = st.columns(3)
with col_1:
    st.write("")
    st.title("Hari Ram Selvaraj")
    st.caption("Associate Software Engineer | TATA ELXSI ")
    st.write("PH : +91 89714 56478 | [LinkedIn] : https://www.linkedin.com/in/hariramselvaraj/")
    st.write(" 27/A, SBI Bank road, Doddanekundi,")
    st.write(" Marathalli, Bangalore, Karnataka - 560037")


with col_3:
    st.image(image='Linkedin_image_hari.jpeg',width=350)



# About me 
# city place grew up etc
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.subheader("About Me",divider="rainbow")
st.write("")
st.write("")
st.text("I'am a 22 year old technology enthusiast, from bangalore, India. Currently working in TATA ELXSI as Associate Software Engineer.")
st.text("Born and brought up in silicon city of india, gave me an opportunity to witness the industrial and technological revolution of Bangalore.")
st.text("I Love foot ball, Playing guitar and also to Automate stuffs thats boring to ease the boredom away")
st.text("buy me a coffee and it would be a good start for a never ending friendship ;)")

st.write("")
st.write("")

st.write("")
st.write("")


# Academics 



st.subheader("Bachelors in Computer Applications - 9.08 CGPA",divider="rainbow")
st.text("About college ")
st.write("")
st.write("")
st.write("")
st.write("")


st.subheader("Internship - TATA ELXSI", divider="rainbow")
st.text("Skills learned")
st.text("")
st.write("")
st.write("")
st.write("")


st.subheader("Associate Software engineer - TATA ELXSI", divider="rainbow")
st.write("")
st.write("")
st.write("")



st.subheader("Certifications : https://hariramcertifications.streamlit.app/",divider="rainbow")
st.write("")
st.write("")
st.write("")
st.subheader("Live Projects: https://list-of-projects.streamlit.app/ ",divider="rainbow")


st.write("")
st.write("")
st.write("")
st.write("")
st.divider()
st.subheader("_Lets connect !_")
st.write("")
st.write("")

footer_col1 , footer_col2, footer_col3= st.columns(3)

with footer_col1:
    st.markdown("LinkedIn -  [Hari Ram S]('https://www.linkedin.com/in/hari-ram-s-342a7621b/')")


with footer_col2:
    st.markdown("Instagram -  [hari____7]('https://www.instagram.com/hari____7/')")


with footer_col3:
    st.markdown("Mail -  [HariramSelvaraj@yahoo.com](mailto:HariramSelvaraj@yahoo.com)")



# 1. academics 
# 2. internship 
# 3. workex
# co curricluar 
