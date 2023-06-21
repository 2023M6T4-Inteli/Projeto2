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

# Renderiza a barra lateral
page = render_sidebar()


if page == "Chat-Btg":
    # Título da página
    st.title('CHAT-BTG')
    st.subheader('Teste o modelo de predição')
    
    with st.form(key='nlpForm'):
        raw_text = st.text_area("Coloque seu texto aqui")
        submit_button = st.form_submit_button(label='Analyze')