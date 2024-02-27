# 추가 연습: 크롤링, DB Insert

# 목표사이트 OZ코딩스쿨 지원절차의 FAQ, 선발기준(notion)

from    bs4                             import  BeautifulSoup
from    selenium                        import  webdriver
from    selenium.webdriver.common.by    import  By
import  time



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
faqLists = driver.find_element(By.ID, 'qaList')
fLists = faqLists.find_elements(By.CLASS_NAME, 'qa_q.bottom-text-l')
print(fLists[1].text)
temps = faqLists.find_elements(By.CLASS_NAME, 'qa_box.bottom-text-m')
aLists = temps.find_elements(By.CLASS_NAME, 'qa_box.bottom-text-m')
# qaList
time.sleep(2)

driver.close()