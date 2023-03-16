import sys
input = sys.stdin.readline

n, m = 5,5
lst = [1,2,3,2,5]
SUM = 0
end = 0
ans = []
for start in range(n):
    while SUM < m and end < n :
        SUM += lst[end]
        end += 1

    if SUM == m :
        ans.append((lst[start],lst[end-1]))
    SUM -= lst[start]

print(ans)
