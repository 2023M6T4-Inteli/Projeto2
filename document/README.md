# Documento Principal do Projeto

<!-- Descrição sucinta do projeto, com descrição do problema, do objetivo e da solução em linhas gerais. -->

Diante do que foi apresentado como objetivo, o principal problema ou necessidade de negócio identificado pelo Banco BTG Pactual é compreender as opiniões, sentimentos e necessidades dos clientes expressos nas redes sociais, em especial, para fins de prova de conceito, na plataforma Instagram. O banco reconhece o impacto das redes sociais em seus processos e entende que ouvir seus clientes é fundamental para aprimorar seus produtos, serviços e a percepção geral da instituição.

Dessa forma, o BTG Pactual identificou a necessidade de implementar algum tipo de serviço que realizasse a classificação de acordo com o sentimento nos comentários. Neste sentido, pretendemos entregar um modelo de análise de sentimentos que faça a detecção de palavras-chave nos comentários das redes sociais, utilizando o Processamento de Linguagem Natural (PLN). 

Este projeto visa suprir a necessidade de entender o cliente, o que ele deseja e o que não deseja em relação ao banco e suas campanhas. A análise de sentimento permite ao banco compreender melhor o cliente, adaptando-se e oferecendo uma experiência cada vez mais satisfatória.

## (Sprint 1) Entendimento do Negócio

 ### 📈 Matriz de avaliação de valor Oceano Azul 

A Matriz Oceano Azul é a ferramenta que ajuda as empresas à identificar novas oportunidades de crescimento dentro do mercado e quais fatores às diferenciam da concorrência, criando valor para seus clientes.

Para esta análise, foram setadas outras Inteligências Artificiais, baseadas em Processamento de Linguagem Natural (PLN), como **Open AI, Amazon Comprehend, Microsoft Azure Cognitive Services, Google Cloud Natural Language, IBM Watson.** 

A OpenAI é uma plataforma de inteligência artificial que oferece uma ampla gama de ferramentas e recursos para empresas e indivíduos. A plataforma utiliza modelos de linguagem natural avançados, como o GPT-3, para criar soluções personalizadas para problemas específicos de negócios.
A Amazon Comprehend é um serviço de análise de texto fornecido pela AWS que permite a identificação de insights e informações úteis a partir de dados textuais, em grande escala. A tecnologia usa técnicas de aprendizado de máquina para extrair informações úteis a partir de dados textuais, como sentimentos, emoções, tópicos, entidades, relações e muito mais. O serviço é capaz de analisar grandes quantidades de texto, em várias línguas, e produzir informações significativas para apoiar a tomada de decisões de negócios, como por exemplo conjuntos de dados de texto, incluindo documentos, mensagens de texto, posts de redes sociais e outras formas de comunicação escrita, para identificar tendências.

O Microsoft Azure Cognitive Services é um conjunto de serviços cognitivos com alocação em nuvem que permite que desenvolvedores agreguem recursos de inteligência artificial (IA) a seus aplicativos sem a necessidade de experiência em aprendizado de máquina ou análise de dados. Esses serviços são construídos com base em algoritmos de aprendizado de máquina, visão computacional, reconhecimento de fala, processamento de linguagem natural e outras tecnologias. Consequentemente, os serviços cognitivos da Azure são altamente escaláveis e personalizáveis, permitindo que as empresas criem aplicativos sob medida para suas necessidades específicas, como por exemplo para realizar tarefas como reconhecimento de voz, análise de sentimentos, detecção de imagens, tradução de idiomas e muito mais. Além disso, os serviços podem ser facilmente integrados a outras tecnologias da Microsoft, como o Microsoft Power BI, Microsoft Dynamics 365 e Microsoft Office 365.

A Google Cloud Natural Language é uma ferramenta de processamento de linguagem natural (PLN) criada pela Google que permite aos usuários extrair informações valiosas a partir de textos não estruturado, incluindo e-mails, documentos, artigos e outras fontes de dados. Com a técnica de aprendizado de máquina e processamento de linguagem natural, a Google Cloud Natural Language pode identificar entidades ou indivíduos mencionados em um texto, como nomes de pessoas, locais, organizações e datas, além de extrair sentimentos e emoções expressos pelo autor. Além disso, há possibilidade de agregação com o Google Cloud Natural Language, que permite as empresas analisarem grandes volumes de dados para obter insights úteis que podem ajudar a orientar decisões importantes de negócios.

O IBM Watson é um sistema de PLN, desenvolvido pela IBM. A ferramenta utiliza da análise de dados e aprendizado de máquina para processar informações e fornecer insights relevantes para seus usuários. O mesmo é utilizado em vários setores, incluindo saúde, finanças, educação, manufatura.
O IBM Watson é uma plataforma de computação cognitiva e inteligência artificial desenvolvida pela empresa americana IBM. Ele utiliza tecnologias avançadas de processamento de linguagem natural, machine learning, análise de dados e outras técnicas de inteligência artificial para fornecer insights e soluções para uma ampla variedade de aplicações.

**Eliminar → Assertividade, Escalabilidade, Robustez, confiabilidade, adaptabilidade, Assertividade, Tecnologia**

A ação de eliminar, dentro da Matriz Oceano Azul, está relacionada à enumeração de fatores que podem ser retirados ou melhorados, ao analisar os atributos do negócio. Portanto, analisa-se a distribuição da ferramentas, em temos de escalabilidade, assertividade, acessibilidade, robustez e outras seções atribuídos à proposta do Chat-BTG, em comparação à outras soluções que utilizam Processamento de Linguagem Natural. Dado que a projeto consiste no desenvolvimento de um MVP, atualmente, o chat-BTG é uma iniciativa sem afunilamento em sua complexidade, por isso, sua escalabilidade é um fator a ser pensado nos próximos passos do projeto, principalmente com ênfase na robustez e maior assertividade da tecnologia.
Já os outros modelos, por já estarem no mercado e ter uma infraestrutura posicionada, tendo em vista que serviços de cloud e outros “web services” fornecem agregação em tempo real, com dados estruturados e já disponibilizados no próprio serviço, conseguem maior escalabilidade e confiabilidade, conforme as tecnologias e funcionalidades contidas em seus serviços.

**Aumentar →  Personalização**

A personalização, nessa análise, é um fator de destaque no mercado, em comparação aos concorrentes. Destaca-se que o modelo de Processamento de Linguagem Natural é desenvolvido conforme a base de dados fornecido pelo cliente, voltado aos comentários feitos nos posts da conta BTG Pactual no Instagram.
Ressalta-se que a visualização dos dados também será pensada afim de facilitar o processo de tomada das decisões nos times de marketing e produto, como vantagem competitiva do banco.

**Criar → Custo do Setup**

Com a visão de ampliar, agregar e integrar diversas ferramentas, pode-se citar alguns fatores determinantes na análise financeira para o escopo do projeto. Neste sentido, é importante ressaltar que o projeto “Chat-BTG” ainda é limitado ao escopo mínimo de requisitos de uma rede social específica, dentro de dados levantados a partir de uma base de dados pré-definida, sem atualização em tempo real. Consequentemente, a níveis de complexidade baixos, possuímos um custo muito interessante com base no benchmark do mercado. Sendo uma solução nativa, o custo de setup da solução é muito baixo, e outros custos de “web services” são mitigados com o processo interno realizado.
<img src = "https://github.com/2023M6T4-Inteli/Projeto2/blob/main/assets/Imagens/Oceano_azul.png">

### ⚠️ Matriz de riscos

A Matriz de Riscos consiste em uma ferramenta de gestão de riscos e oportunidades, a fim de identificar, avaliar e priorizar os fatores associados ao projeto, por grau de impacto e probabilidade de ocorrência.
<img src = "https://github.com/2023M6T4-Inteli/Projeto2/blob/main/docs/Imagens/Matriz%20de%20Risco.png">

Por tanto, entende-se então, que o desenvolvimento de um Plano de Ação é de indubitável importância, dado que, o documento descreve as atividades que precisam ser realizadas para mitigar riscos e alcançar objetivos estipulados. O Plano define o que será feito, quem fará, como, quando e com quais recursos. <br>
No que diz respeito aos riscos evidenciados na Matriz acima, ressalta-se o plano de ação desenvolvido:

**Ameaça 01:** Thainá - Identificar quais são as expectativas do cliente e manter o foco nelas durante a produção do modelo, além de revisar o modelo após cada mudança, comparando-o com as expectativas definidas para o projeto.

**Ameaça 02:**  Vinicius - Identificar as causas da falha, e implementar medidas de solução monitorar os testes no tratamento dos dados. Revisar a metodologia de pré-processamento de dados.

**Ameaça 03:** Kathy e Lucas -  Verificar por quais possíveis motivos existe um erro na coleta das palavras chaves, e indentificar pradões de possíveis palavras que estejam causando esses erros, buscando informações em relação a campanha de marketing. Além disso, caso o problema não for na coleta das palavras, ajustariamos o algoritmo e procurariamos possíveis falhas e tentariamos treinar o modelo  om mais dados e exemplos para melhorar a precisão, realizando testes regulares. 

**Ameaça 04:** Henri e Rodrigo -  Avaliar se a métrica de classificação dos comentários é suficientemente complexa para a correta classificação dos comentários, conferir com testes se não há algum caso que produza resultados incorretos/indesejados.

**Ameaça 05:** João - Aplicar o 'word embedding' após a realização de testes, definindo as adaptações necessárias, validando-as constantemente e utilizando diferentes frases para testar a identificação de contexto no modelo.

### 💊 Canvas Proposta de Valor

O Canvas Proposta de Valor é uma ferramenta de negócios que auxilia no entendimento e criação do posicionamento do projeto (como um produtos que será desenvolvido), com base na criação de ganho que o cliente realmente valoriza e precisa. 

<img src = "https://github.com/2023M6T4-Inteli/Projeto2/blob/main/assets/Imagens/Proposta_Valor.png">

### 💵 Análise Financeira

A análise financeira corresponde à uma avaliação dos aspectos econômicos e financeiros que permeiam o projeto, com o objetivo de estimar a viabilidade e escalabilidade do mesmo.

Conforme o site de notícias Reuters, o BTG Pactual (BTG Pactual S.A.) é um banco de investimentos brasileiro especializado em capital de investimento e capital de risco. O BTG se configura como uma empresa de capital aberto com cerca de 200 sócios (constituído por funcionários internos). Mesmo sua sede sendo no Rio de Janeiro, Brasil, sua atuação ocorre em escala global, alcançando EUA, Chile, México, Reino Unido, Portugal, Argentina, Colômbia e Peru. Além das já citadas, o banco atua em áreas como ‘Corporate Lending (Empréstimos e Financiamentos)’, Sales and Trading, Asset Management, Wealth Management e Ativos Florestais. Apesar da queda das receitas anuais totais (de 2022 para 2023) e também das ações nos últimos 6 meses, o banco BTG continua sendo uma das empresas mais relevantes e consolidadas do Brasil.

Custos em relação ao projeto: Os custos estimados pelo cliente foram de R$250.000. Não foram informadas projeções de receita pelo cliente (projeto interno).

Em paralelo, foi feito uma projeção dos custos do projeto, contabilizando os gastos com funcionários e serviços de infraestrutura da AWS, tendo como média o valor de R$ 167.784.



**Profissionais Necessários Para o Desenvolvimento da Solução:**

- Engenheiro em Machine Learning
- Desenvolver de Software
- Cientista de Dados
- Opcional (Incomum no Brasil): Especialista em linguística Computacional

Salário Médio para Engenheiro em Machine Learning: R$ 8.900 /mês (Glassdoor) <br>
Salário Médio para Desenvolver Pleno: R$ 10.200 /mês (Glassdoor) <br>
Salário Médio para Cientista de Dados: R$ 8.710 /mês (Glassdoor)<br>
 
Gasto Mensal com os três profissionais: R$ 27.810<br>
Gasto em dois meses: R$ 55.620<br>
Gasto em três meses: R$ 83.430<br>

**Custos da infraestrutura em AWS:**
<br>
<br>

 Sem o Amazon Comprehend: 

- Custo Inicial - R$12.312,18<br>
- Custo Mensal - R$34.341,58<br>

- Gastos em dois meses: R$ 80.995,34<br>
- Gastos em três meses: R$ 115.336,92<br>

<br>
<br>
Com o Amazon Comprehend: 

- Custo Inicial - R$12.312,18 <br>
- Custo Mensal - R$34.404,18 <br>

- Gastos em dois meses: R$ 81.120,54 <br>
- Gastos em três meses: R$ 115.524,72 <br>

**Contabilização total:**

Considerando os custos dos funcionários, somado ao da AWS, o valor do projeto pode variar entre R$136.615 e R$ 198.954, com uma média de R$ 167.784.  


## (Sprint 1) Entendimento da Experiência do Usuário

### 👩 Persona

A Persona é a representação fictícia do cliente ideal para o projeto, com o objetivo de compreender os seus comportamentos e necessidades. Nesse momento, entende-se que as personas configuram-se em representantes dos times de marketing, produto e automações.

<img src = "https://github.com/2023M6T4-Inteli/Projeto2/blob/dev-jo%C3%A3o/assets/Imagens/Persona%20-%20Juliano.png" alt="persona juliano" width="600" height="auto" >
<img src = "https://github.com/2023M6T4-Inteli/Projeto2/blob/dev-jo%C3%A3o/assets/Imagens/Persona%20-%20Renata.png"  alt="persona renato" width="600" height="auto">
<img src = "https://github.com/2023M6T4-Inteli/Projeto2/blob/dev-jo%C3%A3o/assets/Imagens/Persona%20-%20Thiago.png"  alt="persona thiago" width="600" height="auto">

### 📄 User Stories

A User Stories são representações simples e clara dos requisitos e funcionalidades de um software, escritas do ponto de vista do usuário final. Essas histórias ajudam a manter o foco nas necessidades dos usuários e a priorizar as funcionalidades mais importantes para o projeto. Portanto, a seguir, existem duas User Story por persona (Marketing, Produto e Automações)

<img src = "https://github.com/2023M6T4-Inteli/Projeto2/blob/dev-jo%C3%A3o/assets/Imagens/user_storie_01.png" alt="user storie 1" width="400" height="auto">
<br>
<img src = "https://github.com/2023M6T4-Inteli/Projeto2/blob/dev-jo%C3%A3o/assets/Imagens/user_storie_02.png" alt="user storie 2" width="400" height="auto">
<br>
<img src = "https://github.com/2023M6T4-Inteli/Projeto2/blob/dev-jo%C3%A3o/assets/Imagens/user_storie_03.png" alt="user storie 3" width="400" height="auto">
<br>
<img src = "https://github.com/2023M6T4-Inteli/Projeto2/blob/dev-jo%C3%A3o/assets/Imagens/user_storie_04.png" alt="user storie 4" width="400" height="auto">
<br>
<img src = "https://github.com/2023M6T4-Inteli/Projeto2/blob/dev-jo%C3%A3o/assets/Imagens/user_storie_05.png" alt="user storie 5" width="400" height="auto">
<br>
<img src = "https://github.com/2023M6T4-Inteli/Projeto2/blob/dev-jo%C3%A3o/assets/Imagens/user_storie_06.png" alt="user storie 6" width="400" height="auto">


## (Sprint 2) Modelo Bag Of Words (IPYNB)

Link do Modelo Bag of Words: <a href="https://github.com/2023M6T4-Inteli/Projeto2/blob/main/src/1_BagOfWords.ipynb">Jupyter Notebook do Modelo Bag of Word</a>

### Preparação dos dados 

A fase de preparação de dados começou com a obtenção da base de dados com os comentários de posts do Instagram do parceiro de projeto (@btgpactual). Depois que os dados foram coletados, foi feita a preparação do ambiente de desenvolvimento (Colab Notebook), na qual foi feita uma análise exploratória dos dados, que inclui a verificação da qualidade dos dados, identificação de valores ausentes, duplicados, outliers, inferências e formulação de hipóteses, entre outros, e posteriormente as etapas de pré-processamento.

###  Importação das bibliotecas:

No Pandas, as importações de bibliotecas são usadas para trazer funcionalidades específicas de bibliotecas externas para o seu código. O Pandas é uma biblioteca popular para análise de dados em Python, mas para aproveitar ainda mais recursos, pode ser necessário importar outras bibliotecas. As importações no Pandas geralmente são feitas no início do código e são usadas para importar módulos adicionais que fornecem funcionalidades extras.

Em primeira instância utilizamos as seguintes bibliiotecas:

pip install emoji: Este comando utiliza o gerenciador de pacotes pip para instalar a biblioteca emoji. A biblioteca emoji é uma biblioteca Python que fornece funcionalidades para trabalhar com emojis, como a exibição, codificação e manipulação de emojis em texto. Ao executar esse comando, você estará instalando a biblioteca emoji em seu ambiente Python.

pip install pyspellchecker: Este comando utiliza o gerenciador de pacotes pip para instalar a biblioteca pyspellchecker. A biblioteca pyspellchecker é uma biblioteca Python que fornece correção ortográfica em texto. Ela pode ser usada para verificar e corrigir erros ortográficos em palavras. Ao executar esse comando, você estará instalando a biblioteca pyspellchecker em seu ambiente Python.

Segue abaixo os códigos:
- ```!pip install emoji```
- ```!pip install pyspellchecker```

### Compreensão dos Dados 
Foi implementado o método de carregamento do Dataframe utilizado. Sendo assim, foi criado o caminho da pasta no Google Drive e sua leitura usando "pd.read_csv".
Reorganizamos dessa forma, e renomeamos algumas colunas com o intuito de facilitar o processo de análise.

Nesta Etapa será explicado as colunas da base de dados, “BASE-DEPRECATED”, fornecida pela empresa BTG Pactual durante a Sprint 2. A base de dados possui 4549 linhas e foram utilizadas apenas 11 colunas para a realização das análises. Tais colunas serão descritas abaixo:
  
- **Coluna 'id':** apresenta os índices das linhas da tabela. | Tipo = *integer64*
- **Coluna 'autor':** mostra a conta do autor do comentário. | Tipo = *object*
- **Coluna 'texto':** o comentário escrito pelo autor. | Tipo = *object*
- **Coluna 'tipoInteracao':** classificação de como foi feito o texto do comentário(resposta, comentário ou marcação). | Tipo = *object*
- **Coluna 'tipoMidia':** categoria do tipo de post(reels, feed, image, carousel). | Tipo = *object*
- **Coluna 'anomalia':**  indica se o comentário pode ser golpe ou spam. | Tipo = *float64*
- **Coluna 'probabilidadeAnomalia':** porcentagem de quanto o comentário pode ser um golpe ou spam. | Tipo = *object*
- **Coluna 'processado':** indica se já houve uma análise de sentimento daquele comentário. | Tipo = *object*
- **Coluna 'contemHyperlink':** mostra se o comentário tem algum link. | Tipo  = *float64*
- **Coluna 'dataPublicada':** retorna quando o comentário foi publicado. | Tipo = *object*
- **Coluna 'URL':** direciona ao link em que está inserido o comentário na rede social. | Tipo = *object*

### Análise Descritiva

A análise descritiva é uma etapa fundamental no acompanhamento e análise de dados. É uma técnica que aplicada no contexto do nosso proejto em parceria com o BTG-Pactual, envolve a interpretação, comprreensão e organização dos dados de forma a obterpadrões e tendências. Em nosso projeto, essa análise será feita com o intuito de realizar uma análise de sentimentos dos usuários em relação às campanhas do BTG, além de facilitar o banco no processo de desenvolver futuras estrtaégias e ompreender melhor como eles podem gerenciar um bom relacionamento com os clientes. Utilizaremos a análise descritiva para identificar:

- **Comentários por tipo de post (Reels, Foto, Vídeo, Carrossel):**
    Dado que cada tipo de mídia possui um objetivo diferente, entende-se que, conforme as suas diferenciações, as palavras mais comentadas podem ser diferentes e podem agregar para o usuário.

- **Palavras que mais aparecem nos comentários:**
    Com a finalidade de entender quais palavras mais se repetem em todos os comentários no perfil do BTG Pactual, desenvolve-se a análise descritiva tendo a *wordcloud*, além dos gráficos de barra e dispersão, como representações visuais.

- **Conjunto de palavras com maior frequência (n-grams = 3):**
    Visualizar a frequência de possíveis frases para identificar padrões em textos que podem ser associados a determinados sentimentos.

-  **Relação determinística entre as colunas Anomalia e Comentário:**
    Verificar e a partir das hipóteses estruturadas, atribuir possibilidades de atuação na coluna "anomalia"

- **Emojis na Base de Dados:**
    Entendimento de qual seria o melhor tratamento para os emojis, para que a análise de sentimento seja mais precisa, com base nas aparições no dataset.
   
### Pré-Processamento

O pré processamento é uma etapa crucial na análise de dados. Esse processo consiste no conjunto de tecnicas aplicados nos dados quando em desenvolvimento de modelos de aprendizado de máquina. No contexto do Processamento de Linguagem Natural (PLN), o pré-processamento refere-se no na técnica de transformar e preparar os dados em uma forma mais adequada para a realização de análise de textos. 

Este processo é crucial no momento de construção de uma análise de dados, e nos modelos de machine learning e geralmente seguem as seguintes etapas: 
* Tokenização: Processo de dividir um texto em pequenas unidades de texto chamadas de "token". 
* Remoção de pontuações: Eliminação de caracteres de pontuação: vírculas, pontos, aspas, entre outros. 
* Conversão para minúscula: Padronizar as palavras. 
* Remoção de stopwords: Remoção das palavrad comuns e que não costumam contribuir significativamente para o texto. 
* Stemming e Lematização: Técnica de reduzir as palavras em seus radicais, ou formas mais básicas. 

### Testando etapas do Pré-processamento
#### Estruturação do Pré-processamento

##### Função: Retirando valores nulos
Descrição: Essa função remove linhas do DataFrame dados que possuem valores nulos nas colunas 'autor' e 'texto'. O resultado é armazenado na variável df_textoAutor.
``` df_textoAutor = dados[['autor', 'texto']].dropna() ```

##### Função: Retirando posts do btg
Descrição: Essa função remove do DataFrame dados todas as linhas em que o valor da coluna 'autor' é igual a 'btgpactual'. O resultado é armazenado na variável 
```df_textoAutor = dados.drop(dados[dados['autor'] == 'btgpactual'].index) ```

##### Função: Shape
Descrição: Essa função retorna a dimensão do DataFrame df_textoAutor, ou seja, o número de linhas e colunas. O resultado será uma tupla com dois elementos, em que o primeiro elemento representa o número de linhas e o segundo elemento representa o número de colunas.
```df_textoAutor.shape```

#### Função: Transformando uma frase em minúsculas
Descrição: Essa função extrai a frase localizada na linha 100 da coluna 'texto' do DataFrame dados. Em seguida, a função lower() é aplicada para converter todos os caracteres da frase em minúsculas. O resultado é armazenado na variável sentence_teste. Essa transformação é comumente utilizada para normalizar o texto, tornando-o uniforme e facilitando comparações e análises, independentemente das diferenças de capitalização.
```sentence_teste = dados['texto'].iloc[100].lower()```

### Tokenização
A tokenização é uma etapa importante no pré-processamento de texto que envolve a divisão de uma sequência de texto em unidades menores chamadas de tokens. Esses tokens podem ser palavras individuais, frases, símbolos ou outros elementos, dependendo do objetivo do processamento.
No contexto do pré-processamento de texto no Pandas, a tokenização geralmente é realizada em um DataFrame que contém uma coluna de texto. Cada valor nessa coluna, que representa uma sentença ou um documento, é dividido em tokens individuais. Isso é útil para várias tarefas de processamento de texto, como contagem de palavras, análise de sentimentos, classificação de texto e muito mais.
Existem diferentes abordagens de tokenização disponíveis, como tokenização com base em espaços em branco, tokenização com base em pontuação, tokenização com base em expressões regulares e tokenização com base em modelos de linguagem pré-treinados. A escolha da técnica de tokenização depende da natureza dos dados e do objetivo específico do processamento de texto que está sendo realizado.

#### Funções utilizadas
A função lower().split() é utilizada para realizar a tokenização de uma frase ou sequência de texto em Python.

O método lower() é aplicado à variável sentence_teste e converte todos os caracteres da sequência de texto em letras minúsculas. Isso é útil para normalizar o texto e garantir consistência ao realizar a tokenização.

Em seguida, o método split() é chamado para dividir a sequência de texto em tokens individuais. Esse método divide a sequência em espaços em branco, resultando em uma lista de tokens.

A lista de tokens é atribuída à variável tokens, que pode ser usada posteriormente para análise de texto, processamento de linguagem natural ou outras tarefas relacionadas ao processamento de texto.

Essa função é simples e eficaz para realizar a tokenização básica de uma frase em Python, dividindo-a em palavras individuais com base nos espaços em branco. No entanto, é importante observar que essa função não trata outros tipos de pontuações ou casos mais complexos de tokenização, que podem exigir o uso de bibliotecas ou técnicas mais avançadas.
Segue o código abaixo:
```tokens = sentence_teste.lower().split() ```

### Stop-Words
Stop words são palavras comuns que geralmente são removidas durante o pré-processamento de texto, pois são consideradas pouco informativas para a análise de texto. Essas palavras incluem artigos, conjunções, preposições e outros termos frequentemente encontrados na linguagem, como "a", "o", "em", "de", "e", entre outros.

A remoção de stop words é uma etapa comum no pré-processamento de texto, pois ajuda a reduzir o ruído e o tamanho do vocabulário utilizado na análise. Ao remover essas palavras, é possível focar em termos mais relevantes e significativos para a tarefa em questão, como análise de sentimentos, classificação de texto ou mineração de tópicos.

No contexto do pandas, a remoção de stop words geralmente envolve o uso de bibliotecas de processamento de linguagem natural, como NLTK (Natural Language Toolkit) ou spaCy. Essas bibliotecas possuem listas predefinidas de stop words em diferentes idiomas, que podem ser aplicadas aos dados textuais para remover essas palavras desnecessárias antes de prosseguir com a análise ou modelagem de texto.

#### Funções utilizadas
A função translate() é utilizada para remover pontuações de uma string. Nesse caso específico, a função ```str.maketrans('', '', string.punctuation)``` cria uma tabela de tradução que mapeia os caracteres de pontuação para um valor vazio (''). Em seguida, a função translate() aplica essa tabela de tradução à string sentence_teste, removendo todas as pontuações.

Já a função ```strip()``` é utilizada para remover espaços em branco (espaços, tabulações, quebras de linha) no início e no final de uma string. Ela retorna a versão da string sem os espaços em branco.

Essas duas funções em sequência têm o objetivo de remover pontuações e espaços em branco extras da string sentence_teste, deixando-a limpa e pronta para ser processada ou analisada posteriormente.
Segue o código abaixo:
- ```sentence_teste = sentence_teste.translate(str.maketrans('', '', string.punctuation)) ```
- ```sentence_teste = sentence_teste.strip()```

Também encontra-se nesse código, a variável stop_words é inicializada com um conjunto de palavras de parada (stop words) em português, obtidas a partir do módulo nltk.corpus.stopwords. Essas palavras são geralmente consideradas irrelevantes para a análise de texto, como artigos, preposições e pronomes.

Em seguida, uma lista adicional chamada stop_words_add é criada, contendo palavras adicionais que serão incluídas nas stop words. Essas palavras podem ser personalizadas de acordo com as necessidades do projeto.

O método update é usado para adicionar as palavras da lista stop_words_add ao conjunto de stop words existente.

Em seguida, é criada uma lista vazia chamada new_words. Em um loop, cada palavra em sentence_teste é verificada se está presente no conjunto de stop words. Se a palavra não for uma stop word, ela é adicionada à lista new_words.

Por fim, a variável sentence_teste é atualizada, substituindo seu valor original pela concatenação das palavras contidas em new_words, formando assim uma nova versão da sentença sem as stop words.

Segue o código abaixo: 
```top_words = set(nltk.corpus.stopwords.words('portuguese'))```

```
stop_words_add = ['ola', 'olá', 'pra', 'para', 'bemvindo','benvindo', 'bem-vindo', 'bemvindos', 'aqui', 'vai', 'btgpactual']
stop_words.update(stop_words_add)
new_words = []
for word in sentence_teste:
    if word not in stop_words:
        new_words.append(word)
        sentence_teste = ''.join(new_words) 
```
        
### Testando corretor de palavras
Nesse código, a biblioteca spellchecker é importada, e em seguida, uma frase incorreta é atribuída à variável frase_errada. A frase é dividida em palavras individuais usando o método split() e armazenada na lista words.

A classe SpellChecker é inicializada com o parâmetro language='pt', indicando que o corretor ortográfico será utilizado para o idioma português.

Por fim, um objeto spell do tipo SpellChecker é criado e está pronto para ser usado para correção ortográfica das palavras contidas na frase incorreta.

Segue o código abaixo:
```from spellchecker import SpellChecker```
```frase_errada = 'As veses estol gostandu di vose```
```words = frase_errada.split()```
```spell = SpellChecker(language='pt')``` 

### Testando corretor de abreviações e deletar emojis

Nesse código, a biblioteca enelvo é importada e em seguida a classe Normaliser é utilizada.

O objetivo desse código é realizar a normalização de texto, que consiste em aplicar transformações específicas para padronizar ou corrigir palavras em um texto.

Na primeira linha, a classe Normaliser é importada da biblioteca enelvo.

Em seguida, uma mensagem é atribuída à variável msg, que contém o texto a ser corrigido ou normalizado.

Por fim, um objeto norm do tipo Normaliser é criado, e é utilizado o parâmetro tokenizer='readable', indicando que o texto será tokenizado de forma legível, ou seja, separando-o em palavras individuais considerando a estrutura gramatical.

O objeto norm está pronto para ser utilizado para realizar as correções ou normalizações no texto contido na variável msg.
Segue o código abaixo:
```from enelvo.normaliser import Normaliser```
```msg = 'hj vou usar meu cartão do banco btg, pq gosto mt dele👊'```
```norm = Normaliser(tokenizer='readable')```

### Stemming
Em pré-processamento de texto, stemming é uma técnica utilizada para reduzir palavras à sua forma básica ou raiz, removendo sufixos e prefixos. O objetivo é simplificar a análise de texto, tratando diferentes variações da mesma palavra como uma única forma, o que pode facilitar a comparação e agrupamento de palavras semelhantes.

Na prática, já no código, a biblioteca nltk é importada e a classe SnowballStemmer é utilizada.

O objetivo desse código é realizar a técnica de stemming, que consiste em reduzir palavras à sua forma básica (ou raiz) removendo sufixos e prefixos, para facilitar a análise de texto.

Na primeira linha, a classe SnowballStemmer é importada da biblioteca nltk e é especificado o idioma 'portuguese' como parâmetro para o construtor do stemmer, indicando que o stemming será realizado para palavras em português.

Em seguida, um loop for é utilizado para iterar sobre cada palavra presente no texto sentence_teste, que provavelmente contém várias palavras tokenizadas.

Dentro do loop, a função stem() do objeto stemmer é chamada para cada palavra, retornando a raiz ou forma básica da palavra.

A raiz de cada palavra é impressa na saída utilizando a função print(), representando o resultado do stemming para cada palavra no texto.

Assim, o código realiza o processo de stemming para cada palavra no texto sentence_teste, retornando suas formas básicas ou raízes.
Segue o código abaixo:
```from nltk.stem.snowball import SnowballStemmer```
```stemmer = SnowballStemmer('portuguese')```
```for word in sentence_teste.split():```
    ```print(stemmer.stem(word))```
    
    
##### Pipeline 
Utiliza-se o pipeline com a finalidade de evidenciar as etapas utilizadas nesse processo, demonstando que os outputs de um procedimento torna-se input da sequente.

![image](https://github.com/2023M6T4-Inteli/Projeto2/blob/main/docs/Imagens/pipeline.jpeg)
    
### Bag Of Words

O modelo Bag-of-Words é uma abordagem comum no pré-processamento de texto usada para representar documentos de texto como vetores numéricos. É uma técnica simples e amplamente utilizada em tarefas de processamento de linguagem natural.

No contexto do Google Colab, o pré-processamento com o modelo Bag-of-Words envolve as seguintes etapas:

Tokenização: O texto é dividido em unidades menores chamadas "tokens". Geralmente, os tokens são palavras individuais, mas também podem ser caracteres, n-grams (sequências de n tokens consecutivos) ou outras unidades, dependendo do caso de uso.

Construção do vocabulário: O vocabulário é criado coletando todos os tokens únicos presentes nos documentos de texto. Cada token único é atribuído a um índice único no vocabulário.

Codificação dos documentos: Cada documento de texto é codificado como um vetor numérico de acordo com o vocabulário construído. O tamanho do vetor é igual ao tamanho do vocabulário. Cada posição no vetor representa uma palavra do vocabulário, e o valor naquela posição indica a frequência ou outra medida de importância do termo no documento.

Matriz de documentos-termos: Todos os documentos são representados em uma matriz, em que cada linha corresponde a um documento e cada coluna corresponde a um termo do vocabulário. Os valores da matriz são geralmente contagens de frequência, mas também podem ser pesos TF-IDF (term frequency-inverse document frequency) ou outros esquemas de ponderação.

Essa representação baseada no modelo Bag-of-Words permite que os algoritmos de aprendizado de máquina trabalhem com dados de texto, que normalmente requerem entrada numérica. No Google Colab, você pode implementar essas etapas usando bibliotecas de processamento de texto, como NLTK (Natural Language Toolkit), e aplicá-las aos seus dados de texto para prepará-los para tarefas de classificação, agrupamento ou outras análises.

#### Funções utilizadas:
O código fornecido realiza a vetorização de texto usando o CountVectorizer da biblioteca scikit-learn. Vejamos o que cada linha faz:

- Importação das bibliotecas:
-Essas linhas importam as classes CountVectorizer e TfidfVectorizer da biblioteca sklearn.feature_extraction.text, necessárias para realizar a vetorização de texto.
```from sklearn.feature_extraction.text import CountVectorizer```
```from sklearn.feature_extraction.text import TfidfVectorizer```

- Instanciação do vetorizador:
-Aqui, um objeto CountVectorizer é criado e atribuído à variável vectorizer. O CountVectorizer é usado para converter o texto em uma matriz de contagens de palavras.
```vectorizer.fit(frases_pre)```

- Ajuste do vetorizador aos dados de entrada:
-Essa linha ajusta o vetorizador aos dados de entrada frases_pre. Ele analisa o texto fornecido, constrói o vocabulário e atribui um índice numérico único a cada palavra encontrada nas frases.
 ``` vectorizer.fit(frases_pre)```

- Exibição do vocabulário ordenado:
-Essa linha imprime o vocabulário ordenado alfabeticamente. O vocabulário é um dicionário que mapeia as palavras encontradas nas frases para seus respectivos índices numéricos.
```print(sorted(vectorizer.vocabulary_)) ```
- Transformação dos dados em uma representação vetorial:
-Aqui, o método transform é chamado para converter as frases pré-processadas frases_pre em uma matriz vetorial. Cada linha da matriz representa uma frase, e cada coluna representa uma palavra do vocabulário. O valor em cada posição da matriz representa a contagem de ocorrências da palavra correspondente na frase.
```vector = vectorizer.transform(frases_pre)```

- Sumarização dos resultados:
-Essas linhas exibem a forma (shape) da matriz resultante, que indica o número de frases e o tamanho do vocabulário. Em seguida, é impressa a representação em formato de array da matriz vetorizada, mostrando as contagens de palavras para cada frase.
```print(vector.shape)```
```print(vector.toarray())```

![image](https://github.com/2023M6T4-Inteli/Projeto2/assets/99270135/0cae7c4b-5c5b-43cf-a164-3917b19e4779)

## TFID
 O TfidVectorizer calcula o inverso das frequências e codifica os vetores a fim de calcular a relevância de cada termo nos documentos. Diferente do CountVectorizer, este algoritmo calcula 'word frequencies'. Isso impede que, por exemplo, artigos ou palavras não muito significantes acabem sendo reconhecidos como muito relevantes apenas pelo grande número de ocorrências na base de dados, uma vez que essa frequência inversa leva mais em conta o contexto das palavras empregadas em cada frase.
 Segue o código abaixo:
``` vectorizer = TfidfVectorizer()```
``` vectorizer.fit(frases_pre)```
```print(sorted(vectorizer.vocabulary_))```
```vector = vectorizer.transform([frases_pre[0]])```

![image](https://github.com/2023M6T4-Inteli/Projeto2/assets/99270135/7161d030-b594-4156-82ea-95336c3f50b7)

## Resultados Obtidos

### Análise Descritiva

Na Análise Descritiva dos dados, trabalhamos com a criação de tabelas para oganizarmos técnicas de visualização, para identificar informações importantes e relevantes das campanhas, e podermos obter insights valiosos dos dados analisados. 

#### - Comentários por tipo de post (Reels, Foto, Vídeo, Carrossel): 

O código apresentado abaixo foi feito com o intuito de identificar as palavras mais comentadas pelos usuários conforme o tipo de post. Foi identificado a grande quantidade de comentários feitos pelo próprio BTG-Pactual, dessa forma optamos por remover os comentários feitos pelo BTG para termos uma análise apenas dos autores externos. 

O código abaixo foi feito para retirarmos os comentários feitos pelo BTG: 
```df_repete = df_repete.drop(df_repete[df_repete['autor'] == 'btgpactual'].index)```
```df_repete```

#### - Palavras que mais aparecem nos comentários (sem stemming): 

Nessa etapa, passamos pelo processo de pré-processamento e fizemos a junção de textos em uma string para então calcular a frequ6encia de cada palavra como mostra o código a seguir: 

```freq_dist = FreqDist(palavras)```
```print(freq_dist.most_common(100))```

Após esse processo o código abaixo foi criado, com o intuito de exibir em formato Word Cloud os resultados obtidos

```wordcloud = WordCloud(width=2000, height=1200, background_color='white').generate(' '.join(frases_pre)))```
```plt.imshow(wordcloud, interpolation='bilinear'))```
```plt.axis('off'))```
```plt.show())```

![image](https://github.com/2023M6T4-Inteli/Projeto2/blob/main/docs/Imagens/wordcloudpalavras.png)

Além disso, criamos a partir do código abaixo uma visualização gráfica da frequência e dispersão das palavras
![image](https://github.com/2023M6T4-Inteli/Projeto2/blob/main/docs/Imagens/freqpalavras.png)


#### - Conjunto de três palavras com maior frequência:

Nessa etapa, a fim de ter maior arcabouço de palavras frequentes nos comentários, opta-se pela seleção dos conjuntos de três palavras. O código abaixo foi realizado e nos trouxe resultados para entendermos melhor quais os conjuntos de plaavras que aparecem com a maior frequência. 

```for frase in frases_pre:```
    ```words = frase.split()```
    ```trigrams += list(ngrams(words, 3))```

```freq_tri = nltk.FreqDist(trigrams)```

```top = freq_tri.most_common(100)```
```top```

Depois disso, criamos uma tabela para represnetarmos qual a frequência dos conjuntos. 
![image](https://github.com/2023M6T4-Inteli/Projeto2/blob/main/docs/Imagens/freqtigramas.png)


#### - Uso de emoji na base de Dados:

o objetivo desta hipótese foi entender quais são emojis que mais aparecem no dataset e qual seria o melhor tratamento para os mesmos, com o intuito de que a análise de sentimento seja mais precisa, com base nas aparições no dataset. Dessa forma, utilizamos o código abaixo para calcular a porcentagem de aparição dos emojis nos comentários

```emoji_dict = dict(Counter(c for c in texto if emoji.is_emoji(c)))```

```most_common_emojis = Counter(emoji_dict).most_common(15) ```

```total_emojis = sum(emoji_dict.values()) ```
```emoji_percentages = {k: v / total_emojis for k, v in most_common_emojis}```

```df = pd.DataFrame({'emoji': list(emoji_percentages.keys()), 'percentage': list(emoji_percentages.values())})```
```df = df.sort_values(by='percentage', ascending=False)```
```print(df)```

![image](https://github.com/2023M6T4-Inteli/Projeto2/blob/main/docs/Imagens/emojidataframe.png)


###  Gráfico Word Cloud

O Gráfico de Nuvem de Palavras, conhecido também como como Word Cloud, é uma ferramenta de representação visual que trabalha com a *plotagem* das palavras mais frequentes em um conjunto de textos. Nesse contexto, foi desenvolvido com o intuito de mostrar as palavras mais recorrentes e utilizadas pelos usuários nos comentários das postagens. 

![image](https://github.com/2023M6T4-Inteli/Projeto2/blob/main/docs/Imagens/wordcloud.png)

### Tokenização:

![image](https://github.com/2023M6T4-Inteli/Projeto2/assets/99270135/cd243004-d587-4c77-8be5-4e53b45b750f)

Esta é uma pequena amostra dos resultados do processo de tokenização. A partir dele conseguimos ter alguns insights de para novos tratamentos de dados e futuras estapas de pré-processamento. A partir desse tokenização é que foi possível progredir com os outros métodos do pré-processamento.

### Stop Words:

Remoção de caracteres especiais

![image](https://github.com/2023M6T4-Inteli/Projeto2/assets/99270135/aa0376df-999c-4e07-af04-e66cbebd8546)

Remoção de stop words

![image](https://github.com/2023M6T4-Inteli/Projeto2/assets/99270135/b5c7e5c3-1f48-41eb-8245-f3edd3946fdf)

Esse foi uns dos resultados que obtivemos ao aplicar o método de remoção de stop words, consistindo em retirar das frases palavras descessárias que não contribuém para a análise de sentimentos.

### Stemming:

Stemming é uma técnica utilizada para reduzir palavras à sua forma básica ou raiz, removendo sufixos e prefixos.
 
![image](https://github.com/2023M6T4-Inteli/Projeto2/assets/99270135/ccd9595b-7f7c-44bb-8692-03c7fb5aeba8)

O output retorna o texto sem caracteres especiais e sem espaços. 

### Bag of Words:

O modelo Bag-of-Words é uma abordagem comum no pré-processamento de texto usada para representar documentos de texto como vetores numéricos. É uma técnica simples e amplamente utilizada em tarefas de processamento de linguagem natural.

Count Vectorizer

O CountVectorizer tokeniza uma coleção de textos e cria um vocábulo com as palavras encontradas. 

![image](https://github.com/2023M6T4-Inteli/Projeto2/assets/99270135/0cae7c4b-5c5b-43cf-a164-3917b19e4779)

TFID Vectorizer

O TfidVectorizer calcula o inverso das frequências e codifica os vetores a fim de calcular a relevância de cada termo nos documentos. 

![image](https://github.com/2023M6T4-Inteli/Projeto2/assets/99270135/7161d030-b594-4156-82ea-95336c3f50b7)

## Modelo utilizando Word2Vec (IPYNB)

<a href="https://github.com/2023M6T4-Inteli/Projeto2/blob/main/src/Notebook/2_Word2Vec.ipynb">Jupyter Notebook do Modelo Word2Vec</a>

## (Sprint 3) Documentação do Modelo utilizando Word2Vec

### Objetivo da Sprint
 
Pré-processamento para utilização de Word2Vec (carregando vetores para cada palavras num modelo já treinado) e entrega do modelo word2vec em algortimos classificatórios.

### Sobre o Modelo Word2Vec 

 O modelo Word2Vec é uma técnica de PLN que permite representar palavras como vetores numéricos em um espaço de várias dimensões. Este processo consiste em capturar relações entre as palavras com base nos seus contextos. Como resultado final, é possível ter uma representação matemática da similaridade entre as palvras disponibilizas para o treinamento. 
 
 Ele, também, permite capturar nuances e contextos que podem influenciar o sentimento de um texto, que são dados pelo nível de similaridade e proximidade entre as palavras. Além disso, o word2vec pode facilitar a extração de características relevantes para a classificação, reduzindo a dimensionalidade e a esparsidade dos dados textuais. Este fatores, são determinates na justificativa da sua utilização no projeto, tão como sua importância.
 
 O modelo word2vec pode ser combinado com outros modelos de aprendizado de máquina com facilidade, para obter melhores resultados de classificação. O word2vec também pode ser usado para gerar incorporações de frases ou documentos inteiros, usando técnicas como média ou soma dos vetores das palavras (neste caso utilizamos a soma, com adição de uma coluna em um novo dataframe). Portanto, o word2vec é um modelo muito útil para a construção e desenvolvimento de nossa análise, pois permite representar as palavras de forma mais rica e eficiente, capturando aspectos semânticos e sintáticos que afetaram na classificação de determinado corpus.


<img src="https://github.com/2023M6T4-Inteli/Projeto2/blob/main/assets/Imagens/exemplo_word2vec.png" alt="representação word2vec" width="300" height="auto">

<em> Representação visual do modelo Word2Vec </em>
<br>
<br>

### Vantagens do Modelo Word2Vec 

Em comparação ao modelo anterior do Bag of Words, o modelo Word2Vec possui várias vantagens, a principal delas é conseguir capturar o contexto e semântica das palavras. Além disso, o Word2Vec também gera uma representação vetorial com uma dimensionalidade muito mais reduzida, ele consegue trabalhar de forma mais efetiva com palavras desconhecidas e é capaz de fazer esses cálculos semânticos entre similaridade entre palavras.

### Arquitetura do Modelo Word2Vec: CBOW

O modelo Word2Vec possui duas arquiteturas principais: CBOW (Continuos Bag-Of-Words) e Skip-Gram. Nossa equipe optou por utilizar o modelo CBOW pois computacionalmente ele é mais eficiente. Esse tipo de arquitetura recebe as palavras circundantes e tenta prever a palavra central. Ambos os modelos (CBOW e Skip-Gram) são treinados para maximizar a probabilidade de previsão correta das palavras.

<img src="https://github.com/2023M6T4-Inteli/Projeto2/blob/main/assets/Imagens/modelo_cbow.png" alt="modelo CBOW" width="300" height="auto">

### Construção do Modelo Word2Vec

Para a construção do modelo Word2Vec, a equipe fez uma nova limpeza e pré-processamento de dados, só que agora, na segunda base disponibilizada:

  - Substituição de Emojis: nas frases, substituimos os emojis por palavras. Esse processo melhora e abrange a base de dados trabalhada
   
   <img src="https://github.com/2023M6T4-Inteli/Projeto2/blob/main/assets/Imagens/emojis_funcao.png" alt="emoji" width="700" height="auto">
   <br>

  - Substituição de Abreviações: substituímos abreviações por suas formas originais
    
   <img src="https://github.com/2023M6T4-Inteli/Projeto2/blob/main/assets/Imagens/func_abreviacoes.png" alt="abreviaçao" width="300" height="auto">
   <br>

  - Lematização: é o processo de transformação de palavras para sua forma base (derivação inversa). Para esse método de pré-processamento utilizamos a bibliotecas spaCy
  
   <img src="https://github.com/2023M6T4-Inteli/Projeto2/blob/main/assets/Imagens/resultado_pipilina_lematizacao.png" alt="lematizacao" width="900" height="auto">
   <em>Tabela pós pré-processamento</em>
   <br>
   <br>
   
  <em>Processos anteriores do último modelo, como remoção de stop words e tokenização, permanecem. O único processo retirado foi o de stemming, pois a lematização o substitui.</em>
  
  <br>
  <br>
  
  - Modelo word2Vec e Características: já na construção do Modelo Word2Vec em si, configuramos seus parâmetros da seguinte forma: 150 vetores de dimensioanalidade, 5 janelas de contexto, contagem mínima de palavras para 1 e 4 threads para treinamento paralelo
  
  <br> 
<img src="https://github.com/2023M6T4-Inteli/Projeto2/blob/main/assets/Imagens/modelo_word2vec_persi.png" alt="wor2vec" width="900" height="auto">  
<em>Definições e contrução do modelo Wor2Vec</em>
  <br>
  <br>

  
  - Vetorização para Word2Vec: a vetorização consiste em transformar dados textuais em representações numéricas. É um processo crucial para a contrução do modelo Wor2Vec, só assim será possível organizar a distribuição das palavras em um plano. Todos o tokens são vetorizados e suas somas em uma frase também são contabilizados.

  <br> 
<img src="https://github.com/2023M6T4-Inteli/Projeto2/blob/main/assets/Imagens/funcao_vetorizacao.png" alt="vetorizacao" width="900" height="auto">  
<em>Função para o processo de Vetorização</em>
  <br>
  <br>
  
  - Output e tabela pós Word2Vec: ao final do processo de Word2Vec, configuramos a tabela que será utilizada para algorítimos de aprendizado. Um dos passos é tranformação da coluna de sentimentos para valores numéricos. O segundo passo é exatamente a atribuição dos tokens às 150 colunas definidas.

  <br> 
  <br> 
<img src="https://github.com/2023M6T4-Inteli/Projeto2/blob/main/assets/Imagens/map_sentimentos.png" alt="map_sentimentos" width="800" height="auto">  
<em>Mapeamento da Coluna Sentimentos</em>
  <br> 
  <br> 
<img src="https://github.com/2023M6T4-Inteli/Projeto2/blob/main/assets/Imagens/alocacao_150vetores.png" alt="150vetores" width="1000" height="auto">  
<em>função para distribuição dos tokens nos vetores</em>
  <br> 
<img src="https://github.com/2023M6T4-Inteli/Projeto2/blob/main/assets/Imagens/tabel_final_word2Vec.png" alt="tabela w2v" width="900" height="auto">  
<em>Tabela final pós Word2Vec</em>
  <br> 

  <br>
  <br>
  
### Algorítimos de Aprendizado: 

 O objetivo no nosso projeto é fazer a classificação de frases com o intuito de conferir o desempenho de campanhas de marketing. Assim, apenas o modelo Word2Vec não é o suficente, pois mesmo organizando a similaridade de palavras, ele não consegue fazer a classificação de sentimentos. A solução é utilizar algorítimos de aprendizado supervizionado para fazer esse tipo de classificação. Neste sentido, testamos alguns algoritmos, mas optamos pela utilização do Naive Bayes e do Catboost.


#### Naive Bayes

 O Naive Bayes foi o primeiro algorítimo testado pelo grupo, ele se baseia em uma teoria matemática de probabilidades condicionais (teorema de Bayes). O algorítimo se detaca por sua eficiência e simplicidade. A biblioteca utilizada para esse método foi o sklearn (GaussianNB). A principal intenção do grupo, era de usar o algoritmo para realizar o cálculo da probabilidade condicional de cada palavra ou "n-grama" ocorrer em cada classe, com o intuito de estimar a probabilidade do texto pertencer a uma classificação de sentimento específico.

<img src="https://github.com/2023M6T4-Inteli/Projeto2/blob/main/assets/Imagens/modelo_naive_bayes.png" alt="naive bayes" width="900" height="auto">  
<em>Construção do modelo Naive Bayes aplicado</em>
<br>
<br>

#### CatBoost

 O catboots é outro algorítimo de classificação, se destacando principalemnte com dados com características categóricas e dados desbalanceados. Esse algorítimo se baseia em conhecimentos matemáticos de gradiente (gradient boosting). É importante ressaltar que o Catboost é muito usado na definição de características categóricas como palavras ou frases, sem a necessidade de codificá-las numericamente, o que pode reduzir a complexidade e o tempo de processamento. Com base nestes fatores, e mediante o uso prévio de alguns membros de nosso grupo, decidimos optar pela sua utilização nesta Sprint.


<img src="https://github.com/2023M6T4-Inteli/Projeto2/blob/main/assets/Imagens/modelo_catboost.png" alt="modelo catboost" width="900" height="auto">  
<em>Construção do modelo CatBoost aplicado</em>
<br>
<br>

- Resultados dos Algorítimos de Apredizado Supervisionado:

Diante as etapas exemplificadas acima, dividimos nossos dados para realizar o treinamento e avaliação do nosso modelo, com base na estruturação realizada. Sendo dividimos em duas seções

- Dados de treino: separação com o intuito de fazer o modelo aprender as características e os padrões dos dados que permitem fazer previsões ou classificações. 

- Dados de teste: separação usada como método de verificação do modelo, com base nas previsões ou classificações corretas e precisas.

### Naive Bayes:

![image](https://github.com/2023M6T4-Inteli/Projeto2/assets/99270135/2858ee49-47b2-4a80-aa4c-19ab348ef506)

![image](https://github.com/2023M6T4-Inteli/Projeto2/assets/99270135/27f6dd26-3243-4a51-a9e3-31b614bdf577)

<em>Os resultados conferidos pleo Naive Bayes foram satisfatórios mas não ideais. Com 54% de acurárica de treinamento e 55% de acurácia total</em>


#### CatBoost:

![image](https://github.com/2023M6T4-Inteli/Projeto2/assets/99270135/3952b8c2-fca2-4af5-8ea1-027dd886e15c)

![image](https://github.com/2023M6T4-Inteli/Projeto2/assets/99270135/86c8da56-7164-44b6-ba7c-2613cdf7d996)

![image](https://github.com/2023M6T4-Inteli/Projeto2/assets/99270135/4bbca284-8b45-4c13-94aa-d7e32abcbae5)

<em>Os resultados conferidos pleo CatBoost foram satisfatórios. Entretanto, apresenta um overfitting, já que existe 95% de acurácia de treinamento e 72% de acurácia total, tendo uma diferença grande entre as duas separações, portanto, sendo necessário entender o motivo. Também foi obtido resultados satisfatórios na matriz de confusão </em>

#### Avaliação e métricas do Modelo

Para avaliar o desempenho do nosso modelo, precisamos definir algumas métricas que nos permitam quantificar a sua capacidade de classificar corretamente os textos em categorias como positivo, negativo ou neutro. Essas métricas devem levar em conta não apenas a taxa de acerto do modelo, mas também cada tipo de erro e o balanceamento das classes nos dados.

Nesta seção, vamos apresentar as principais métricas que usamos para avaliar o nosso modelo, explicar como elas são calculadas e interpretadas, e mostrar os resultados obtidos com o nosso conjunto de teste. As métricas que vamos usar são:

- Acurácia: foi uma das métricas que mais olhamos na definição e relevância dos dados que foram passados. A acurácia, em termos mais objetivos, se refere a “taxa de acerto” do modelo. Ela é calculada dividindo o número de previsões corretas pelo número total de previsões. É importante ressaltar que seu balanceamento foi feito de acordo com a base de dados que nos foi deferida.

- Precisão: pode ser definido como a proporção de previsões positivas que são realmente positivas. Ela mede a confiabilidade do modelo em prever a classe positiva.

- Revocação: é a proporção de positivos reais que são corretamente previstos como positivos. Ela mede a sensibilidade do modelo em capturar a classe positiva, mas pode ignorar a quantidade de falsos positivos.

- F1-score: é a média harmônica entre precisão e revocação. Ela mede o equilíbrio entre essas duas métricas, dando mais peso aos valores baixos. Ela é útil para comparar modelos que têm trade-offs entre precisão e revocação.

Para termos de referência, recomendamos a análise dos resultados obtidos com o nosso modelo usando estas métricas como base.

Lembrando que diante da denfinição e alinhamento com o professor, pudemos definir:

- **Verdadeiro Positivo:** referem-se aos comentários negativos que são classificados como negativos;

- **Falso Positivo:** referem-se aos comentários positivos que são classificados como negativos;

- **Falso Negativo:** referem-se aos comentários negativos que são classificados como positivos;

- **Verdadeiro Negativo:** referem-se aos comentários positivos que são classificados como positivos.

É importante ressaltar que a partir de análises feitas, foi possível identificar as proporções de "falso negativo" como as mais importantes, diante das predições que o modelo deve fazer, e com base na estratégia de negócio do parceiro.

#### Comparação entre BOW e Word2Vec

A acurácia do BOW com TF-IDF resultou em 75% e o recall resultou em 72%.

Já os valores do Word2Vec ficaram como a seguir:

![image](https://github.com/2023M6T4-Inteli/Projeto2/assets/99270135/c56abbd0-19e7-4d12-ac9a-8b2dc90b9170)

Assim, conclui-se que a métrica na qual estamos focando no projeto, o recall, não sofreu muita alteração com o uso de um modelo diferente.

### Arquitetura da Solução

<img src="https://github.com/2023M6T4-Inteli/Projeto2/blob/main/assets/Imagens/Arquitetura%20de%20solu%C3%A7%C3%A3o.png" alt="Arquitetura de solução" width="5000">

1. Extração dos dados:

<img src="https://github.com/2023M6T4-Inteli/Projeto2/blob/main/assets/Imagens/Extra%C3%A7%C3%A3o.png" alt="Extração de dados" width="5000">

- Utilizando a API da rede social Instagram, é possível extrair dados de comentários em postagens públicas. Esses dados são retornados em formato JSON, que é uma forma de representação de dados estruturados que facilita a análise e manipulação.

- Depois de extrair os dados da API do Instagram, eles são processados e estruturados em uma fileira de dados, que pode ser um arquivo CSV, por exemplo. Isso facilita a manipulação e análise dos dados em etapas posteriores.

- Em seguida, os dados são enviados para um sistema de mensageria, que pode ser um serviço de mensagens instantâneas(RabbitMQ), por exemplo. Isso permite que os dados sejam acessados por usuários autorizados em tempo real.

- Depois de serem recebidos pelo sistema de mensageria, os dados passam por um processo de processamento, no qual podem ser manipulados e transformados em uma estrutura mais adequada para análise.

- Por fim, os dados são pré-estruturados, o que significa que são organizados em uma estrutura que facilita a consulta e análise. Isso pode incluir a organização dosdados em tabelas ou a atribuição de tags ou categorias específicas para cada dado. Com a pré-estruturação, é possível realizar consultas mais eficientes e respostas mais rápidas a perguntas específicas sobre os dados.

2. Análise descritiva:

<img src="https://github.com/2023M6T4-Inteli/Projeto2/blob/main/assets/Imagens/descritiva.png" alt="Análise descritiva" width="5000">

- Tipos de dados: identificação de quais são os tipos de dados presentes no dataset. Por exemplo, os dados podem incluir informações sobre o autor do comentário, a data e hora em que o comentário foi feito, o tipo de post (Reels, Foto, Vídeo, Carrossel) e o próprio comentário. Cada um desses tipos de dados pode ser tratado de forma diferente na análise.

- Colunas no dataset: listar todas as colunas no dataset e entender o que cada uma delas representa.

- Dados estatísticos do dataset: é possível calcular estatísticas básicas dos dados, como média, mediana, desvio padrão e intervalos de confiança. Usado para a entender a distribuição dos dados e identificar possíveis outliers.

- Comentários por tipo de post: analise da distribuição dos comentários por tipo depost (Reels, Foto, Vídeo, Carrossel). Usado para entender qual tipo de postagem gera mais engajamento e interação com os usuários.

- Palavras que mais aparecem nos comentários: é possível identificar as palavras mais frequentes nos comentários. Isso pode ajudar a entender os principais temas e assuntos abordados pelos usuários e possíveis stop-words. Essa análise pode ser feita utilizando técnicas de processamento de linguagem natural, como a tokenização e a contagem de frequência de palavras.

- Conjunto de três palavras com maior frequência (trigramas): além das palavras individuais, é possível identificar os conjuntos de três palavras mais frequentes nos comentários. Isso pode ajudar a entender quais as expressões mais comuns utilizadas pelos usuários.

- Relação determinística entre as colunas Anomalia e Comentário: Análise se há alguma relação determinística entre a presença de anomalias em uma postagem e a natureza dos comentários feitos pelos usuários.

- Uso de emojis na base de dados: é possível identificar o uso de emojis nos comentários e analisar quais são os emojis mais frequentes. Isso pode ajudar a entender aemoção e o sentimento dos usuários em relação às postagens. Sendo realizado uma substituição por palavras de seus respectivos significados.

3. Pré-processamento do Dataset

No pré-processamento do dataset, são realizadas etapas de limpeza e preparação dos dados antes de serem usados em análises ou modelos de machine learning. Isso envolve a aplicação de técnicas e bibliotecas para transformar os dados brutos em um formato adequado para análise.

Neste caso específico, foram utilizadas as seguintes bibliotecas adicionais para realizar o pré-processamento:

- Normaliser:
A biblioteca "Normaliser" é uma ferramenta utilizada para normalizar e padronizar textos. Ela oferece recursos para lidar com a normalização de caracteres, remoção de caracteres especiais, conversão de letras maiúsculas para minúsculas, entre outros. Essa biblioteca pode ser útil para garantir que os textos do dataset estejam em um formato consistente e pronto para serem processados.

- SpaCy: 
A biblioteca "SpaCy" é uma biblioteca de processamento de linguagem natural (NLP) em Python. Ela fornece uma variedade de recursos para realizar tarefas de processamento de texto, como tokenização, lematização, reconhecimento de entidades nomeadas, análise de dependência, entre outros. O SpaCy é amplamente utilizado em tarefas de NLP e pode ser aplicado no pré-processamento de dados para extrair informações relevantes e realizar análises mais avançadas.

Para utilizar essas bibliotecas, é necessário instalá-las previamente no ambiente Python em que o código está sendo executado. Você pode instalar as bibliotecas usando os seguintes comandos:

```!pip install Normaliser```
```!pip install spacy```
Esses comandos utilizam o gerenciador de pacotes pip para instalar as bibliotecas "Normaliser" e "SpaCy" em seu ambiente Python. Após a instalação, você pode importar essas bibliotecas em seu código e utilizar suas funcionalidades para realizar as etapas necessárias de pré-processamento do dataset.

4. Pipeline
No pré-processamento do dataset, são realizadas etapas de limpeza e preparação dos dados antes de serem usados em análises ou modelos de machine learning. Isso envolve a aplicação de técnicas e bibliotecas para transformar os dados brutos em um formato adequado para análise.

Neste caso, o pré-processamento do dataset foi realizado utilizando um pipeline que incluiu as seguintes etapas:

- Tokenização: A tokenização é o processo de dividir o texto em unidades menores, chamadas de tokens. Os tokens podem ser palavras individuais, pontuações, números, ou outras unidades significativas. A biblioteca "SpaCy" foi utilizada para realizar a tokenização dos textos, dividindo-os em tokens que podem ser processados individualmente.

- Retirada de stop words: Stop words são palavras comuns que geralmente não contribuem muito para o significado do texto, como "a", "o", "para", etc. A remoção de stop words é uma etapa comum no pré-processamento de textos para reduzir o ruído e melhorar a eficiência da análise. A biblioteca "SpaCy" foi utilizada para remover as stop words dos textos do dataset.

- Corretor de palavras: Um corretor de palavras é utilizado para identificar e corrigir erros ortográficos em palavras. A biblioteca "pyspellchecker" foi utilizada como corretor de palavras, verificando e corrigindo erros ortográficos nas palavras do texto.

- Transcrição de emojis: Emojis são símbolos usados para expressar emoções, sentimentos ou ideias em mensagens de texto. A biblioteca "emoji" foi utilizada para realizar a transcrição dos emojis presentes nos textos, convertendo-os em uma representação textual adequada.

- Correção de abreviações: Abreviações e formas reduzidas de palavras são comuns em mensagens de texto, mas podem dificultar a compreensão e análise dos textos. Foi utilizado um método para corrigir abreviações, substituindo-as por suas formas completas para facilitar a interpretação dos textos.

- Stemming: O stemming é um processo de redução de palavras à sua forma base ou radical. Ele remove os sufixos das palavras, mantendo apenas o núcleo significativo. O stemming pode ajudar a reduzir a dimensionalidade dos dados e agrupar palavras relacionadas. No pré-processamento, foi aplicado o stemming nas palavras do texto.

- Lematização: A lematização é um processo semelhante ao stemming, mas em vez de simplesmente remover sufixos, ele retorna a forma base da palavra com base em seu significado léxico. A lematização considera a parte gramatical da palavra e busca o "lemma" correspondente. O objetivo é obter uma representação mais precisa das palavras no texto. A biblioteca "SpaCy" foi utilizada para realizar a lematização das palavras.

Após a aplicação dessas etapas de pré-processamento, o texto tratado estará pronto para análises posteriores, como modelagem de tópicos, classificação de sentimentos, entre outros.

#### Modelos de vetorização:

Após as etapas de pré-processamento mencionadas anteriormente, foram utilizados dois modelos de vetorização para representar os textos de forma numérica. Esses modelos são:

- Bag of Words (Saco de Palavras): O modelo Bag of Words é uma abordagem comum na vetorização de textos. Ele cria uma representação numérica dos textos, considerando a frequência de ocorrência de cada - palavra em um documento ou em todo o corpus. Cada documento é representado por um vetor em que cada elemento corresponde a uma palavra e seu valor é a contagem de ocorrências dessa palavra no documento. Essa representação é adequada para muitas tarefas de processamento de texto, como classificação de documentos e análise de sentimentos.

- Word2Vec: O Word2Vec é um modelo de vetorização baseado em redes neurais que captura as relações semânticas entre as palavras. Ele mapeia palavras para vetores densos de valores reais, de modo que palavras semanticamente similares fiquem próximas no espaço vetorial. Essa técnica permite representar palavras como vetores contínuos e capturar relações de significado entre elas, como analogias e similaridades. O modelo Word2Vec é amplamente utilizado para tarefas de processamento de linguagem natural, como análise de sentimento, recomendação de palavras e tradução automática.

- Após a aplicação desses modelos de vetorização, o texto tratado é representado em forma numérica, pronta para ser utilizada como entrada para algoritmos de aprendizado de máquina ou análises estatísticas. O output dessas etapas de vetorização será uma matriz numérica em que cada documento é representado por um vetor de características correspondentes às palavras ou conceitos relevantes extraídos do texto.

#### Bibliotecas para os modelos de vetorização
Para o modelo acima, foram utilizadas as seguintes bibliotecas e técnicas para realizar o pré-processamento do texto:

- NLTK (Natural Language Toolkit): O NLTK é uma biblioteca popular em Python para processamento de linguagem natural. Ele oferece uma ampla gama de recursos e ferramentas para tarefas como tokenização, lematização, stemming, análise sintática, entre outros. A biblioteca NLTK foi utilizada para realizar algumas etapas de pré-processamento, como tokenização e stemming.

- Gensim: O Gensim é uma biblioteca de processamento de linguagem natural em Python que oferece ferramentas para modelagem de tópicos, indexação e similaridade de documentos. Neste contexto, o Gensim foi utilizado para aplicar o modelo Word2Vec mencionado anteriormente, que permite a vetorização baseada em palavras.

- CountVectorizer: O CountVectorizer é uma classe da biblioteca scikit-learn em Python que permite a vetorização de textos usando a abordagem Bag of Words. Ele transforma o texto em uma matriz numérica em que cada documento é representado por um vetor que contém a contagem de ocorrência de cada palavra. O CountVectorizer foi utilizado como um modelo de vetorização baseado em frequência de palavras.

- TfidfVectorizer: O TfidfVectorizer também é uma classe da biblioteca scikit-learn em Python que realiza a vetorização de textos usando a abordagem TF-IDF (Term Frequency-Inverse Document Frequency). Essa abordagem leva em consideração a frequência de uma palavra em um documento específico e sua frequência inversa em todo o corpus. Isso permite atribuir maior importância a palavras menos frequentes e reduzir a importância de palavras muito comuns. O TfidfVectorizer foi utilizado como um modelo de vetorização baseado no esquema TF-IDF.

- Após a aplicação dessas técnicas e bibliotecas de pré-processamento, o texto tratado é transformado em uma representação numérica adequada para análise posterior, como classificação de documentos, agrupamento de tópicos ou outros modelos de aprendizado de máquina. O output dessas etapas de vetorização será uma matriz numérica em que cada documento é representado por um vetor de características correspondentes às palavras relevantes extraídas do texto.


# Treinamento do Modelo
- O treinamento do modelo é uma etapa fundamental no desenvolvimento de sistemas de aprendizado de máquina. Nessa fase, um algoritmo é alimentado com um conjunto de dados de treinamento para aprender padrões e relacionamentos entre as variáveis de entrada e saída. O objetivo é obter um modelo capaz de fazer previsões ou tomar decisões com base nos dados fornecidos.

- Durante o treinamento do modelo, os dados de entrada são transformados em vetores numéricos por meio de técnicas de vetorização, como Bag of Words, Word2Vec, CountVectorizer ou TfidfVectorizer. Essa representação numérica permite que o modelo compreenda e processe os dados textuais de forma eficiente.

## Algoritmos:
### - CatBoost
- O CatBoost é um algoritmo de aprendizado de máquina desenvolvido pela Yandex. Ele é particularmente adequado para lidar com dados categóricos, como variáveis com valores discretos. O CatBoost utiliza a técnica de "gradient boosting" para construir um modelo preditivo. Ele é capaz de tratar automaticamente variáveis categóricas, evitando a necessidade de codificação manual dessas variáveis. Além disso, o CatBoost inclui recursos como tratamento automático de valores ausentes e implementações eficientes para lidar com grandes conjuntos de dados.

### Naive Bayes
- O Naive Bayes é um algoritmo de aprendizado de máquina probabilístico baseado no teorema de Bayes. Ele é amplamente utilizado em problemas de classificação de texto, como filtragem de spam, análise de sentimento e categorização de documentos. O Naive Bayes assume a independência entre as características, o que simplifica o cálculo das probabilidades condicionais. Embora essa suposição simplificadora nem sempre seja verdadeira na prática, o Naive Bayes é conhecido por sua simplicidade, eficiência computacional e bom desempenho em muitos casos.

## Métricas de Avaliação do Modelo
- Ao avaliar o desempenho de um modelo de aprendizado de máquina para tarefas de classificação, é comum utilizar várias métricas para medir sua eficácia. Algumas métricas comumente usadas incluem:

### Precisão: 
- A precisão é a proporção de exemplos classificados corretamente como positivos em relação a todos os exemplos classificados como positivos, ou seja, a capacidade do modelo de evitar classificar incorretamente exemplos negativos como positivos.

### F1-Score: 
- O F1-Score é uma métrica que combina a precisão e o recall de um modelo. É a média harmônica dessas duas métricas e fornece uma medida equilibrada do desempenho do modelo em termos de precisão e capacidade de recuperar exemplos positivos.

### Recall: 
- O recall, também conhecido como taxa de verdadeiros positivos, é a proporção de exemplos positivos corretamente classificados em relação a todos os exemplos verdadeiramente positivos presentes no conjunto de dados. O recall mede a capacidade do modelo de identificar corretamente os exemplos positivos.

### Acurácia (métrica central):
- A acurácia é a proporção de exemplos classificados corretamente em relação a todos os exemplos do conjunto de dados. É uma métrica amplamente utilizada como medida geral de desempenho de um modelo. Ela fornece uma visão geral de quão bem o modelo está fazendo em todas as classes, considerando tanto os verdadeiros positivos quanto os verdadeiros negativos.

- Essas métricas são utilizadas para avaliar diferentes aspectos do desempenho do modelo em tarefas de classificação. A precisão é útil quando o foco está na minimização de falsos positivos, enquanto o recall é importante quando é necessário evitar falsos negativos. O F1-Score é uma métrica balanceada que leva em consideração tanto a precisão quanto o recall.

- Ao interpretar essas métricas, é importante considerar a natureza do problema e os requisitos específicos do contexto em que o modelo está sendo aplicado. Uma alta precisão pode ser fundamental em algumas situações, enquanto um alto recall pode ser mais importante em outras.

- Além dessas métricas, existem outras que também podem ser utilizadas, dependendo do contexto. Algumas delas incluem a área sob a curva ROC (Receiver Operating Characteristic), a matriz de confusão, o índice de Gini e a taxa de erro.

- Ao avaliar o desempenho de um modelo, é essencial considerar várias métricas e analisar seus resultados de forma holística, levando em conta as necessidades e os objetivos específicos do problema em questão.

## Bibliotecas:
### - Sklearn
- O Sklearn, é uma biblioteca amplamente utilizada em Python para aprendizado de máquina. Ela oferece uma variedade de algoritmos e ferramentas para tarefas como classificação, regressão, agrupamento e pré-processamento de dados. O sklearn possui uma interface consistente e intuitiva, o que facilita a construção e avaliação de modelos de aprendizado de máquina. Além disso, ele fornece funções para dividir conjuntos de dados em treinamento e teste, realizar validação cruzada, aplicar métricas de avaliação e muito mais.

### SpaCy
- O SpaCy é uma biblioteca de processamento de linguagem natural (NLP) escrita em Python. Ela fornece uma ampla gama de recursos e ferramentas para realizar tarefas de processamento de texto, como tokenização, lematização, identificação de entidades nomeadas, análise sintática, entre outros. O SpaCy é conhecido por sua eficiência e desempenho, sendo capaz de processar grandes volumes de texto de forma rápida. Ele também possui modelos pré-treinados para várias línguas, que podem ser utilizados para tarefas de análise de texto sem a necessidade de treinamento adicional. O SpaCy é uma escolha popular para desenvolvedores e pesquisadores que trabalham com NLP devido à sua facilidade de uso e eficácia em diversas aplicações.

# Serviço - API
- Um serviço de API (Interface de Programação de Aplicativos) permite que os modelos de aprendizado de máquina sejam implantados e acessados de forma fácil e conveniente por meio de uma interface de programação. Ele oferece a capacidade de expor o modelo treinado como um serviço online, permitindo que os usuários façam solicitações e recebam previsões ou resultados do modelo em tempo real.

- Ao fornecer um serviço de API, é possível integrar o modelo de aprendizado de máquina em diferentes aplicativos, plataformas ou sistemas, permitindo sua utilização em diversos contextos. Isso facilita a implementação e o consumo do modelo, eliminando a necessidade de executar todo o processo de treinamento e inferência localmente.

## Pipeline
- Um pipeline, no contexto de processamento de linguagem natural (NLP), é uma sequência de etapas ou transformações aplicadas a um texto durante o pré-processamento ou a análise. Ele consiste em encadear diferentes componentes, como tokenização, remoção de stop words, lematização, entre outros, para obter um resultado final desejado.

- O uso de um pipeline permite automatizar e sistematizar o fluxo de trabalho de processamento de texto, aplicando uma série de operações em sequência. Cada etapa do pipeline é executada de forma consecutiva, utilizando os resultados intermediários como entrada para a próxima etapa.

- Os pipelines são úteis para organizar e reutilizar o código de pré-processamento de texto, permitindo que diferentes textos passem por um conjunto consistente de etapas. Eles também simplificam o processo de análise e extração de informações dos textos, fornecendo uma estrutura clara para a implementação de fluxos de trabalho de NLP.

## Modelos de Vetorização
- Os modelos de vetorização são técnicas utilizadas para representar palavras ou documentos como vetores numéricos, de modo a serem processados por algoritmos de aprendizado de máquina. Essas representações vetoriais são essenciais para que os modelos de aprendizado de máquina possam trabalhar com dados textuais, que são representados por sequências de caracteres.

- Existem diferentes modelos de vetorização, cada um com suas características e abordagens específicas. Alguns exemplos comuns incluem o Bag of Words (BoW), que representa cada documento como um vetor contendo a contagem de ocorrência de cada palavra, e o Word2Vec, que mapeia cada palavra para um espaço vetorial de dimensões reduzidas, capturando relações semânticas entre palavras.

- A vetorização de textos é uma etapa crucial no processamento de linguagem natural, pois permite que as informações textuais sejam traduzidas em representações numéricas que podem ser processadas pelos algoritmos de aprendizado de máquina.

## Visualização dos Dados
- A visualização dos dados é uma técnica utilizada para representar informações de forma gráfica ou visual, permitindo uma compreensão mais intuitiva dos padrões, tendências e relações presentes nos dados. No contexto de processamento de linguagem natural (NLP), a visualização dos dados pode ser aplicada para explorar e entender características dos textos, tais como a frequência de palavras, distribuição de tópicos ou sentimentos.

- As técnicas de visualização de dados podem incluir gráficos de barras, gráficos de dispersão, nuvens de palavras, mapas de calor, nuvens de palavras, entre outros. Essas representações visuais podem ajudar a identificar insights, detectar padrões, destacar outliers e comunicar informações de forma mais eficaz.

- A visualização dos dados é uma ferramenta poderosa para auxiliar na exploração e análise de grandes conjuntos de dados textuais. Ela permite visualizar as características textuais de maneira intuitiva, facilitando a identificação de tendências e a comunicação dos resultados de forma clara e concisa.

- Ao visualizar os dados textuais, é possível obter uma visão geral das informações contidas nos textos, identificar palavras-chave relevantes, verificar a distribuição de palavras ao longo do tempo ou comparar diferentes categorias ou grupos de textos.

- A visualização dos dados textuais pode ser realizada utilizando bibliotecas gráficas como o Matplotlib, Seaborn ou Plotly, que oferecem uma ampla variedade de opções e recursos para criar visualizações atrativas e informativas.

## API do Modelo
- A API do modelo é uma interface que permite a comunicação e interação com um modelo de aprendizado de máquina implantado em um serviço ou servidor. Essa API define os endpoints e métodos disponíveis para fazer solicitações e receber respostas do modelo.

- Ao expor um modelo como uma API, é possível enviar dados para o modelo e obter previsões ou resultados processados em tempo real. Isso facilita a integração do modelo em diferentes aplicativos, sistemas ou plataformas, permitindo sua utilização de forma flexível e escalável.

- A API do modelo pode receber dados como parâmetros de entrada, realizar a pré-processamento necessário, aplicar o modelo treinado e retornar as previsões ou resultados ao usuário. Ela pode ser implementada usando frameworks web, como Flask ou Django, que fornecem ferramentas para criar e gerenciar uma API de forma eficiente.

- A API do modelo permite que o modelo de aprendizado de máquina seja consumido de maneira mais acessível e fácil, oferecendo uma interface consistente e simplificada para interagir com o modelo e obter os resultados desejados.

<img src = "![Captura de Tela 2023-05-30 às 17 27 47](https://github.com/2023M6T4-Inteli/Projeto2/assets/99759369/990249b2-9540-4b8a-923b-3432ccb20ff1)">



## (Sprint 4) Proposta de uma nova modelagem utilizando novas features (IPYNB)

- Elmo: https://github.com/2023M6T4-Inteli/Projeto2/blob/main/src/Notebook/ELMo.ipynb 

- BERT: https://github.com/2023M6T4-Inteli/Projeto2/blob/main/src/Notebook/3_2_BERT(OVER).ipynb

- DOC2Vec: https://github.com/2023M6T4-Inteli/Projeto2/blob/main/src/Notebook/DOC2Vec_2.ipynb

- GloVe: https://github.com/2023M6T4-Inteli/Projeto2/blob/main/src/Notebook/GloVe.ipynb 

- FastText: https://github.com/2023M6T4-Inteli/Projeto2/blob/main/src/Notebook/Fast_Text.ipynb 

- TF_IDF: https://github.com/2023M6T4-Inteli/Projeto2/blob/main/src/Notebook/TF_IDF_com_Regressao_logistica.ipynb


## (Sprint 4) Documentação da proposta de uma nova modelagem

## 1. Elmo 

O Elmo (Embeddings from Language Models) é um modelo de vetorização pré-treinado que captura representações contextuais de palavras e frases. 
Tal utilização é fundamentada nas características estruturais do modelo. Evidencia-se a possibilidade de identificar palavras iguais ou semelhantes em contextos diferentes, agrupá-los e diferenciá-los.
O modelo se destaca dado que possui capacidade de generalização, dado que, foi treinado em grandes quantidades de texto. 
Ao aplicá-lo, a fim de obter melhores resultados, utiliza-se o csv do texto pré-processado. Em seguida, aplica-se no modelo de vetorização ELMo. 
É de indubitável importância ressaltar que para a utilização do ELMo os arquivos de pré-treinamento, em português precisam ser importados.
```
weight_file = "/content/drive/MyDrive/Colab Notebooks/SI-MOD6/entrega_spt4/elmo_pt_weights_dgx1 (1).hdf5
```
Já a linha a seguir, define o local do arquivo JSON de opções para o modelo ELMo em português. O arquivo JSON contém a configuração e os hiperparâmetros do modelo.
```
options_file = 'https://s3-us-west-2.amazonaws.com/allennlp/models/elmo/contributed/pt/brwac/options.json'
```
As frases de input são convertidas em identificadores de caracteres e, em seguida, é calculado os embeddings correspondentes. Os resultantes são armazenados em um array. Após a vetorização dos dados, os mesmos são direcionados para a rede neural simples. 
Na rede neural, seta-se 2 dimensões dos embeddings redimensionados, uma vez que, a dimensionalidade do input, sem tratamento, é incompatível com o suporte da rede. Na mesma, são passados os vetores resultantes do ELMo e os targets. <br>

Defini-se, então, a arquitetura da rede neural em duas camadas densas. A primeira camada possui 2 unidades com ativação sigmoidal, e a segunda camada possui 1 unidade com ativação sigmoidal. <br>
Destaca-se a utilização do otimizador “Adam” devido a frequente utilização em conjuntos de dados enxutos e com redes profundas. Além disso, o otimizador atualiza os pesos da rede mais rapidamente.<br>

A métrica escolhida para avaliar o resultado do modelo é recall, visto que, dentre todas as classificações positivas como valor esperado, quantas foram assertivas. Entretanto, ocorreram alguns desajustes durante o arranjo da rede neural. Portanto, nesse momento, a fim de avaliar a performance geral, utiliza-se a acurácia. <br>
Os resultados emitidos na rede neural demonstram 43.17% de acurácia. A porcentagem apresentada, em consideração ao que é considerado ideal ou avaliativo para os modelos, não é satisfatória para aplicação, em comparação à modelos que obtiveram resultados mais assertivos. <br>

Em síntese, destaca-se que esse número pode ser melhorado em decorrência da separação dos dados de treino e teste, diferenciação no número de epochs e variação nas dimensões.



## 2. BERT 

O BERT (Bidirectional Encoder Representations from Transformers) é um modelo de linguagem baseado em Transformers, arquitetura que é baseada em mecanismos de "atenção" e relevância. Isto permite que o modelo capture relações de dependência entre palavras de maneira eficiente e paralela. 

Neste caso, o que utilizamos é uma versão pré-treinada, com o uso do "preenchimento de máscara" (masked language modeling), com a intenção de uma futura implementação da funcionalidade de predição da "próxima sentença" (next sentence prediction). Uma das principais características do BERT é sua capacidade de gerar representações contextualizadas de palavras. O modelo leva em consideração o contexto em que uma palavra aparece, o que ajuda a capturar relações e significados mais precisos. Consequentemente, essas representações contextualizadas são obtidas através do pré-treinamento bidirecional e podem ser usadas como entrada para o algoritmo.

- Algoritmo: Rede Neural 

Como algoritmo, utilizamos a Rede Neural na arquitetura Transformers, para realizar as etapas de predição.

Etapas de implementação 

- Preparação dos dados (exemplo com Label Encoder realizado):

```
label_encoder = LabelEncoder()

df_lemma['sentimento_3'] = label_encoder.fit_transform(df_lemma['sentimento'])

```

- Pré-treinamento do modelo BERT:

```
model = BertModel.from_pretrained('neuralmind/bert-base-portuguese-cased')
```

Esta etapa envolve também a definição dos parâmetros, a alimentação dos dados no modelo, atribuição dos tensores e da famosa "attention_mask".

- Avaliação e ajuste: 

  Nesta etapa realizamos a avaliação do modelo, com base nos dados de treino e teste que foram previamente divididos, e realizamos a iteração do modelo sobre o conjunto de treinamento, para assim, em seguida, atribuir as predições às categorias (e targets) definidos. Por fim, realizamos a impressão das métricas de classificação.


Após diversas implementações do modelo, e devido a sua complexidade nas etapas de entrada da Rede Neural, obtivemos resultados medianos com o modelo BERT. Consequentemente, com a primeira implementação, na métrica de maior relevância para o projeto, o "Recall" obtivemos 72% (0.72). Em termos de assertividade, em comparação aos outros modelos foi o nosso terceiro maior. 

No entanto, devido ao seu alto nível de complexidade, obtivemos resultados com muitos sinais de overfitting e do enviesamento na entrada dos tensores, o que ocorreu após tentativa de resolução de problemas no código.

Devido a isso, tratamos o modelo BERT como um "nice to have", mas não como principal modelo a ser utilizado. Mesmo assim, consideramos que na escala de modelos com algoritmos de Rede Neural, é com certeza o que mais gera escalabilidade e por isso há o interesse em sua implementação.

**Próximos passos**

  - Fine-tuning para tarefas específicas:
    Depois do pré-treinamento, o BERT pode ser ajustado (fine-tuned) para tarefas específicas, como classificação de texto, extração de informações e resposta a perguntas. Ao ajustar o BERT para uma tarefa específica, as camadas de classificação são adicionadas ao modelo e o modelo é treinado em um conjunto de dados rotulados para aprender a tarefa específica.

- Atention Mask: 
  Na tarefa de preenchimento de máscara, palavras são mascaradas aleatoriamente e o modelo é treinado para prever as palavras mascaradas com base no contexto das palavras vizinhas e sua relevância.

É importante citar que o modelo BERT tem sido amplamente utilizado em uma variedade de tarefas de processamento de linguagem natural e estabeleceu um novo parâmetro em muitas delas. Isso foi um dos fatores determinantes para a escolha e utilização deste modelo em nosso grupo. Ele se destaca pela sua capacidade de capturar informações contextuais em textos e fornecer representações de alta qualidade que podem ser usadas em várias aplicações de NLP.

## 3. Doc2Vec

O modelo Doc2Vec é uma técnica de aprendizado de máquina utilizada para representar documentos em formato vetorial. Ele é uma extensão do modelo Word2Vec, que é usado para representar palavras em vetores. O Doc2Vec permite que documentos inteiros sejam representados como vetores contínuos de valores numéricos, capturando o contexto semântico dos documentos.

O objetivo do Doc2Vec é gerar representações vetoriais para documentos que preservem a semântica e a similaridade entre eles. Essas representações vetoriais podem ser usadas em várias tarefas de processamento de linguagem natural, como classificação de documentos, recomendação de conteúdo, agrupamento de documentos semelhantes e recuperação de informações.

Algoritmos utilizados: Naive Bayes, Regressão Logística e Rede Neural

No processamento do modelo, realizamos alguns tipos de taggeamento, que são próprios para treinamento do modelo, assim como a definição de parâmetros e outros recursos de vetorização. Abaixo segue o exemplo de taggeamento:

```
tagged_data = [TaggedDocument(words=word_tokenize(text.lower()), tags=[str(i)]) for i, text in enumerate(dados['texto'])]

```

Após estas definições realizamos a vetorização dos tokens com base nas definições da própria biblioteca gensim, e após impressão das iterações destes vetores, podemos aplicar nos algoritmos.

** É importante ressaltar que a métrica de avaliação central foi o Recall **. 

Na primeira implementação, com Regressão Logística, tivemos a porcentagem de 58% (0.58), em relação às classificações, assim como na segunda implementação em Random Search, que obtivemos, também, o recall em 58%. Já na terceira implementação utilizando Naive Bayes, conseguimos o bom resultado de 82% (0.82) em recall. 

Por fim, implementamos a Rede Neural, apenas para satisfazer os termos acadêmicos, e obtivemos a acurácia de 73% (0.73).

No caso específico, o modelo Doc2Vec foi escolhido como modelo final devido às suas vantagens e desempenho em relação aos outros métodos de representação de documentos. Além disso, levamos em conta a sua aplicabilidade, tendo em vista que o Doc2Vec é capaz de capturar relações semânticas complexas entre palavras e documentos, gerando vetores que preservam a semelhança semântica entre textos.

Também foi evidenciado, nos testes que realizamos, que o modelo Doc2Vec possui uma implementação mais simples, eficiente e bem estabelecida na biblioteca Gensim, o que facilita sua utilização e treinamento. E em termos de assertividade, com a métrica de prioridade (Recall), em relação aos outros modelos, o modelo Doc2vec foi muito bem.

## 4. GloVe

O Global Vectors for Word Representation, também conhecido como GloVe, é um modelo de vetorização de palavras desenvolvido com o intuito de identificar as relações sintáticas e semânticas em um conjunto de um texto. Esse modelo, utiliza estatísticas de co-ocorrência global de palavras para desenvolver representações vetoriais. O seu processo de treinamento, envolve a construção de uma matriz que registra a frequência da ocorrência das palavras a partir da utilização da 'função de perda' (loss function) com o intuito de maximizar a probabilidade de co-ocorrência de pares de palavras. 

- Algoritmo: Regressão Logística 

O código está trabalhando com a leitura de um arquivo CSV, contendo os dados lematizados que já passaram pelo Pré-Processamento. Depois disso, como mostra o código abaixo, foi realizado o carregamento do modelo spaCy com vetores GloVe e feito um teste com a palavra 'amor' para calcular seus vetores. 

```
import spacy

# Carregamento do modelo com a utilização de vetores GloVe
nlp = spacy.load('en_core_web_sm')

# Vetor da palavra teste (amor)
word_vector = nlp('amor')[0].vector
print("Vetor de 'amor':", word_vector)
```

Após isso, foi realizado a utilização da classe CountVectorizer do sklearn.feature_extraction.text para vetorizar os dados contidos na coluna "texto" doDataframe desenvolvido. Assim, a vetroização foi aplicada aos dados de teste (x_test) e treinamento (x_train) e armazenados em duas variáveis com o parâmetro 'random_state' definido como 42. Depois disso, foi realizado o treinamento do modelo de regressão logística utilizando os dados de treinamento. Dessa forma, a acurácia do modelo é calculada a partir do método score com X_test e y_test. 



```
X = df_lemma['texto']
y = df_lemma['sentimento']

vectorizer = CountVectorizer()
X_counts = vectorizer.fit_transform(X)
tfidf_transformer = TfidfTransformer()
X_tfidf = tfidf_transformer.fit_transform(X_counts)

X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print("Acurácia:", accuracy)
```
Com base nos resultados obtidos é possível fazer as seguintes análises do algoritmo de Regressão Logística. A acurácia obtida para o modelo foi de 0.75, o que indica uma boa significância e uma taxa de acerto razoavelmente alta. Além disso foi também calculado os valores de precisã para cada uma das classes desenvolvidas. O valor obtido para as classe NEGATIVE, NEUTRAL e POSITIVE foram: 0,77; 0,71; e 0,81 respectivamente. Valores relativamente bons. Além disso, foi obtido também os valores de recall para cada uma das classes (NEGATIVE = 0,54; NEUTRAL = 0,85 e POSITIVE = 0,75. 
Por fim, foi então calculado o F1-score, que é uma medida que combina a precisão e o recall em uma única métrica. Para a classe NEGATIVE, o F1-score é de 0,64, para a classe NEUTRAL é de 0,77 e para a classe POSITIVE é de 0,78.que o modelo tem uma taxa de acerto razoavelmente alta.




- Algoritmo: Modelo Naive Bayes 

Primeiramente foi mapeado os rótulos 'POSITIVE', 'NEUTRAL' e 'NEGATIVE' para os valores numéricos 3, 1 e 2, respectivamente, e o resultado foi armazenado em uma variável. 

```
sentimento_mapping = {'POSITIVE': 3, 'NEUTRAL': 1, 'NEGATIVE': 2}
y_mapped = df['sentimento'].map(sentimento_mapping)
```

Depois disso, foi realizado o treinamento do modelo Naive Bayes Gaussiano, porém não foi obtido um valor de acurácia tão satisfatório, equivalente a 0.57. Isso indicou que o modelo tem uma taxa de acerto um pouco mais baixa com o valor obtido previamente com o algoritmo da regressão logística.

```
model = GaussianNB()
model.fit(X_train, y_train)

# Predição e cálculo da acurácia
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
```



Por fim, foi realizado um gráfico de plotagem da curva ROC, que pode ser visto abaixo. 


<img src = "https://github.com/2023M6T4-Inteli/Projeto2/blob/main/assets/Imagens/GloVe.png">


Em resumo, os resultados obtidos indicam que o modelo de regressão logística teve um desempenho melhor em comparação com o modelo de Naive Bayes. A regressão logística obteve uma acurácia mais alta e um melhor equilíbrio entre precisão e recall. Além disso, o gráfico de curva ROC mostra que o modelo de regressão logística possui uma capacidade satisfatória de distinguir entre as diferentes classes. No entanto, é importante lembrar que esse modelo obteve valores bons, porém não foram os melhores diante dos outros modelos desenvolvidos.


## 5. FastText

O FastText é uma biblioteca gratuita e de código aberto do Facebook AI Research (FAIR) para aprender embeddings e classificações de palavras. Este modelo permite a criação de um algoritmo de aprendizado para a obtenção de representações vetoriais de palavras, avaliando esses modelos.

Primeiramente, os valores da coluna alvo foram transformados em valores numéricos:

```
df_2['sentimento'] = df_2['sentimento'].map({'NEUTRAL': 0, 'POSITIVE': 1, 'NEGATIVE': -1})
```

Foi feito o teste com o modelo possuindo 50 e 100 dimensões mas, como a diferença não foi significante, foi utilizado o de 50. O modelo de word embeddings pré treinadas foi instalado do repositório de word embeddings do NILC. Para aplicação no projeto, foi utilizada a base de dados com os dados já lematizados e tratados. O modelo foi carregado e aplicado em uma vetorização da coluna 'tokens', assim como é feito com o modelo Word2Vec. 

```
# Função para vetorizar um token
def vetorizar_token(token):
    vetor = np.zeros(model.vector_size) # incializa vetor de zeros com a mesma dimensão
    if token in model: # verifica se a palavra está no word2vec treinado
        vetor = model[token] # adiciona o valor do vetor
    return vetor

# Função para vetorizar uma frase
def vetorizar_frase(frase):
    vetores_tokens = [vetorizar_token(token) for token in frase] # verifica cada token da lista
    return np.sum(vetores_tokens, axis=0) # retorna a soma dos vetores

# Aplicar a função 'vetorizar_frase' a todas as frases
df_2['vetores'] = df_2['tokens'].apply(vetorizar_frase)
```

Após isso, com os vetores criados, foram aplicados o modelo Naive Bayes (que retornou uma acurácia de 0.31) e a Regressão Logística (com esta última obtendo um melhor resultado, com acurácia de 0.56). Estes resultados foram um pouco inferiores em relação aos testes realizados em outros modelos com os mesmos algoritmos (Regressão logísitica e Naive Bayes). Sendo assim, o modelo não foi considerado com grande relevância para a escolha do modelo final.

Com base nos resultados e processamentos, construímos diferentes gráficos: o da curva ROC, o da curva de aprendizado e o da curva de validação. 

Abaixo estão os gráficos da curva ROC obtidos com cada modelo:

![image](https://github.com/2023M6T4-Inteli/Projeto2/assets/99270135/0a41966a-07cd-4309-ae1e-d80c82755166)

![image](https://github.com/2023M6T4-Inteli/Projeto2/assets/99270135/0a6b22a9-7f79-4ba9-8b96-97f243fa2915)

## 6. TF-IDF

O TF-IDF (Term Frequency-Inverse Document Frequency) é uma medida estatística que permite avaliar a importância de uma palavra em um documento. Essa técnica foi escolhida por sua capacidade de destacar palavras-chave relevantes e reduzir o peso de palavras comuns, ajudando a identificar a relevância de um termo em relação ao contexto específico de um documento. Suas vantagens incluem a capacidade de lidar com grandes volumes de texto de maneira eficiente, reduzindo essa influência de palavras comuns e destacando exatamente os termos-chave que fornecem insights relevantes. O TF-IDF também é uma técnica simples de implementar e interpretar.

- Algoritmo: Regressão Logística 

A Regressão Logística é um algoritmo de aprendizado de máquina que é amplamente utilizado para tarefas de classificação binária. Ele modela a relação entre variáveis independentes e a probabilidade de uma resposta pertencer a uma determinada classe. Sua escolha foi feita especialmente pela sua capacidade de lidar com dados categóricos (como é o caso da base de dados trabalhada).

A combinação de TF-IDF com Regressão Logística aproveita as vantagens de ambos os métodos. O TF-IDF fornece uma representação ponderada das palavras em um documento, enquanto a Regressão Logística modela a relação entre essas palavras e a probabilidade de classificação. Essa combinação é comum em processos de análise de sentimentos como esse.
<br>
<br>
A base de dados utilizada já passou pelos primeiros processos de PLN (remoção de stop words, substituição de gírias e, em destaque, a lematização). Essa é a mesma base de dados lematizada que foi desenvolvida na Sprint 3 e utilizada no modelo anterior. Contudo, apenas as colunas das frases e suas qualificações estão sendo utilizadas. 
<br>
```
#dividi os dados em conjunto de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(dados["texto"], dados["sentimento"], test_size=0.2, random_state=42)
```
Após a importação da base de dados no modelo, foi feita uma divisão dos dados em conjunto de treinamento e teste, com o test size de 0.2 e random state de 42.
<br>
```
#cria pipeline com TF-IDF e modelo de classificação
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("model", LogisticRegression(max_iter=1000))  # número máximo de iterações
])
```
Como já indicado, o modelo criado utiliza TF-IDF com Regressão Logística para a análise de sentimentos. Para a regressão Logística o número de iterações foi configurado para mil a fim de conseguir um modelo que identifica mais correlações entre as palavras.
<br>
<br>
Para avaliar os resultados obtidos foi utilizado principalmente os parâmetros de Recall e Acurácia 
<br>

<img src = "https://github.com/2023M6T4-Inteli/Projeto2/blob/main/assets/Imagens/TF-IDF_Dados.png" alt="td-idf dados" width="500" height="auto">

<img src = "https://github.com/2023M6T4-Inteli/Projeto2/blob/main/assets/Imagens/TF-IDF_grafico.png">

<br>

Com base nos resultados obtidos, podemos concluir que o modelo apresenta um desempenho equilibrado e consistente, com valores de acurácia e recall macro próximos, na faixa de 0,7. Isso indica que o modelo é capaz de fazer previsões precisas na maioria das amostras de teste, classificando corretamente tanto as instâncias positivas quanto as negativas.

Além disso, a similaridade entre a acurácia e o recall macro sugere que o modelo não está enviesado para uma classe específica e está tratando ambas as classes de forma equilibrada.

<img src = "https://github.com/2023M6T4-Inteli/Projeto2/blob/main/assets/Imagens/TF-IDF_MC.png">

A partir da matriz de confusão é possível perceber que o modelo tem mais dificuldades ao avaliar comentários neutros e uma facilidade para avaliar positivos e, em segundo lugar, negativos. Os resultados nessa instância foram satisfatórios.

Por fim, o modelo obteve bom resultados em avaliações de recall, acurácia e matriz de confusão, contudo, não foram os melhores diante dos outros modelos desenvolvidos.


## 7.Comparação entre os modelos e escolha do modelo final

Os modelos foram submetidos aos seus respectivos processos de vetorização e, em seguida, aos mesmos algoritmos, sendo eles, regressão logística e naive bayes, a fim de garantir a avaliação conforme a mesma otimização. Além do mais, ressalta-se a utilização do recall como métrica central de avaliação, pois, para a problemática estabelecida, é importante identificar verdadeiros positivos.

Portanto, observa-se, respectivamente, as maiores precisões dos modelos: Doc2Vec, GloVe, Bert, TF-IDF e Fast-Text. Dessa forma, nota-se esse resultado como possibilidade de realizar melhores combinações no modelo Doc2Vec e os algoritmos associados, com o objetivo de resultantes mais precisos.

<img src = "https://github.com/2023M6T4-Inteli/Projeto2/blob/main/assets/Imagens/gr%C3%A1fico_comparativo.png">

Esclarece-se que os resultados do ELMo não são expostos na comparação entre os modelos, dado que, durante a exploração do mesmo, foi possível perceber a complexidade no qual está equiparado, além da utilização de redes neurais profundas, diferente dos demais modelos, que utilizam algoritmos.

## 8.Adicionando Features Novas

Foram criadas novas features baseadas no tamanho das frases, em particular o número de tokens por frase, para comparar com modelos que incluam ou não essas features. Quatro algoritmos foram utilizados para esta comparação: regressão logística, cat-boost, naive-bayes e xg-boost. A vetorização escolhida para esta comparação foi o TF-IDF devido sua facilidade de aplicação e a combinação com os algoritimos escolhidos. Todos os modelos que utilizaram as novas features tiveram resultados inferiores em comparação aos modelos que não as utilizaram, apresentando uma média de recall de 38.7. No entanto, a inclusão das novas features permitiu a utilização do gráfico KDE (Estimativa de Gráfico Kernel) que demonstra a probabilidade de um sentimento, dado o número de tokens de uma frase. Onde -1 representa sentimentos negativos, 0 representa sentimentos neutros e 1 representa sentimentos positivos.

![image](https://github.com/2023M6T4-Inteli/Projeto2/assets/99209230/5500412f-e3df-499d-baea-1ff9c862f9b1)

Cálculo KDE para a Estimativa:
KDE(x) = (1 / (n * h)) * Σ K((x - xi) / h)
KDE(x) é o valor estimado da densidade de probabilidade para um determinado ponto x. n é o número total de pontos de dados no conjunto de dados. h é o parâmetro de suavização ou largura de banda (bandwidth). Σ representa a soma ao longo de todos os pontos de dados. K é a função kernel, que é uma função simétrica em torno de zero que define a forma da contribuição de cada ponto de dados para a estimativa de densidade.



Comparação entre os modelos com a feature aplicada:

![image](https://github.com/2023M6T4-Inteli/Projeto2/assets/99209230/6212235f-588c-466f-9439-38f3751095c6)


Maior valor(cat-boost):

![image](https://github.com/2023M6T4-Inteli/Projeto2/assets/99209230/4c7c25b6-fa7a-4f83-8143-d0c970215746)


Modelos sem a adição da feature aplicada:

![newplot](https://github.com/2023M6T4-Inteli/Projeto2/assets/99209230/af9eb689-e0a6-4ce9-b0de-e08411b1dc27)


Maior valor(xg-boost):

![image](https://github.com/2023M6T4-Inteli/Projeto2/assets/99209230/f4a55487-b5b3-4d7a-94bd-ef23f8c63b03)



## (Sprint 5) Apresentação Final

Colocar o link do artefato (deve estar na pasta apresentacoes do repositório do projeto).

## (Sprint 5) Deploy do melhor modelo

Colocar o link dos artefatos (devem estar nas pastas videos e src do repositório do projeto).

## (Sprint 5) Documentação da Solução

Preencher conforme a descrição do artefato na Adalove.
