from selenium import webdriver

WEB_DRIVER_PATH = "C:\\Users\\Gohar Muzammil\\Desktop\\Git Repos\\Web Scraping\\chromedriver.exe"
WEBSITE_URL = "https://www.google.com/maps/search/gyms+in+lahore/@31.4885131,74.3442119,13z/data=!3m1!4b1"

driver = webdriver.Chrome(WEB_DRIVER_PATH)
driver.get(WEBSITE_URL)
print(driver.title)

# driver.quit()
# driver.close()