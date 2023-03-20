import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = list(map(int,input().split()))
parent = list(range(n+1))
tp = lst[1:lst[0]+1]
ans = []
for _ in range(m):
    temp = 0
    check = list(map(int,input().split()))
    check = check[1:]
    ans.append(check)

    for i in check:
        if parent[i] in tp :
            temp = parent[i]

            break

    if temp :
        for i in check :
            parent[i] = temp


ans.sort(reverse=True)

for i in range(len(ans)):
    temp = 0
    for j in range(len(ans[i])):
        if parent[ans[i][j]] in tp :
            for k in ans[i] :
                parent[k] = parent[ans[i][j]]

cnt = 0
for i in range(len(ans)):
    temp = 0
    for j in range(len(ans[i])):
        if parent[ans[i][j]] in tp :
            temp = 1
    if temp == 0:
        cnt += 1
print(parent)
print(cnt)