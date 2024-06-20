# Aqui está definido os itens do nosso bloco de dados que estamos
# buscando e retornando, para ajudar no cleanse dos dados coletados

import scrapy


class NewsScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# class NewsItem(scrapy.Item):
#     url = scrapy.Field()
#     title = scrapy.Field()
#     subtitle = scrapy.Field()
#     article_release_date = scrapy.Field()
#     author = scrapy.Field()
#     topic = scrapy.Field()
