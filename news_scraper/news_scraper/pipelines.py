# Configurado ITEM_PIPELINES no arquivo settings.py
#
# ITEM_PIPELINES = {
#    "news_scraper.pipelines.NewsScraperPipeline": 300,
# }


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class NewsScraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)


        """O item 'topic' será convertido para letras minusculas, para ajudar
         na coleta de dados """
        lowercase_keys = ['topic']
        for lowercase_key in lowercase_keys:
            value = adapter.get(lowercase_key)
            adapter[lowercase_key] = value.lower()

        
        return item
