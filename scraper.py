import scrapy
from scrapy import Spider, Request

class Recipe(scrapy.Item):
    author = scrapy.Field()
    name = scrapy.Field()
    ingr = scrapy.Field()
    prep = scrapy.Field()

class MyFirstSpyder(scrapy.Spider):
    name = "my_first_spider"
    allowed_domains = 'https://www.tudogostoso.com.br'
    start_urls = [
        'https://www.tudogostoso.com.br/categorias/1004-carnes'
    ]
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
    }
    custom_settings = {
        'CONCURRENT_REQUESTS': '3',
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
    }

    def parse(self, response):
        #import ipdb #; ipdb.set_trace()
        # pegar os links de todas as receitas da pagina atual
        #base_url = 'https://www.tudogostoso.com.br'
        for recipe in response.css('div.card a::attr(href)').getall():
            #ipdb.set_trace()
            yield scrapy.Request(
                url=response.urljoin(recipe),
                headers=self.headers,
                callback=self.parse_recipes,
                errback=self.parse_error
            )

    def parse_recipes(self, response):
        #import ipdb; ipdb.set_trace()
        print("PARSE_PARSE")
        _author = response.xpath('/html/body/div[8]/div[1]/div/div[3]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[5]/div').extract()
        _name = response.xpath('//*[@id="item-id-1251"]').extract()
        _ingr = response.xpath('/html/body/div[7]/div[1]/div/div[3]/div[4]').extract()
        _prep = response.xpath('/html/body/div[7]/div[1]/div/div[3]/div[5]/div/div[1]').extract()
        yield ({
            'author': _author,
            'name': _name,
            'ingr': _ingr,
            'prep': _prep
        })

    def parse_error(self, failure):
        self.logger.error(repr(failure))

