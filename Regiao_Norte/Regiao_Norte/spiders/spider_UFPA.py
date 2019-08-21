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
            yield response.follow(link+"?mode=full", self.extracao)
        # Percorrer paginas    
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)        
    def extracao(self,response):
        itens = RegiaoNorteItem()
        campoDC  = response.css('td.metadataFieldLabel::text').extract()
        valor  = response.css('td:nth-child(2)::text').extract()
        autores = []
        palavrachave = []
        for i in range(len(campoDC)):
            if campoDC[i] == 'dc.title':
                itens['titulo'] = valor[i]
            elif campoDC[i] == 'dc.description.resumo':
                itens['resumo'] = valor[i]
            elif campoDC[i] == 'dc.creator':
                autores.append(valor[i])
            elif campoDC[i] == 'dc.date.issued':
                itens['data'] = valor[i]
            elif campoDC[i] == 'dc.identifier.uri':
                itens['url'] = valor[i]
            elif campoDC[i] ==  'dc.subject':
                palavrachave.append(valor[i])
        itens['autores'] = autores
        itens['palavrachave']= palavrachave


        yield itens
