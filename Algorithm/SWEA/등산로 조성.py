T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    point = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    high = []
    h = 0
    for i in range(n):
        for j in range(n):
            if h <= graph[i][j]:
                if h == graph[i][j]:
                    high.append((i, j))
                else:
                    high.clear()
                    high.append((i, j))
                h = graph[i][j]

    MAX = 2
    def dfs(i, j, value, length, k, check):
        global MAX
        MAX = max(MAX,length)

        for di, dj in point:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and graph[ni][nj]-k <= value :
                visited[ni][nj] = 1
                if check :
                    if graph[ni][nj] == value :
                        pass
                    else:
                        dfs(ni,nj,graph[ni][nj],length+1,0,1)
                else :
                    if graph[ni][nj] == value :
                        dfs(ni,nj,graph[ni][nj]-1,length+1,0,1)
                    elif graph[ni][nj] < value :
                        dfs(ni,nj,graph[ni][nj],length+1,k,0)
                    elif graph[ni][nj] > value :
                        for d in range(1,k+1):
                            if graph[ni][nj] - d < value :
                                dfs(ni,nj,graph[ni][nj]-d,length+1,0,1)
                                break
                visited[ni][nj] = 0

        return

    for row,col in high :
        visited = [[0] * n for _ in range(n)]
        visited[row][col] = 1
        dfs(row, col, graph[row][col], 1, k, 0)

    print(f'#{tc} {MAX}')



