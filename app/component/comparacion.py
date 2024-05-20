import streamlit as st
import seaborn as sns
import plotly.express as px


def compare_age_survived_by_sex(data):
    st.subheader('Comparación de Edad y Sobrevivencia por Sexo')

    # Contar el número de personas de cada sexo y si sobrevivieron para cada edad
    count_by_age_survived_sex = data.groupby(['Age', 'Survived', 'Sex']).size().reset_index(name='Count')

    # Filtrar para obtener solo los registros de personas que sobrevivieron
    survived_data = count_by_age_survived_sex[count_by_age_survived_sex['Survived'] == 1]

    # Crear el gráfico interactivo con plotly
    fig = px.line(survived_data, x='Age', y='Count', color='Sex',
                  labels={'Age': 'Edad', 'Count': 'Cantidad', 'Sex': 'Sexo'},
                  title='Comparación de Edad y Sobrevivencia por Sexo')

    # Configuración adicional del gráfico
    fig.update_layout(yaxis=dict(title='Cantidad'))

    st.plotly_chart(fig)

def compare_survival_by_class(data):
    st.subheader('Comparación de Supervivencia por Clase')

    # Crear el gráfico interactivo con plotly
    fig = px.histogram(data, x='Pclass', color='Survived',
                       labels={'Pclass': 'Clase', 'Survived': 'Supervivencia'},
                       title='Número de pasajeros por Clase y Estado de Supervivencia')

    # Configuración adicional del gráfico
    fig.update_layout(barmode='group')

    st.plotly_chart(fig)


def compare_age_by_survival(data):
    st.subheader('Comparación de Edad por Supervivencia segun Clase')

    # Widget de selección de clase
    pclass = st.selectbox('Selecciona la Clase:', [1, 2, 3])

    # Filtrar el DataFrame por la clase seleccionada
    filtered_data = data[data['Pclass'] == pclass]

    # Crear el gráfico interactivo con plotly
    fig = px.histogram(filtered_data, x='Age', color='Survived', barmode='overlay',
                       labels={'Age': 'Edad', 'Survived': 'Supervivencia'},
                       title=f'Distribución de Edad por Estado de Supervivencia en la Clase {pclass}',
                       marginal='rug',  # Muestra líneas en los márgenes para representar cada punto de datos
                       histnorm='density')  # Normaliza el histograma para que la suma de las áreas sea 1

    st.plotly_chart(fig)


def plot_comparisons(data):
    st.header('Comparaciones en el Dataset del Titanic')

    compare_age_survived_by_sex(data)

    compare_survival_by_class(data)

    compare_age_by_survival(data)


