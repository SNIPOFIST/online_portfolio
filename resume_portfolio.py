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
st.image(image='data:image/jpeg;base64,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', cpation='Syracuse University Logo')
# Syracuse University Background Image
# Define a container
with st.container():
    # Apply CSS to that container
    st.markdown("""
        <style>
            .my-syracuse-container {
                background-image: url('/images/4HURt5EyqJLPhQ2hH4fOT2-mgNM=/5436/width-1300/hall-of-languages-winter-2025.jpg');
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
                background-image: url('https://media.licdn.com/dms/image/v2/D5616AQGt6R2pkH0xaA/profile-displaybackgroundimage-shrink_200_800/profile-displaybackgroundimage-shrink_200_800/0/1666849445740?e=2147483647&v=beta&t=eOtIpMZiPu2yVBt0Iz8mgxW1wVXtnELtDZDGddgWbEU');
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
