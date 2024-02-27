import pymysql
import mysql.connector
from bs4 import  BeautifulSoup
from selenium import  webdriver
from selenium.webdriver.common.by import By
import time

# (1) mysql 연결 설정
db_connection = mysql.connector.connect(
    host = 'localhost', # 내 컴퓨터
    user = 'root', # 계정 
    password = '485029', # 비밀번호 
    database = 'DB_all' # 연결할 DB명
)

# (2) mysql 연결 
cursor = db_connection.cursor()

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

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
# items = soup.select(".qa_item.select") # 값 1개만 가져와짐
items = soup.find_all('div', class_ = 'qa_item')
# 같은 클래스 명의 태그를 다 가져와서 리스트 형태로 저장 (q1, q2 ~ )
# select / find_all 같은 기능 (각 상황마다 다름)

sql = 'insert into ozcodig(Question,Answer) values(%s, %s)'
    # => 데이터를 넣을 부분 테이블명, (개수 % )

for i in items:  # for 문으로 각 값들 출력
    Q1 = i.select_one(".qa_q.bottom-text-l").text
    A1 = i.select_one(".qa_box.bottom-text-m").text.replace('A',"")

    values = (Q1, A1)
            # ->  집어넣을 데이터 변수 명
    cursor.execute(sql,values)  
        # 위에 cursor 선언 꼭 해줘야 함 (sql 연결 부분) 
    db_connection.commit()
        # 위에 sql 문 선언 필수 
            # sql 반영 -> db에  보낸 데이터를 반영하겠다. ( 이부분 필수 )  
    
# import 부분도 sql 되어 있는지 꼭 체크 