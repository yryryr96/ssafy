# Union Find

```python
# boj 1717 집합의 표현

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
parent = list(range(n+1))

def find(x):
    if parent[x] != x :
        parent[x] = find(parent[x]) # 갱신 하는 과정 (재귀)
    return parent[x]    # 다 갱신하고 리턴

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b :
        parent[a] = b
    else :
        parent[b] = a

for i in range(m):
    check, a, b = map(int,input().split())
    if check ==  0 :	# 0 일때 합치기
        union(a,b)
    else :				# 1 일때 부모 확인하기
        if find(a) == find(b):
            print("YES")
        else :
            print('NO')

# 전체적인 흐름
# 각 인덱스값을 원소로 가지는 n개의 집합이 있다
# find 함수는 그 인덱스의 부모 노드를 찾는 함수이다.
# union 함수는 두개의 인자를 받아 find함수를 통해 각 인자의 부모를 찾고 더 큰 부모쪽으로 작은 쪽을 합쳐주는 함수이다. 합치는 조건은 쓰기 나름
```

<img src="https://blog.kakaocdn.net/dn/1IkpF/btrX2qAyKOP/0PAwWPzhvRIfT48vMbQmd0/img.png" alt="img" style="zoom: 33%;" />

<img src="https://blog.kakaocdn.net/dn/ejvpPF/btrX1N35EE9/K7mK3TIOHtGEIRg9N89P50/img.png" alt="img" style="zoom: 33%;" />

### Union : 서로 교집합이 없는 집합이 여러개 있을 때 합쳐주는 역할

- 기본적으로 각 집합의 루트노드를 찾아 더 높은 인덱스를 가진 쪽이 작은 쪽을 흡수하는 성질을 가지고 있다.