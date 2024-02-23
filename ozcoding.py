from selenium import webdriver
from selenium.webdriver.chrome.options import Options as opt
from selenium. webdriver.common.by import By
from selenium. webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time

options = opt()
user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
options.add_argument(f"User-Agent={user}")

options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=options)

url = "https://ozcodingschool.com/"
driver.get(url)


x_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div")
print(x_button)

time.sleep(1)
if x_button:
  x_button.click()


# html = driver.page_source
# soup = BeautifulSoup(html, "html.parser")

# items = soup.select(".promotion_item") 

# for i in items:
#     name_DB = i.select_one(".translated_name")
    
#     print (f"")