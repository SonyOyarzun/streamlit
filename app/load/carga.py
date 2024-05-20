import streamlit as st
import pandas as pd
# Cargar los datos
@st.cache_data
def load_data():
    data = pd.read_csv('datos/MDAS-HVD_EVAL_1_Datos.csv')
    return data

