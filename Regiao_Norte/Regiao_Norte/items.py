# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RegiaoNorteItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    titulo = scrapy.Field()
    Resumo = scrapy.Field()
    Data_Publicacao = scrapy.Field()
