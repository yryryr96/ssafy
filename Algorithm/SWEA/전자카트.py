T = int(input())

for tc in range(1,T+1) :
    n = int(input())
    MIN = int(1e9)
    lst = list(range(2,n+1))
    graph = [list(map(int,input().split())) for _ in range(n)]
    p = [0]*(n-1)
    visited = [0]*(n-1)

    def perm(i, k):
        global MIN
        if i == k:
            ANS = 0
            ans = [1] + p + [1]
            for m in range(len(ans)-1):
                ANS += graph[ans[m]-1][ans[m+1]-1]
                if ANS > MIN:
                    return

            if MIN > ANS:
                MIN = ANS
            return
        else:
            for j in range(k):
                if visited[j] == 0:
                    visited[j] = 1
                    p[i] = lst[j]
                    perm(i + 1, k)
                    visited[j] = 0

    perm(0,len(lst))
    print(f'#{tc} {MIN}')
