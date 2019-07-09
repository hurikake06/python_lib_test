# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import SitemapSpider
from scrapy.selector import Selector
from aeonpet.items import AeonpetItem

class ScrapyAeonpetSpiderSpider(SitemapSpider):
    name = 'scrapy_aeonpet_spider'
    allowed_domains = ['www.aeonpet-memorial.com']
    sitemap_urls = ['http://www.aeonpet-memorial.com/sitemap.xml']
    sitemap_rules = [
        (r'https://www.aeonpet-memorial.com/reien/.+', 'parse'),
    ]

    def parse(self, response):
        print('-----------------------')
        print("URL:", response.url)
        print('-----------------------')
        #self.name = "response.css('.dethead').extract_first().strip()"
        item = AeonpetItem()
        sel = Selector(response)
        item['name'] = sel.xpath('//h1').extract_first()

        yield item