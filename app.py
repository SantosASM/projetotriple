import os
import streamlit as st
import pandas as pd
import plotly.express as px

# Obter a porta da variável de ambiente fornecida pelo Render
port = int(os.environ.get("PORT", 8501))

# Carregar os dados
car_data = pd.read_csv("vehicles.csv", sep=",")

# Renomear a coluna 'model_year' para 'year'
car_data = car_data.rename(columns={'model_year': 'year'})

# Botão para mostrar amostra dos dados
sample_button = st.button('Mostrar amostra dos dados')

if sample_button:
    st.header("Amostra dos Dados")
    st.write(car_data.head())  # Exibe as 5 primeiras linhas do DataFrame

# Caixa de seleção para filtrar por condição do veículo
condition_options = car_data['condition'].unique()
selected_condition = st.selectbox("Selecione a condição do veículo", options=condition_options)

# Filtrar os dados pela condição selecionada
filtered_data = car_data[car_data['condition'] == selected_condition]

# Botão para criar o histograma
hist_button = st.button('Criar histograma')

if hist_button:
    st.header("Histograma dos dados")
    st.write(f'Criando um histograma para veículos na condição: {selected_condition}')
    
    # Criar um histograma
    fig_hist = px.histogram(filtered_data, x="odometer", title="Histograma: Hodômetro dos veículos")
    
    # Exibir o gráfico de histograma
    st.plotly_chart(fig_hist, use_container_width=True)

# Botão para criar o gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.header("Gráfico de Dispersão")
    st.write(f'Criando um gráfico de dispersão entre a idade do veículo e o preço para veículos na condição: {selected_condition}')
    
    # Criar um gráfico de dispersão
    fig_scatter = px.scatter(filtered_data, x="year", y="price", color="condition", title="Dispersão: Ano do Veículo vs Preço")
    
    # Exibir o gráfico de dispersão
    st.plotly_chart(fig_scatter, use_container_width=True)
