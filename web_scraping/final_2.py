from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
import sys 
import os.path

file_list = list()
class scraper(object):
	def __init__(self):
		chrome_options = Options()
		chrome_options.add_argument("--headless")			#run in hidden mode
		global path
		global browser
		global save_path
		global complete_name_1
		global complete_name_2
		global complete_name_3
		global file_list
		path ='C:/Users/islam/Desktop/web_scraping_by_image/chromedriver_win32/chromedriver.exe'
		save_path = 'C:/Users/islam/Desktop/web_scraping_by_image/output'
		browser = webdriver.Chrome(executable_path = path , chrome_options= chrome_options )

	def newEggScrap(self, key_word):
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
		for link, price in zip(link_list[5:25], price_total_list[5:25]):  #to define limits
		    name_list.append(link.text)
		    price_list.append(price.text)
		    link_list2.append(link.get_attribute("href"))
		    print()

		#CSV Extrating
		item = str(key_word)
		file_name = 'newegg_data_'+item+'.csv'
		complete_name_1 = os.path.join(save_path, file_name)
		file_list.append(complete_name_1)
		#print(complete_name_1)
		with open(complete_name_1, 'w', newline='') as f:
		    w = csv.writer(f)
		    w.writerow(["Name", "Price" , "Link"])
		    for name, price , link in zip(name_list[0:20],price_list[0:20], link_list2[0:20]):
		    	w.writerow([name, price, link])


	def souqScrap(self, key_word):
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
		for link, price in zip(link_list[0:20], price_total_list[0:20]):  #to define limits
		    name_list.append(link.text)
		    price_list.append(price.text)
		    link_list2.append(link.get_attribute("href"))
		    print()

		#CSV Extrating
		item = str(key_word)
		file_name = 'souq_'+item+'.csv'
		complete_name_2 = os.path.join(save_path, file_name)
		file_list.append(complete_name_2)
		with open(complete_name_2, 'w', newline='') as f:
		    w = csv.writer(f)
		    w.writerow(["Name", "Price" , "Link"])
		    for name, price , link in zip(name_list[0:20],price_list[0:20], link_list2[0:20]):
		    	w.writerow([name, price, link])


	def aliExpressScrap(self, key_word):
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
		for link, price in zip(link_list[0:20], price_total_list[0:20]):  #to define limits
		    name_list.append(link.text)
		    price_list.append(price.text)
		    link_list2.append(link.get_attribute("href"))
		    print()

		#CSV Extrating
		item = str(key_word)
		file_name = 'aliexpress_'+item+'.csv'
		complete_name_3 = os.path.join(save_path, file_name)
		file_list.append(complete_name_3)
		with open(complete_name_3, 'w', newline='') as f:
		    w = csv.writer(f)
		    w.writerow(["Name", "Price" , "Link"])
		    for name, price , link in zip(name_list[0:20],price_list[0:20], link_list2[0:20]):
		    	w.writerow([name, price, link])

	def get_files(self):
		print('getting your files')
		return file_list