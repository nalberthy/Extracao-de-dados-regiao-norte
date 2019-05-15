# -*- coding: utf-8 -*-
import scrapy
from ..items import RegiaoNorteItem

class SpiderUfpaSpider(scrapy.Spider):
    name = 'spider_UFPA'
    start_urls = ['http://repositorio.ufpa.br/jspui/simple-search?query=saude+mental']


    def parse(self, response):
        #Lista de artigos da página
        lista = response.css('td[headers = "t2"] a::attr(href)').extract()
        #link de referência do botão next
        next_page = response.css('.pagination  li:last-child > a::attr(href)').get()
        # Percorrer artigos da pagina
        for link in lista:
            yield response.follow(link, self.extracao)
        # Percorrer paginas    
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)        
    def extracao(self,response):
        itens = RegiaoNorteItem()
        titulo = response.css('tr:nth-child(5) td.metadataFieldValue ::text').extract()
        resumo= response.css('tr:nth-child(8) td.metadataFieldValue::text').extract()
        data = response.css('tr:nth-child(2) > td.metadataFieldValue::text').extract()
        self.log(resumo)
        itens['titulo']=titulo
        itens['resumo']=resumo
        itens['data']=data
        yield itens
