# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class RegiaoNortePipeline(object):
    def process_item(self, item, spider):
        try:
            item['titulo']=item['titulo'].replace("\r\n"," ")
            item['titulo']=item['titulo'].replace("\n"," ")
            item['titulo']=item['titulo'].replace("\"","") 
            item['titulo']=item['titulo'].replace("\t","")

            item['resumo']=item['resumo'].replace("\r\n"," ")
            item['resumo']=item['resumo'].replace("\n"," ")
            item['resumo']=item['resumo'].replace("\"","") 
            item['resumo']=item['resumo'].replace("\t","") 

            item['data']=item['data'].replace("\r\n"," ")
            item['data']=item['data'].replace("\n"," ")
            item['data']=item['data'].replace("\"","") 
            item['data']=item['data'].replace("\t","") 
        except:
            return item
        # item['resumo'].replace("\n"," ")
        # item['resumo'].replace("\r","")

        # item['data'].replace("\n"," ")
        # item['data'].replace("\r","")
        return item
