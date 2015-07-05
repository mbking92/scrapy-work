# -*- coding: utf-8 -*-
import scrapy
import urlparse
from fb.items import QBItem



class FBSpider(scrapy.Spider):
    name = "fb"
    allowed_domains = ["fftoday.com"]
    start_urls = [
        'http://fftoday.com/stats/playerstats.php?Season=2014&GameWeek=&PosID=10'
    ]

    def parse(self, response):
        for row in response.xpath("//table[2]//table[6]//tr[position()>2]"):
            item = QBItem()
            item['player_name'] = row.select("td[1]//a/text()").extract()
            yield item


        
