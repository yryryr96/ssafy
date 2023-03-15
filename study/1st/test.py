import heapq,sys
input = sys.stdin.readline

n,m = map(int,input().split())
q = list(map(int,input().split()))
q.sort()
ans = 0
while q :
    A = q.pop()
    temp = A

    if not q :
        ans+=temp
    while A != 0 and q :
        for _ in range(m-1):
            B = q.pop()
            A -= B
            if A == 0 :
                ans += temp
                temp = 0
                break
        if not q:
            ans += temp
            break




print(ans)
