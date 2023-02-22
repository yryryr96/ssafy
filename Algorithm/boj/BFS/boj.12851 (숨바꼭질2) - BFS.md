# boj.12851 (숨바꼭질2) - BFS

```python
from collections import deque
visited = [0]*100001
N,K = map(int,input().split())
ans_way = 0
ans_count = 0
def bfs(v,K):
    global ans_way,ans_count
    q = deque()
    q.append(v)
    visited[v] = 1
    ans_way = 0
    ans_count = 0
    
    while q :
        now = q.popleft()

        if now == K :
            ans_way += 1
            ans_count = visited[now] - 1

        for after in [now-1,now+1,now*2]:
            if 0<= after <= 100000 and (visited[after] == 0 or visited[after] == visited[now] + 1) :
                visited[after] = visited[now] + 1
                q.append(after)
bfs(N,K)
print(ans_count)
print(ans_way)
```

visited[after] == 0 or vistied[after] == visited[now] + 1 이라는 조건은 after가 한번도 방문한적 없거나 이미 방문했지만 최소 거리로 찾은 레벨에서 또 방문하는건지를 체크한다. 

예로 입력이 5 17 이면 3레벨에서 16,18 이 나와 17이 되는 경우가 2가지인데 이 때, 조건식에 부합해서 q에 17을 두번 append한다. now가 17일 때 ans_count 는 최소거리로 유지되고 ans_way ( 경우의 수 ) 는 17이 2번 pop됐으니 1씩 증가해 총 2가된다.

이런식으로 경우의수와 최소거리를 구할 수 있다는 것을 알게됐고 기억해두면 좋을 것 같다.