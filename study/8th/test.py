from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[0]*(n+1) for _ in range(m+1)]
for _ in range(4):
    x,y = map(int,input().split())
    graph[y][x] = 1

for i in range(m+1):
    print(*graph[i])

