# 트리 (Tree)

![image-20230222090806002](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230222090806002.png)

- ### 트리의 개념

  - 비선형 구조
  - 원소들 간에 1:n 관계를 가지는 자료구조
  - 원소들 간에 계층관게를 가지는 계층형 자료구조
  - 상위 원소에서 하위 원소로 내려가면서 확장되는 트리 모양

- ### 트리의 용어

  - 노드 - 트리의 원소 (A,B,C,D,E,F,G,H,I,J)
  - 간선- 노드를 연결하는 선. 부모 노드와 자식 노드를 연결
  - 루트 노드 - 트리의 시작 노드 (A)
  - 형제 노드 - 같은 부모 노드의 자식 노드들 (F,G)
  - 조상 노드 - 간선을 따라 루트 노드까지 이르는 경로에 있는 모든 노드들 (J의 조상노드 : E,B,A)
  - 서브 트리 - 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리
  - 자손 노드 - 서브 트리에 있는 하위 레벨의 노드들 (D의 자손 노드 - H,I)
  - 차수
    - 노드의 차수 - 노드에 연결된 자식 노드의 수 ( B의 차수 2 , E 의 차수 1)
    - 트리의 차수 - 노드의 차수중에 가장 큰 값 (T - 2)
    - 단말 노드 - 차수가 0인 노드, 자식 노드가 없는 노드
  -  높이
    - 노드의 높이 - 루트에서 노드에 이르는 간선의 수, 노드의 레벨 (D의 높이 2, H의 높이 3)
    - 트리의 높이 - 노드의 높이 중에 가장 큰 값 , 최대 레벨 (T의 높이 3) 

- ### 트리의 특징

  - 그래프의 한 종류이다. ' 최소 연결 트리 ' 라고도 불린다.
  - 트리는 DAG( Directed Acyclic Graphs, 방향성이 있는 비순환 그래프)의 한 종류이다.
    - loop, circuit 이 없다. 당연히 self-loop 도 없다.
    - 즉, 사이클이 없다.
  - 노드가 N개인 트리는 항상 N-1개의 간선을 가진다.
    - 즉, 간선은 항상 (정점의 개수 -1) 만큼 가진다.
  - 루트에서 어떤 노드로 가는 경로는 유일하다.
    - 임의의 두 노드 간의 경로도 유일하다. 즉, 두개의 정점 사이에 반드시 1개의 경로만을 가진다.
  - 한 개의 루트 노드만이 존재하며 모든 자식 노드는 한 개의 부모 노드만을 가진다.
    - 부모-자식 관계이므로 top-bottom or bottom-top 으로 이루어진다.
  - 순회는 Pre-order, In-order, Post-order 로 이루어진다. 이 3가지 모두 BFS/DFS 안에 있다.
  - 트리는 이진트리, 이진 탐색 트리, 균형트리(AVL 트리, red-black 트리), 이진 힙(최대힙, 최소힙) 등이 있다.

- ### 트리의 종류 

  - #### 이진 트리 (Binary Tree)

    - 각 노드가 최대 두개의 자식을 갖는 트리
    - 모든 트리가 이진 트리는 아니다.
    - 레벨 i에서의 노드의 최대 개수는 2^i 개
    - 높이가 h인 이진 트리가 가질 수 있는 노드의 최소 개수는 (h+1) 개가 되며, 최대 개수는 2^(h+1)-1 개가 된다.

  

  - #### 포화 이진 트리(Full Binary Tree)

    - 모든 레벨에 노드가 포화상태로 차 있는 이진 트리
    - 높이가 h일 때, 최대의 노드 개수인 (2^(h+1)-1)의 노드를 가진 이진 트리
      - 높이 3일 때 15개의 노드
    - 루트를 1번으로 하여 2^(h+1)-1 까지 정해진 위치에 대한 노드 번호를 가짐

  <img src="C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230222093157881.png" alt="image-20230222093157881" style="zoom:50%;" />

  - #### 완전 이진 트리 (Complete Binary Tree)

    - 높이가 h이고 노드의 수가 n개일 때, 포화 이진 트리의 노드 번호 1번부터 n번까지 빈 자리가 없는 이진 트리

  <img src="C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230222093446088.png" alt="image-20230222093446088" style="zoom: 50%;" />

  - #### 편향 이진 트리 (Skewed Binary Tree)

    - 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 이진 트리

  <img src="C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230222093738919.png" alt="image-20230222093738919" style="zoom:50%;" />

  - #### 순회 (traversal) - 트리의 노드들을 체계적으로 방문하는 것

  - #### 3가지의 기본적인 순회방법

    - 전위 순회 (preorder traversal) : VLR
      - 부모노드 방문 후, 자식 놔드를 좌,우 순서로 방문한다.
    - 중위 순회(Inorder traversal) : LVR
      - 왼쪽 자식노드, 부모노드, 오른쪽 자식노드 순으로 방문한다.
    - 후위 순회(postorder traversal) : LRV
      - 자식노드를 좌우 순서로 방문한 후, 부모노드로 방문한다.

```python
def pre(n):	# 전위순회(VLR)
    print(n, end=' ')

    if left[n]:
        pre(left[n])

    if right[n]:
        pre(right[n])
    return

def inorder(n):	# 중위순회(LVR)

        if left[n] :
            inorder(left[n])
        print(n, end=' ')
        if right[n] :
            inorder(right[n])
        return


def post(n):    # 후위순회(LRV) 는 루트에서 끝이난다
    if left[n]:
        post(left[n])

    if right[n]:
        post(right[n])

    print(n, end=' ')

    return

V = int(input())
lst = list(map(int,input().split()))
E = V - 1   # 간선 수
left = [0] * (V+1)  # 부모를 인덱스로 왼쪽 자식 저장
right = [0] * (V+1) # 부모를 인덱스로 오른쪽 자식 저장
par = [0] * (V+1)   # 자식을 인덱스로 부모 저장

for i in range(E):
    p,c = lst[i*2], lst[i*2 + 1]
    if left[p] == 0 :
        left[p] = c
    else :
        right[p] = c
    par[c] = p

root = 1
while par[root] != 0:   # root 찾기 -> 자식의 부모가 0 이면 그때 노드가 루트다.
   root += 1

pre(3)
print()
inorder(3)
print()
post(3)
```



- #### 이진 탐색 트리

  - 탐색 작업을 효율적으로 하기 위한 자료구조

  - 모든 원소는 서로 다른 유일한 키를 갖는다.

  - 왼쪽 서브트리 < 루트 노드 < 오른쪽 서브트리

  - 왼쪽 서브트리와 오른족 서브트리도 이진 탐색 트리다.

  - 중위 순회하면 오름차순으로 정렬된 값을 얻을 수 있다. (VLR)

  - ##### 탐색 연산

    - 루트에서 시작한다.
    - 탐색할 키 값 x를 루트 노드의 키 값과 비교한다.
      - x = 루트노드의 키 값인 경우 : 원하는 원소를 찾았으므로 탐색연산 성공
      - x < 루트노드의 키 값인 경우 : 루트 노드의 왼쪽 서브트리에 대해 탐색연산 수행
      - x > 루트노드의 키 값인 경우 : 루트 노드의 오른쪽 서브트리에 대해 탐색연산 수행

  - ##### 삽입 연산

    - 먼저 탐색 연산을 수행
      - 삽입할 원소와 같은 원소가 트리에 있으면 삽입할 수 없으므로, 같은 원소가 트리에 있는지 탐색하여 확인한다.
      - 탐색에서 탐색 실패가 결정되는 위치가 삽입 위치가 된다.
    - 탐색 실패한 위치에 원소를 삽입한다.

- ### HEAP (힙)

  - 완전 이진 트리에 있는 노드 중에서 키 값이 가장 큰 노드나 키 값이 가장 작은 노드를 찾기 위해서 만든 자료구조

  - 힙 트리에서는 중복된 값을 허용한다. ( 이진 탐색 트리에서는 중복된 값을 허용하지 않는다. )

  - 힙은 일종의 반정렬 상태(느슨한 정렬 상태) 를 유지한다.

    - 큰 값이 상위 레벨에 있고 작은 값이 하위 레벨에 있다는 정도
    - 간단히 말하면 부모 노드의 키 값이 자식 노드의 키 값보다 큰(작은) 이진 트리를 말한다.

  - ##### 최대 힙(max heap)

    - 키 값이 가장 큰 노드를 찾기 위한 완전 이진 트리
    - 부모노드의 키 값 > 자식 노드의 키 값
    - 루트 노드 : 키 값이 가장 큰 노드

  - ##### 최소 힙(min heap)

    - 키 값이 가장 작은 노드를 찾기 위한 완전 이진 트리
    - 부모노드의 키 값 < 자식 노드의 키 값
    - 루트 노드 : 키 값이 가장 작은 노드

```python
# max heap

def enq(n):
    global last
    last += 1           # 완전이진트리에 마지막 정점을 추가하고
    heap[last] = n      # 마지막 정점에 저장
    c = last            # 부모가 있고, 부모 > 자식 조건 검사를 위해
    p = c//2
    while p > 0 and heap[p] < heap[c] : # 정렬하는 과정
        heap[c],heap[p] = heap[p], heap[c]
        c = p           # 옮긴 자리에서 부모와 비교하기 위해
        p = c//2

    return

def deq():
    global last
    temp = heap[1]          # 루트 임시 저장
    heap[1] = heap[last]    # 마지막 정점의 값을 루트로 이동
    last -= 1               # 마지막 정점 삭제
    p = 1
    c = p * 2
    while c <= last :   # 자식이 하나 이상 있으면
        if c+1 <= last and heap[c] < heap[c+1] : # 오른쪽 자식도 있고, 오른쪽 자식의 키가 더 크면
            c += 1          # 비교 대상을 오른쪽 자식으로 변경

        if heap[c] > heap[p] :  # 자식이 부모보다 크면
            heap[c] , heap[p] = heap[p], heap[c]
            p = c
            c = p * 2

        else :
            break
    return temp

heap = [0] * 101 # 완전이진트리 1-100번 인덱스 준비
last = 0

enq(5)
print(heap[1])
enq(10)
print(heap[1])
enq(8)
print(heap[1])
enq(20)
print(heap[1])

while last > 0 :
    print(deq())
```

