from bs4 import  BeautifulSoup 
from selenium import  webdriver
from selenium.webdriver.common.by import By
import time

siteUrl = 'https://ozcodingschool.com/ozcoding/startupcamp'

driver = webdriver.Chrome()
driver.get(siteUrl)
# 셀레니움 방식
promotion = driver.find_element(By.CLASS_NAME, 'promotion_list')
time.sleep(2)
item = promotion.find_elements(By.CLASS_NAME, 'promotion_item')[2]
# 지원절차 URL 탐색
target = item.find_elements(By.CLASS_NAME, 'link-item')[0].get_attribute('href')
print('지원절차:', target)

driver.get(target)
# faqLists = driver.find_element(By.ID,'qaList')
# fLists = faqLists.find_elements(By.CLASS_NAME,'.qa_item.select>.qa_q.bottom-text-l')
# print(fLists[1].text)
# temps = faqLists.find_elements(By.CLASS_NAME, 'qa_box.bottom-text-m')
# aLists = temps.find_elements(By.CLASS_NAME, 'qa_box.bottom-text-m')


html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
# items = soup.select(".qa_item.select") # 값 1개만 가져와짐
items = soup.find_all('div', class_ = 'qa_item')
# 같은 클래스 명의 태그를 다 가져와서 리스트 형태로 저장 (q1, q2 ~ )
# select / find_all 같은 기능 (각 상황마다 다름)

#print(len(items))

for i in items:  # for 문으로 각 값들 출력
    Q1 = i.select_one(".qa_q.bottom-text-l").text
    A1 = i.select_one(".qa_box.bottom-text-m").text.replace('A',"")
                       # .replace('A',"") A를 공백으로 만들기
    print(f"{Q1}")
    print(f"{A1}")
    # print(Q1)


time.sleep(1)
driver.close()
