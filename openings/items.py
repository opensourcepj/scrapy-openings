# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OpeningsItem(scrapy.Item):
    link = scrapy.Field()
    job_title = scrapy.Field()
    recruiter_url = scrapy.Field()
    job_description = scrapy.Field()
    job_url = scrapy.Field()
    tags = scrapy.Field()
    processed_jsondate = scrapy.Field()
    posted_jsondate = scrapy.Field()
