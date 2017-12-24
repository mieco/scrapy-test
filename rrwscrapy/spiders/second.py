import scrapy


class mySecondSpider(scrapy.Spider):
    name = "secondBlood"

    start_urls = [
        'http://scitech.people.com.cn/'
    ]

    def parse(self, response):
        # follow links to author pages
        for href in response.css('div.hdNews  a::attr(href)'):
            yield response.follow(href, self.parse_content)

        next_page = response.css('div.page_n a::attr(href)').extract()[-1]
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        # follow pagination links
        # for href in response.css('div.page_n a::attr(href)'):
        #     yield response.follow(href, self.parse)

    def parse_content(self, response):
        # def extract_with_css(query):
        #     return response.css(query).extract_first().strip()

        yield {
            'title': response.css("h1::text").extract_first(),
            'content': response.css("div.box_con p::text").extract()
        }
