import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from news_crawler.items import NewsCrawlerItem
import json


class ApNewsSpider(CrawlSpider):
    name = "ap_news"
    allowed_domains = ["apnews.com"]
    start_urls = ["https://apnews.com/"]
    rules = [Rule(LinkExtractor(
        allow=r'\/article\/[a-zA-Z\-]+\-[a-zA-Z0-9]{32}'), callback='parse', follow=True)]

    def parse(self, response):
        news = NewsCrawlerItem()
        news['url'] = response.url
        news['source'] = 'Associated Press'

        jsonData = json.loads(response.xpath(
            '//script[@type="application/ld+json"]/text()').get())
        news['title'] = jsonData['headline']
        news['description'] = jsonData['description']
        news['date'] = jsonData['datePublished']
        news['author'] = jsonData['author'][0]
        news['text'] = response.xpath(
            '//div[@class="Article"]/p/text()').getall()
        return news
