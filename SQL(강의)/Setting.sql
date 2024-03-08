(1) MySQL Community 다운로드 : https://dev.mysql.com/downloads/mysql/
(2) Workbench 다운로드 : https://www.mysql.com/products/workbench/
(3) 터미널 열고 Homebrew 코드 입력(설치 (리눅스명령어))
 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
(4) 터미널 창에서 Homebrew 이용해 mysql 설치 코드 입력 
brew install mysql
(5) MySQL 시작 자동으로 실행 안 될 경우 수동 실행 코드 입력 (시작, 종료)
brew services start mysql
brew services stop mysql
(6) 루트 비밀번호 설정 (명령 코드로 mysql 로그인)
mysql - root
(7) 로그인 후 비밀번호 설정 
alter user 'root'@'localhost'IDENTIFIED by 'class-password';
-- 비밀번호는 입력해도 안 보임 입력 후 엔터 누르면 됨.
(8) 완료 후 나가기 코드 입력
exit

---------- [ Login ]

워크밴치 로그인 시 맥 터미널에 
mysql -u root -p 입력하고 로그인 하면 됨 

----------------Setting [ 2강 참고 ]---------------->>>

-- create database testdatabase; -- 테스트 데이터베이스 생성
-- use testdatabase; -- 테스트 데이터베이스를 사용하겠다.

create table user(  -- 테이블 이름을 만들어주세요 -> 테이블 네임은 user
    id int auto_increment primary key, -- 아이디 값은 int(숫자), primary(고유한값(유일))을 만들거다 (auto_increment - 숫자 1씩증가)
    username varchar(30) not null, -- 필드(컬럼)은 username 이라는 걸 만들거다 (30글자 안으로) - null값 넣을 수 없다는 규칙을 줌
    email varchar(100) unique, -- (100글자 안으로)
    is_business varchar(10) default false, -- 비즈니스 계정을 신청해서 받으면 트루로 바꿔준다.
    age int check (age >= 10) -- 나이 체크 10살이거나 낮으면

-- % 부분은 사용자 입력

-- 유저 확인 
USE mysql;
select * from user;

-- 유저 생성
USE mysql;
CREATE USER 'username'@'localhost' IDENTIFIED BY 'user_password';

-- 사용자 비밀번호 변경
SET PASSWORD FOR 'username'@'%' = '신규비번';

-- 권한 부여 (모든 데이터베이스에 대한 권한 부여)
GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost';
FLUSH PRIVILEGES; (변경된 권한 적용)
SHOW GRANTS FOR 'username'@'localhost'; (부여한 권한 확인)
SHOW GRANTS; (현재 로그인한 유저의 권한 확인)
    -- 권환 확인 예시 : 
    -- show grants for 'username'@'localhost';
    -- show grants;

-- 사용자 삭제 
USE mysql;
DROP USER 'username'@'%';
-- 삭제 예시
drop user 'username'@'localhost';

-- 데이터베이스 생성  (mydatabase 라는 데이터베이스 생성)
CREATE DATABASE mydatabase;

-- 데이터베이스 목록 조회 (모든 데이터베이스 목록 조회)
SHOW DATABASE;

-- 데이터베이스 사용 (mydatabase 데이터베이스 사용)
USE mydatabase

-- 데이터베이스 삭제 ()
DROP DATABASE IF EXISTS mydatabase;
