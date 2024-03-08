-- tabel 생성 
use testdatabase; -- 여기서 진행중일때 작성
create table orders(
	order_id int primary key 
    user_id int, 
    product_name varchar (255), 
    -- product_name: 주문된 제품의 이름을 저장
    -- 255짜리 공간을 비워두는데 10개가 들어오면 10칸으로 공간 최적화한다.
    quantity int , 
    -- quantity: 주문된 제품의 수량을 저장
    foreign key (user_id) references users(user_id) -- foreign (외부키) users table 에 user_id를 참고하겠다.
);

-- 해당 테이블 불러오기
use testdatabase;
-- 모든 컬럼 조회 
select * from users;

-- 파이썬 if else 동일하게 사용
when age >= 50 then '값' 
else '값'

-- 1. insert문 [ 가장 기본적 형태로 모든 컬럼에 값을 지정하여 레코드 추가]
-- users 라는 tabel 에 () 를 넣어달라 내용은 ()다.
insert into users (username, email, age) values ('sohee','sohee@gmail.com',29);

-- 2. 모든 컬럼에 값을 지정하지 않는 경우 [일부 컬럼에만 값을 지정하고 나머지는 null 값을 가지도록]
insert into users (username, email) values ('yoonsohee', 'jen@naver.com');

-- 3. 다수의 레코드 한 번에 추가 [일부만 추가하려면 하나씩 빼주면 됨]
insert into users (username, email,age) values
    ('bob', 'hello@naver.com','20'),
     ('jenny', 'jenny@gmail.com','30');

-- 4. 중복된 값이 있는 경우 해당 레코드를 업데이트 [25와 같은 데이터 있을 경우 100으로 업데이트]
insert into users (username, email,age) values ('yoonsohee', 'jen@naver.com','100')
ON duplicate key update age = 25;


-- 5. set문을 사용하여 컬럼에 여러 값들을 설정할 수 있다.
insert into users set username='jon',email='jon@gmail.com',age=30;


--------------[ SQL 기초 ]--------------

-- 기본적인 조회 select from [ * 는 모든 것 조회 뜻 ]
-- 모든 컬럼 조회 
select * from users;
-- 특정 컬럼만 조회 
select user_id, username, emil from users;

-- distinct 를 사용하면 전체 컬럼 중에서 중복이 없는 유일한 값만 불러오기
select distinct age from users;

-- 일시적으로 추가 컬럼 만들기 - AS
-- 나이와 나이에 100을 곱한 값 조회 
select age, age * 100 from users;

-- AS를 사용하여 새로운 컬럼명 정의
select age, age * 100 AS 곱100 from 

-- 데이터 정렬 
select * from users order by age;

-- 나이순으로 오름, 내림차순 정렬 [ ASC : 오름차순, BESC : 내림차순 ]
select * from users order by age desc;
select * from users order by age ASC;
-- 1번째 차순으로 정렬 후, 생성된 순[created] 으로 2번째 정렬
select * from users order by age ASC, created desc;

-- 조건문 [ where ]
-- 조건에 맞는 데이터 조회
select * from users where age = 30;
-- 문자열은 ''표시 
select * from users where username = 'sohee';

-- >= 데이터 조회
select * from users where age >=30 ;

-- and, or를 사용한 복합 조건 
-- age 30인 데이터 or name 이 sohee 라는 데이터 조회
select * from users where age = 30 or username = 'sohee';
-- 둘 다 조건에 만족하는 데이터를 조회 
select * from users where age = 30 and username = 'sohee';

-- NOT 을 사용한 부정 조건 [나이가 25가 아닌 것 조회]
select * from users where not age = 25;

-- between 을 사용한 범위 지정 [20에서 25까지 조회]
select * from users where age between 20 and 25;

-- 특정 개수 제한 limit [ 3개의 결과값만 조회]
select * from users limit 3;
-- 3번째 페이지부터는 3개의 데이터만 조회 (페이징)
select * from users limit 3 ,3;

-- group by 결과 그룹핑 [ 전체 값에서 age 가 각 몇 개 있는지]
select age, count(*) from users group by age;
-- AS 사용하여 이름 넣어주기
select age, count(*) AS age_count from users group by age; 

-- 특정 조인에 따라 값 변환 case when
-- 나이가 30인 경우 '성인', 미만인 경우 '미성년자'로 변환하여 조회
-- 데이터 저장은 아니기 때문에 실제 조회 시 구분이 뜨진 않음
select username, age, case when age >= 30 then '성인'
else '미성년자' end as 구분 from users;

-- 결과를 나이에 따라 내림 차순으로 순위 부여 
select username, age, row_number()over (order by age desc) as 'rank' from users;

-- 데이터 업데이트 - update set [ update 쿼리 ]
    -- update 할거다 user_id 가 1인 것을 또히로 set(변경)
update users -- 테이블명 : 업데이트할 테이블 이름 
set username = '또히' -- 컬럼 = 값 : 업데이트할 컬럼과 새로운 값을 지정
where user_id = 1; -- where 조건 : 어떤 레코드를 업데이트할지 결정하는 조건 

-- 나이가 100살인 사람 이름을 백살로 모두 변경
update users 
set username = '백살'
where user_id = 5;

-- 세이프 모드 중 오류 시 세이프 모드 비활성화 입력 
set sql_safe_updates = 0; 

-- 업데이트된 레코드 수 확인 (반환)
select row_count();

-- age가 30인 레코드 중 가장 위 1번째 이름을 변경
update users set username = 'top5_young_people'
where age = 30 limit 1; 

update users set email = count(email, '_new')
where email regexp '@naver\.com$';

--------------[ SQL 데이터 삭제 ]--------------

-- 조건을 사용한 삭제 
delete from users where age = 25;
delete from users where username = '또또히';

-- 또또히 중 1개만 삭제 (limit)
delete from users where username = '또또히' limit 1;


--------------[ SQL 심화 ]--------------


