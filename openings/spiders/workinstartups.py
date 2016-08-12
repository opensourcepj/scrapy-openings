# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import datetime
from openings.items import OpeningsItem


class WorkinstartupsSpider(CrawlSpider):
    name = 'workinstartups'
    allowed_domains = ['workinstartups.com']
    start_urls = ['http://www.workinstartups.com/']

    rules = (
            Rule(LinkExtractor(allow=r'job-board/'),
                 callback='parse_item',
                 follow=True),
    )

    def parse_item(self, response):
        i = OpeningsItem()
        job_title = response.xpath("//*[@id='job-title']/text()").extract_first()
        if job_title is not None:
            job_title = job_title.replace("\t", "").replace("\n", "")
            i['job_title'] = '' if len(job_title) == 0 else job_title.encode('ascii', 'ignore')
            i['recruiter_url'] = response.xpath("//*[@id='job-subtitle']//a/@href").extract_first()
            job_description = " ".join(response.xpath("//*[@id='job-description']//p/text()").extract())
            i['job_description'] = '' if len(job_description) == 0 else job_description.encode('ascii', 'ignore')
            i['job_url'] = response.url
            i['processed_jsondate'] = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
            date_str = response.xpath("//*[@id='number-views']//strong/text()").extract()[0]
            i['posted_jsondate'] = datetime.datetime.strptime(date_str, "%d %b %Y").strftime('%Y-%m-%dT%H:%M:%S')
            return i
