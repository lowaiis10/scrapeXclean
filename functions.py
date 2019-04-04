'''
File list 
  > company_symbols.txt 
  > company_urls.txt
  > company_fundamentals.txt
'''

def create_url_list(url):
  f1 = open('company_symbols.txt', 'r')
  f2 = open('company_urls.txt', 'w+')
	symbol_list = f1.read().splitlines()
	for symbol in symbol_list:
		link = '%s/%s'%(url,symbol)
		f2.write('%s|%s\n'%(symbol,link))
  
def get_company_fundmentals():
  f1 = open('company_urls.txt', 'w+')
  f2 = open('company_fundmanentals.txt', 'w+')  
	data = f1.read().splitlines()
	symbol_list = []
	url_list = []
	for x in data:
		x = x.split('|')
		symbol_list.append(x[0])
		url_list.append(x[1])

	class FundamentalsExtractionSpider(scrapy.Spider):
		name = 'fundamental_spider'
		company_symbols = symbol_list
		start_urls = url_list
    
		def parse(self, response):
        # Insert your own identifier accordingly in .css('')
			name = response.css('').css('::text').extract()
			dividend_yield = response.css('').css('::text').extract()
				f2.write('%s|%s\n'%(name, dividend_yield))
			  yield {'name':name}	


	process = CrawlerProcess({
	    'USER_AGENT': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36"
	})

	spider =FundamentalsExtractionSpider()
	process.crawl(spider)
	process.start()
  
  def process_003(min_yield):
	f1 = open('company_fundamentals.txt', 'r')
	f2 = open('company_cleaned.txt', 'w+')
	data = f5.read().splitlines()

	for x in data:
		x = x.split('|')

		if dividend_yield > min_yield:
			f6.write('%s|%s|%s\n'%(x[0],str(dividend_yield)))

