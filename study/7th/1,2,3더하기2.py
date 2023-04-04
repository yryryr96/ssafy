import sys
input = sys.stdin.readline

n,k = map(int,input().split())
lst = [1,2,3]
cnt = 0
ans = '-1'

def dfs(v,word):
    global cnt,temp,ans
    if v == n :
        cnt += 1
        if cnt == k :
            ans = word[:-1]
        return

    if v > n :
        return

    for i in lst :
        dfs(v+i,word+str(i)+'+')

dfs(0,'')
print(ans)