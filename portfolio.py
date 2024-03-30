import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image, ImageDraw
import base64

image = Image.open("Assets/Passport_Photograph.jpg")
height,width = image.size 
lum_img = Image.new('L', [height,width] , 0) 
draw = ImageDraw.Draw(lum_img) 
draw.pieslice([(0,0), (height,width)], 0, 360, fill = 255, outline = "white") 
img_arr =np.array(image) 
lum_img_arr =np.array(lum_img) 
final_img_arr = np.dstack((img_arr,lum_img_arr)) 

st.sidebar.image(final_img_arr)
st.sidebar.header("**ARVINDH C VIGNESH**")
st.sidebar.link_button('Github','https://github.com/Arvindh99',use_container_width=True)
st.sidebar.link_button('LinkedIn','https://www.linkedin.com/in/arvindh22199',use_container_width=True)
st.sidebar.link_button('Kaggle','https://www.kaggle.com/arvindh22',use_container_width=True)
st.sidebar.button('✉ cvarvindh@gmail.com',use_container_width=True)
st.sidebar.button('📞 +91 9444422199',use_container_width=True)

tab1, tab2, tab3, tab4 = st.tabs(["ABOUT", "PROJECTS", "CERTIFICATIONS", "RESUME"])

with tab1:
        st.header("An Inspiring Data Analyst")
        st.markdown("""**Having a Masters degree in Health Data Science and have over 2.5 years of work experience**
        with a strong foundation in :orange[***Python, Machine Learning, SQL, Tableau, Power BI, and Excel***]. 
                My journey in the world of data is marked by a relentless pursuit 
                of unlocking actionable insights that fuel business growth.""")
        st.divider()

        st.header("Skills at Glance")

        python_exp = st.expander("**Python Programming**")
        python_exp.caption("*Known Packages:*")
        python_exp.text("Pandas, Numpy, Matplotlib, Seaborn, Plotly, Scikit-learn, Streamlit, Regex.")

        ml_exp = st.expander("**Machine Learning Algorithms**")
        ml_exp.caption("*Known Algorithms:*")
        ml_exp.text("""Decision Tree, Random Forest, KNN, Logistic Regression,Linear Regression,
Navie Bayes, Gradient Boost, LightGBM, SVM.""")

        dl_exp = st.expander("**Deep Learning Methods**")
        dl_exp.caption("*Known Algorithms:*")
        dl_exp.text("""ANN, CNN, RNN.""")

        excel_exp = st.expander("**Microsoft Excel**")
        excel_exp.caption("*Known Skills:*")
        excel_exp.text("""VLOOKUP, Pivot Tables, Conditional Formatting, COUNTIF, Filters, Charts, SUMIF,
Sorting, Excel Shortcuts, Formatting, Average, IF Functions and All Basics.""")

        bi_exp = st.expander("**Power BI**")
        bi_exp.caption("*Known Skills:*")
        bi_exp.text("""Importing Data, Data Manipulations, Building Relationships and Visualization""")

        tableau_exp = st.expander("**Tableau**")
        tableau_exp.caption("*Known Skills:*")
        tableau_exp.text("""Importing Data from various sources, Data Manipulations, Building Relationships,
Visualization and Dashboard Creation""")

        sql_exp = st.expander("**SQL**")
        sql_exp.caption("*Known Skills:*")
        sql_exp.text("""Connecting Server, Database/Table Creation, Aggregate Functions, JOINS, 
DELETE, DROP""")

        offc_exp = st.expander("**Microsoft Office**")
        offc_exp.caption("*Known Tools:*")
        offc_exp.text("""Word, Excel, Powerpoint, Outlook""")

        st.divider()

with tab2:
        proj = st.radio("Select:",["Python Projects","Excel Projects"],horizontal=True,index=None)
        if proj == "Python Projects":
                ml_proj = st.checkbox('ML PROJECTS')
                st_proj = st.checkbox('STREAMLIT PROJECTS')
                dl_proj = st.checkbox('DEEP LEARNING PROJECTS')
                st.divider()
                if ml_proj:
                        with st.expander("Project 1: :orange[Predicting Disease based on the Symptoms and identifying specialist based on predicted disease]"):
                                with st.container(border=True):
                                        st.write("""This ML project provides a concise and informative overview 
of the predicted disease, its associated likelihood, the recommended doctor, and a brief description to aid in understanding and decision-making
regarding the predicted disease. Using a classification model, diseases have been predicted based on the given symptoms.""")
                                        st.caption("Ouput includes:")
                                        st.write("""1. :blue[Predicted Disease:] The disease that has been predicted based on the symptoms provided.
2. :blue[Chance of the Disease:] The likelihood or probability of having that disease, as determined by the classification model.
3. :blue[Recommended Doctor:] The doctor or specialist recommended to visit for further evaluation or treatment of the predicted disease.
4. :blue[Description of the Disease:] A brief overview or description of the predicted disease, providing additional information about its symptoms, causes, and potential treatments.""")
                                        col1, col2, col3 = st.columns(3,gap="large")
                                        with col2:
                                                st.link_button("VIEW PROJECT", "https://github.com/Arvindh99/Disease_Speciality_Recommendation/tree/main")
                        
                        with st.expander("Project 2: :orange[Medical Cost Insurance using Simple Linear Regression]"):
                                with st.container(border=True):
                                        st.write("""The objective of this project is to build a simple linear regression model that can predict the 
total expenses based on the given features. This model can be useful for estimating the costs for medical treatment and insurance purposes.
The features includes age, BMI, sex, number of children, smoker status, region of residence, and the total expenses.""")
                                        st.caption("Model Performance:")
                                        st.write("The linear regression model achieved an accuracy of 76.68% in predicting the total expenses.")
                                        col1, col2, col3 = st.columns(3,gap="large")
                                        with col2:
                                                st.link_button("VIEW PROJECT", "https://github.com/Arvindh99/Medical-Cost-Insurance---Simple-Linear-Regression")

                        with st.expander("Project 3: :orange[Predicting Disease based on the patient characteristics and symptoms]"):
                                with st.container(border=True):
                                        st.write("""This project provides valuable insights into the relationship between symptoms, 
patient characteristics, and disease outcomes. EDA (Exploratory Data Analysis) and classification algorithms were performed on the dataset. """)
                                        st.caption("Model Performance:")
                                        st.write("""Through EDA and classification modeling, the Gradient Boost algorithm was identified as the 
best performing model for predicting the outcome of the diagnosis or assessment for specific diseases. The trained model can be 
used to make predictions on new patient profiles and assist in disease diagnosis and treatment decisions.""")
                                        col1, col2, col3 = st.columns(3,gap="large")
                                        with col2:
                                                st.link_button("VIEW PROJECT", "https://github.com/Arvindh99/Disease-Symptoms-EDA-ML")
                
                if st_proj:
                        with st.expander("Project 1: :orange[Electronic Health Record (EHR) Web Application]"):
                                with st.container(border=True):
                                        st.write("""The Electronic Health Record (EHR) Web Application is designed to store and manage basic 
information of patients' health records. This web application allows users to create, edit, view, and delete health records using the Streamlit framework.""")
                                        st.caption("Features:")
                                        st.write("""The EHR Web Application provides the following features:
1. :blue[Create Health Record:] Users can enter and save basic information about a patient's health record, such as name, age, gender, medical history, and contact details.
2. :blue[Edit Health Record:] Users have the ability to modify the existing health records and update any changes in the patient's information.
3. :blue[View Health Record:] Users can view the stored health records in a user-friendly format, allowing easy access to patient information.
4. :blue[Delete Health Record:] Users can remove unwanted or outdated health records from the system.""")
                                        col1, col2, col3, col4 = st.columns(4,gap="medium")
                                        with col1:
                                                st.link_button("VIEW PROJECT", "https://github.com/Arvindh99/Elecronic-Health-Record?tab=readme-ov-file")
                                        with col4:
                                                st.link_button("WEB APP","https://share.streamlit.io/arvindh99/elecronic-health-record/main/ehr.py")

                        with st.expander("Project 2: :orange[Predict the winner of the IPL Cricket Match]"):
                                with st.container(border=True):
                                        st.write("""This project focuses on predicting the winner of IPL cricket matches based on teams, toss winner, toss decision, and venues.""")
                                        st.caption("Model Performance:")
                                        st.write("""The Random Forest model achieved an accuracy of 85.90%""")
                                        col1, col2, col3, col4 = st.columns(4,gap="medium")
                                        with col1:
                                                st.link_button("VIEW PROJECT", "https://github.com/Arvindh99/IPL-Match-Prediction/tree/main")
                                        with col4:
                                                st.link_button("WEB APP","https://arvindh99-ipl-match-predicting-web-app-ipl-pred-dmnrqy.streamlit.app/")
                
                if dl_proj:
                        with st.expander("Project 1: :orange[Bank Customer Churn Prediction using ANN]"):
                                with st.container(border=True):
                                        st.write("""The objective of this project is to build a ANN model that can predict the 
whether the customer will churn or not.""")
                                        st.caption("Model Performance:")
                                        st.write("The ANN model achieved an accuracy of 86.1%.")
                                        col1, col2, col3 = st.columns(3,gap="large")
                                        with col2:
                                                st.link_button("VIEW PROJECT", "https://github.com/Arvindh99/ANN-Bank-Churn-Dataset/tree/main")



        elif proj == "Excel Projects":
                with st.expander("Project 1: :orange[Demonstrating Innovative Charts in Excel]"):
                        with st.container(border=True):
                                st.write("""In this Excel project, I embarked on a compelling journey to bring data to life 
through innovative visualizations, demonstrating my proficiency in leveraging 
Microsoft Excel for powerful data analysis and presentation. The focal point of this endeavor was the COVID-19 dataset, 
a poignant reminder of the unprecedented times we faced.""")
                                st.write(":blue[Speedometer Chart:] Shows the Recovery Rate and Death Ratio.")
                                st.write(":blue[Thermometer Chart:] Shows the Active Cases.")
                                st.write(":blue[Shaded curve line Chart:] Month wise confirmed cases.")
                                st.write("Slicers are also added to know the country wise metrics")
                                projimg1 = Image.open("Assets/COVID_Dashboard.png")
                                st.image(projimg1)
                                col1, col2, col3 = st.columns(3,gap="large")
                                with col2:
                                        st.link_button("VIEW PROJECT", "https://github.com/Arvindh99/COVID-19-Dashboard")
             

with tab3:
        with st.expander(":orange[Tableau 2022 A-Z: Hands-On Tableau Training for Data Science]"):
                with st.container(border=True):
                        st.caption("**Issued by:** :blue[***UDEMY***]")
                        st.link_button("SHOW CREDENTIALS", "https://www.udemy.com/certificate/UC-a40b45ce-f9d3-48cf-925a-2a6d506f7698/")
        
        with st.expander(":orange[Foundations of Data Science]"):
                with st.container(border=True):
                        st.caption("**Issued by:** :blue[***ONE FOURTH LABS***]")
                        st.link_button("SHOW CREDENTIALS", "https://padhai.onefourthlabs.in/certificates/uyoxbwevyd")

        with st.expander(":orange[Business Analytics and Text Mining Modelling using Python]"):
                with st.container(border=True):
                        st.caption("**Issued by:** :blue[***NPTEL***]")
        
        with st.expander(":orange[Python for Data Science]"):
                with st.container(border=True):
                        st.caption("**Issued by:** :blue[***NPTEL***]")


with tab4:
        with open("Assets/Arvindh Resume.pdf", "rb") as pdf_file:
                PDFbyte = pdf_file.read()
                
        st.download_button(label="Download Resume",
                    data=PDFbyte,
                    file_name="resume.pdf",
                    mime='application/octet-stream')

        @st.cache_data
        def displayPDF(file):
                with open(file, "rb") as f:
                        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

                pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1200" type="application/pdf"></iframe>'

                st.markdown(pdf_display, unsafe_allow_html=True)
        
        file = "Assets/Arvindh Resume.pdf"
        displayPDF(file)


        
