import scrapy
import json
from mclmovieSpider.items import ShowListItem
import time


class mclShowingListSpider(scrapy.Spider):
    name = "mclcinemaShowingList"
    allowed_domains = ["www4.mclcinema.com"]
    start_urls = [
        "http://www4.mclcinema.com/MCLWebAPI2/GetNowShowingList.aspx?l=2&ci=012"
    ]

    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        moviejson = jsonresponse["movies"]
        items = []
        for movie in moviejson:
            id = movie['id']
            print id
            showTypes = movie['vst']
            for showType in showTypes:
                language = showType['l']
                shows = showType['c'][0]['s']
                for show in shows:
                    item = ShowListItem()
                    item['sid'] = show['si']
                    item['id'] = id
                    item['language'] = language
                    info = show['sn']
                    info = info.split('$')
                    if len(info) <=1:
                        continue
                    item['price'] = info[1]
                    info = info[0].split('House')
                    if len(info) <=1:
                        continue
                    item['house'] = info[1]
                    info = info[0]
                    info = info.replace("BEA", "")
                    item['time'] =  time.strptime(info,"%a, %b %d, %I:%M %p, ")
                    item['time'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', item['time'])
                    items.append(item)
        return items



#orgi web
#http://www4.mclcinema.com/MCLCinema.aspx?gv=1&visLang=2&ci=012

#showList
#http://www4.mclcinema.com/MCLWebAPI2/GetNowShowingList.aspx?l=2&ci=012

#getMovieDetail
#http://www4.mclcinema.com/MCLWebAPI2/GetMovieDetails.aspx?l=2&m=n&r=b&ci=012

#getSeatPlan
#https://www2.mclcinema.com/SeatPlan.aspx?visLang=1&ci=012&si=12822