import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://stackoverflow.com/jobs?sort=i&q=python&l=germany',
    ]

    def parse(self, response):
        for quote in response.css('div.-item.-job.p24.pl48.bb.ps-relative.bc-black-2.js-dismiss-overlay-container'):
            yield {
                'job': quote.css('h2.fs-subheading.job-details__spaced.mb4 a::text').extract_first(),
                'link': quote.css('h2.fs-subheading.job-details__spaced.mb4 a::attr("href")').extract_first(),
                'company': quote.css('div.fc-black-700.fs-body2::text').extract_first(),
                'location': quote.css('div.fc-black-700.fs-body2 span.fc-black-500::text').extract_first(),
                'tags': quote.css('div.mt12 a::text').extract(),
            }

        #next_page = response.css('li.next a::attr("href")').extract_first()
        next_page = response.css('a.prev-next.job-link.test-pagination-next::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
