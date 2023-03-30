T = int(input())
for tc in range(1,T+1):
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    point = [[1,1],[1,-1],[-1,-1],[-1,1]]
    MAX = -1
    def dfs(i,j,lst,dir):
        global MAX

        for k in range(dir,dir+2):
            k = k%4
            ni,nj = i + point[k][0], j + point[k][1]

            if ni == s and nj == e and k != 0:
                MAX = max(len(lst), MAX)
                return

            if 0<=ni<n and 0<=nj<n and ni > s and graph[ni][nj] not in lst :
                lst.append(graph[ni][nj])
                dfs(ni,nj,lst,k)
                lst.remove(graph[ni][nj])
        return

    for i in range(n):
        for j in range(n):
            s,e = i,j
            lst = []
            lst.append(graph[i][j])
            dfs(i,j,lst,0)

    print(f'#{tc} {MAX}')