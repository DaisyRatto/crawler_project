from google.cloud import bigquery

# Construir um objeto BigQuery Client
client = bigquery.Client()

''' 
    Definir table_id com o ID da tabela que vamos criar dentro do projeto do GCP e 
    do conjunto de dados criado no BQ

    table_id = 'id-do-projeto.nome_dado_ao_dataset.nome_da_tabela_que_será_gerada'
'''
table_id = 'lima-news-crawler-project.news_data_api.the_guardian_data'

''' 
    Configurar o Job de carregamento com definições do esquema e outros detalhes, como:
    
    write_disposition -> especifica o comportamento desejado no momento da escrita 
    dos dados na tabela
    source_format -> especifica o formato do arquivo de entrada
'''
job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField('topic', 'STRING'),
        bigquery.SchemaField('author', 'STRING'),
        bigquery.SchemaField('article_release_date', 'STRING'),
        bigquery.SchemaField('subtitle', 'STRING'),
        bigquery.SchemaField('title', 'STRING'),
        bigquery.SchemaField('url', 'STRING'),
    ],
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
)

# Procura o caminho do dado em JSON no GCS Bucket 
uri = 'gs://theguardian_news/theguardian_data.json'


load_job = client.load_table_from_uri(
    uri,
    table_id,
    location='US', #Localização do conjunto de dados (data set)
    job_config=job_config,
) # Faz um requisito à API

load_job.result() 

destination_table = client.get_table(table_id)
print('{} table has been created and Loaded {} rows'.format(
    table_id,destination_table.num_rows))