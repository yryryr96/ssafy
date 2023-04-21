import sys
input = sys.stdin.readline

n = int(input())
h = list(int(input()) for _ in range(n))
st = []
ans = 0

for i in range(n-1,-1,-1):
    cnt = 0
    for j in range(len(st)):
        if h[i] > st[-1][0] :
            cnt += (st[-1][1] + 1)
            st.pop()
        else:
            st.append((h[i],cnt))
            break
    else :
        st.append((h[i],cnt))

    if len(st) == 0 :
        st.append((h[i],cnt))

    ans += cnt

print(ans)