import os
import streamlit as st
import pandas as pd
import plotly.express as px

# Obter a porta da variável de ambiente fornecida pelo Render
port = int(os.environ.get("PORT", 8501))

# Carregar os dados
car_data = pd.read_csv("vehicles.csv", sep=",")

# Botão para criar o histograma
hist_button = st.button('Criar histograma')

if hist_button:
    st.header("Histograma dos dados")
    
    # Criar um histograma
    fig_hist = px.histogram(car_data, x="odometer", title="Histograma: Hodômetro dos veículos")
    
    # Exibir o gráfico de histograma
    st.plotly_chart(fig_hist, use_container_width=True)

# Botão para criar o gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.header("Gráfico de Dispersão")
    
    # Criar um gráfico de dispersão
    fig_scatter = px.scatter(car_data, x="year", y="price", color="year", title="Dispersão: Ano do Veículo vs Preço")
    
    # Exibir o gráfico de dispersão
    st.plotly_chart(fig_scatter, use_container_width=True)
