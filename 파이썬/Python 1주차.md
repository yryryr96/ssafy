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



## 데이터 구조

- 데이터 구조(Data Structure)
  - 여러 데이터를 효과적으로 사용, 관리하기 위한 구조 ( 많이 사용해보니까, 비슷한 구조가 있음)
  - 파이썬에서는 대표적으로 List, Tuple, Dict, Set 등의 데이터 구조가 있음

```
1. Set : Set이란 중복되는 요소가 없이, 순서에 상관없는 데이터들의 묶음
	- 데이터의 중복을 허용하지 않기 때문에 중복되는 원소가 있다면 하나만 저장
	- 순서가 없기 때문에 인덱스를 이용한 접근 불가능
	- 가변 자료형 (mutable)

2. Dictionary : key, value 쌍으로 이뤄진 자료형
	- key : immutable 데이터만 활용가능 (string, integer, float, boolean, tuple, range)
	- value : 각 key의 값	
```



- 자료형과 메모리

```
데이터 10을 컴퓨터가 기억하는 과정
1. 10을 저장할 공간을 메모리에 만들고
2. 저장할 공간에 대한 주소를 할당받는다.
3. 할당 받은 주소를 기억했다가
4. 10이라는 데이터를 해당 주소로 찾아가서 저장한다.
5. 이후에 10이 필요해지면 해당 주소로 가서 읽어온다. 
```



