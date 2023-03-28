import sys
input = sys.stdin.readline

n,m,h = map(int,input().split())
graph = [[0]*(n+1) for _ in range(h+1)]
row_check = [0] * (n + 1)

def move():
    cnt = 0
    for j in range(1,n+1):
        col = j
        for row in range(1,h+1):
            if graph[row][col] :
                col += 1
            elif graph[row][col-1] :
                col -= 1
        if col != j :
            return False
    return True

for i in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    row_check[b] += 1
MIN = sys.maxsize
def dfs(i,j,cnt):
    global MIN
    if j >= n+1 :
        i += 1
        j = 1

    if i == h + 1 :
        return

    if cnt > 3 :
        return

    if move():
        MIN = min(MIN,cnt)
        return


    if graph[i][j] == 0 :
        if (j+1 <= n and graph[i][j+1] != 1) and (graph[i][j-1] != 1) and row_check[j] < m :
            graph[i][j] = 1
            row_check[j] += 1
            dfs(i,j+1,cnt+1)
            row_check[j] -= 1
            graph[i][j] = 0



    dfs(i,j+1,cnt)


dfs(1,1,0)

if MIN == sys.maxsize or MIN > 3 :
    print(-1)

else:
    print(MIN)

