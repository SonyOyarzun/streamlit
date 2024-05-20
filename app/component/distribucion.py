import streamlit as st
import plotly.express as px
import pandas as pd
import altair as alt

def distribution_age(data):
    # Distribución de la Edad
    st.subheader('Distribución de la Edad')

    # Filtro por género con identificador único
    gender_filter = st.radio("Filtrar por género (edad)", ["Todos", "Masculino", "Femenino"], key="age_gender_filter")

    if gender_filter == "Todos":
        filtered_data = data
    elif gender_filter == "Masculino":
        filtered_data = data[data["Sex"] == "male"]
    else:
        filtered_data = data[data["Sex"] == "female"]

    # Gráfico interactivo con Plotly Express
    fig = px.box(filtered_data, y='Age', title='Distribución de la Edad')
    st.plotly_chart(fig)

def distribution_fare(data):
    # Distribución de la Tarifa
    st.subheader('Distribución de la Tarifa')

    # Filtro por género con identificador único
    gender_filter = st.radio("Filtrar por género (tarifa)", ["Todos", "Masculino", "Femenino"], key="fare_gender_filter")

    if gender_filter == "Todos":
        filtered_data = data
    elif gender_filter == "Masculino":
        filtered_data = data[data["Sex"] == "male"]
    else:
        filtered_data = data[data["Sex"] == "female"]

    # Gráfico interactivo con Plotly Express
    fig = px.histogram(filtered_data, x='Fare', title='Distribución de Tarifa', nbins=30)
    st.plotly_chart(fig)

def distribution_survived(data):
    # Distribución de la Supervivencia
    st.subheader('Distribución de la Supervivencia')

    # Filtro por género con identificador único
    gender_filter = st.radio("Filtrar por género (tarifa)", ["Todos", "Masculino", "Femenino"], key="survived_gender_filter")

    if gender_filter == "Todos":
        filtered_data = data
    elif gender_filter == "Masculino":
        filtered_data = data[data["Sex"] == "male"]
    else:
        filtered_data = data[data["Sex"] == "female"]

    # Crear el boxplot interactivo
    boxplot = alt.Chart(filtered_data).mark_boxplot().encode(
        x="Survived:O",
        y="Age:Q",
        color="Sex:N"
    ).properties(
        width=500,
        height=300
    )

    # Mostrar el boxplot
    st.altair_chart(boxplot, use_container_width=True)

def plot_distributions(data):
    st.header('Distribuciones en el Dataset del Titanic')

    distribution_age(data)

    distribution_fare(data)

    distribution_survived(data)
