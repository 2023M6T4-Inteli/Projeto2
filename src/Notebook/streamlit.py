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
    page = st.sidebar.radio("Navegue entre as seções", ["Dashboards", "Chat-Btg", "Predição"])
    return page

# Função para ler o arquivo CSV 
def read_csv(upload_file):
    df = pd.read_csv(upload_file)
    
    return df
#baixar csv
def download_link(df, filename='predicoes.csv', link_text='Download CSV'):
    """Gera um hyperlink para baixar um DataFrame em formato CSV"""
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{link_text}</a>'
    return href


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


    
# Renderiza a barra lateral
page = render_sidebar()

# Mostra a página correspondente à opção selecionada na barra lateral
if page == "Dashboards":
    #Título Página
    st.title("DASHBOARDS")
    st.subheader('Coloque o seu arquivo CSV para gerar os gráficos')
    # Variável para armazenar o arquivo CSV
    upload_file = st.file_uploader('Escolha o seu arquivo CSV', type='csv')
    # Condição para colocar na tela o arquivo CSV
    if upload_file:
        st.markdown('---')
        # Lê os dados do arquivo CSV e armazena em um cache persistente
        df = read_csv(upload_file)
        st.dataframe(df)

        # Select box para os gráficos que gostaria de analisar
        plot_select = st.selectbox(
            'O que você gostaria de analisar?',
            ('Porcentagem de Sentimento', 'Word Cloud', 'Número de Tokens por Sentimento', 'Emojis que mais aparecem')
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

elif page == "Chat-Btg":
    # Título da página
    st.title('CHAT-BTG')
    st.subheader('Teste o modelo de predição')
    
    with st.form(key='nlpForm'):
        raw_text = st.text_area("Coloque seu texto aqui")
        submit_button = st.form_submit_button(label='Analyze')


elif page == "Predição":
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

            
