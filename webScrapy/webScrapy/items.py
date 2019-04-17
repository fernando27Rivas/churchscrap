# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WebscrapyItem(scrapy.Item):
    
    year = scrapy.Field()
    speaker = scrapy.Field()
    topic = scrapy.Field()
    url = scrapy.Field()
    headline = scrapy.Field()
    words = scrapy.Field()
    
   
