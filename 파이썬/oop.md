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

print(isinstance(person, Person)) # True
print(type(person1)) # <class '__main__.Perosn'>
```

### 1) 객체 비교
``` python
a = [1,2,3]
b = [1,2,3]

print(a == b, a is b ) # True False

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

### 3) 인스턴스 변수
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

