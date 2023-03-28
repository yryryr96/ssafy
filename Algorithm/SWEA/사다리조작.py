import sys
input = sys.stdin.readline

n,m,h = map(int,input().split())
graph = [[0]*(n+1) for _ in range(h+1)]

def check(): # 가로 선 개수 세는 함수
    row_check = [0] * (n + 1)
    for j in range(1,n):
        for i in range(1,h+1):
            if graph[i][j] == 1:
                row_check[i] += 1
    if max(row_check) < m :
        return True
    else :
        return False

def move():
    for j in range(1,n+1):
        i = 1
        visited = [[0]*(n+1) for _ in range(h+1)]
        row,col = i,j
        while True :
            visited[row][col] = 1
            if row == h :
                if col != j :
                    return False
                break
            if graph[row][col] == 1 and visited[row][col+1] == 0:
                col += 1
            else:
                if graph[row][col-1] == 1 and visited[row][col-1] == 0 :
                    col-=1
                else:
                    row += 1
    return True

for i in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1

for i in range(h+1):
    print(*graph[i])

def dfs(i,j,cnt):
    if j >= n+1 :
        i += 1
        j = 1

    if i == h + 1 :
        return

    if move():
        return cnt

    if graph[i][j] == 0 :
        if (j+1 <= n and graph[i][j+1] != 1) and (graph[i][j-1] != 1) and check:
            print(i, j,cnt)
            graph[i][j] = 1
            dfs(i,j+1,cnt+1)
            graph[i][j] = 0

    dfs(i,j+1,cnt)



print(dfs(1,1,0))
print()
for i in range(h+1):
    print(*graph[i])
