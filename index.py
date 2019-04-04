import functions

if __name__ == '__main__':
	print('starting...')
	start = time.time()
	min_yield = 8
	url = 'www.some_website_with_data.com'

	create_url_list(url)
	get_company_fundmentals()
	clean_and_process_data(min_yield)
  
	end = time.time()
	print('End// /ntime taken: ', end-start)
