import sys
from collections import deque
input = sys.stdin.readline

def find_enter():
    global ans
    for i in [0,n-1] :  # 첫 행, 마지막 행
        for j in range(m):
            a = graph[i][j]
            if a.isalpha():
                if a.isupper() and a.lower() in KEY :
                    enter.add((i,j))
                elif a.islower() :
                    enter.add((i,j))
                    KEY.add(graph[i][j])
            elif a == '.' :
                enter.add((i,j))
            elif a == '$' :
                ans += 1
                enter.add((i,j))
                graph[i][j] = '.'

    for j in [0,m-1] : # 첫 열, 마지막 열
        for i in range(n):
            a = graph[i][j]
            if a.isalpha():
                if a.isupper() and a.lower() in KEY:
                    enter.add((i, j))
                elif a.islower():
                    enter.add((i, j))
                    KEY.add(graph[i][j])
            elif a == '.':
                enter.add((i, j))
            elif a == '$' :
                ans += 1
                enter.add((i,j))
                graph[i][j] = '.'

def bfs():
    global ans
    visited =[[0]*m for _ in range(n)]
    q = deque(list(enter))

    while q :
        now = q.popleft()
        for di,dj in point :
            ni,nj = now[0] + di, now[1] + dj
            if 0<=ni<n and 0<=nj<m and visited[ni][nj] == 0 :
                g = graph[ni][nj]
                visited[ni][nj] = 1
                if g == '$' :
                    ans += 1
                    graph[ni][nj] = '.'
                    q.append((ni,nj))
                elif g.isalpha(): # 알파벳일 때
                    if g.isupper() and g.lower() in KEY : # 대문자의 소문자가 KEY에 있을 때
                        q.append((ni,nj))
                    elif g.islower(): # 소문자라면 키에 넣기
                        KEY.add(g)
                        q.append((ni,nj))

                elif g == '.': # .이면 지나가기
                    q.append((ni,nj))

T = int(input())
for tc in range(T):
    n,m = map(int,input().split())
    graph = [list(input().rstrip()) for _ in range(n)]
    point = [[0,1],[1,0],[-1,0],[0,-1]]
    KEY = set(input().rstrip())
    enter = set()
    ans = 0
    check = sys.maxsize

    while True:
        find_enter()
        bfs()
        temp = len(KEY) + ans
        if temp == check : # key의 갯수와 답의 갯수가 바뀌지 않으면 더이상 갈 곳이 없으니 종료
            break
        check = temp


    print(ans)