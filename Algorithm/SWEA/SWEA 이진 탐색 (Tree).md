# SWEA 이진 탐색 (Tree)

```python
#SWEA 문젠데 트리의 값을 중위순회(LVR)로 지정해주는 것
T = int(input())

def binary_search(v):
    global num
    if v <= N:
        binary_search(v*2)		# L
        tree[v] = num			# V	, 그 노드의 값 지정 (중위순회 순서)
        num += 1
        binary_search(v*2+1)	# R

for tc in range(1,T+1):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    num = 1
    binary_search(1)
    ans1 = tree[1]
    ans2 = tree[N//2]
    print(f'#{tc} {ans1} {ans2}')
```

```python
#SWEA 문제인데 이건 트리의 값을 중위순회(LVR)를 통해 읽어오는것
for tc in range(1,11):
    N = int(input())
    graph = [[] for _ in range(N+1)]

    for _ in range(N):
        lst = list(map(str,input().split()))
        graph[int(lst[0])] = lst[1]			# 노드의 값을 미리 지정


    def binary(v):
        if v<=N:
            binary(2*v)
            print(graph[v],end='')		# 이미 지정된 노드의 값을 출력(중위순회 순서로)
            binary(2*v+1)
    print(f'#{tc}',end =' ')
    binary(1)
    print()
```



