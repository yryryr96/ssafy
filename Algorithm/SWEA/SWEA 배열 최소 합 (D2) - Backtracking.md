# SWEA 배열 최소 합 (D2) - Backtracking

```python
SUM = 0 ; MIN = 1000000
def back(y,x):
    global SUM,MIN
    SUM += graph[y][x]
    if SUM >= MIN: 
	# 처음에 시간초과 떴는데 MIN 보다 SUM이 클때 리턴시켜 시간을 줄여주니 pass
        return
    if y == N-1 :
        if MIN > SUM :
            MIN = SUM
        return

    for i in range(N):
        visited[i][x] = 1

    for i in range(N):
        if visited[y+1][i] == 0 :
            for j in range(N):
                visited[j][i] = 1
            back(y+1,i)
            for j in range(N):
                visited[j][i] = 0
            SUM -= graph[y+1][i]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    visited =[[0 for _ in range(N)] for _ in range(N)]
    ans = []
    SUM = 0
    MIN = 1000000
    y ,x = 0,0
    for i in range(N):
        back(y,x+i)
        visited = [[0 for _ in range(N)] for _ in range(N)]
        SUM = 0
    print(f'#{tc} {MIN}')
```

