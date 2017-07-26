import scrapy


class Data(scrapy.Spider):
    name = "Data"
    start_urls = [
        'http://economictimes.indiatimes.com/'
        
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
            print(response.xpath('//body//p//text()').extract())
            




