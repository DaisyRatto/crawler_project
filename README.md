# The Guardian News Crawler
Este projeto consiste em um crawler que coleta notícias do site theguardian.com e armazena esses dados no BigQuery para realizar as consultas desejadas. <!-- e disponibiliza uma API para busca desses dados. -->

## Índice

- [Introdução](#introdução)
- [Funcionalidades](#funcionalidades)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Uso](#uso)

## Introdução
Este projeto é um crawler que coleta artigos de notícias do site theguardian.com. Foi utilizado o framework Scrapy para ajudar no desenvolvimento deste projeto e as notícias coletadas foram armazenadas no BigQuery para análise e consulta. O intuito  <!-- Uma API RESTful é fornecida para facilitar a busca e recuperação desses dados.  -->

## Funcionalidades

- Coleta as notícias do site theguardian.com/au (código desta funcionalidade está em news_scraper/news_scraper/spiders/news_spider.py);
- Os dados coletados são: URLs, títulos e subtítulos dos artigos, data de lançamento do artigo, nome do autor e a categoria daquela notícia;
- As coletas feitas estão na pasta news_scraper em formato CSV e em JSON;
- A coleta dos dados foram armazenados no Google BigQuery no formato CSV.

## Requisitos

- Python 3.7 ou superior;
- Scrapy 2.11.2;
- Conta no Google Cloud com acesso ao BigQuery;
- Criar um projeto no BigQuery.

## Instalação
### Clone o Repositório
~~~bash
git clone https://github.com/seu-usuario/crawler_project.git
cd the-guardian-news-crawler
~~~

### Crie um Ambiente Virtual
~~~bash
python -m venv venv
venv\Scripts\activate # No Mac, use 'source venv/bin/activate' 
~~~

### Instale as Dependências
~~~bash
pip install -r requirements.txt
~~~

## Uso

Para visualizar esses dados, vamos inserir nosso arquivo news_scraper.csv em nosso projeto do BigQuery. 

Caso queira extrair esses dados novamente, entre na pasta
~~~bash 
cd news_scraper/news_scraper
~~~
Execute o crawler para criar um novo arquivo.csv e escolha um nome diferente do arquivo existente
~~~bash 
scrapy crawl news_spider -o nome_do_novo_arquivo.csv
~~~

Com o arquivo.csv pronto, basta inserir no seu projeto do BigQuery e para isso você deve criar o seu conjunto de dados dentro do seu projeto e dentro deste conjunto de dados criar uma tabela.

No momento de criação da tabela é importante, no 'Esquema', atribuir os nomes dos campos para cada tipo de dado. 

# Exemplo de Consultas/Querys
Consultas para fazer no BigQuery

## Buscar todas as notícias por ordem dos primeiros artigos encontrados
~~~bash 
SELECT *
 FROM `lima-news-crawler-project.news_data.news_data`
 ORDER BY article_release_date;
~~~

## Retornar valor pela 'palavra-chave' na coluna escolhida
~~~bash 
SELECT *
 FROM `lima-news-crawler-project.news_data.news_data`
 WHERE topic 
 LIKE ('%culture%');
~~~