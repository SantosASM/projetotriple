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
