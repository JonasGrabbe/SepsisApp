# -*- coding: utf-8 -*-
######################
# Import libraries
######################
import pandas as pd
import numpy as np
import streamlit as st
import pickle
from sklearn.ensemble import RandomForestClassifier 



st.image('./titleApp4.png')

# Patient Input Parameters
st.sidebar.header('Patient Input Parameters')

def user_input_features():
    hr = st.sidebar.slider('Heart rate', 60, 160, 80)
    o2sat = st.sidebar.slider('Pulse oximetry (O2Sat)', 70, 100, 95)
    temp = st.sidebar.slider('Temperature', 34, 42, 36)
    sbp = st.sidebar.slider('Systolic blood pressure', 90, 180, 110)
    mean_ap = st.sidebar.slider('Mean arterial pressure', 75, 125, 100)
    resp = st.sidebar.slider('Respiration rate', 2, 40, 17)
    data = {'HR': hr,
            'O2Sat': o2sat,
            'Temp': temp,
            'SBP': sbp,
            'MAP': mean_ap,
            'Resp': resp}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()



# Reads in saved model
load_model = pickle.load(open('xgb_clf_model.pkl', 'rb'))

# Apply model to make predictions
prediction = load_model.predict(df)
prediction_proba = load_model.predict_proba(df)


if prediction == 0 :
 
   st.write("""
           Predicts sepsis with only six vital sings **6 hours** before onset!
           """) 
   st.subheader('Sepsis:')
   st.write("""        
            Sepsis is a life-threatening condition caused by your body’s response to an infection (bacterial, viral or fungal) and damages its own tissues.

            Sepsis is the leading cause of global mortality, around 20% of annual global death. Eraly detection is vital in the survival of the patient. Every 10min, death risk increases by 1%.
            """)
   st.subheader('Input:')
   st.write(df)
   st.subheader('Prediction Probability:')
   st.write(prediction_proba)
   
   
else:
   st.write(""" `You may want to contact a doctor!` """)
   st.image('./sepsisDetected9.png')
   st.subheader('Prediction Probability:')
   st.write(prediction_proba)

st.write(""" *** """)
#st.header('qSOFA')
st.image('./qsofablack.png')
st.write(""" ###### The qSOFA score (also known as quickSOFA) is a bedside prompt that may identify patients with suspected infection who are at greater risk for a poor outcome outside the intensive care unit (ICU). It uses three criteria, assigning one point for low blood pressure (SBP≤100 mmHg), high respiratory rate (≥22 breaths per min), or altered mentation (Glasgow coma scale<15).""")
st.subheader('qSOFA Score:')

qsofa = 0
if df['Resp'].values >= 22:
    qsofa += 1
if df['SBP'].values <= 100:
    qsofa += 1
#qsofa[df['Resp'].values >= 22] += 1
#qsofa[df['SBP'].values <= 100] += 1



if qsofa >= 2:
    st.write(""" `Sepsis suspected!!!` """)
if qsofa == 1:
    st.write(""" `If your mental state is altered: Sepsis suspected!!!` """)       
if qsofa == 0:
    st.write(""" `No Sepsis suspected` """)


