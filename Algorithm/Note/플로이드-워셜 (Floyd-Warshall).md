# 플로이드-워셜 (Floyd-Warshall)

```python
import sys
input = sys.stdin.readline

INF = int(1e9)
n = int(input())
m = int(input())

distance = [[INF]*(n+1) for _ in range(n+1)] # 2차원 거리 테이블
											# i -> j 거리값 = distance[i][j]
for i in range(n+1):
    for j in range(n+1):
        if i == j :
            distance[i][j] = 0	# 자기 자신과의 거리 0

for _ in range(m):
    a,b,c = map(int,input().split()) # a에서 b까지 거리 c
    distance[a][b] = c

for now in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            distance[i][j] = min(distance[i][j],distance[i][now]+distance[now][j])
            # i->j 거리와 i->now->j 거리를 비교했을 때 최소 거리로 갱신

for i in range(1,n+1):
    for j in range(1,n+1):
        if distance[i][j] == INF :
            pass
        else :
            print(distance[i][j],end = ' ')
```

![img](https://blog.kakaocdn.net/dn/1Vjwv/btrfRDJ3ecJ/Bjx8iypwFpY74b5OmAqdsK/img.png)
