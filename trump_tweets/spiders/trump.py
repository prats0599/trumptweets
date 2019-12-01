# -*- coding: utf-8 -*-
import scrapy
import json


class TrumpSpider(scrapy.Spider):
    name = 'trump'
    allowed_domains = ['trumptwitterarchive.com']
    start_urls = ['http://d5nxcu7vtzvay.cloudfront.net/data/realdonaldtrump/2016.json',
                    'http://d5nxcu7vtzvay.cloudfront.net/data/realdonaldtrump/2017.json',
                    'http://d5nxcu7vtzvay.cloudfront.net/data/realdonaldtrump/2018.json',
                    'http://www.trumptwitterarchive.com/data/realdonaldtrump/2019.json']

    def parse(self, response):
        jsonresponse=json.loads(response.body)
        for tweet in jsonresponse:
            yield{
            'created_at':tweet['created_at'],
            'favorite_count':tweet['favorite_count'],
            'source': tweet['source'],
            'id_str': tweet['id_str'],
            'retweet_count':tweet['retweet_count'],
            'in_reply_to_user_id_str':tweet['in_reply_to_user_id_str'],
            'is_retweet': tweet['is_retweet'],
            'text': tweet['text']
            }
