# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DunkinItem(scrapy.Item):
    loc_name=scrapy.Field()
    loc_url=scrapy.Field()
    add=scrapy.Field()
    dist=scrapy.Field()
    

    pass
