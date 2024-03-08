from selenium import webdriver
from selenium.webdriver.chrome.options import Options as opt
from selenium. webdriver.common.by import By
from selenium. webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

options = opt()
user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
options.add_argument(f"User-Agent={user}")

options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=options)

url = "https://legend-palm-1f1.notion.site/ce4c8faa78b54c0cbe388acc109bf194"