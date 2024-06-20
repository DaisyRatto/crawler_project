# The Guardian News Crawler
Este projeto consiste em um crawler que coleta notícias do site theguardian.com e armazena esses dados no BigQuery para realizar as consultas desejadas. <!-- e disponibiliza uma API para busca desses dados. -->

## Índice

- [Introdução](#introdução)
- [Funcionalidades](#funcionalidades)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Licença](#licença)

## Introdução
Este projeto é um crawler que coleta artigos de notícias do site theguardian.com. As notícias coletadas são armazenadas no BigQuery para análise e consulta. <!-- Uma API RESTful é fornecida para facilitar a busca e recuperação desses dados.  -->

## Funcionalidades

- Coleta as notícias do site theguardian.com/au (código desta funcionalidade está em news_scraper/news_scraper/spiders/news_spider.py);
- Os dados coletados são: URLs, títulos e subtítulos dos artigos, data de lançamento do artigo, nome do autor e a categoria daquela notícia;
- As coletas feitas estão na pasta news_scraper em formato CSV e em JSON;
- Armazenamento de dados no Google BigQuery.

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

### Instale as Dependências
~~~bash
pip install -r requirements.txt
~~~

## Uso