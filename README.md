# The Guardian News Crawler
Este projeto consiste em um crawler que coleta notícias do site theguardian.com e armazena esses dados no BigQuery para realizar as consultas desejadas. <!-- e disponibiliza uma API para busca desses dados. -->

## Índice

- [Introdução](#introdução)
- [Funcionalidades](#funcionalidades)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Exemplo de Consultas/Querys Simples](#exemplo-de-consultasquerys-simples)

## Introdução
Este projeto é um crawler que coleta artigos de notícias do site theguardian.com. Foi utilizado o framework Scrapy para ajudar no desenvolvimento deste projeto e as notícias coletadas foram armazenadas no BigQuery para análise e consulta. <!-- Uma API RESTful é fornecida para facilitar a busca e recuperação desses dados.  -->

## Funcionalidades

- Coleta as notícias do site theguardian.com/au (código desta funcionalidade está em news_scraper/news_scraper/spiders/news_spider.py);
- Os dados coletados são: URLs, títulos e subtítulos dos artigos, data de lançamento do artigo, nome do autor e a categoria da notícia;
- As coletas feitas estão na pasta news_scraper em formato CSV e em JSON;
- A coleta dos dados foi armazenada no Google BigQuery no formato CSV.

## Requisitos

- Python 3.7 ou superior;
- Scrapy 2.11.2;
- google-cloud-bigquery 3.24.0;
- Conta no Google Cloud com acesso ao BigQuery;
- Criar um projeto no BigQuery.

## Instalação
### Clone o Repositório
~~~bash
git clone https://github.com/seu-usuario/crawler_project.git
cd crawler_project
~~~

### Crie um Ambiente Virtual
~~~bash
python -m venv venv
venv\Scripts\activate # No Mac, use 'source venv/bin/activate' 
~~~

### Instale as Dependências
~~~bash
cd news_scraper
pip install -r requirements.txt
~~~

## Uso

Para visualização dos dados, é necessário criar um dataset dentro do seu projeto do GCP, criar um bucket no Google Cloud Storage e inserir o arquivo theguardian_data.json para realizar a execução do script upload_data.py

~~~bash 
(your-env) ..\crawler_project> py -m upload_data
~~~
Essa execução criará uma nova tabela para trabalhar com os dados no BigQuery


Para extrair esses dados novamente, acesse a pasta
~~~bash 
cd news_scraper
~~~
Execute o crawler para criar um arquivo CSV ou JSON
~~~bash 
scrapy crawl news_spider -o nome_do_arquivo.json 
~~~


# Exemplo de Consultas/Querys Simples

## Buscar todas as notícias por ordem dos primeiros artigos encontrados
~~~bash 
SELECT *
 FROM `nome-do-projeto.nome_do_conjunto_de_dados.nome_da_tabela`
 ORDER BY article_release_date;
~~~

## Retornar valor pela 'palavra-chave' na coluna escolhida
~~~bash 
SELECT *
 FROM `nome-do-projeto.nome_do_conjunto_de_dados.nome_da_tabela`
 WHERE topic 
 LIKE ('%culture%');
~~~
