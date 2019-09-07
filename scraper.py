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
        #'https://www.tudogostoso.com.br',
        'https://www.tudogostoso.com.br/categorias/1004-carnes'
        #'https://www.tudogostoso.com.br/categorias/1009-aves',
        #'https://www.tudogostoso.com.br/categorias/1014-peixes-e-frutos-do-mar',
        #'https://www.tudogostoso.com.br/categorias/1023-saladas-molhos-e-acompanhamentos',
        #'https://www.tudogostoso.com.br/categorias/1027-sopas',
        #'https://www.tudogostoso.com.br/categorias/1028-massas',
        #'https://www.tudogostoso.com.br/categorias/1032-bebidas',
        #'https://www.tudogostoso.com.br/categorias/1037-doces-e-sobremesas',
        #'https://www.tudogostoso.com.br/categorias/1044-lanches',
        #'https://www.tudogostoso.com.br/categorias/1334-alimentacao-saudavel'
    ]
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.5',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'datadome=SYWjhs7hDYFHI2.wcw1W_c~fg8fGvIa1VLspjkgmgGP67.8.cPwwSE6-tU.PQKIicrqXRzISbuOJbTvuPqA4pigowmyA-XsNhs8skhSG9S; _ga=GA1.3.998695355.1567189468; _fbp=fb.2.1567189468739.826510059; nvg55810=9be4191b405a0959065ab26e809|0_250; trc_cookie_storage=tudogostoso%253Asession-data%3Dv2_d90ca24c31be1d27ce29a4773eec91b7_388f3f82-a787-438d-a059-b8e32727c5d9-tuct462ef5c_1567736394_1567736394_CIi3jgYQwPBAGLDg-6LQLSABKAQwHzjb1AdA_YcQSPiTG1D___________8BWABgAA%7Ctaboola%2520global%253Alocal-storage-keys%3D%255B%2522tudogostoso%253Asession-data%2522%252C%2522taboola%2520global%253Alspb%2522%252C%2522taboola%2520global%253Auser-id%2522%255D%7Ctaboola%2520global%253Alspb%3DCwsIQRDx-DUMCwhCEPD4NQwLCIkBEIvANgwLCEwQ8Pg1DAsIHBDx-DUMCwgdEPH4NQwLCB4Q8fg1DAsIHxDx-DUMCwggEPD4NQwLCCEQ8fg1DAsIIxDRxzYMCwgkEPD4NQwLCGQQ8Pg1DAsIJxDw-DUMCwgtEPD4NQwLCDEQ8fg1DAsIOxDw-DUMCwg9ELDxNQwLCD8Q8Pg1DAwTFA%7Ctaboola%2520global%253Auser-id%3D388f3f82-a787-438d-a059-b8e32727c5d9-tuct462ef5c; _hjid=8b190e2f-bfb1-4a12-ad6d-2c0ca00e773c; __gads=ID=656cf2b1edb599a1:T=1567189471:S=ALNI_MbG4RzMsdKqlXPvpPW0tJELQXl8RA; _ttuu.s=1567736472721; tt.u=7A0B000AE71C695D8E69695502756C55; tg_term=2019-08-030; cto_lwid=0583f148-7d8a-4b5b-a688-67f642399374; cto_bundle=nfHneF9HR2VXWkN4NlQ2RUJWTjlCRTZSR0N4aUglMkZ1cmFsUnh5MiUyRiUyRjUyZUV0V1BFUlJ6OXh3RVY0MENoVWRsMEIlMkZKWHNaZllkbU1hUDdDYm5IRmdNJTJCUTdpJTJGTjlWNHhXTlh5NCUyRnlWaDJMd3JGT0sySUViSUR0U0Zsc1Nybm03MEk2VlRs; _gid=GA1.3.91408702.1567736393; tt_c_vmt=1567736400; tt_c_c=direct; tt_c_s=direct; tt_c_m=direct; tt.nprf=',
        'Host': 'www.tudogostoso.com.br',
        'If-None-Match': 'W/"64b48b58546a64167649117bb47f322d"',
        'Referer': 'https://www.tudogostoso.com.br/',
        'TE': 'Trailers',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse_recipe)

    '''
    def parse(self, response):
        import ipdb; ipdb.set_trace()
        items = response.css('div class rounded')

        for link in items.xpath('div/nav/ul/li[*]/a/@href').getall():
            url = response.urljoin(link)
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse_recipe)
    '''

    def parse_recipe(self, response):
        import ipdb; ipdb.set_trace()
        # pegar os links de todas as receitas da pagina atual
        base_url = 'https://www.tudogostoso.com.br'
        for recipe in response.css('div.card a::attr(href)').getall():
            try:
                yield scrapy.Request(base_url+recipe, callback=self.parse_parse)
            except:
                print('ERROR_ERROR_ERROR')



    def parse_parse(self, response):
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





'''
if response is not None:
    print( {
            'author': response.xpath('/html/body/div[8]/div[1]/div/div[3]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[5]/div').extract(),
            'name': response.xpath('//*[@id="item-id-1251"]').extract(),
            'ingr': response.xpath('/html/body/div[7]/div[1]/div/div[3]/div[4]').extract(),
            'prep': response.xpath('/html/body/div[7]/div[1]/div/div[3]/div[5]/div/div[1]').extract()
            }
        )
'''

'''
    def start_requests(self, response):
        for category in self.start_urls:
            scrapy.http.Request(url=self.start_urls[0], headers=self.headers)
            next_page = response.xpath('/html/body/div[6]/div[1]/div[2]/div[2]/div/div[19]/div[1]/a[9]/@href').extract()
            print(next_page)
            #for pages in
            #yield scrapy.http.Request(url=self.start_urls[0], headers=self.headers, callback=self.parse_recipe)





        next_page = response.xpath('/html/body/div[6]/div[1]/div[2]/div[2]/div/div[19]/div[1]/a[9]/@href').extract()

        yield {
            'author': response.xpath('/html/body/div[7]/div[1]/div/div[3]/div[1]/div/div[1]/div[1]/div[1]/h1').extract(),
            'name': response.xpath('/html/body/div[8]/div[1]/div/div[3]/div[1]/div/div[1]/div[1]/div[1]/h1').extract(),
            'ingr': response.xpath('//*[@id="info-user"]').extract(),
            'prep': response.xpath('/html/body/div[8]/div[1]/div/div[3]/div[5]/div/div[1]').extract()
        }

        for recipe in response.xpath('/html/body/div[6]/div[1]/div[2]/div[2]/div/div[*]/a/@href').extract():
            #url = response.urljoin(recipe)
            #yield scrapy.http.Request(url=url, headers=self.headers, callback=self.parse_recipe)

            author = response.xpath('/html/body/div[7]/div[1]/div/div[3]/div[1]/div/div[1]/div[1]/div[1]/h1').extract()
            name = response.xpath('/html/body/div[8]/div[1]/div/div[3]/div[1]/div/div[1]/div[1]/div[1]/h1').extract()
            ingr = response.xpath('//*[@id="info-user"]').extract()
            prep = response.xpath('/html/body/div[8]/div[1]/div/div[3]/div[5]/div/div[1]').extract()

            #response.follow(url, callback=self.parse_recipe)
        if next_page is not None:
            print("next")
            yield response.follow(next_page, callback=self.parse_recipe)
            #url_next_page = response.urljoin(str(next_page))





    def parse_get_categories(self, response):
        categories = response.xpath('/html/body/header/div/div[2]/div/nav/ul/li[*]/a/@href').extract() #works
        i=0
        for categorie in categories:
            if i == 0:
                i = i + 1
                #print("I'll get this page: " + self.start_urls[0]+categorie)
                yield scrapy.http.Request(url=self.start_urls[0]+categorie+'.html', headers=self.headers, callback=self.parse_get_recipes)



# works like a charm
def parse(self, response):
    items = response.xpath('/html/body/header/div/div[2]')
    for item in items:
        r = item.xpath('div/nav/ul/li[*]/a/@href').extract()
        print(r)

# test (works too)
def parse_test(self, response):
    items = response.xpath('/html/body/header/div/div[2]/div/nav/ul/li[*]/a/@href').extract() #works
    print(self.start_urls[0] + items[0])
    print(items)
'''
