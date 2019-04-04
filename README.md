# scrapeXclean

Just a test project that works in the following sequence:
  1. Creates a list of urls using company symbols 
  2. Pulls desired data from website
  3. Cleans and processes data into a final txt file

A slightly more detailed and context specific explaination would be:
- Create entry points:
   > In the first function, I open 'company_symbols.txt' file reading all the company symbols and forming URLs and writing it to 'company_urls.txt'.
- Enter and extract data:
	>Next, the second function opens 'company_urls.txt' and uses a scrapy spider to crawl for the desired data and stores it in 'company_fundamentals.txt'. In this case, for simplicity sake, I extract only company name and dividend yield. 
- Clean and sort data:
	>Finally, the third function opens 'company_fundamentals.txt', cleans and filters data that is unwanted with a simple criteria of dividend yield greater than 8%.  
	
Honestly, the code is pretty shit, but the architecture/ concept is sound IMO. Will slowly improve it! Just using this to test out github instead of 'hello world'.

Once again, the code is shit but it just proves <b>| scrape > store > process > read | x [repeat]</b> is possible for myself, cheers anyways~

/ᐠ. ᴗ.ᐟ\ Happy developing /ᐠ. ᴗ.ᐟ\
