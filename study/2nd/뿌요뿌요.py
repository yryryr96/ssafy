from collections import deque
import sys
input = sys.stdin.readline

graph = [list(map(str,input().rstrip())) for _ in range(12)]
point = [[0,0],[0,1],[1,0],[-1,0],[0,-1]]

def bfs(i,j):	# 알파벳일 때 뻗어나가서 4개가 넘는다면 그 알파벳들을 모두 . 으로 바꿔주기위해 사용
    global cnt,check
    q = deque()
    visited = [[0 for _ in range(6)] for _ in range(12)]
    q.append((i,j))
    visited[i][j] = 0
    lst = []
    while q:
        now = q.popleft()
        for di,dj in point :
            ni, nj = now[0] + di, now[1] + dj
            if 0<=ni<12 and 0<=nj<6 and visited[ni][nj] == 0 :
                if graph[ni][nj] == graph[now[0]][now[1]] :	# 이동한 값이 조사한 값과 같다면
                    q.append((ni,nj))	# 뻗어 나갈 좌표 q에 저장
                    visited[ni][nj] = 1
                    lst.append((ni,nj))	# 이어진 블럭을 기억하기위해 lst에 따로 저장
                    cnt += 1
    if cnt >= 4 :
        check = 1		# 연쇄가 일어났는지 아닌지 판단하기위한 변수
        for k,n in lst:	# 붙어있는 개수가 4개가 넘는다면 저장해뒀던 이어진 블럭 모두 . 으로 변경
            graph[k][n] = '.'

ans = 0
while True :
    cnt = check = 0
    ans += 1	# 연쇄가 일어난 싸이클이 몇 싸이클인지 확인
    for j in range(6):
        for i in range(11,-1,-1):
            cnt = 0
            if graph[i][j].isalpha():
                bfs(i,j)

    if check == 0 :	# break 를 중간에 넣어줘야 바로 나감
        break		# 연쇄가 일어나지 않았다면 break

    # 정렬 : 밑에 빈칸이 있을 때 빈칸이 없을때까지 내려주는 역할
    for j in range(6):
        for i in range(11, -1, -1):
            Idx = i
            if graph[i][j].isalpha():
                for k in range(i + 1, 12):
                    if graph[k][j] == '.':
                        Idx = k
                graph[i][j], graph[Idx][j] = graph[Idx][j], graph[i][j]


print(ans-1)