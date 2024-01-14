import scrapy
import os
import datetime



class GethtmlSpider(scrapy.Spider):
    name = "getHtml"
    allowed_domains = ["ishikawa.lg.jp"]
    start_urls = ["https://www.pref.ishikawa.lg.jp/"]

    def parse(self, response):
        t_delta = datetime.timedelta(hours=9)
        JST = datetime.timezone(t_delta, 'JST')
        dt_now = datetime.datetime.now(JST)
        # dt_path = dt_now.strftime('%Y%m%d_%H%M%S%z')
        dt_path = dt_now.strftime('%Y%m%d')

        output_path = os.path.join('./downloads/', dt_path)
        os.makedirs(output_path, exist_ok=True)

        full_path = os.path.join(output_path, 'index.html')
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(response.text)
