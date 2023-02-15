# SEWA 미로 (Backtracking)

```python
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
