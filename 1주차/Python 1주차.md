 # Python 1주차

- 프로그래밍이란 ?

​		컴퓨터에게 명령하는 적절한 수행 절차를 정의하고 이를 프로그래밍 언어로 표현하는 과정

​		소프트웨어를 개발하기 위한 과정 > 소프트웨어==컴퓨터에게 일을 시키는 도구



- ### 프로그래밍 과정

1. 컴퓨터에게 시키고 싶은 일을 정한다
2. 컴퓨터가 이해할 수 있도록 수행 절차를 정의해서 표현한다
3.  적절한 프로그래밍 언어를 선택하고, 언어를 이용해서 절차를 기술한다
4. 발생하는 오류를 수정한다



- ### 컴퓨팅 사고력

1. 컴퓨터의 특성을 잘 이해한다
2. 문제 해결 능력을 기른다
3. 프로그래밍 언어에 능숙해진다



# 자료구조

- CRUD : 생성,조회,수정,삭제
- 생성, 삭제 : dictionary 유리
- 조회 : list 유리



## 제어

- continue :  만나면 바로 다음 순번의 루프 실행
- pass : 실행할 코드가 없는 것으로 없는거처럼 실행
- break : 반복문을 멈추고 루프를 나감



## Python의 범위

- Built - in  > Global > Enclosing > Local ( LEGB )

ex) 

x=~

def input():

​		y=~

​			def output():

​				z=~

- **x = global , y = enclosing , z = local**



## 모듈과 패키지

- pip(관리자) > 라이브러리(묶음) > 패키지(폴더) > 모듈(파일)
- 가상환경 : 패키지의 활용공간

calc(폴더)

​	tools.py(모듈)

​	def add(num1,num2):

​		return num1+num2

​	def sub(num1,num2):

​		return num1-num2



check.py(모듈)

1. from calc(패키지) import tools(모듈)

​		tools.add(num1,num2), tools.sub(num1,num2) ~~

2. from calc,tools import add,sub

​		check 에서 선언 시 add sub 사용 가능

