# -*- coding: utf-8 -*-
import scrapy
from ..items import RegiaoNorteItem

class SpiderUfamSpider(scrapy.Spider):
    name = 'spider_UFAM'
    start_urls = ['http://riu.ufam.edu.br/simple-search?query=saude+mental']

 


    def parse(self, response):
        lista = response.css('td[headers = "t2"] a::attr(href)').extract()
        for link in lista:
            yield response.follow(link, self.extracao)
        
    def extracao(self,response):
        itens = RegiaoNorteItem()

        titulo = response.css('tbody tr:nth-child(2) td:nth-child(2) ::text').extract()
        resumo= response.css('tbody :nth-child(5) td[class="metadataFieldValue"]').extract()
        data = response.css('tbody :nth-child(17)').extract()
        self.log(resumo)
        itens['titulo']=titulo
        itens['resumo']=resumo
        itens['data']=data
        yield 

