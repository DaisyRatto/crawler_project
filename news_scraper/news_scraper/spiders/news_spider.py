import scrapy

class NewsSpiderSpider(scrapy.Spider):
    name = "news_spider"
    allowed_domains = ["theguardian.com"]
    start_urls = ["https://theguardian.com/au"]

    def parse(self, response):
        # Variável 'news' está relacionada aos artigos do site dcr-16c50tn
        news = response.css('div.dcr-4z6ajs')

        for n in news:
            relative_url = n.css('div.dcr-4z6ajs a ::attr(href)').get()
        # Neste loop, vamos analisar cada artigo e puxar as informações de cada um
            if relative_url is not None:
                news_url = 'https://www.theguardian.com/' + relative_url
                yield response.follow(news_url, callback= self.parse_news_page)
               

    # A partir daqui será para pular para a próxima página e verificar novamente
    # todo o loop da condição anterior

        next_page = response.css('li.dcr-9ra8aa a ::attr(href)').get()

        if next_page is not None:
            next_page_url = 'https://www.theguardian.com/' + next_page
            yield response.follow(next_page_url, callback= self.parse)

    def parse_news_page(self, response):

        yield {
            'url': response.url,
            'title':  response.css('.dcr-cohhs3 h1::text').get(),
            'subtitle': response.css('.dcr-4gwv1z p::text').get(),
            'article_release_date': response.css('.dcr-u0h1qy::text').get(),
            'author': response.css('.dcr-1cfpnlw a::text').get(),
            'topic': response.css('.dcr-1u8qly9 a span::text').get(),
        }
        
        
