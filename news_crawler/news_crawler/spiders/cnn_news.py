# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from news_crawler.items import NewsCrawlerItem


class CnnSpider(CrawlSpider):
    name = 'cnn'
    allowed_domains = ['cnn.com']
    # Articles on the front page are dynamically loaded
    start_urls = ['https://www.cnn.com/africa']
    # /2020/08/28/weather/rapid-fire-disasters-in-coronavirus-pandemic-weir-wxc/index.html
    rules = [Rule(LinkExtractor(
        allow=r'\/2020\/[0-9][0-9]\/[0-9][0-9]\/[a-zA-Z\-]+\/[a-zA-Z\-]+\/index.html'), callback='parse', follow=True)]

    def parse(self, response):
        article = NewsCrawlerItem()
        # <script data-rh="true">
        article['url'] = response.url
        article['source'] = 'CNN'
        article['title'] = response.xpath('//h1/text()').get()
        article['description'] = response.xpath(
            '//meta[@name="description"]/@content').get()
        article['date'] = response.xpath(
            '//meta[@itemprop="datePublished"]/@content').get()
        article['author'] = response.xpath(
            '//meta[@itemprop="author"]/@content').get().replace(', CNN', '')
        article['text'] = response.xpath(
            '//section[@data-zone-label="bodyText"]/div[@class="l-container"]//*/text()').getall()
        return article
