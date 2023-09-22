import scrapy


class PaintsSpider(scrapy.Spider):
    name = 'paints'
    start_urls = ["https://order-nn.ru/kmo/catalog/"]

    def parse(self, response):
        page = response.xpath('//a[contains(., "Краски и материалы специального назначения")]').attrib["href"]  # noqa E501
        yield response.follow(page, callback=self.parse_special_paint)

    def parse_special_paint(self, response):
        links = response.xpath(
            '//div[@class="horizontal-product-item-block_3_2"][@id]/a/@href'
        ).getall()
        yield from response.follow_all(links, self.parse_data)

        next_page = response.xpath(
            '//li/a[@rel="canonical"][@href]'
        ).attrib["href"]
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse_special_paint)

    def parse_data(self, response):
        return {
            "Наименование": response.xpath('//h1[@itemprop]/text()').extract_first(),  # noqa E 501
            "Цена": response.xpath('//span[@itemprop="price"]/text()').extract_first(),  # noqa E 501
            "Описание": response.xpath('//div[@id="block-description"]/descendant::p/text()').extract()  # noqa E 501
        }
