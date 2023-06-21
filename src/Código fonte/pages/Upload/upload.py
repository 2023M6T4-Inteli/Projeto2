import streamlit as st
import pandas as pd
import plotly.express as px
import base64
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from io import BytesIO
from collections import Counter
import emoji




# Função para renderizar a barra lateral com os links para as seções da sua aplicação
def render_sidebar():
    st.sidebar.title("Seções")
    page = st.sidebar.radio("Navegue entre as seções", ["Upload do dataset", "Dashboard", "Chat-Btg", "Predição"])
    return page

# Função para ler o arquivo CSV 
def read_csv(upload_file):
    if upload_file is not None:
        df = pd.read_csv(upload_file)
        return df
    else:
        return None
    
# Renderiza a barra lateral
page = render_sidebar()

if page == "Upload do dataset":
    #Título Página
    st.title("Upload dos dados")
    st.subheader('Coloque o seu arquivo CSV para gerar os gráficos')
    # Variável para armazenar o arquivo CSV
    upload_file = st.file_uploader('Escolha o seu arquivo CSV', type='csv')

    # Condição para colocar na tela o arquivo CSV
    if upload_file:
        st.markdown('---')
        # Lê os dados do arquivo CSV e armazena em um cache persistente
        df = read_csv(upload_file)
        st.dataframe(df)
        # success
        st.success("Success")
        #Botão
        next_button = st.button("Próximo")
        if next_button:
            
