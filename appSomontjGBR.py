# -*- coding: utf-8 -*-
"""
Created on 08.02.23

@author: Loiq Mirov
"""

# -*- coding: utf-8 -*-
"""
Created on 08.02.23

@author: Loiq Mirov
"""


import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("gbrSomonTj.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(market_code, rooms, floor, area, remodel_code):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[market_code, rooms, floor, area, remodel_code]])
    print(prediction)
    return prediction



def main():
    st.title("Prediction of House Price")
    html_temp = """
    <div style="background-color:blue    ;padding:10px">
    <h2 style="color:white;text-align:center;">Prediction of house price in Dushanbe. Based on data from Somon.tj, algorithm GBoosting Regressor  </h2>
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    m=st.radio("Type of market 👉",
        key="market",
        options=["New", "Old"],    )
    if m=="Old":
        market_code=2
    elif m=="New":
        market_code=1

    rooms = st.text_input("rooms","")
    floor = st.text_input("floor","")
    area = st.text_input("area","")
    
    r = st.radio("Remodel",
                 key="Remodel",
                 options=["No remodel(box)", "Old", "New"], )
    if r == "No remodel(box)":
        remodel_code = 0
    elif r == "Old":
        remodel_code = 1
    elif r == "New":
        remodel_code = 2

    result=""
    if st.button("Predict"):
        result=int(predict_note_authentication(market_code, rooms, floor, area, remodel_code))


    #st.success('The output is {}'.format(result))
    st.success('Predicted cost of the house is {}'.format(result)+" TJS")
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    
