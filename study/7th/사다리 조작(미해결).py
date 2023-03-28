import sys
input = sys.stdin.readline

n,m,h = map(int,input().split())
graph = [[0]*(n+1) for _ in range(h+2)]

def move():
    for j in range(1,n+1):
        col = j
        for row in range(1,h+2):
            if graph[row][col] :
                col += 1
            elif graph[row][col-1] :
                col -= 1
        if col != j :
            return False
    return True

for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1

MIN = sys.maxsize
def dfs(idx,cnt):
    global MIN
    if cnt > MIN :
        return

    if move():
        MIN = min(MIN,cnt)
        return MIN

    if cnt == 3 :
        return

    for i in range(idx,h+1):
        for j in range(1,n):
            if graph[i][j] == 0 and graph[i][j - 1] == 0 and graph[i][j+1] == 0 :
                graph[i][j] = 1
                print(i,j)
                dfs(i+1, cnt + 1)
                graph[i][j] = 0

dfs(1,0)

if MIN > 3 :
    print(-1)

else:
    print(MIN)