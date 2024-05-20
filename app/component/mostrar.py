import streamlit as st

def display_data(data):
    st.header('Datos del Titanic')
    st.write('Vista previa de los datos cargados:')
    st.dataframe(data.head())