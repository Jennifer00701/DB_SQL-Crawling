# DB, python 연결 자세한 내용은 git에 크롤링/DB 폴더 확인하면 됨

import mysql.connector
from faker import Faker
import random #파이썬 기본모듈

파이썬에서 sql 명령 내리기 전 모듈 다운로드 (기본아니라 직접 설치)
pip3 install pymysql


# (1) mysql 연결 설정
db_connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '485029',
    database = 'testdatabase'
)

# (2) mysql 연결 
cursor = db_connection.cursor()
faker = Faker()

# 100명의 users 더미 데이터 생성 (랜덤)

for _ in range(100):
    username = faker.user_name()
    email = faker.email()

    sql = 'insert into users(username, email) values(%s, %s)'
    Values = (username, email)

    cursor.execute(sql, Values)

# user_id 가져오기
cursor.execute('select user_id * from users')
valid_user_id = [ row[0] for row in cursor.fetchall()]

# 100개의 주문 더미 데이터 생성
for _ in range(100):
    user_id = random.choice(valid_user_id)
    product_name = faker.word()
    quantity = random.randint(1, 10)
    
    try : 
        sql = 'insert into orders (user_id, product_name, quantity) values(%s, %s, %s)'
        Values = (user_id, product_name, quantity)

        cursor.execute(sql, Values)
    except :
        pass


db_connection.commit()
cursor.close()
db_connection.close()