import streamlit as st
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def plot_heatmap(data):
    st.subheader('Mapa de Calor de Variables Numéricas')

    numeric_columns = data.select_dtypes(include=['int', 'float']).columns.tolist()

    # Calcular la matriz de correlación
    correlation_matrix = data[numeric_columns].corr()

    # Crear el mapa de calor interactivo con plotly
    fig = px.imshow(correlation_matrix, color_continuous_scale='Viridis',
                     labels=dict(x='Variables', y='Variables', color='Correlación'),
                     title='Mapa de Calor de Correlación')

    # Agregar los valores de correlación en cada celda del mapa de calor
    fig.update_traces(hovertemplate='Correlación: %{z:.2f}')

    st.plotly_chart(fig)

    
    

def plot_relationships_age_fare(data):
    st.subheader('Relación entre Edad y Tarifa pagada')

    # Ajustar el estilo del gráfico
    fig = px.scatter(data, x='Age', y='Fare',
                     title='Edad vs Tarifa pagada',
                     labels={'Age': 'Edad', 'Fare': 'Tarifa'})

    # Personalizar el eje y para mejorar la visibilidad de las etiquetas
    fig.update_yaxes(tickvals=[0, 50, 100, 150, 200, 250, 300], tickformat='$,.2f')

    # Personalizar los colores
    fig.update_traces(marker=dict(size=8, opacity=0.8),
                      marker_line=dict(width=1, color='DarkSlateGrey'))

    st.plotly_chart(fig)
    
    

def plot_gender_by_age(data):
    st.subheader('Cantidad de Mujeres y Hombres por Edad')

    # Calcular la cantidad de mujeres y hombres por edad
    gender_by_age = data.groupby(['Age', 'Sex']).size().unstack(fill_value=0).reset_index()

    # Crear el gráfico interactivo con Plotly
    fig = px.line(gender_by_age, x='Age', y=['female', 'male'],
                  labels={'value': 'Cantidad', 'variable': 'Género', 'Age': 'Edad'},
                  title='Cantidad de Mujeres y Hombres por Edad')

    st.plotly_chart(fig)




def plot_relationships(data):
    st.header('Visualización de Relaciones en el Titanic Dataset')
    
    plot_heatmap(data)

    plot_relationships_age_fare(data)
    
    plot_gender_by_age(data)









