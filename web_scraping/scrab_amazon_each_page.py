from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#run in hidden mode
# options.add_arguments("--headless")

chrome_options = Options()
#chrome_options.add_argument("--headless")
path ='C:/Users/islam/Desktop/CS3_2/SW_Project/chromedriver_win32/chromedriver.exe'
browser = webdriver.Chrome(executable_path = path, chrome_options= chrome_options)
KEY_WORD = "iphone"                                                                # A Key to search wtih


#AMAZON SCRAPING
first_url = 'https://www.amazon.com/'
browser.get(first_url)
search_box = browser.find_element_by_id('twotabsearchtextbox')
search_box.send_keys(KEY_WORD)
search_box.send_keys(Keys.ENTER)

# for multiple classes we have to use one of these options (xpath selector , css selector , bs4)
elements_list = browser.find_elements_by_css_selector("a.a-link-normal.s-access-detail-page.s-color-twister-title-link.a-text-normal")
link_list = []
price_total_list = []
name_total_list = []
asin_list = []
link_list_s=[]

# parsing links from all 'a' elements
for element in elements_list:
    link_list.append(element.get_attribute("href"))

print("***************** scraping started *****************\n")
for url in link_list[0:5]: #limit links
    browser.get(url)
    asin_list.append(browser.find_element_by_id('averageCustomerReviews').get_attribute('data-asin'))
    name_total_list.append(browser.find_element_by_id('productTitle').text)
    price_total_list.append(browser.find_element_by_id('priceblock_ourprice').text)



print("***************** scraping result *****************\n")
for name , price, asin  in zip(name_total_list, price_total_list, asin_list):
    print("product name  : ",name)
    print("product price : ",price)
    print("product link  : ", 'https://www.amazon.com/dp/'+asin)
    link_list_s.append('https://www.amazon.com/dp/'+asin)
    d = { name:{price:link} for name, price, link in zip(name_total_list, price_total_list, link_list_s)}
    print()



with open('amazon_data.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(["Name", "Price" , "Link"])
    for name, price , link in zip(name_total_list, price_total_list, link_list_s):
    	w.writerow([name, price, link])

print(d)