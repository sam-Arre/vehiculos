import streamlit as st
import pandas as pd
import plotly.express as px
car_data = pd.read_csv('vehicles_us.csv') 
st.header('Datos venta de coches')
hist_button = st.button('Construir histograma')
        
if hist_button: 
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
                   
    fig = px.histogram(car_data, x="odometer")
        
    st.plotly_chart(fig, use_container_width=True)

disp_button= st.button ('Construir dispersión')

if disp_button:
    st.write('Creación de gráfico de dispersión para el conjunto de datos de anuncio de venta de coches')
    fig_d = px.scatter(car_data, x='model_year', y="price")
    st.plotly_chart(fig_d, use_container_width=True)