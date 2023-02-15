# Python

### 1. 프로그래밍이란 ?

- 소프트웨어 == 컴퓨터에게 일을 시키는 도구

- 남들과 다른 일을 시키고 싶다면 소프트웨어를 **개발** 
- 소프트웨어를 개발하기 위한 과정 - 코딩 



### 2. python 기초 문법

#### 1) 변수(variable)

- 어떠한 '값'을 저장하기위한 메모리 공간 또는 메모리 공간에 붙인 이름

- a=80   >> 80을 a에 할당한다.

#### 2) 식별자(identifiers)

- 변수의 이름을 식별자라고 함
- 읽기 쉽고 이해하기 쉬운 변수명이 최고임

#### 3) 주석(comment)

- 코드의 실행에 영향을 미치지 않는 나만의 메모
- 이해, 유지보수, 협업에 용이하다



### 3. 자료형(Data type)

- 변수는 주소값의 별명

- my_score = 10 > 10 공간할당 > 공간의 주소 할당 > 주소에 변수 설정

#### 1) 실수형 

```
int : 정수형
float : 실수형
```

#### 2) 문자열 str

```
a = str(6)
print(a) = '6'
```

#### 3) dictionary 

``` 
grade=['john' : 70, 'chris' : 80]

print(dict['key']) >> key의 value값 출력

ex ) print(grade['john'])  > 70
```

### 4. python 제어문

#### 1) for 반복문

- for i in [0,1,2] >> i 에 0,1,2 차례대로 반복
- ex ) scores = [70, 80, 90]

​		for score in scores :

​			print(score)

​		output) 70 80 90 

score에 scores 요소들을 할당 

### 5. python 함수

- parameters  : 함수를 **정의**할 때, 함수 내부에서 사용되는 변수
- return : 함수의 output

def function_name(parameter):
	return returning_value

- Argument : 함수를 **호출** 할 때, 넣어주는 값



#### 6. python의 범위

- Local scope : 지역 범위
- Enclosed scope : 지역 범위 한 단계 위 범위
- Global scope : 최상단에 위치한 범위
- Built-in scope : 모든 것을 담고 있는 범위
- L<E<G<B  :  변수를 검색 할 때 L E G B 순서로 검색
- nonlocal x : 함수내의 x값을 enclosed 함수 x값에 할당 ( 안에서 밖으로~)



#### 7. 모듈과 패키지

- 모듈 : 다양한 기능을 하나의 파일로 : 특정 기능을 하는 코드를 파이썬파일(.py) 단위로 작성한 것
- 패키지 : 다양한 모듈을 하나의 폴더로 : 특정 기능과 관련된 여러 모듈의 집합, 패키지 안에는 또 다른 서브 패키지를 포함
- 라이브러리 : 다양한 패키지를 하나의 묶음으로
- 가상환경 : 패키지의 활용 공간
- pip : 관리자

ex) 모듈과 패키지 불러오기

- import module
- from module import var,function, class
- from module import



- from package import module
- from package.modul import var,function,class

