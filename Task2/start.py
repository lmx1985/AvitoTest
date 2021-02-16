from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
chrome = webdriver.Chrome(options=chrome_options)

chrome.get('https://m.avito.ru/moskva/kommercheskaya_nedvizhimost?cd=1&searchForm=true')
# блок авторизации (если это требуется)
# chrome.find_element_by_id("main_login_btn").click()


chrome.find_element_by_class_name("css-1bsvtvg").click()

time.sleep(2)
chrome.find_element_by_class_name("css-7ohp1y").click()
time.sleep(2)

chrome.find_element_by_class_name("css-m66apo").click()


# Дальше должна идти проверка по атрибутам, но моих знаний на данный момент не хватает, чтоб корректно выбрать селекторы кнопок, т.к. не сталкивался с data-marker
# Для работы скрипта нужен Python 3.9 и Selenium webdriver