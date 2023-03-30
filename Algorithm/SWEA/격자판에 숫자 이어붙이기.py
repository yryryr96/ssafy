def dfs(i,j,cnt,number):

    if cnt == 6 :
        if number not in ans :
            ans.append(number)
        return

    for di,dj in point :
        ni,nj = i+di, j+dj
        if 0<=ni<4 and 0<=nj<4 :
            dfs(ni,nj,cnt+1,number+graph[ni][nj])

T = int(input())
for tc in range(1,T+1):
    graph = [list(map(str,input().split())) for _ in range(4)]
    point = [[1,0],[0,1],[-1,0],[0,-1]]
    ans = []

    for i in range(4):
        for j in range(4):
            dfs(i,j,0,graph[i][j])

    ans = len(ans)
    print(f'#{tc} {ans}')