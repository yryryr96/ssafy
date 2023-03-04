# 1. 상하좌우를 탐색해서 좋아하는 학생 번호가 몇개인지 파악
# 2. 좋아하는 학생 번호의 수가 같으면 빈칸의 개수 많은 순서
# 3. 1,2 둘다 같다면 더 작은 행
# 4. 행도 같다면 더 작은 열
# 1,2,3,4 를 한번에 파악하기 위해서 하나의 리스트로 만들어 저장
# lambda 정렬을 이용해서 순서대로 저장
import sys
input = sys.stdin.readline

N = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]
point = [[0,1],[1,0],[0,-1],[-1,0]]
total = []
for _ in range(N*N):
    st = list(map(int,input().split()))
    total.append(st)
    ANS = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0 :
                zero_cnt = 0
                like = 0
                for di,dj in point :
                    ni,nj = i+di, j+dj
                    if 0<=ni<N and 0<=nj<N :
                        if graph[ni][nj] in st[1:]:
                            like += 1

                        elif graph[ni][nj] == 0 :
                            zero_cnt += 1
                ANS.append([like,zero_cnt,i,j])
    ANS.sort(key = lambda x : (-x[0], -x[1], x[2], x[3]))   # max값 따로 안구하고 순서대로 정렬 가능 !!!!
    graph[ANS[0][2]][ANS[0][3]] = st[0]

ans = 0
for n in total :
    cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == n[0] :
                for di,dj in point :
                    ni,nj = i+di,j+dj
                    if 0<=ni<N and 0<=nj<N :
                        if graph[ni][nj] in n[1:] :
                            cnt += 1
    if cnt == 1:
        ans += 1
    elif cnt == 2 :
        ans += 10
    elif cnt == 3:
        ans += 100
    elif cnt == 4:
        ans += 1000

print(ans)



