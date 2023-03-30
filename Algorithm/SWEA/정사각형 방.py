T = int(input())
for tc in range(1,T+1) :
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    point = [[0,1],[1,0],[0,-1],[-1,0]]
    ans_list = []
    def dfs(i,j,cnt) :
        global ans
        if ans == n**2:
            return

        if ans < cnt :
            ans = cnt

        for di,dj in point :
            ni,nj = i+di, j+dj
            if 0<=ni<n and 0<=nj<n and graph[ni][nj]-graph[i][j] == 1:
                visited[ni][nj] = 1
                dfs(ni,nj,cnt+1)

        return ans

    MAX = 0
    for i in range(n):
        for j in range(n):
            ans = 0
            if visited[i][j] == 0 :
                dfs(i,j,1)

                if ans >= MAX :
                    MAX = ans
                    ans_list.append((graph[i][j],MAX))

    ans_list.sort(key=lambda x:(-x[1],x[0]))

    print(f'#{tc}',*ans_list[0])



