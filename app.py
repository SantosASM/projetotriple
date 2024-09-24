import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar os dados
car_data = pd.read_csv(r"C:\Users\Santos\Documents\vehicles.csv", sep=",")
car_data = car_data.rename(columns={'model_year': 'year'})

# Botão para criar o histograma
hist_button = st.button('Criar histograma')

if hist_button:
    st.header("Histograma dos dados")
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    # Criar um histograma
    fig_hist = px.histogram(car_data, x="odometer")
    
    # Exibir o gráfico de histograma
    st.plotly_chart(fig_hist, use_container_width=True)

# Botão para criar o gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.header("Gráfico de Dispersão")
    st.write('Criando um gráfico de dispersão entre a idade do veículo e o preço')
    
    # Criar um gráfico de dispersão
    fig_scatter = px.scatter(car_data, x="year", y="price", color="condition", title="Dispersão: Ano do Veículo vs Preço")
    
    # Exibir o gráfico de dispersão
    st.plotly_chart(fig_scatter, use_container_width=True)
