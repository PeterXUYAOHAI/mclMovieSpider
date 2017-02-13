# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShowListItem(scrapy.Item):
    sid = scrapy.Field()
    id = scrapy.Field()
    language= scrapy.Field()
    price = scrapy.Field()
    time = scrapy.Field()
    house = scrapy.Field()


class MovieItem(scrapy.Item):
    id = scrapy.Field()
    movie_name = scrapy.Field()
    movie_genre = scrapy.Field()
    movie_length = scrapy.Field()
    movie_class = scrapy.Field()
    movie_subtitle = scrapy.Field()
    movie_language = scrapy.Field()

class SeatPlanItem(scrapy.Item):
    timeStamp = scrapy.Field()
    sid = scrapy.Field()
    seatmap = scrapy.Field()
