T = int(input())
for tc in range(1,T+1):
    ticket = list(map(int,input().split()))
    month = [0] + list(map(int,input().split()))
    MIN = int(1e9)
    def dfs(idx, money) :
        global MIN
        if money > ticket[-1] :
            return

        if idx > 12 :
            MIN = min(money,MIN)
            return

        if month[idx+1] :
            dfs(idx+1,money+ticket[0]*month[idx+1])
            dfs(idx+1,money+ticket[1])
        else:
            dfs(idx+1,money)

        dfs(idx+3,money+ticket[2])

    dfs(0,0)
    if MIN > ticket[-1] :
        MIN = ticket[-1]
    print(f'#{tc} {MIN}')
