import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
Indegree = [0]*(n+1)
Time = [0]*(n+1)
graph = [[] for _ in range(n+1)]
for i in range(1,n+1):
    lst = list(map(int,input().split()))
    Time[i] = lst[0]
    length = lst[1]
    if length == 0 : continue
    lst = lst[2:]
    for j in range(length):
        if i not in graph[lst[j]] :
            graph[lst[j]].append(i)
            Indegree[i] += 1

q = deque()
for i in range(1,n+1):
    if Indegree[i] == 0 :
        q.append(i)

ans = []
while q :
    now = q.popleft()
    ans.append(now)
    for i in graph[now] :
        Indegree[i] -= 1
        if Indegree[i] == 0 :
            q.append(i)

if len(ans) == n :
    print(sum(Time)-max(Time)//2)
else :
    print(-1)