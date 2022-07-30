import pandas as pd
import numpy as np
import streamlit as st
import json
import requests as re
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
import pickle
import warnings
warnings.filterwarnings("ignore")

pipe = pickle.load(open('fraud_random_forest.pkl','rb'))

st.title("Fraudulent Transactions Prediction Web App")

st.write("""
## About
Fraudulent Transactions Prediction is a form of identity theft that involves an unauthorized taking of another's account information for the purpose of charging purchases to the account or removing funds from it.
**This Streamlit App utilizes a Machine Learning model served as an API in order to detect fraudulent transactions based on the following criteria: hours, type of transaction, amount, balance before and after transaction etc.**       
""")


st.sidebar.header('Input Features of The Transaction')

step = st.sidebar.slider("""Number of Hours it took the Transaction to complete: """)
types = st.sidebar.subheader(f"""
                 Enter Type of Transfer Made:\n\n\n\n
                 '0' for 'Cash In' Transaction\n 
                 '1' for 'Cash Out' Transaction\n 
                 '2' for 'Debit' Transaction\n
                 '3' for 'Payment' Transaction\n  
                 '4' for 'Transfer' Transaction\n""")
types = st.sidebar.selectbox("",('Cash In','Cash Out','Debit','Payment','Transfer'))
x = ''
if types == 'Cash In':
    x = 'Cash in'
if types == 'Cash Out':
    x = 'Cash Out'
if types == 'Debit':
    x = 'Debit'
if types == 'Payment':
    x = 'Payment'
if types == 'Transfer':
    x =  'Transfer'
    
amount = st.sidebar.number_input("Amount in $",min_value=0, max_value=11000000)
oldbalanceorg = st.sidebar.number_input("""Original Balance Before Transaction was made""",min_value=0, max_value=11000000)
newbalanceorg= st.sidebar.number_input("""New Balance After Transaction was made""",min_value=0, max_value=11000000)
oldbalancedest= st.sidebar.number_input("""Old Balance""",min_value=0, max_value=11000000)
newbalancedest= st.sidebar.number_input("""New Balance""",min_value=0, max_value=11000000)
isflaggedfraud = 0
if amount >= 200000:
  isflaggedfraud = 'Fraud'
else:
  isflaggedfraud = 'Not Fraud'
  
if st.button("predict Result"):
    values = {
    "step": step,
    "types": types,
    "amount": amount,
    "oldbalanceorig": oldbalanceorg,
    "newbalanceorig": newbalanceorg,
    "oldbalancedest": oldbalancedest,
    "newbalancedest": newbalancedest,
    "isflaggedfraud": isflaggedfraud
    }

    st.write(f"""### These are the transaction details:\n
    
    1. Number of Hours it took to complete: {step}\n
    2. Type of Transaction: {x}\n
    3. Anount Sent: {amount}\n
    4. Previous Balance Before Transaction: {oldbalanceorg}\n
    5. New Balance After Transaction: {newbalanceorg}\n
    6. Old Balance Destination Recepient Balance: {oldbalancedest}\n
    7. New Balance Destination Recepient Balance: {newbalancedest}\n
    8. System Flag Fraud Status: {isflaggedfraud}
                """)

