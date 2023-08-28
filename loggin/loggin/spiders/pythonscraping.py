# -*- coding: utf-8 -*-
import scrapy


class PythonscrapingSpider(scrapy.Spider):
    name = 'pythonscraping'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/cookies/profile.php']

# pylint: disable=no-member
    def make_requests_from_url(self, url):
        request = super(PythonscrapingSpider, self).make_requests_from_url(url)
        request.cookies['loggedin'] = 1
        request.cookies['username'] = 123

        return request

    def parse(self, response):
        return {'text': response.xpath('//body/text()').get()}
