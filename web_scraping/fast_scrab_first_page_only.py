from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#run in hidden mode
# ChromeOptions options = new ChromeOptions();
# options.addArguments("--headless");
# ChromeDriver chromeDriver = new ChromeDriver(options);

path ='C:/Users/islam/Desktop/CS3_2/SW_Project/chromedriver_win32/chromedriver.exe'
browser = webdriver.Chrome(executable_path = path)

#AMAZON SCRAPING
url = 'https://www.amazon.com/'
browser.get(url)
search_box = browser.find_element_by_id('twotabsearchtextbox')
search_box.send_keys('tv')
search_box.send_keys(Keys.ENTER)

# for multiple classes we have to use one of these options (xpath selector , css selector , bs4)
link_list = browser.find_elements_by_css_selector("a.a-link-normal.s-access-detail-page.s-color-twister-title-link.a-text-normal")
price_total_list = browser.find_elements_by_class_name('sx-price-whole')
price_fractional_list = browser.find_elements_by_class_name('sx-price-fractional')
price_currency_list = browser.find_elements_by_class_name('sx-price-currency')

print("scraping started *****************")
for name , tot , frac , currency in zip(link_list, price_total_list, price_fractional_list, price_currency_list):
    print("product name  : ",name.text)
    print("product price : ",tot.text,'.', frac.text, currency.text)
    print("product link  : ",name.get_attribute("href"))
    print()



