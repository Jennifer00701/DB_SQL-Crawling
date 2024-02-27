from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://legend-palm-1f1.notion.site/ce4c8faa78b54c0cbe388acc109bf194'

driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.select('.notion-table-content')

for i in items: 
    A1 = i.select_one('.notion-table-cell-text').text

    print(A1)


time.sleep(1)
driver.close()