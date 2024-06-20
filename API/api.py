import os
from google.cloud import bigquery
from google.oauth2 import service_account


project_id = "lima-news-crawler-project"
key_path = "../config/lima-news-crawler-project-3faad564d1ad.json"
credentials = service_account.Credentials.from_service_account_file(key_path)
client = bigquery.Client(credentials=credentials, project=credentials.project_id)

external_config = bigquery.ExternalConfig('CSV')
external_config.source_uris = [
    'gs://theguardian_news/news_data.csv'
]
external_config.schema = [
    bigquery.SchemaField('url', 'STRING'),
    bigquery.SchemaField('title', 'STRING'),
    bigquery.SchemaField('subtitle', 'STRING'),
    bigquery.SchemaField('article_release_date', 'STRING'),
    bigquery.SchemaField('author', 'STRING'),
    bigquery.SchemaField('topi', 'STRING'),
]

table_id = 'news_data_table'

sql_query = """
SELECT * 
FROM {0}
LIMIT 1000
""".format(table_id)
# `lima-news-crawler-project.news_data.news_data` 

job_config = bigquery.QueryJobConfig(table_definitions={table_id: external_config})
query_job = client.query(sql_query, job_config=job_config)

w_states = list(query_job)
print(w_states)




# os.environ['GOOGLE_APPLICATION_CREDENCIALS'] = 'lima-news-crawler-project-3faad564d1ad.json'


# client -> credentials=credentials, project=credentials.project_id






# for row in query_job.result():
#     print(row)