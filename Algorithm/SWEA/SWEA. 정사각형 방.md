# SWEA. 정사각형 방

```python
T = int(input())

def dfs(i,j):

    global cnt
    point = [[0,1],[1,0],[-1,0],[0,-1]]
    st = [(i,j)]

    while st:
        now = st.pop()
        for di, dj in point:
            ni,nj = now[0]+di, now[1]+dj
            if 0<=ni<N and 0<=nj<N and graph[now[0]][now[1]]+1 == graph[ni][nj] :
                cnt += 1
                st.append((ni,nj))
    return cnt

for tc in range(1,T+1):

    N = int(input())
    ans = []
    graph = [list(map(int,input().split())) for _ in range(N)]
    lst = [0]*(N*N+1)
    MAX = 0
    for i in range(N):
        for j in range(N):
            cnt = 1
            dfs(i,j)
            if MAX <= cnt :
                MAX = cnt
                lst[graph[i][j]] = cnt

    print(f'#{tc} {lst.index(MAX)} {MAX}')
```

스택으로 안하니까 리커전에러