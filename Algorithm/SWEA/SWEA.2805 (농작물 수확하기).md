# SWEA.2805 (농작물 수확하기)

![image-20230224170418849](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230224170418849.png)

```python
# 1. 상하좌우 말단부에서 4방향 델타를 진행해주면 다음 마름모형이 나오는 규칙을 발견
# 2. 정중앙 좌표에서 마름모 범위 내의 최대거리가 N//2 인 것을 이용한다.
# 3. bfs를 통해 중앙부터 전체 그래프를 훑으며 최대거리 내에 있는 좌표들을 모두 더해준다.


from collections import deque

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    graph = [list(map(int,input())) for _ in range(N)]

    def bfs(i, j):	# 문제의 규칙성을 찾아 조건에 부합하는 값을 도출하기 위해 사용
        visited = [[0 for _ in range(N)] for _ in range(N)]
        q = deque()
        q.append((i, j))
        visited[i][j] = 1
        point = [[0, 1], [1, 0], [-1, 0], [0, -1]]	# 델타
        ans = 0
        
        while q:
            now = q.popleft()	# 현재 좌표
            if visited[now[0]][now[1]] <= N//2+1:	# 시작좌표에서의 거리가 N//2 이내라면
                ans += graph[now[0]][now[1]]		# 답에 그 좌표값 더해주기

            for di, dj in point:
                ni, nj = now[0] + di, now[1] + dj
                if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                    visited[ni][nj] = visited[now[0]][now[1]] + 1 
                    # 방문처리와 동시에 거리 계산
                    
                    q.append((ni, nj))
        return ans

    i,j = N//2,N//2	# 시작 좌표
    ANS = bfs(i,j)
    print(f'#{tc} {ANS}')
```

