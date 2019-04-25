# -*- coding: utf-8 -*-
import scrapy


class SpiderUfamSpider(scrapy.Spider):
    name = 'spider_UFAM'
    allowed_domains = ['http://riu.ufam.edu.br/simple-search?location=']
    start_urls = ['http://http://riu.ufam.edu.br/simple-search?location=/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'Regiao_Norte.pipelines.RegiaoNortePipeline': 400
        },
        'LOG_FILE': 'RegiaoNorte.log',
        'FEED_FORMAT': 'csv',
        'JOBDIR': 'crawls\\regiao',
        'FEED_URI': 'ufam_resultado.csv'
    }


    def extracao ( self,response,link):
        pass

    def parse(self, response):
        for link in response.css('table.table td[headers = "t2"] a'):
            yield extracao(self,response,link)


