# -*- coding: utf-8 -*-
import scrapy
from ..items import RegiaoNorteItem

class SpiderUfgSpider(scrapy.Spider):
    name = 'spider_UFG'
    start_urls = ['https://repositorio.bc.ufg.br/simple-search?query=saude+mental']

    def parse(self, response):
        #Lista de artigos da página
        lista = response.css('td[headers = "t2"] a::attr(href)').extract()
        self.log(lista)
        #link de referência do botão next
        # next_page = response.css('.pagination  li:last-child > a::attr(href)').get()
        # Percorrer artigos da pagina
        for link in lista:
            yield response.follow(link+"?mode=full", self.extracao)
        # Percorrer paginas    
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)        
    def extracao(self,response):
        itens = RegiaoNorteItem()
        titulo = response.css('tr:nth-child(26)  td:nth-child(2) ::text').extract()
        resumo= response.css('tr:nth-child(29) td:nth-child(2)::text').extract()
        data = response.css('tr:nth-child(7) td:nth-child(2) ::text').extract()
        self.log(resumo)
        itens['titulo']=titulo
        itens['resumo']=resumo
        itens['data']=data
        yield itens

