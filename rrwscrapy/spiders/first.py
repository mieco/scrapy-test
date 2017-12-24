import scrapy


class myFirstSpider(scrapy.Spider):
    name = "firstBlood"

    start_urls = [
        'http://politics.people.com.cn/n1/2017/1221/c1024-29722172.html'
    ]

    def parse(self, response):
        ps = response.css("div.box_con p")
        yield {
            'title': response.css("h1::text").extract_first(),
            'content': response.css("div.box_con p::text").extract()
        }
        # page = response.url.split("/")[-2]
        # filename = 'myspider-%s.txt' % page
        # with open(filename, 'r+') as f:
        #     f.write(response.css("h1::text").extract_first())
        # self.log('Saved file %s' % filename)
