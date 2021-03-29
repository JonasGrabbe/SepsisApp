# -*- coding: utf-8 -*-
######################
# Import libraries
######################
import pandas as pd
import streamlit as st
import pickle
from sklearn.ensemble import RandomForestClassifier 


st.write("""
# Sepsis Easly Detection App
This app predicts sepisi **6 hours** befor on set with only six vital signs!

###### Sepsis is a life-threatening condition caused by your body’s response to an infection (bacterial, viral or fungal) and damages its own tissues.

""")

st.sidebar.header('Patient Input Parameters')

def user_input_features():
    hr = st.sidebar.slider('HR', 60, 160, 80)
    o2sat = st.sidebar.slider('O2Sat', 70, 100, 95)
    temp = st.sidebar.slider('Temp', 34, 42, 36)
    sbp = st.sidebar.slider('SBP', 90, 180, 110)
    mean_ap = st.sidebar.slider('MAP', 75, 125, 100)
    resp = st.sidebar.slider('Resp', 2, 40, 17)
    data = {'HR': hr,
            'O2Sat': o2sat,
            'Temp': temp,
            'SBP': sbp,
            'MAP': mean_ap,
            'Resp': resp}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)



# Reads in saved model
load_model = pickle.load(open('RF_Clf_model.pkl', 'rb'))

# Apply model to make predictions
prediction = load_model.predict(df)
prediction_proba = load_model.predict_proba(df)


##st.subheader('Class labels and their corresponding index number')
##st.write(df.SepsisLabel)

st.subheader('Prediction')
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)