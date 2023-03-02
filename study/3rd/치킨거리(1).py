# 조합 내장함수 사용
import sys
from itertools import combinations
input = sys.stdin.readline
# combinations : 조합
# permutations : 순열

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

chicken = []
houses = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 :
            houses.append((i,j))
        elif graph[i][j] == 2 :
            chicken.append((i,j))

ans = sys.maxsize
for chickens in combinations(chicken,m):
    SUM = 0
    for house in houses :
        distance = sys.maxsize
        for store in chickens :
            distance = min(distance,abs(house[0] - store[0]) + abs(house[1] - store[1]))
        SUM += distance
    ans = min(ans,SUM)
print(ans)