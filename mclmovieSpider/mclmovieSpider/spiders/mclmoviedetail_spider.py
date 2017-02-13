import scrapy
import json
from mclmovieSpider.items import MovieItem



class mclmoviedetailSpider(scrapy.Spider):
    name = "mclmoviedetail"
    allowed_domains = ["www4.mclcinema.com"]
    start_urls = [
        "http://www4.mclcinema.com/MCLWebAPI2/GetMovieDetails.aspx?l=2&m=n&r=b&ci=012"
    ]

    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        items = []
        for movie in jsonresponse:
            id = movie['id']
            moviename = movie['mn']
            detail = movie['b']
            item = MovieItem()
            item['id'] = id
            item['movie_name'] = moviename
            item['movie_genre'] = detail['mg']
            item['movie_length'] = detail['mrt']
            item['movie_class'] = detail['mc']
            item['movie_language'] = detail['ml']
            item['movie_subtitle'] = detail['ms']
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