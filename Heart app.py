# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 17:18:42 2022

@author: Anuja
"""

import streamlit as st
import numpy as np
import pickle as pkl
from PIL import Image
#Load the saved model
model=pkl.load(open("final_model.p","rb"))


#st.title('Heart Disease Prediction Web App')
st.set_page_config(page_title="Heart Disease Predication",layout="centered",initial_sidebar_state="expanded")
image = Image.open('heart image.jpg')
st.image(image)


def preprocess(BMI,Smoking,AlcoholDrinking,Stroke,PhysicalHealth,MentalHealth,DiffWalking,Sex,AgeCategory,Race,Diabetic,PhysicalActivity,Asthma,KidneyDisease,SkinCancer): 

    # Pre-processing user input   
    
    if Smoking=="Yes":
        Smoking=1
    elif Smoking=="No":
        Smoking=0
        
    if AlcoholDrinking=="Yes":
        AlcoholDrinking=1
    elif AlcoholDrinking=="No":
        AlcoholDrinking=0
        
    if Stroke=="Yes":
        Stroke=1
    elif Stroke=="No":
        Stroke=0
        
    if DiffWalking=="Yes":
         DiffWalking=1
    elif DiffWalking=="No":
         DiffWalking=0
         
    if Sex=="Male":
        Sex=1 
    else: Sex=0
    
    
    if AgeCategory=="18-24":
        AgeCategory=0
    elif AgeCategory=="25-29":
        AgeCategory=1
    elif AgeCategory=="30-34":
        AgeCategory=2
    elif AgeCategory=="35-39":
        AgeCategory=3
    elif AgeCategory=="40-44":
        AgeCategory=4
    elif AgeCategory=="45-49":
        AgeCategory=5
    elif AgeCategory=="50-54":
        AgeCategory=6
    elif AgeCategory=="55-59":
        AgeCategory=7
    elif AgeCategory=="60-64":
        AgeCategory=8
    elif AgeCategory=="65-69":
        AgeCategory=9
    elif AgeCategory=="70-74":
        AgeCategory=10
    elif AgeCategory=="75-79":
        AgeCategory=11
    elif AgeCategory=="80 or older":
        AgeCategory=12
    
    if Race=="American Indian/Alaskan Native":
         Race=0
    elif Race=="Asian":
         Race=1
    elif Race=="Black":
         Race=2
    elif Race=="Hispanic":
         Race=3
    elif Race=="Other":
         Race=4
    elif Race=="White":
         Race=5
  
        
    if Diabetic=="No":
         Diabetic=0
    elif Diabetic=="No, borderline diabetes":
         Diabetic=1
    elif Diabetic=="Yes":
         Diabetic=2
    elif Diabetic=="Yes (during pregnancy)":
         Diabetic=3
    
        
    
    if PhysicalActivity=="Yes":
        PhysicalActivity=1
    elif PhysicalActivity=="No":
        PhysicalActivity=0
        
    if Asthma=="Yes":
        Asthma=1
    elif Asthma=="No":
        Asthma=0
        
    if KidneyDisease=="Yes":
       KidneyDisease=1
    elif KidneyDisease=="No":
       KidneyDisease=0     
       
    if SkinCancer=="Yes":
        SkinCancer=1
    elif SkinCancer=="No":
        SkinCancer=0     
    
    
    user_input=[BMI,Smoking,AlcoholDrinking,Stroke,PhysicalHealth,MentalHealth,DiffWalking,Sex,AgeCategory,Race,Diabetic,PhysicalActivity,Asthma,KidneyDisease,SkinCancer]
    user_input=np.array(user_input)
    user_input=user_input.reshape(1,-1)
    prediction = model.predict(user_input)

    return prediction

    # front end elements of the web page 
html_temp = """ 
    <div style ="background-color:pink;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Heart Disease Prediction </h1> 
    </div> 
    """
# display the front end aspect
st.markdown(html_temp, unsafe_allow_html = True) 
#st.subheader('by Anuja ')


# following lines create boxes in which user can enter data required to make prediction
BMI=st.number_input('Enter BMI', min_value=(0.0),max_value=(95.99))
Smoking=st.selectbox('Are Smoker',["Yes","No"])
AlcoholDrinking=st.selectbox('Alcoholic',["Yes","No"])
Stroke=st.selectbox('have Stroke before',["Yes","No"])
PhysicalHealth=st.selectbox ("Physical Health",range(0,31,1))
MentalHealth=st.selectbox ("Mental Health",range(0,31,1))
DiffWalking=st.selectbox('Difficulty in Walking',["Yes","No"])
Sex=st.selectbox('Sex',["Male","Female"])
AgeCategory=st.selectbox ("Select Age Category",["18-24","25-29","30-34","35-39","40-44","45-49","50-54","55-59","60-64","65-69","70-74","75-79","80 or older"])
Race=st.selectbox ("Race",["American Indian/Alaskan Native","Asian","Black","Hispanic","Other","White"])
Diabetic=st.selectbox ("Diabetic",["No","No, borderline diabetes","Yes","Yes (during pregnancy)"])
PhysicalActivity=st.selectbox('PhysicalActivity',["Yes","No"])
Asthma=st.selectbox('Have Asthma',["Yes","No"])
KidneyDisease=st.selectbox('Have KidneyDisease',["Yes","No"])
SkinCancer=st.selectbox('Have SkinCancer',["Yes","No"])


#user_input=preprocess
pred=preprocess(BMI,Smoking,AlcoholDrinking,Stroke,PhysicalHealth,MentalHealth,DiffWalking,Sex,AgeCategory,Race,Diabetic,PhysicalActivity,Asthma,KidneyDisease,SkinCancer)


  


if st.button("Predict"):    
     if pred[0] == 0:
         st.error('You have low risk of getting a heart attack!')

     else:
          st.success('Warning! You have high risk of getting a heart attack!')

       
    
st.sidebar.subheader("About App")

st.sidebar.info("This web app is helps you to check whether you have Heart Disease at high risk or low risk.")
st.sidebar.info("Enter all fields and click on the 'Predict' button to check prediction!!! ")









    
    
        
    

