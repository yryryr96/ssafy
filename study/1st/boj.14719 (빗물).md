# boj.14719 (빗물)

```python
#1 그래프 구현
import sys
input = sys.stdin.readline
h, w = map(int,input().split())
lst = list(map(int,input().split()))
graph = [[0 for _ in range(h)] for _ in range(w)]
k = 0
for n in lst:
    cnt = 1
    for i in range(n):
        graph[k][i] = cnt
        cnt+=1
    k+=1

SUM = 0
MAX1 = max(graph[0])
M_Idx = lst.index(max(lst))
for i in range(M_Idx):
    if max(graph[i]) > MAX1 :
        MAX1 = max(graph[i])
    SUM += MAX1-max(graph[i])
MAX2 = max(graph[-1])
for i in range(w-1,M_Idx,-1):
    if max(graph[i]) > MAX2:
        MAX2 = max(graph[i])
    SUM += MAX2-max(graph[i])

print(SUM)
```

```python
#2 그래프 구현 안하고
import sys
input = sys.stdin.readline
h, w = map(int,input().split())
lst = list(map(int,input().split()))
M_Idx = lst.index(max(lst))
SUM = 0
MAX1 = 0
MAX2 = 0
for i in range(M_Idx):
    if lst[i] > MAX1 :
        MAX1 = lst[i]
    SUM += MAX1 - lst[i]

for j in range(w-1,M_Idx,-1):
    if lst[j] > MAX2:
        MAX2 = lst[j]
    SUM += MAX2 - lst[j]

print(SUM)
```

