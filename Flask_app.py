#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import libraries
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
import pickle


app = Flask(__name__)

# Load the model From model.pkl
model = pickle.load(open('model_randomforest.pkl','rb'))


#Untuk menerima masukan API

@app.route('/api',methods=['POST'])
def predict():
    datas=request.get_json(force=True)
    output=[]
    
    for data in datas:
        prediction = models.predic(np.array([data['PAY_1'],data['PAY_2'],data['LIMIT_BAL']]))
        if prediction==0:
            output.append(str(prediction)+', pelanggan akan membayar')
        else:
            output.append(str(prediction)+', pelanggan tidak akan membayar')
    return jsonify(output)

