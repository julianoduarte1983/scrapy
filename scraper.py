import scrapy
from scrapy import Spider, Request

class Recipe(scrapy.Item):
    author = scrapy.Field()
    name = scrapy.Field()
    ingr = scrapy.Field()
    prep = scrapy.Field()

class MyFirstSpyder(scrapy.Spider):
    name = "my_first_spider"
    allowed_domains = 'tudogostoso.com.br'
    start_urls = [
        'https://www.tudogostoso.com.br/categorias/1004-carnes'
    ]

    custom_settings = {
        'CONCURRENT_REQUESTS': '1',
        'LOG_LEVEL': 'ERROR',
        'DOWNLOADER_MIDDLEWARES' : {
                'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
                'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
            }
    }

    def parse(self, response):
        for recipe in response.css('div.card a::attr(href)').getall():
            yield scrapy.Request(
                url=response.urljoin(recipe),
                callback=self.parse_recipes
            )
            #self.logger.error(repr(response))

    def parse_recipes(self, response):
        print("PARSE_PARSE")
        '''
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
        '''

    def parse_error(self, failure):
        self.logger.error(repr(failure))
