import streamlit as st
import pickle
import numpy as np
import pandas as pd

#import the model
pipe=pickle.load(open('pipe.pkl','rb'))
df=pickle.load(open('df.pkl', 'rb'))

st.title("Laptop Predictor")

#brand
company= st.selectbox('Brand', df['Company'].unique())
#type of laptop
type= st.selectbox('Type',df['TypeName'].unique())
#Ram
ram= st.selectbox('Ram(in GB)',[2,4,6,8,12,16,24,32,64])
#weight
weight=st.number_input('Weight of the Laptop')

#Touchscreen
touchscreen=st.selectbox('TouchScreen', ['No','Yes'])
#IPS
ips=st.selectbox('IPS',['No','Yes'])
#screen size
screen_size=st.number_input('Screen Size')
#Resolution
resolution=st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900',
'3840x2160','3200x1800','2880x1800','2560x1600','2560x1400','2304x1440'])

#cpu
cpu=st.selectbox('Brand',df['Cpu Brand'].unique())
hdd=st.selectbox('HDD(inGB)',[0,128,256,512,1024,2048])
ssd=st.selectbox('SSD(inGB)',[0,8,128,256,512,1024])
gpu=st.selectbox('GPU',df['Gpu Brand'].unique())
os=st.selectbox('OS',df['os'].unique())


if st.button('Predict Price'):

    touchscreen = 1 if touchscreen == 'Yes' else 0
    ips = 1 if ips == 'Yes' else 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = (((X_res**2) + (Y_res**2)) ** 0.5) / screen_size


    query_df = pd.DataFrame({
        'Company': [company],
        'TypeName': [type],
        'Ram': [ram],
        'Weight': [weight],
        'Touchscreen': [touchscreen],
        'IPS': [ips],
        'ppi': [ppi],
        'Cpu Brand': [cpu],
        'HDD': [hdd],
        'SSD': [ssd],
        'Gpu Brand': [gpu],
        'os': [os]
    })


    prediction = pipe.predict(query_df)[0]
    final_price = np.exp(prediction)
    st.subheader(f"💻 Estimated Laptop Price: ₹{int(round(final_price, 0)):,}")










