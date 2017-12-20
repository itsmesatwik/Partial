import scrapy
	
class Partial(scrapy.Spider):
	name = "partial"
	start_urls = ['https://www.theguardian.com/commentisfree/2017/dec/18/republican-tax-bill-american-tragedy-brute-force-politics']

	def parse(self, response):
		divs = response.xpath('//div')
		for p in divs.xpath('p'):
			print(p.extract())