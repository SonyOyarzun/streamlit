import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#carga de datos
from app.load.carga import load_data
from app.component.mostrar import display_data

#visualizaciones
from app.component.relaciones import plot_relationships
from app.component.comparacion import plot_comparisons
from app.component.composicion import plot_composition
from app.component.distribucion import plot_distributions


data = load_data()

logo ="https://assets.isu.pub/document-structure/230227151116-4673fcc5b4922b04cd2d36c66d5ace91/v1/b75dc761fb79305a7dce64a1673bf113.jpeg"


def main_mod():
    # Título de la aplicación
    st.title('Análisis del conjunto de datos del Titanic')

    # Descripción en el menú principal
    st.markdown("""
    Esta aplicación permite explorar el conjunto de datos del Titanic y visualizar diferentes análisis
    interactivos según varios propósitos:

    1. **Ver Relaciones**: Observa las relaciones entre diferentes variables.
    2. **Ver Comparaciones**: Compara diferentes grupos de datos.
    3. **Ver Composiciones**: Examina la composición de diferentes categorías.
    4. **Ver Distribuciones**: Visualiza las distribuciones de las variables.

    Utiliza las pestañas laterales para navegar por los diferentes tipos de análisis.
    """)

 # Título de la aplicación con logo
    st.sidebar.markdown("""
     <style>
        /* Estilo para el contenedor del logo */
        .logo-button {
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 10px;
            border: 2px solid #000; /* Puedes cambiar el color del borde */
            border-radius: 10px; /* Bordes redondeados */
            background-color: #f0f0f0; /* Color de fondo */
            text-decoration: none; /* Quitar subrayado de los enlaces */
            transition: background-color 0.3s, border-color 0.3s;
        }

        .logo-button:hover {
            background-color: #e0e0e0; /* Color de fondo al pasar el ratón */
            border-color: #666; /* Color del borde al pasar el ratón */
        }

        /* Estilo para la imagen del logo */
        .logo-img {
            max-width: 100%;
            height: auto;
        }
    </style>
    """, unsafe_allow_html=True)

    # Título de la aplicación con logo
    st.sidebar.markdown(f"""
    <a class="logo-button" href="/">
    <img src={logo} alt="Logo" class="logo-img">
    </a>
    """, unsafe_allow_html=True)

    # Sidebar: Opciones de visualización
    st.sidebar.title('Opciones de Visualización')
    st.sidebar.write('Seleccione el gráfico que desea visualizar')
    visualization = st.sidebar.selectbox('Tipo de gráfico:', ['Seleccione una opción', 'Relación', 'Comparación', 'Composición', 'Distribución'], index=0)

    #opciones modulares
    if visualization == 'Seleccione una opción':
        display_data(data)

    if visualization == 'Relación':
        plot_relationships(data)

    if visualization == 'Comparación':
        plot_comparisons(data)

    if visualization == 'Composición':
        plot_composition(data)

    if visualization == 'Distribución':
        plot_distributions(data)