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

#baixar csv
def download_link(df, filename='predicoes.csv', link_text='Download CSV'):
    if df is not None:
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{link_text}</a>'
        return href
    else:
        return ""
    
# Renderiza a barra lateral
page = render_sidebar()

if page == "Predição":
    st.title("PREDIÇÃO")
    st.subheader("Faça a predição do seu arquivo CSV")
    #Instanciando arquivo para importação
    upload_file_2 = st.file_uploader('Escolha o seu arquivo CSV', type='csv')
    #botão para executar a função
    if upload_file_2:
        df_2 = pd.read_csv(upload_file_2)
        st.dataframe(df_2)
        
        pred_button = st.button(label='Predição')
        if pred_button:
            #Executar função de criar coluna com predição
            #Lembrar de mudar df_2 para o dataframe com a coluna de predição
            st.dataframe(df_2)
            #Baixar CSV 
            st.markdown(download_link(df_2), unsafe_allow_html= True)

            