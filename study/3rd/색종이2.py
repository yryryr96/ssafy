N = int(input())
graph = [[0 for _ in range(101)] for _ in range(101)]
point = [[0,1],[1,0],[-1,0],[0,-1]]

cnt = 0
ans = 0
def search(i,j):
    global cnt,ans
    cnt = 0
    for di,dj in point :
        ni,nj = i+di, j+dj
        if graph[ni][nj] == 0 : # 0의 개수를 카운트
            cnt += 1

    if cnt == 1:    # 0이 1개라면 길이 1 증가
        ans += 1

    elif cnt == 2:  # 0이 2개라면 길이 2 증가 > 모서리 부분
        ans += 2

for _ in range(N):
    x,y = map(int,input().split())

    for i in range(y,y+10):
        for j in range(x,x+10):
            graph[i][j] = 1

for i in range(101):
    for j in range(101):
        if graph[i][j] == 1:
            search(i,j)

print(ans)

# 모서리일 때 2개 카운트해주는 방법