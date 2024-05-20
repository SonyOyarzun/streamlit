import streamlit as st
import plotly.express as px
import pandas as pd

def explore_sex_distribution(data):
    # Explorar la composición por género
    st.subheader('Composición por Género')

    # Calcular la distribución de pasajeros por sexo
    gender_distribution = data['Sex'].value_counts().reset_index()
    gender_distribution.columns = ['Sexo', 'Cantidad']

    # Gráfico de barras
    fig1 = px.bar(gender_distribution, x='Sexo', y='Cantidad',
                  labels={'Cantidad': 'Cantidad de Pasajeros', 'Sexo': 'Sexo'},
                  title='Distribución de Pasajeros por Sexo')

    # Gráfico de pastel
    fig2 = px.pie(gender_distribution, values='Cantidad', names='Sexo',
                  title='Composición de Género', hole=0.3)

    # Mostrar los gráficos
    st.plotly_chart(fig1)
    st.plotly_chart(fig2)

def explore_class_distribution(data):
    # Explorar la composición por clase
    st.subheader('Composición por Clase')

    # Calcular la distribución de pasajeros por clase
    class_distribution = data['Pclass'].value_counts().reset_index()
    class_distribution.columns = ['Clase', 'Cantidad']

    # Gráfico de barras
    fig1 = px.bar(class_distribution, x='Clase', y='Cantidad',
                  labels={'Cantidad': 'Cantidad de Pasajeros', 'Clase': 'Clase'},
                  title='Distribución de Pasajeros por Clase')

    # Gráfico de pastel
    fig2 = px.pie(class_distribution, values='Cantidad', names='Clase',
                  title='Composición por Clase', hole=0.3)

    # Mostrar los gráficos
    st.plotly_chart(fig1)
    st.plotly_chart(fig2)

def explore_survival_distribution(data):
    # Explorar la composición por supervivencia
    st.subheader('Composición por Supervivencia')

    # Calcular la distribución de pasajeros por supervivencia
    survival_distribution = data['Survived'].value_counts().reset_index()
    survival_distribution.columns = ['Supervivencia', 'Cantidad']

    # Gráfico de barras
    fig1 = px.bar(survival_distribution, x='Supervivencia', y='Cantidad',
                  labels={'Cantidad': 'Cantidad de Pasajeros', 'Supervivencia': 'Supervivencia'},
                  title='Distribución de Pasajeros por Supervivencia')

    # Gráfico de pastel
    fig2 = px.pie(survival_distribution, values='Cantidad', names='Supervivencia',
                  title='Composición por Supervivencia', hole=0.3)

    # Mostrar los gráficos
    st.plotly_chart(fig1)
    st.plotly_chart(fig2)

def plot_composition(data):
    st.header('Exploración de Composición en el Dataset del Titanic')

    explore_sex_distribution(data)

    explore_class_distribution(data)

    explore_survival_distribution(data)

