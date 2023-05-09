import sys
input = sys.stdin.readline

N,K,D = map(int,input().split())
lst = [[] for _ in range(N+1)]
for i in range(1,N+1):
    M,d = map(int,input().split())
    algo = list(map(int,input().split()))
    lst[i].append((d,algo))

lst.sort(reverse=True)
print(lst)