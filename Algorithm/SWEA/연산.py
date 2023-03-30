from collections import deque

T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    q = deque()
    q.append(n)
    visited = [0]*1000001
    while q :
        now = q.popleft()
        if now == m :
            break
        for i in [now+1,now-1,now*2,now-10] :
            if i <= 1000000 and visited[i] == 0:
                visited[i] = visited[now] + 1
                q.append(i)

    ans = visited[m]
    print(f'#{tc} {ans}')
