def find(x):
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b) :
    a = find(a)
    b = find(b)
    parent[max(a,b)] = min(a,b)

T = int(input())
for tc in range(1,T+1):
    v,e = map(int,input().split())
    parent = list(range(v+1))
    edges = []
    for _ in range(e):
        a,b,c = map(int,input().split())
        edges.append((c,a,b))

    edges.sort()
    ans = 0
    for i in range(e):
        c,a,b = edges[i]
        if find(a) != find(b) :
            union(a,b)
            ans += c

    print(f'#{tc} {ans}')
