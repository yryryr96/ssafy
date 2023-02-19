def dfs(i,j):
    point = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    graph[i][j] = 0
    for di, dj in point:
        ni,nj = i+di, j+dj
        if 0<=ni<h and 0<=nj<w and graph[ni][nj] == 1:
            dfs(ni,nj)

while True :
    w,h = map(int,input().split())

    if w == 0 and h == 0 :
        break

    graph = [list(map(int,input().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 :
                dfs(i,j)
                cnt += 1
    print(cnt)

# 1일 때 연결된 1들 다 0으로 바꿔주면서 섬의 개수 카운트