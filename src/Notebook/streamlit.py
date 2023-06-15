import streamlit as st
import pandas as pd
import plotly.express as px
import base64
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from io import BytesIO

# Função para baixar csv
def generate_csv_download_link(df):
    towrite = BytesIO()
    df.to_csv(towrite, encoding="utf-8", index=False, header=True)
    towrite.seek(0)
    b64 = base64.b64encode(towrite.read()).decode()
    href = f'<a href="data:text/csv;base64,{b64}" download="data_download.csv">Download CSV File</a>'
    return st.markdown(href, unsafe_allow_html=True)

# Título da página
st.set_page_config(page_title='Chat-BTG')
# Título da seção
st.title('CSV Plotter')
st.subheader('Coloque o seu arquivo CSV')
# Variável para armazenar o arquivo CSV
upload_file = st.file_uploader('Escolha o seu arquivo CSV', type='csv')
# Condição para colocar na tela o arquivo CSV
if upload_file:
    st.markdown('---')
    df = pd.read_csv(upload_file)
    st.dataframe(df)

    # Select box para os gráficos que gostaria de analisar
    plot_select = st.selectbox(
        'O que você gostaria de analisar?',
        ('Porcentagem de Sentimento', 'Word Cloud', 'Número de Tokens por Sentimento', 'Emojis que mais aparecem')
    )

    # Mostrar gráfico correspondente à opção selecionada
    if plot_select == 'Porcentagem de Sentimento':
        st.write('Gráfico de Barras')
        # Porcentagens
        # Positivo
        total = len(df)
        positivo = len(df.query('sentimento == 1')) / total
        # Neutro
        neutro = len(df.query('sentimento == 0')) / total
        # Negativo
        negativo = len(df.query('sentimento == -1')) / total
        # Criar DataFrame para o gráfico de barras
        data = {
            'Sentimento': ['Positivo', 'Neutro', 'Negativo'],
            'Porcentagem': [positivo, neutro, negativo],
            'Cor': ['#008000', '#ffff00', '#ff0000']
        }
        df_plot = pd.DataFrame(data)
        # Plotar o gráfico de barras
        fig = px.bar(df_plot, x='Sentimento', y='Porcentagem', color='Cor')
        st.plotly_chart(fig)

    elif plot_select == 'Word Cloud':
        # Código para criar a nuvem de palavras
        st.write("Gráfico Word Cloud de Frases Positivas")
        # WordCloud das frases positivas
        # Pegando apenas as frases com label positiva
        pos = df.query('sentimento == 1')
        # Transformando em tokens
        tokens_pos = pos['texto_pre'].apply(lambda x: x.split())
        # Array para armazenar
        word_positive = []
        # Looping para salvar os tokens em um array
        for sentences in tokens_pos:
            for tokens in sentences:
                word_positive.append(tokens)
        # Concatenar tudo em uma string
        text_positive = ' '.join(word_positive)

        # Criar um objeto WordCloud
        wordcloud_positive = WordCloud(width=800, height=400, background_color="white").generate(text_positive)

        # Plotar a nuvem de palavras com Plotly Express
        fig_positive = px.imshow(wordcloud_positive.to_array())
        fig_positive.update_layout(
            showlegend=False, width=800, height=400, margin=dict(l=0, r=0, t=0, b=0),
            xaxis=dict(visible=False), yaxis=dict(visible=False)
        )
        st.plotly_chart(fig_positive)

        # Código para criar a nuvem de palavras
        st.write("Gráfico Word Cloud de Frases Negativas")
        # Filtrar o DataFrame pelo sentimento negativo
        neg = df.query('sentimento == -1')
        # Transformar as frases em tokens
        tokens_neg = neg['texto_pre'].apply(lambda x: x.split())
        # Lista para armazenar os tokens
        word_negative = []
        # Looping para salvar os tokens em uma lista
        for sentences in tokens_neg:
            for tokens in sentences:
                word_negative.append(tokens)
        # Concatenar tudo em uma string
        text_negative = ' '.join(word_negative)

        # Criar um objeto WordCloud com cor vermelha
        wordcloud_negative = WordCloud(
            width=800, height=400, background_color="white", colormap='Reds'
        ).generate(text_negative)

        # Plotar a nuvem de palavras com Plotly Express
        fig_negative = px.imshow(wordcloud_negative.to_array())
        fig_negative.update_layout(
            showlegend=False, width=800, height=400, margin=dict(l=0, r=0, t=0, b=0),
            xaxis=dict(visible=False), yaxis=dict(visible=False)
        )
        st.plotly_chart(fig_negative)

    elif plot_select == 'Número de Tokens por Sentimento':
        # Código para criar o gráfico de barras
        st.write("Gráfico KDE")

    elif plot_select == 'Emojis que mais aparecem':
        # Código para criar o gráfico de dispersão
        st.write("Gráfico de barra")
