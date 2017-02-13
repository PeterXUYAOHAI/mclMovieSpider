import scrapy
from mclmovieSpider.items import SeatPlanItem
import json
import datetime


class seatPlanSpider(scrapy.Spider):
    name = "seatplan"
    allowed_domains = ["https://www2.mclcinema.com"]
    with open('movies.json') as data_file:
        data = json.load(data_file)
    sids = []
    for d in data:
        sids.append(d['sid'])

    start_urls = []

    for sid in sids:
        start_urls.append("https://www2.mclcinema.com/SeatPlan.aspx?visLang=1&ci=012&si="+str(sid))

    def parse(self, response):
        item = SeatPlanItem()

        item['timeStamp'] = datetime.datetime.now().isoformat()
        item['sid'] = response.request.url.split("=")[-1]
        item['seatmap'] = response.body

        return item


