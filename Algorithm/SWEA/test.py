T = int(input())
for tc in range(1,T+1):
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    point = [[1,1],[1,-1],[-1,-1],[-1,1]]
    MAX = -1
    def dfs(i,j,dir,lst,dir_lst,depth):
        if depth == 12 :
            print(i,j,lst,dir_lst)
        global MAX
        if len(dir_lst) < 2:
            for d in range(4):
                if d != (dir+2)%4 :
                    ni,nj = i+point[d][0], j+point[d][1]
                    if 0<=ni<n and 0<=nj<n and visited[ni][nj] == 0 and graph[ni][nj] not in lst :
                        visited[ni][nj] = 1
                        if d == dir :
                            lst.append(graph[ni][nj])
                            dfs(ni,nj,d,lst,dir_lst,depth+1)
                            lst.remove(graph[ni][nj])
                        else :
                            lst.append(graph[ni][nj])
                            dir_lst.append(d)
                            dfs(ni, nj, d, lst, dir_lst,depth+1)
                            lst.remove(graph[ni][nj])
                            dir_lst.remove(d)
                        visited[ni][nj] = 0

        else :
            check = (dir_lst[-1]+2)%4
            ki,kj = i+point[check][0],j+point[check][1]
            if ki==s and kj == e and depth >=4:
                MAX = max(MAX,depth)
                return
            for d in range(4) :
                if d in dir_lst :
                    ni,nj = i+point[d][0], j+point[d][1]
                    if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and graph[ni][nj] not in lst:
                        visited[ni][nj] = 1
                        lst.append(graph[ni][nj])
                        dfs(ni,nj,d,lst,dir_lst,depth+1)
                        lst.remove(graph[ni][nj])
                        visited[ni][nj] = 0
        return -1

    for i in range(n):
        for j in range(n) :
            for k in range(4):
                lst = [graph[i][j]]
                dlst = [(k+2)%4]
                s,e = i,j
                visited[i][j] = 1
                dfs(i,j,k,lst,dlst,1)
                visited[i][j] = 0

    print(f'#{tc} {MAX}')