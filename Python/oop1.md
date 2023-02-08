# 객체 지향 프로그램

## 1. 객체

- 속성(정보) : 직업, 생년월일, 국적 ...
- 행동(동작) : 랩(),댄스() ...
- 속성 - 변수 , 행동 - 함수(메서드)
- 클래스로 정의된 객체는 데이터와 함수를 가진다.


## 2. 인스턴스
- 클래스로 만든 객체를 인스턴스라고 한다.
- 객체와 인스턴스의 차이점 ?
- 클래스 가수 > 이찬혁은 객체다(O) ,  이찬혁은 인스턴스다(X), 이찬혁은 가수의 인스턴스다(O)


```python
class Person:
    pass
print(type(Person)) # <class 'type'>
person1 = Person()

print(isinstance(person1, Person)) # True
print(type(person1)) # <class '__main__.Perosn'>
```

### 1) 객체 비교
``` python
# 변수가참조하는 객체가 내용이 같을 경우 True
a = [1,2,3]
b = [1,2,3]

print(a == b, a is b ) # True False

#두 변수가 동일한 객체를 가리키는 경우 True
a = [1,2,3]
b = a
print(a == b , a is b ) # True True

```

### 2) 인스턴스와 클래스 간의 이름 공간(namespace)

- 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
- 인스턴스를 만들면, 인스턴스 객체가 생성되고 이름 공간 생성
- 인스턴스에서 특정 속성에 접근하면, 인스턴스-클래스 순으로 탐색

```python
# Person 정의
class Person :
    name = 'unknown'
    def talk(self):
        print(self.name)

p1 = Person()
p1.talk() # unknown

# p2 인스턴스 변수 설정 전/후
p2 = Person()
p2.talk() # unknown
p2.name = 'kim'
p2.talk() # Kim

print(Person.name) # unknown
print(p1.name) # unknown
print(p2.name) # Kim
```
### 3) 클래스 변수
```python
class Circle():
    pi = 3.14 # 클래스 변수 정의

    def __init__(self, r):
        self.r = r # 인스턴스 변수

c1 = Circle(5)
c2 = Circle(10)

print(Circle.pi) # 3.14
print(c1.pi) # 3.14
print(c2.pi) # 3.14

Circle.pi = 5
print(Circle.pi) # 5
print(c1.pi) # 5
print(c2.pi) # 5
```
- 한 클래스의 모든 인스턴스가 공유하는 값을 의미
- 같은 클래스의 인스턴스들은 같은 값을 갖게 됨
- 예) 특정 사이트의 User 수 등은 클래스 변수를 사용해야함


### 4) 인스턴스 변수
```python
class Person:

    def __init__(self,name): # 클래스를 생성할 때 부르는 함수 : 생성자
        self.name = name

john = Person('john')
print(john.name) # john
john.name = 'john Kim'
print(john.name) # john Kim
```
- self : 인스턴스 자기 자신

## 3.메서드
- 특정 데이터 타입/클래스에 객체에 공통적으로 적용 가능한 행위(함수)
```python
class Person :

    def talk(self):
        print('안녕')
    def eat(self, food) :
        print(f'{food}를 냠냠')

person1 = Person()
person1.talk() # 안녕
person1.eat('피자') # 피자를 냠냠
person1.eat('치킨') # 치킨을 냠냠
```
### 1) 인스턴스 메서드
- 인스턴스 변수를 사용하거나, 인서턴스 변수에 값을 설정하는 메서드
- 클래스 내부에서 정의되는 메서드의 기본
- 호출 시, 첫번째 인자로 인스턴스 자기자신(self)이 자동으로 전달됨


### 2) 클래스 메서드
- 클래스가 사용 할 메서드
- @classmethod 데코레이터를 사용하여 정의
- 호출 시, 첫번째 인자로 클래스(cls)가 전달됨
```python
class Person :
    count = 0 # 클래스 변수
    def __init__(self, name): # 인스턴스 변수 설정
        self.name = name
        Person.count += 1

    @classmethod
    def number_of_population(cls):
        print(f'인구수는 {cls.count}입니다.')

person1 = Person('아이유')
person2 = Person('이찬혁')

Person.number_of_population()
person1.number_of_population()
person2.number_of_population()
```

### 3) 클래스 메서드와 인스턴스 메서드
- 클래스 메서드 -> 클래스 변수 사용
- 인스턴스 메서드 -> 인스턴스 변수 사용
- 그렇다면 인스턴스 변수, 클래스 변수 모두 사용하고 싶다면?

    - 클래스는 인스턴스 변수 사용이 불가능
    - 인스턴스 메서드는 클래스 변수, 인스턴스 변수 둘 다 사용이 가능

### 4) 스태틱 메서드
- 스태틱 메서드
  - 인스턴스 변수, 클래스 변수 아무것도 사용하지 않을 경우 사용
    - 즉, 객체 상태나 클래스 상태를 수정할 수 없음
  - @staticmethod 데코레이터를 사용하여 정의
  - 일반 함수처럼 동작하지만, 클래스의 이름공간에 귀속됨
    - 주로 해당 클래스로 한정하는 용도로 사용
```python
class Person:
    count = 0 # 클래스 변수
    def __init__(self, name): # 인스턴스 변수 설정
        self.name = name
        Person.count += 1

    @staticmethod
    def check_rich(money): # 스태틱은 cls, self 사용 x
        return money > 10000

person1 = Person('아이유')
person2 = Person('이찬혁')
print(Person.check_rich(100000)) # True 스태틱은 클래스로 접근 가능
print(person1.check_rich(100000)) # True 스태틱은 인스턴스로 접근 가능

```
## 4. 데코레이터
- 함수를 어떤 함수로 꾸며서 새로운 기능을 부여
- @데코레이터(함수명) 형태로 함수 위에 작성
- 순서대로 적용되기 때문에 작성 순서가 중요

```python
def ko_hello(name);
    print(f'안녕하세요, {name}님!')

def en_hello(name):
    print(f'Hello, {name}님!')

def emoji_hello(name, func):
    func(name)
    print('^~^//')

emoji_hello('aiden', ko_hello)
emoji_hello('aiden', en_hello)
```
```python
def emoji_decorator(func):
    def wrapper(name):
        func(name)
        print("^~^//")

    return wrapper

def ko_hello(name):
    print(f'안녕하세요, {name}님!')

def en_hello(name):
    print(f'Hello, {name}!)

emoji_decorator(ko_hello)('aiden') 
# emoji_decorator(ko_hello) = wrapper
# emoji_decorator(ko_hello)('aiden') = wrapper('aiden')
```
```python
def emoji_decorator(func):
    def wrapper(name):
        func(name)
        print("^~^//")

    return wrapper

@emoji_decorator
def ko_hello(name):
    print(f'안녕하세요, {name}님!')

@emoji_decorator
def en_hello(name):
    print(f'Hello, {name}!)

ko_hello('aiden')
```
