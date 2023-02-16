```python
point = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
def tracking(i,j,k):
    board[i][j] = k
    for di,dj in point:
        ni = i + di
        nj = j + dj
        lst = []
        while 0<=ni<N and 0<=nj<N:
            if board[ni][nj] == 0 :
                break
            lst.append((ni,nj))
            if board[ni][nj] == k:
                while lst:
                    a,b = lst.pop()
                    board[a][b] = k
                break
            ni, nj = ni+di, nj+dj

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    board = [[0 for _ in range(N)] for _ in range(N)]
    board[N//2-1][N//2-1] = board[N//2][N//2] = 2
    board[N//2-1][N//2] = board[N//2][N//2-1] = 1

    for _ in range(M):
        i,j,k = map(int,input().split())
        i-=1
        j-=1
        tracking(i,j,k)

    W = B = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1 :
                B += 1
            elif board[i][j] == 2:
                W += 1
    print(f'#{tc} {B} {W}')
```

```
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    point = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    graph = [[0 for _ in range(N)] for _ in range(N)]
    graph[N//2-1][N//2-1] = graph[N//2][N//2] = 2
    graph[N//2-1][N//2] = graph[N//2][N//2-1] = 1

    for _ in range(M):
        j, i, color = map(int,input().split())
        i -= 1
        j -= 1
        if not graph[i][j]:
            graph[i][j] = color
            for di,dj in point :
                ni, nj = i + di , j + dj
                lst = []
                while True:
                    if ni < 0 or N - 1 < ni or nj < 0 or N - 1 < nj:
                        reverse = []
                        break
                    if graph[ni][nj] == 0 :
                        lst.clear()
                        break
                    if graph[ni][nj] == color:
                        break
                    else :
                        lst.append((ni,nj))

                    ni += di
                    nj += dj
                for i, j in lst:
                    graph[i][j] = color

    W,B = 0,0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2 :
                W += 1
            elif graph[i][j] == 1:
                B += 1
    print(f'#{tc} {B,W}')
```

문제 잘 읽어보고 좌표 잘 보기