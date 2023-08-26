import scrapy
from dunkin.items import DunkinItem
import requests


class DunkinGetSpider(scrapy.Spider):
    name = "dunkin_get"
    allowed_domains = ["www.dunkindonuts.com"]

    # def start_requests(self):
    #     locs = ['02155']
    #     for loc in locs:
    # start_urls = ["https://www.dunkindonuts.com/en/locations?location=02155"]

    cookies = {
        '_fbp': 'fb.1.1692997076751.1004387414',
        'RT': '"z=1&dm=www.dunkindonuts.com&si=7a0d7d6d-dfee-461d-a151-c71447370aca&ss=llqysrcp&sl=0&tt=0&bcn=%2F%2F684dd326.akstat.io%2F&rl=1&nu=3a4qmivq&cl=4c52l"',
        'AWSALB': 'L/2UWIOOS/Jf27jHFRo1nlJ9OCT/HshLuOnujdt5G10VAixsXQyGGPn/dfZdk5MOjEk0N/Br5Wy4e0X1mm30bxB/i+r7oCp9RjD0rTWb5aE6OGQjQvQmmDv1CNMW',
        'AWSALBCORS': 'L/2UWIOOS/Jf27jHFRo1nlJ9OCT/HshLuOnujdt5G10VAixsXQyGGPn/dfZdk5MOjEk0N/Br5Wy4e0X1mm30bxB/i+r7oCp9RjD0rTWb5aE6OGQjQvQmmDv1CNMW',
    }

    headers = {
        'authority': 'www.dunkindonuts.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '_fbp=fb.1.1692997076751.1004387414; RT="z=1&dm=www.dunkindonuts.com&si=7a0d7d6d-dfee-461d-a151-c71447370aca&ss=llqysrcp&sl=0&tt=0&bcn=%2F%2F684dd326.akstat.io%2F&rl=1&nu=3a4qmivq&cl=4c52l"; AWSALB=L/2UWIOOS/Jf27jHFRo1nlJ9OCT/HshLuOnujdt5G10VAixsXQyGGPn/dfZdk5MOjEk0N/Br5Wy4e0X1mm30bxB/i+r7oCp9RjD0rTWb5aE6OGQjQvQmmDv1CNMW; AWSALBCORS=L/2UWIOOS/Jf27jHFRo1nlJ9OCT/HshLuOnujdt5G10VAixsXQyGGPn/dfZdk5MOjEk0N/Br5Wy4e0X1mm30bxB/i+r7oCp9RjD0rTWb5aE6OGQjQvQmmDv1CNMW',
        'csrf-token': 'undefined',
        'origin': 'https://www.dunkindonuts.com',
        'referer': 'https://www.dunkindonuts.com/en/locations?location=02155',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'service': 'DSL',
        'origin': '42.4274971,-71.10920120000002',
        'radius': '25',
        'maxMatches': '30',
        'pageSize': '1',
        'units': 'm',
        'ambiguities': 'ignore',
    }

    response = requests.post('https://www.dunkindonuts.com/bin/servlet/dsl',
                             cookies=cookies, headers=headers, data=data)
    print("result---------------")
    print(response.json())
    # url=open("file:///F:/python%20course/linkedin/1/GeocodeService.js")
    # yield s`crapy.Request(url, callback=self.parse)

    def parse(self, response):
        # item = DunkinItem()
        # item['loc_name'] = response.xpath(
        #     '//a[@class="js-address-line1"]/text()').get()
        # print("result---------------")
        # print(response)
        # print(response.xpath(
        #     '//div[@class="store-item__distance"]/text()').getall())
        # return item
        pass
