from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
import pandas as pd

chrome_options = Options()
chrome_options.add_argument("--headless")			#run in hidden mode
path ='C:/Users/islam/Desktop/CS3_2/SW_Project/chromedriver_win32/chromedriver.exe'
browser = webdriver.Chrome(executable_path = path)

#AliExpress SCRAPING
url = 'https://aliexpress.com/'
browser.get(url)
search_box = browser.find_element_by_id('search-key')
search_box.send_keys('mobile')
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
with open('aliexpress_data.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(["Name", "Price" , "Link"])
    for name, price , link in zip(name_list[0:10],price_list[0:10], link_list2[0:10]):
    	w.writerow([name, price, link])


print(d)



