import streamlit as st
# Configurando a barra lateral
st.sidebar.title("Menu")
secao = st.sidebar.radio("Seção", ("Dashboard", "Modelo", "Tabela"))

if secao == "Dashboard":
    st.title("Dashboard")
    # Adicione o código para criar o dashboard aqui
    
    
if secao == "Modelo":
    st.title("Modelo")
    # Adicione o código para o modelo aqui


if secao == "Tabela":
    st.title("Tabela")
    # Adicione o código para exibir a tabela CSV aqui


if __name__ == '__main__':
    st.set_page_config(page_title='Meu Aplicativo', layout='wide')
    app()


