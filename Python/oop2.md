# 객체지향 프로그래밍

### 1.객체지향의 핵심개념
#### 1) 객체지향의 핵심 4가지
- #### 추상화 : 핵심이 되는 부분만 추리기
```python
# 학생(Student)을 표현하기 위한 클래스를 생성
class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa
    
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')
    
    def study(self):
        self.gpa += 0.1

# 교수(Professor)를 표현하기 위한 클래스를 생성
class Professor :
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')
    
    def teach(self):
        self.age += 1

# 사람 클래스
class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')
```


- #### 상속 : 코드의 재사용성을 높이고 기능을 확장
  - 하위 클래스는 상위 클래스에 정의된 속성, 행동, 관계 및 제약 조건을 모두 상속 받음
  - 부모 클래스의 속성, 메서드가 자식 클래스에 상속되므로, 코드 재사용성이 높아짐
```python
class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self) :
        print(f'반갑습니다. {self.name}입니다.')

class Professor(Person):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

class Student(Person):
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa
p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)

p1.talk() # 부모 Person 클래스의 talk 메서드를 활용
s1.talk() # 부모 Person 클래스의 talk 메서드를 활용
```
```
- 파이썬의 모든 클래스는 object로부터 상속됨
- 부모 클래스의 모든 요소(속성,메서드)가 상속됨
- super()를 통해 부모 클래스의 요소를 호출할 수 있음
- 메서드 오버라이딩을 통해 자식 클래스에서 재정의 가능함
- 상속관계에서의 이름 공간은 인스턴스, 자식클래스, 부모클래스 순으로 탐색
```
- 다중 상속
  - 두 개 이상의 클래스를 상속 받는 경우
  - 상속받은 모든 클래스의 요소를 활용 가능함
  - 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정됨

```python
class Person:
    def __init__(self, name):
        self.name = name
    
    def greeting(self):
        return f'안녕, {self.name}'

class Mom(Person):
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'

class Dad(Perosn):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'

class FirstChild(Dad, Mom):
    def swim(self):
        return '첫째가 수영'

    def cry(self):
        return '첫째가 응애'

baby1 = FirstChild('아가')
print(baby1.cry()) # 첫째가 응애
print(baby1.swim()) # 첫째가 수영
print(baby1.walk()) # 아빠가 걷기
print(baby1.gene) # XY

- mro 메서드(Method Resoultion ORder)
    - 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드
    - 기존의 인스턴스 > 클래스 순으로 이름 공간을 탐색하는 과정에서 상속 관계에 있으면 인스턴스 > 자식클래스 > 부모 클래스로 확장
```


- #### 다형성 : 각자의 특성에따라 다른 결과 만들기
    - 여러 모양을 뜻하는 그리스어
    - 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음을 의미
    - 즉, 서로 다른 클래스에 속해있는 객체들이 동일한 메시지에 대해 다른 방식으로 응답할 수 있음
```python
class Person:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')
    
# 자식 클래스 - Professor
class Professor(Person):
    def talk(self):
        print(f'{self.name}일세.')

# 자식 클래스 - Student
class Student(Person):
    def talk(self):
    	super().talk()
    	print(f'저는 학생입니다.')

p1 = Professor('김교수')
p1.talk() # 김교수일세.

s1 = Student('이학생')
s1.talk() 
# 반갑습니다. 이학생입니다.
# 저는 학생입니다.
```
- #### 캡슐화 : 데이터 보호하기
    - 객체의 일부 구현 내용에 대해 외부로부터의 직접적인 액세스를 차단 (주민등록번호~)
    - 파이썬에서 암묵적으로 존재하지만, 언어적으로는 존재하지 않음
- ##### 접근제어자 종류
    - ##### Public Access Modifier
      - 언더바 없이 시작하는 메서드나 속성
      - 어디서나 호출 가능, 하위클래스 override 허용
      - 일반적으로 잓어되는 메서드와 속성의 대다수를 차지
    - ##### Protected Access Modifier
      - 언더바 1개로 시작하는 메서드나 속성
      - 암묵적 규칙에 의해 부모 클래 내부와 자식 클래스에서만 호출 가능
      - 하위 클래스 override 허용
    - ##### Private Access Modifier
      - 언더바 2개로 시작하는 메서드나 속성
      - 본 클래스 내부에서만 사용이 가능
      - 하위클래스 상속 및 호출 불가능(오류)
      - 외부 호출 불가능 (오류)


### 2. 에러와 예외 처리
#### 1) 디버깅
- 잘못된 프로그램을 수정하는 것을 디버깅이라 함
- 에러 메시지가 발생하는 경우
  - 해당하는 위치를 찾아 메시지를 해결
- 로직 에러가 발생하는 경우
  - 명시적인 에러 메시지 없이 예상과 다른 결과가 나온 경우
    - 정상적으로 동작했던 코드 이후 작성된 코드를 생각해봄
    - 전체 코드를 살펴봄
  #### 2) 예외처리
- 예외 처리는 작은 것부터 처리

