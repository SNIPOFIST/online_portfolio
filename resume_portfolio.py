import streamlit as st


# PAGE CONFIGURATIONS
st.set_page_config(page_title="Hari Ram Selvaraj's Portfolio", page_icon="star", layout="wide", initial_sidebar_state="expanded")

col_1 , col_2, col_3 = st.columns(3)
with col_1:
    st.write("")
    st.write("")
    st.write("")
    st.title("***Hari Ram Selvaraj***")
    st.caption("Student in ***Masters of Applied Data Science*** at ***Syracuse University*** | Former - Associate Software Engineer | TATA ELXSI, bangalore India ")
    st.write("")
    st.markdown("***LinkedIn -  [Hari Ram Selvaraj](https://www.linkedin.com/in/hariramselvaraj/)***")
    st.markdown("***📍 Syracuse, US***")


with col_3:
    st.image(image='Linkedin_image_hari.jpeg', width=350)

# City place grew up etc
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")


# Academics Masters
st.subheader("Masters in Applied Data Science - Syracuse University 🍊 Aug'24 - May'26")
st.divider()
st.image(image='Syracuse_Linkedin_background.jpeg')
# Syracuse University Background Image
# Define a container
with st.container():
    # Apply CSS to that container
    st.markdown("""
        <style>
            .my-syracuse-container {
                background-image: url('Syracuse_Linkedin_background.jpeg');
                background-size: auto;
                background-position: center;
                padding: 80px;
                height: 320px;
            }
        </style>
        """, unsafe_allow_html=True)

    st.markdown('<div class="my-syracuse-container"></div>', unsafe_allow_html=True)


st.write("")
st.write("")
st.write("**Master’s in Applied Data Science at School of Information Studies | Syracuse University** emphasizes both theoretical and practical skills in data science and analytics. For the Fall 2024 semester, I have enrolled myself in several fundamental and Data Science imperative courses, In **Introduction to Data Science**, I learn core concepts like data wrangling, preprocessing, transformation, model building, model evaluation, and analysis using R. **Data Administration and Database Management** covers Azure cloud databases, SQL Server, Power Apps, and Docker for building scalable applications. Additionally, **Business Analytics** from the Whitman School of Management involves Tableau, R, and MS Access, focusing on decision-making through data analysis.")
st.write("")
st.write("")
st.write("")

# Tata Elxsi Background image
# Define a container

with st.container():
    # Apply CSS to that container
    st.markdown("""
        <style>
            .my-tata_elxsi-container {
                background-image: url('TATA-ELXSI-Linkedin-Background.jpeg');
                background-size: auto;
                background-position: center;
                height:100px;
            }
        </style>
        """, unsafe_allow_html=True)

    st.markdown('<div class="my-tata_elxsi-container"></div>', unsafe_allow_html=True)

st.write("")
st.write("")
st.subheader("Internship - TATA ELXSI")
st.divider()
"During my term as a Trainee at TATA ELXSI, I developed a Jinja-based interface for log analysis that gives users access to test videos, screenshots, and status updates, and includes **automated email reports** for product owners. Additionally, I created an **APK using FFMPEG** to convert pixelated images into videos for black frame verification, and performed **web scraping with BeautifulSoup and Requests** to gather user reviews, transforming them into a CSV dataset for **sentiment analysis**. I dove headfirst into the world of **Automation and Machine Learning**. From scripting snazzy user interfaces to brewing up **predictive ML models**. My dedication and knack for tinkering with tech not only earned me appreciations and recognition but also set the stage for bigger adventures ahead."
st.text("")
st.write("")
st.write("")
st.write("")


st.subheader("Associate Software engineer - TATA ELXSI")
st.divider()
"As an Associate Software Engineer at TATA ELXSI,I was responsible in developing a Random Forest model to predict streaming outages, boosting reliability by ***28%*** and enhancing user experience by ***33%*** during high-demand periods. I also created the **'Batch Log Analyzer'** with **Naive Bayes** to categorize batch logs, cutting processing time from **2 hours to 13 minutes** and reducing errors. Additionally, I **built a Python-based automation framework for 87 APIs**, reducing manual work to **18** minutes, and deployed a **live Grafana dashboard connecting to a central SQL database**, with version control managed via Gerrit.)"
st.write("")
st.write("")
st.write("")


st.subheader("Bachelors of Computer Applications - New Horizon college")
st.divider()
"My tech journey and passion in Computer Science began at New Horizon College, Bengaluru, where I earned my stripes with a Bachelor of Computer Applications; Pure computer science, focusing on the **Logical and Computation techniques** supported by the subjects, **Numerical and Statistical methods, Operational Research and Theory of Computations**.I delved deep into Python puzzles and trained myself well in **data Structures and Algorithms** from 4 different programming languages. Those academic adventures? They laid the groundwork for the wild tech ride ahead."
st.write("")
st.write("")
st.write("")
st.write("")


st.subheader("Certifications : https://hariramcertifications.streamlit.app/")
st.caption("These are the online course with certifications i achieved to keep my self abreast of techs and to sharpen my knowledge.")

st.divider()
st.write("")
st.write("")
st.write("")


st.subheader("Live Projects: https://list-of-projects.streamlit.app/ ")
st.caption("The above link would take you to working projects that I worked on after courses and books I read from online platforms. Take a look at it, it should be worth a visit.")

st.write("")
st.write("")
st.write("")
st.write("")
st.divider()
st.subheader("_Lets connect !_")
st.write("")
st.write("")

footer_col1, footer_col2 = st.columns(2)

with footer_col1:
    st.markdown("LinkedIn -  [Hari Ram S]('https://www.linkedin.com/in/hari-ram-s-342a7621b/')")


with footer_col2:
    st.markdown("Mail -  [HariramSelvaraj@yahoo.com](mailto:HariramSelvaraj@yahoo.com)")
