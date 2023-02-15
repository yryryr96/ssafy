# SEWA 미로 (Backtracking)

```python
# 참고해서 푼거
point = [[1,0],[0,1],[-1,0],[0,-1]]
found = 0
def back(i,j):
    global found
    for di,dj in point:
        ni = i +di; nj = j+dj
        if 0<= ni < N and 0 <= nj < N and visited[ni][nj]==0:
            visited[ni][nj] = 1
            if lst[ni][nj] == 0 :
                back(ni,nj)
            elif lst[ni][nj] == 3 :
                found = 1
                return

T = int(input())
for tc in range(1,T+1):
    found = 0
    N = int(input())
    lst = [list(map(int,input())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if lst[i][j] == 2:
                visited[i][j] = 1
                back(i,j)
                break
    print(f'#{tc} {found}')

```

```python
# 내가 푼거
T = int(input())
for tc in range(1,T+1):
    point = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    N = int(input())
    graph = [list(map(str,input())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    stack = []
    row = col = 0
    temp = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == '2' :
                row = i
                col = j
    
    stack.append([row,col])
    
    while stack:
        now = stack.pop()
        visited[now[0]][now[1]] = 1
        
        for di,dj in point:
            ni = now[0] + di
            nj = now[1] + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 :
                if graph[ni][nj] == '0' :
                    stack.append([ni,nj])
                elif graph[ni][nj] == '3' :
                    temp = 1
                    break
                else :
                    continue

    print(f'#{tc} {temp}')
```

