import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
dic = defaultdict(int)
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

s,e = map(int,input().split())
q = deque()
q.append((s,sys.maxsize))
a = 0
while q:
    now, weight = q.popleft()

    if now == e :
        dic[e] = max(weight,dic[e])

        a+=1
        if a >= 10**6 :
            break
    for i,w in graph[now] :
        q.append((i,min(weight,w)))

print(dic[e])

