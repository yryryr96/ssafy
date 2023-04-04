import sys,math
input = sys.stdin.readline

def dist(x1,y1,x2,y2):  # 거리 계산 함수
    return math.sqrt(pow(x1-x2,2) + pow(y1-y2,2))

def find(x):
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    parent[max(a,b)] = min(a,b)

n,m = map(int,input().split())
parent = list(range(n+1))
graph = [0]

for _ in range(n):  # 좌표 받아주기
    x,y = map(int,input().split())
    graph.append((x,y))

for _ in range(m) : # 이미 연결 돼있는 노드번호 -> union 함수로 합쳐준다
    a,b = map(int,input().split())
    union(a,b)

edges = []
for i in range(1,n):
    for j in range(i+1,n+1) :
        edges.append((dist(*graph[i],*graph[j]),i,j)) # 거리, 노드번호 edges에 등록
edges.sort() # 거리 작은 값 순으로 정렬

ans = 0
for i in range(len(edges)) :
    distance,a,b = edges[i]
    if find(a) != find(b):  # 부모가 같지 않으면 연결 , 즉 최소 스패닝 구현
        union(a,b)
        ans += distance
print(f'{ans:.2f}')
