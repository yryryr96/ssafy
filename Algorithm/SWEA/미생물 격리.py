from collections import deque

def merge():
    for i in range(n):
        for j in range(n):
            if visited[i][j] :
                SUM = 0
                check = 0
                di = 0
                for lst in visited[i][j]:
                    SUM += lst[0]
                    if check < lst[0]:
                        check = lst[0]
                        di = lst[1]
                graph[i][j] = SUM
                q.append((i, j, SUM, di))

T = int(input())
for tc in range(1,T+1):
    n,m,k = map(int,input().split())
    graph = [[0]*n for _ in range(n)]
    point = [[-1,0],[1,0],[0,-1],[0,1]]
    visited = [[[] for _ in range(n)] for _ in range(n)]
    q = deque()

    for _ in range(k):
        r,c,bug,dir = map(int,input().split())
        dir -= 1
        graph[r][c] = bug
        q.append((r,c,bug,dir))

    # for i in range(n):
    #     print(*graph[i])

    while q:
        row,col,b,d= q.pop()
        graph[row][col] = 0

        ni,nj = row + point[d][0], col + point[d][1]
        if ni == 0 or ni == n-1 or nj == 0 or nj == n-1 :
            if d == 1 :
                d = 0
            elif d == 0 :
                d = 1
            elif d == 2 :
                d = 3
            elif d == 3 :
                d = 2
            b = b//2
        if b == 0 :
            continue
        visited[ni][nj].append((b,d))
    merge()

    ans = 0
    for i in range(m - 1):
        visited = [[[] for _ in range(n)] for _ in range(n)]
        while q:
            row, col, b, d = q.pop()
            graph[row][col] = 0
            ni, nj = row + point[d][0], col + point[d][1]
            if ni == 0 or ni == n-1 or nj == 0 or nj == n-1:
                if d == 1:
                    d = 0
                elif d == 0:
                    d = 1
                elif d == 2:
                    d = 3
                elif d == 3:
                    d = 2
                b = b // 2
            if b == 0:
                continue
            visited[ni][nj].append((b, d))

        merge()

    for i in range(n):
        ans += sum(graph[i])
    print(f'#{tc} {ans}')







