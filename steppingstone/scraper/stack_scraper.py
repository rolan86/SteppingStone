import scrapy
from links import urls


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = urls

    def parse(self, response):
        for quote in response.css('div.-job-summary'):
            yield {
                'position': quote.css('div.-title a::text').extract_first(),
                'link': quote.css('div.-title a::attr("href")').extract_first(),
                'company': quote.css('div.fc-black-700.fs-body1.-company').css('span::text').extract(),
                'perks': quote.css('div.mt2.-perks.fs-body1::text').extract(),
                'tags': quote.css('div.mt12.-tags a::text').extract(),
            }

        next_page = response.css('a.prev-next.job-link.test-pagination-next::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
