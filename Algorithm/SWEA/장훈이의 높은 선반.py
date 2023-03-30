T = int(input())
for tc in range(1,T+1):
    n, top = map(int,input().split())
    person = list(map(int,input().split()))
    now = 1e9
    def dfs(idx,height):
        global now
        if height >= top :
            if height < now :
                now = height

        if now == top :
            return

        for i in range(idx+1,n) :
            dfs(i,height+person[i])
    dfs(-1,0)
    ans = now-top
    print(f'#{tc} {ans}')