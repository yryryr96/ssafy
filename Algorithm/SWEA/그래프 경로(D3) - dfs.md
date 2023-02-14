# 그래프 경로(D3) - dfs

```python
T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    graph = [[0 for _ in range(V+1)] for _ in range(V+1) ]
    for i in range(E):
        a,b = map(int,input().split())
        graph[a][b] = 1 # 간선 상태 표시
    S,G = map(int,input().split())
    visited = [0]*(V+1) # visited 함수 초기화
    stack = [S]

    while stack:
        now = stack.pop()
        visited[now] = 1

        for i in range(1,V+1):
            if graph[now][i] == 1 and visited[i] == 0 :
                stack.append(i)

    if visited[G] == 1 :
        print(f'#{tc} 1')
    else :
        print(f'#{tc} 0')
```

