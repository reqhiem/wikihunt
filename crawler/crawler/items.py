# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    from_ = scrapy.Field()
    to_ = scrapy.Field()
    hash_from_ = scrapy.Field()
    hash_to_ = scrapy.Field()
