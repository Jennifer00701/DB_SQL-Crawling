import pymysql
# 파이썬에서 sql 명령 내리기 전 모듈 다운로드 (기본아니라 직접 설치)
import mysql.connector
# from faker import Faker
import random

# (1) mysql 연결 설정
db_connection = mysql.connector.connect(
    host = 'localhost', # 내 컴퓨터
    user = 'root', # 계정 
    password = '485029', # 비밀번호 
    database = 'DB_all' # 연결할 DB명
)

# (2) mysql 연결 
cursor = db_connection.cursor()

# faker = Faker()

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

url = "https://kream.co.kr/"
driver.get(url)

driver.find_element(By.CSS_SELECTOR, ".btn_search").click()
# css 요소에 접근하는 방식 -> 버튼 태그 클릭 (마지막에 액션)
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("슈프림") 
# ("슈프림\n") 도 엔터 기능 가능 
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)

for i in range(20) :
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    driver.save_screenshot("/Users/mac/Desktop/Project/Crawling/kream_screenshot/supreme.png")
    # driver.save_screenshot(f"/Users/mac/Desktop/Project/Crawling/kream_screenshot/supreme{i}.png")
    # tag name 선택 가능 
    time.sleep(0.2)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.select(".product_card")  

sql = 'insert into crawling(product_name,product_info,money,review,wish) values(%s, %s, %s, %s, %s)'
                    # -> 크롤링 : 테이블명
for i in items:
    product_name = i.select_one(".translated_name").text
    product_info = i.select_one(".product_info_product_name").text
    money = int(i.select_one(".amount").text.strip().replace(',',"").replace('원',""))

    wish = i.select_one(".wish_figure").text.replace(',',"").replace('.',"").replace('만',"")
    #크롤링 시 , 나올 때 없애주기 코드 replace(',',"") , .replace('원',"")) 
    

    # int 값 없으면 0으로 표시 
    review = i.select_one(".review_figure").text
    if review == "":
        review = 0
    else:
        review = int(review)
  
    if wish == "":
        wish = 0 
    else:
        wish == int(wish)



    values = (product_name,product_info,money,review,wish)
                   # ->  집어넣을 데이터 변수 명
    cursor.execute(sql, values)
    db_connection.commit()
    # 위에 sql 문 반영 -> db에  보낸 데이터를 반영하겠다. ( 이부분 필수 )




'''
for _ in range(10): #어떤 일을 10번 반복하겠다. 
# 전체적 요약 : 가짜 사용자 이름,이메일 만들어 데이터 베이스에 10번 추가
    
    username = faker.user_name() 
    email = faker.email()
    # faker 임의의 값을 생성하는 라이브러리 가짜 사용자 name,email만들겠다.

    sql = 'insert into users(username, email) values(%s, %s)'
    # 데이터베이스에 새로운 사용자를 추가하겠다. % 는 아직 정해지지 않은 값 의미
    # 나중에 이 자리에 실제 사용자 이름, 이메일이 들어감 
    
    values = (username, email)
    # 앞서 만든 가짜 사용자 이름,이메일을 values 변수에 저장

    cursor. execute(sql, values)
    # 실제로 데이터베이스 사용자 정보를 추가하는 명령 실행
    # cursor : 데이터베이스와 연결을 제어하는 객체 
    # execute : SQL 명령을 실행하는 메소드
    '''