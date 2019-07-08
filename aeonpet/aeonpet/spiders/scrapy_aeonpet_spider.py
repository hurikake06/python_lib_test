# -*- coding: utf-8 -*-
import scrapy


class ScrapyAeonpetSpiderSpider(scrapy.Spider):
    name = 'scrapy_aeonpet_spider'
    allowed_domains = ['www.aeonpet-memorial.com']
    start_urls = ['http://www.aeonpet-memorial.com/sitemap.xml']
    sitemap_rules = [
        (r'/https://www.aeonpet-memorial.com/reien/.+/', 'parse'),
    ]

    def parse(self, response):
        self.name = "response.css('.dethead').extract_first().strip()"
