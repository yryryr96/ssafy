# 최소 신장 트리 (MST)

```python
import sys
input = sys.stdin.readline

v,e = map(int,input().split())
parent = list(range(1,v+1))

def find_parent(parent,x):
    if parent[x] != x :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    
    parent[max(a,b)] = min(a,b)

edges = []
total_cost = 0

for _ in range(e):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))

edges.sort() #reverse=True 해주면 최대값으로 구할 수 있다.

for i in range(e):
    c,a,b = edges[i]
    if find_parent(parent,a) != find_parent(parent,b) :
        union(parent,a,b)
        total_cost += c
print(total_cost)
```