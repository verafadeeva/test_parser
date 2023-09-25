import scrapy


class PaintsSpider(scrapy.Spider):
    name = 'paints'
    start_urls = ["https://order-nn.ru/kmo/catalog/"]

    def parse(self, response):
        page = response.xpath(
            '//a[contains(., "Краски и материалы специального назначения")]'
        ).attrib["href"]
        yield response.follow(page, callback=self.parse_paint)
        page = response.xpath(
            '//a[contains(., "Краски для наружных работ")]'
        ).attrib["href"]
        yield response.follow(page, callback=self.parse_paint)
        page = response.xpath('//a[contains(., "Лаки")]').attrib["href"]
        yield response.follow(page, callback=self.parse_paint)

    def parse_paint(self, response):
        links = response.xpath(
            '//div[@class="horizontal-product-item-block_3_2"][@id]/a[contains(@href, "catalog")]/@href'  # noqa E501
        ).getall()
        # yield from response.follow_all(links, self.parse_data)
        for link in links:
            yield response.follow(link, callback=self.parse_data)

        next_page = response.xpath(
            '//li[@class="active"]/following-sibling::li/a[@href]'
        ).attrib["href"]
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse_paint)

    def parse_data(self, response):
        description_list = response.xpath(
            '//div[@id="block-description"]/descendant::p/text()'
        ).getall()
        yield {
            "Наименование": response.xpath('//h1[@itemprop]/text()').get(),
            "Цена": response.xpath('//span[@itemprop="price"]/text()').get(),
            "Описание": ' '.join(description_list)
        }
