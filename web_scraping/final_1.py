from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
import sys

#sys.path.append('C:/Users/islam/Desktop/web_scraping_by_image/object_detection')
#import model_1

chrome_options = Options()
chrome_options.add_argument("--headless")			#run in hidden mode
path ='C:/Users/islam/Desktop/web_scraping_by_image/chromedriver_win32/chromedriver.exe'
browser = webdriver.Chrome(executable_path = path)
d = dict()

def newEggScrap(key_word):
	#NewEgg SCRAPING
	url = 'https://www.newegg.com/'
	browser.get(url)
	search_box = browser.find_element_by_id('haQuickSearchBox')
	search_box.send_keys(key_word)
	search_box.send_keys(Keys.ENTER)

	# for multiple classes we have to use one of these options (xpath selector , css selector , bs4)
	link_list = browser.find_elements_by_css_selector("a.item-title")
	price_total_list = browser.find_elements_by_class_name('price-current')
	name_list = list()
	price_list = list()
	link_list2 = list()

	print("***************** scraping started *****************\n")
	for link, price in zip(link_list[5:15], price_total_list[5:15]):  #to define limits
	    print("product name  : ",link.text)
	    print("product price : ",price.text)
	    print("product link  : ",link.get_attribute("href"))
    
	    name_list.append(link.text)
	    price_list.append(price.text)
	    link_list2.append(link.get_attribute("href"))
	    d = { name:{price:link} for name, price, link in zip(name_list[0:10],price_list[0:10], link_list2[0:10])}
	    print()

	#CSV Extrating
	with open('newegg_data_'+key_word+'.csv', 'w', newline='') as f:
	    w = csv.writer(f)
	    w.writerow(["Name", "Price" , "Link"])
	    for name, price , link in zip(name_list[0:10],price_list[0:10], link_list2[0:10]):
	    	w.writerow([name, price, link])


	print(d)


def souqScrap(key_word):
	#Souq SCRAPING
	url = 'https://egypt.souq.com/eg-en/'
	browser.get(url)
	search_box = browser.find_element_by_id('search_value')
	search_box.send_keys(key_word)
	search_box.send_keys(Keys.ENTER)

	# for multiple classes we have to use one of these options (xpath selector , css selector , bs4)
	link_list = browser.find_elements_by_css_selector("a.itemLink.sk-clr2.sPrimaryLink")
	price_total_list = browser.find_elements_by_class_name('itemPrice')
	name_list = list()
	price_list = list()
	link_list2 = list()

	print("***************** scraping started *****************\n")
	for link, price in zip(link_list[0:10], price_total_list[0:10]):  #to define limits
	    print("product name  : ",link.text)
	    print("product price : ",price.text)
	    print("product link  : ",link.get_attribute("href"))
    
	    name_list.append(link.text)
	    price_list.append(price.text)
	    link_list2.append(link.get_attribute("href"))
	    d = { name:{price:link} for name, price, link in zip(name_list[0:10],price_list[0:10], link_list2[0:10])}
	    print()

	#CSV Extrating
	with open('souq_data_'+key_word+'.csv', 'w', newline='') as f:
	    w = csv.writer(f)
	    w.writerow(["Name", "Price" , "Link"])
	    for name, price , link in zip(name_list[0:10],price_list[0:10], link_list2[0:10]):
	    	w.writerow([name, price, link])


	print(d)

def aliExpressScrap(key_word):
	#AliExpress SCRAPING
	url = 'https://aliexpress.com/'
	browser.get(url)
	search_box = browser.find_element_by_id('search-key')
	search_box.send_keys(key_word)
	search_box.send_keys(Keys.ENTER)
	browser.refresh()

	# for multiple classes we have to use one of these options (xpath selector , css selector , bs4)
	link_list = browser.find_elements_by_css_selector("a.history-item.product")
	price_total_list = browser.find_elements_by_class_name('value')
	name_list = list()
	price_list = list()
	link_list2 = list()

	print("***************** scraping started *****************\n")
	for link, price in zip(link_list[0:10], price_total_list[0:10]):  #to define limits
	    print("product name  : ",link.text)
	    print("product price : ",price.text)
	    print("product link  : ",link.get_attribute("href"))

	    name_list.append(link.text)
	    price_list.append(price.text)
	    link_list2.append(link.get_attribute("href"))
	    d = { name:{price:link} for name, price, link in zip(name_list[0:10],price_list[0:10], link_list2[0:10])}
	    print()

	#CSV Extrating
	with open('aliexpress_data_'+key_word+'.csv', 'w', newline='') as f:
	    w = csv.writer(f)
	    w.writerow(["Name", "Price" , "Link"])
	    for name, price , link in zip(name_list[0:10],price_list[0:10], link_list2[0:10]):
	    	w.writerow([name, price, link])


	print(d)
#################################################
fhand = open('C:/Users/islam/Desktop/web_scraping_by_image/object_detection/objects.txt')

print('heeeere')

for line in fhand:
	print(line)
	line = line.rstrip()
	souqScrap(line)
	aliExpressScrap(line)
	#newEggScrap(line)

#print(list_g)
#souqScrap('mobile')
#aliExpressScrap('car')
#newEggScrap('tv')
