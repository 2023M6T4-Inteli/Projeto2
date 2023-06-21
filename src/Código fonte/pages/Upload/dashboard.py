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
    
#Função para gerar gráfico de porcentagem de sentimento e histograma
#df = dataframe
#sentimento = coluna de sentimento
def percentage_hist_sentiment(df, sentimento):
    st.write('Gráfico de Pizza e Histograma')
    # Porcentagens
    # Positivo
    total = len(df)
    positivo = len(df.query(f'{sentimento} == 1')) / total
    # Neutro
    neutro = len(df.query(f'{sentimento} == 0')) / total
    # Negativo
    negativo = len(df.query(f'{sentimento} == -1')) / total
    # Criar DataFrame para o gráfico de barras
    # Plotar o gráfico de barras
    fig = px.pie(df, values=[positivo, neutro, negativo], names=['Positivo', 'Neutro', 'Negativo'])
    st.plotly_chart(fig)
    #Histograma
    labels = df[sentimento].map({1 :'Positivo', 0: 'Neutro', -1: 'Negativo'})
    fig_hist = px.histogram(df, labels)
    st.plotly_chart(fig_hist)

#Gráfico word cloud positivo
def word_cloud_positive(df, sentimento):
    st.write(f"Gráfico Word Cloud de Frases {sentimento.capitalize()}s")
    # Pegando apenas as frases com o sentimento correspondente
    filtered_df = df.query(f'{sentimento} == 1')
    # Transformando em tokens
    tokens = filtered_df['texto_pre'].apply(lambda x: x.split())
    # Array para armazenar
    words = []
    # Looping para salvar os tokens em um array
    for sentences in tokens:
        for token in sentences:
            words.append(token)
    # Concatenar tudo em uma string
    text = ' '.join(words)

    # Criar um objeto WordCloud
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

    # Plotar a nuvem de palavras com Plotly Express
    fig = px.imshow(wordcloud.to_array())
    fig.update_layout(
        showlegend=False, width=800, height=400, margin=dict(l=0, r=0, t=0, b=0),
        xaxis=dict(visible=False), yaxis=dict(visible=False)
    )
    st.plotly_chart(fig)
    
#Gráfico word cloud negativo
def word_cloud_negative(df, sentimento):
    st.write(f"Gráfico Word Cloud de Frases {sentimento.capitalize()}s")
    # Pegando apenas as frases com o sentimento correspondente
    filtered_df = df.query(f'{sentimento} == -1')
    # Transformando em tokens
    tokens = filtered_df['texto_pre'].apply(lambda x: x.split())
    # Array para armazenar
    words = []
    # Looping para salvar os tokens em um array
    for sentences in tokens:
        for token in sentences:
            words.append(token)
    # Concatenar tudo em uma string
    text = ' '.join(words)

    # Criar um objeto WordCloud
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

    # Plotar a nuvem de palavras com Plotly Express
    fig = px.imshow(wordcloud.to_array())
    fig.update_layout(
        showlegend=False, width=800, height=400, margin=dict(l=0, r=0, t=0, b=0),
        xaxis=dict(visible=False), yaxis=dict(visible=False)
    )
    st.plotly_chart(fig)



def count_emojis(df, text):
    texto = "".join(df[text]).lower()
    count = emoji.emoji_count(texto) # Contar a quantidade de emojis 
    emoji_dict = dict(Counter(c for c in texto if emoji.is_emoji(c))) # Contagem de emojis do dicionario

    most_common_emojis = Counter(emoji_dict).most_common(15) # Top 15 emojis mais utilizados nos comentários

    total_emojis = sum(emoji_dict.values()) # Cálculo da porcentagem de aparição de cada emoji
    emoji_percentages = {k: v / total_emojis for k, v in most_common_emojis}

    df = pd.DataFrame({'emoji': list(emoji_percentages.keys()), 'percentage': list(emoji_percentages.values())}) # Dataframe dos resultados

    df = df.sort_values(by='percentage', ascending=False)# Ordena os resultados por porcentagem decrescente
    
    # Criar o gráfico de barras
    fig = px.bar(df, x='emoji', y='percentage', labels={'emoji': 'Emoji', 'percentage': 'Porcentagem'})

    # Exibir o gráfico
    st.plotly_chart(fig)

# NOVOS GRÁFICOS

# Extração de palavras que mais aparecem (gráfico de frequência)
def scatter_plot():

    # Transformando em tokens
    tokens = df['texto_pre'].astype(str).apply(lambda x: x.split())
    # Array para armazenar
    words = []
    # Looping para salvar os tokens em um array
    for sentences in tokens:
        for token in sentences:
            words.append(token)
    # Concatenar em uma string
    text = ' '.join(words)

    word_counts = Counter(text.split())
    top_words = word_counts.most_common(10)
    x = range(len(top_words))
    y = [count for word, count in top_words]

    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_xlabel('Palavras')
    ax.set_ylabel('Frequência')
    ax.set_title('Gráfico de Dispersão de Palavras')

    # Adicionar rótulos das palavras
    for i, (word, count) in enumerate(top_words):
        ax.annotate(word, (x[i], y[i]))

    st.pyplot(fig)

# Barra de pesquisa
def search_bar():
    text_search = st.text_input("Pesquise palavras relacionas à campanha", value="")
    m1 = df["texto_pre"].str.contains(text_search)
    m2 = df["sentimento"].str.contains(text_search)
    df_search = df[m1 | m2]

# Renderiza a barra lateral
page = render_sidebar()

  # Mostra a página correspondente à opção selecionada na barra lateral
if page == "Dashboard":
    upload_file = st.file_uploader('Escolha o seu arquivo CSV', type='csv')
    df = read_csv(upload_file)
      
    #Título Página
    st.title("DASHBOARD")
    
    # Select box para os gráficos que gostaria de analisar
    plot_select = st.selectbox(
            'O que você gostaria de analisar?',
            ('Porcentagem de Sentimento', 'Word Cloud', 'Número de Tokens por Sentimento', 'Emojis que mais aparecem', 'Frequência das palavras')
        )

        # Mostrar gráfico correspondente à opção selecionada
    if plot_select == 'Porcentagem de Sentimento':
        
        percentage_hist_sentiment(df, 'sentimento')

    elif plot_select == 'Word Cloud':
            #word cloud positiva
            word_cloud_positive(df, 'sentimento')
            #word cloud negative
            word_cloud_negative(df, 'sentimento')

    elif plot_select == 'Número de Tokens por Sentimento':
            # Código para criar o gráfico de barras
            st.write("Gráfico KDE")

    elif plot_select == 'Emojis que mais aparecem':
            # Código para criar o gráfico de dispersão
            st.write("Gráfico de barra")

            count_emojis(df, 'texto')
        
    elif plot_select == 'Frequência das palavras':
            # Código para criar o gráfico de dispersão
            st.write("dispersão")
            scatter_plot()

    if search_bar():
     st.write('yep')
       