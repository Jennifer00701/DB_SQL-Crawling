-- kream 크롤링 한 것 DB 연결 workbench 에서 실행한 것들 참고 메모 ! 


create table crawling( -- crawling 테이블 생성
id int not null auto_increment, -- id 는 고유 값이라 not null 필수, 데이터자동증가
product_name varchar(255) not null, -- str값은 varchar(255)로 지정 
product_info varchar(255) not null, -- 동일하게 null 허용하지 않겠다.(타입 뒤에 넣어야함)
money int not null,
review int,
wish int,
primary key(id) -- ID 값을 이 테이블 고유 값으로 설정하겠다 명령어
);