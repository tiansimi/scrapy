# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import json


class BookspiderPipeline(object):
    def __init__(self):
        self.filename = open("itcast.json", "a")

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False)  # ensure_ascii=False 意思是不把中午转换成ascii码
        self.filename.write(text)

        return item


    def close_spider(self):
        self.filename.close()
