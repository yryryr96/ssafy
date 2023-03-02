from collections import deque
import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = list(map(int,input().split()))
st = [] # 인덱스를 저장
ans = [-1]*N

for i in range(N):
    if not st :
        st.append(i)
    else:
        while st and lst[st[-1]] < lst[i] :
            ans[st.pop()] = lst[i]
        st.append(i)

print(*ans)