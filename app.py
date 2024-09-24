import os
import streamlit as st
import pandas as pd
import plotly.express as px

# Obter a porta da variável de ambiente fornecida pelo Render
port = int(os.environ.get("PORT", 8501))

# Carregar os dados
car_data = pd.read_csv("vehicles.csv", sep=",")

# Função para renomear todas as colunas
def rename_columns(df):
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace(':', '').str.replace('-', '_')
    return df

# Renomear todas as colunas
car_data = rename_columns(car_data)

# Botão para mostrar amostra dos dados renomeados
sample_button = st.button('Mostrar amostra dos dados renomeados')

if sample_button:
    st.header("Amostra dos Dados Renomeados")
    st.write(car_data.head())  # Exibe as 5 primeiras linhas do DataFrame

# Verificar se a coluna 'year' (ano) existe no DataFrame
if 'year' in car_data.columns:
    # Caixa de seleção para filtrar por ano do veículo
    year_options = car_data['year'].unique()
    selected_year = st.selectbox("Selecione o ano do veículo", options=year_options)

    # Filtrar os dados pelo ano selecionado
    filtered_data = car_data[car_data['year'] == selected_year]
    
    # Botão para criar o histograma
    hist_button = st.button('Criar histograma')

    if hist_button:
        st.header("Histograma dos dados")
        st.write(f'Criando um histograma para veículos do ano: {selected_year}')
        
        # Criar um histograma
        fig_hist = px.histogram(filtered_data, x="odometer", title=f"Histograma: Hodômetro dos veículos do ano {selected_year}")
        
        # Exibir o gráfico de histograma
        st.plotly_chart(fig_hist, use_container_width=True)

    # Botão para criar o gráfico de dispersão
    scatter_button = st.button('Criar gráfico de dispersão')

    if scatter_button:
        st.header("Gráfico de Dispersão")
        st.write(f'Criando um gráfico de dispersão entre a idade do veículo e o preço para veículos do ano: {selected_year}')
        
        # Criar um gráfico de dispersão
        fig_scatter = px.scatter(filtered_data, x="year", y="price", color="year", title=f"Dispersão: Ano do Veículo vs Preço ({selected_year})")
        
        # Exibir o gráfico de dispersão
        st.plotly_chart(fig_scatter, use_container_width=True)
else:
    st.error("A coluna 'year' não foi encontrada no arquivo CSV. Por favor, verifique o arquivo de dados.")
