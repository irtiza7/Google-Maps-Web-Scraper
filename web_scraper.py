from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time


WEB_browser_PATH = "C:\\Users\\Gohar Muzammil\\Desktop\\Git Repos\\Web Scraping\\chromebrowser.exe"
WEBSITE_URL = "https://www.google.com/maps/@31.6093654,74.3011063,15z"

options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(options = options)

browser.get(WEBSITE_URL)

search_bar_id = "searchboxinput"
query_text = "gyms in lahore"

search_bar = browser.find_element_by_id(search_bar_id)
search_bar.send_keys(query_text)
search_bar.send_keys(Keys.RETURN)

# Adding a waiting time because Maps take time to load search results. 
time.sleep(20)

container_1 = browser.find_element_by_id("pane")
container_2 = container_1.find_element_by_class_name("widget-pane-content.cYB2Ge-oHo7ed")
container_3 = container_2.find_element_by_class_name("siAUzd-neVct.section-scrollbox.cYB2Ge-oHo7ed.cYB2Ge-ti6hGc.siAUzd-neVct-Q3DXx-BvBYQ")
container_4 = container_3.find_element_by_class_name("siAUzd-neVct.section-scrollbox.cYB2Ge-oHo7ed.cYB2Ge-ti6hGc.siAUzd-neVct-Q3DXx-BvBYQ")

list_of_gyms = container_4.find_elements_by_class_name("V0h1Ob-haAclf.OPZbO-KE6vqe.o0s21d-HiaYvf")

for gym in list_of_gyms:
    print(gym.text)
    print("........................")

time.sleep(10)

browser.quit()
# browser.close()