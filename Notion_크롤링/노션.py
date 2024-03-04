from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://legend-palm-1f1.notion.site/ce4c8faa78b54c0cbe388acc109bf194'

driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.find_all('div', class_ = 'notion-table-row')

for i in items: 
    A1 = i.select_one('.notion-table-cell').text

    print(f"{A1}")                                        

# li:nth-of-type(2) -> li 태그 2번째 가져오겠다. 
# div ---- : nth-of-type(n) { 스타일 지정 }
    
time.sleep(2)
driver.close()