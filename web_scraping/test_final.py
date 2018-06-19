from final_2 import scraper
def run(scraper):
	scrap = scraper()
	scrap.aliExpressScrap('tv')
	print(scrap.get_files())
run(scraper)