# 스택 (Stack)


<img src="https://wikidocs.net/images/page/130075/%EA%B7%B8%EB%A3%B9_5.png" alt="img" style="zoom:67%;" />

>>>>>>> 719098f45c65dabe6dfa3879c920e81495e6c049

- 스택은 위 사진처럼 같은 구조와 크기의 자료를 정해진 방향으로만 쌓을 수 있고, top으로 정한 곳을 통해서만 접근할 수 있다.
- top은 가장 최근에 들어온 자료를 가리키며, 삽입되는 새 자료는 top 위에 쌓인다.
- 스택에서 자료를 삭제할 때도 top에서 이루어진다.
- 삽입을 'push', 삭제를 'pop' 이라 한다.
- 가장 마지막에 삽입된 자료가 가장 먼저 삭제된다 -> 후입선출(LIFO, Last-In-First-Out) 구조
  - stack underflow : 비어있는 스택에서 원소를 추출하는 경우
  - stack overflow : 스택이 넘치는 경우
-  활용 예시
  - 웹 브라우저 방문기록 (뒤로 가기) : 가장 나중에 열린 페이지부터 다시 보여준다.
  - 역순 문자열 만들기 : 가장 나중에 입력된 문자부터 출력한다.
  - 실행 취소 (undo) : 가장 나중에 실행된 것부터 실행을 취소한다.

```python
# 스택 문제 예시 (boj 1874번)
# 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.

import sys
input = sys.stdin.readline
n = int(input())
lst = []
ans = []
cnt = 1
temp = True
for i in range(n):
    num = int(input())

    while cnt <= num : 		# num 까지 순서대로 스택에 채워줌
        lst.append(cnt)		# cnt 초기화 안해서 마지막  push한 숫자 기억
        ans.append('+')
        cnt += 1

    if lst[-1] == num :		# push한 숫자가 num이면 pop
        lst.pop()
        ans.append('-')
    else :
        temp = False		# push한 숫자가 num이 아니면 만들기 불가능
if temp == False :
    print('NO')
else:
    for i in ans:
        print(i)
```



# 큐 (QUEUE)

<img src="https://wikidocs.net/images/page/130075/%EA%B7%B8%EB%A3%B9_41.png" alt="img" style="zoom: 50%;" />

- rear을 통해서 삽입, front를 통해서 삭제가 이루어짐 ( **rear -> front**  )
- 삽입연산을 인큐(enQueue), 삭제연산을 디큐(deQueue)라 한다.

- 접근은 가장 첫 원소와 끝 원소로만 가능
- 가장 먼저 들어온 front가 가장 먼저 삭제 -> **선입선출(FIFO, First in first out) 방식** 자료구조
- 활용 예시
  - 우선순위가 같은 작업 예약 (프린터의 인쇄 대기열)
  - 은행 업무
  - 콜센터 고객 대기시간
  - 프로세스 관리
  - 너비 우선 탐색 (BFS) 구현
  - 캐시(Cache) 구현

```python
import sys

q = []
for _ in range(int(sys.stdin.readline().rstrip())):
    command = list(sys.stdin.readline().split())

    if command[0] == 'push':
        q.append(command[1])

    elif command[0] == 'pop':
        if q:
            a = q.pop(0)
            print(a)
        else :
            print(-1)

    elif command[0] == 'size' :
        print(len(q))

    elif command[0] == 'empty' :
        if q:
            print(0)
        else :
            print(1)

    elif command[0] == 'front' :
        if q:
            print(q[0])
        else :
            print(-1)

    elif command[0] == 'back' :
        if q:
            print(q[-1])
        else :
            print(-1)
```



# Deque (Double-ended queue)

- 큐의 앞과 뒤 모두에서 삽입 및 삭제가 가능한 큐

```python
import sys
input = sys.stdin.readline

lst = []
T = int(input())
for tc in range(1,T+1):
    command = list(map(str,input().split()))

    if command[0] == 'push_back' :
        lst.append(int(command[1]))

    elif command[0] == 'push_front' :
        lst.insert(0,int(command[1]))

    elif command[0] == 'pop_front' :
        if not lst:
            print(-1)
        else:
            print(lst.pop(0))

    elif command[0] == 'pop_back' :
        if not lst :
            print(-1)
        else :
            print(lst.pop())

    elif command[0] == 'size' :
        print(len(lst))

    elif command[0] == 'empty' :
        if lst:
            print(0)
        else :
            print(1)

    elif command[0] == 'front' :
        if lst :
            print(lst[0])
        else :
            print(-1)

    elif command[0] == 'back' :
        if lst :
            print(lst[-1])
        else :
            print(-1)
```

