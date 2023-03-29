
T = int(input())
for tc in range(1,T+1):
    total,*energy = map(int,input().split())
    energy = [0] + energy
    MIN = 1e9
    def dfs(idx,charge,cnt):

        global MIN
        if cnt > MIN :
            return

        if idx+charge >= total :
            MIN = min(MIN,cnt)
            return

        for i in range(idx+1,idx+charge+1):
            dfs(i, energy[i], cnt + 1)

    dfs(1,energy[1],0)
    print(f'#{tc} {MIN}')
