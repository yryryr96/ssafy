import sys, copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n,m,d = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
point = [[0,-1],[-1,0],[0,1]]

def bfs(hunters):
    temp = copy.deepcopy(graph)
    visited = [[0]*m for _ in range(n)]
    kill = 0

    for i in range(n-1,-1,-1):
        monster = set()
        for hunter in hunters : # 궁수의 열 좌표
            q = deque([(i,hunter,1)])
            while q :
                r,c,D = q.popleft()
                if temp[r][c] == 1 :
                    monster.add((r,c))
                    if visited[r][c] == 0 :
                        visited[r][c] = 1
                        kill += 1
                    break

                if D < d :
                    for di,dj in point :
                        ni,nj = r+di, c+dj
                        if 0<=ni<n and 0<=nj<m :
                            q.append((ni,nj,D+1))

        for r,c in monster :
            temp[r][c] = 0

    return kill

hunters = combinations(list(range(m)),3)
ans = 0
for hunter in hunters :
    ans = max(ans,bfs(hunter))
print(ans)