import sys
input = sys.stdin.readline

def search(i,j,p,cnt):
    global total
    if cnt == n :
        total += p
        return

    now = p # 건네받은 확률을 담은 변수
    visited[i][j] = 1

    for di,dj in point :
        ni,nj = i+di, j+dj
        if 0<= ni < 2*n+1 and 0<=nj<2*n+1 :
            if visited[ni][nj] == 1 :
                continue
            else :
                search(ni,nj,now*percent[i],cnt+1)
                visited[ni][nj] = 0


n, E, W, S, N = map(int,input().split())
percent = [E/100,W/100,S/100,N/100]
point  = [[0,1],[0,-1],[1,0],[-1,0]]

visited = [[0 for _ in range(2*n+1)] for _ in range(2*n+1)]
total = 0
search(n,n,1,0)
print(total)