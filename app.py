import pandas as pd
import plotly.express as px
import streamlit as st

# Título do seu site
st.header('Dashboard de Vendas de Veículos')

# Lendo os dados (usando o nome correto que descobrimos)
car_data = pd.read_csv('vehicles.csv') 

# Criando o primeiro botão
hist_button = st.button('Criar histograma')

if hist_button: # se o botão for clicado
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")
    
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# Criando o segundo botão (Extra para o seu projeto ficar completo)
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Exibindo a relação entre preço e quilometragem')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)