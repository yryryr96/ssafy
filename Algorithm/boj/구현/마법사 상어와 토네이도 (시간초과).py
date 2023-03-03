import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
point = [[0,-1],[1,0],[0,1],[-1,0]]
si,sj = N//2 , N//2
k = 0

def move(i, j, dir):
    temp_list = [[0] * (N) for _ in range(N)]
    tmp = 0
    if dir == 0:
        delta = [[-1, 1], [-1, 0], [-2, 0], [-1, -1], [0, -2], [1, -1], [1, 0], [2, 0], [1, 1]]
        lst = deque([int(0.01 * graph[i][j]), int(0.07 * graph[i][j]), int(0.02 * graph[i][j]), int(0.1 * graph[i][j]),
                     int(0.05 * graph[i][j]), int(0.1 * graph[i][j]), int(0.07 * graph[i][j]), int(0.02 * graph[i][j]),
                     int(0.01 * graph[i][j])])
        d = 0
        while d < 9:
            di, dj = delta[d][0],delta[d][1]
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                temp_list[ni][nj] = lst[d]
            tmp += lst[d]
            d += 1
        if 0 <= i < N and 0 <= j - 1 < N:
            graph[i][j-1] += (graph[i][j] - tmp)
        graph[i][j] = 0
        if tmp > 0:
            for i in range(N):
                for j in range(N):
                    graph[i][j] += temp_list[i][j]

    elif dir == 1:
        delta = [[-1, -1], [0, -1], [0, -2], [1, -1], [2, 0], [1, 1], [0, 1], [0, 2], [-1, 1]]
        lst = deque([int(0.01 * graph[i][j]), int(0.07 * graph[i][j]), int(0.02 * graph[i][j]), int(0.1 * graph[i][j]),
                     int(0.05 * graph[i][j]), int(0.1 * graph[i][j]), int(0.07 * graph[i][j]), int(0.02 * graph[i][j]),
                     int(0.01 * graph[i][j])])
        d = 0
        while d < 9:
            di, dj = delta[d][0],delta[d][1]
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                temp_list[ni][nj] = lst[d]
            tmp += lst[d]
            d += 1
        if 0 <= i+1 < N and 0 <= j < N:
            graph[i+1][j] += (graph[i][j] - tmp)
        graph[i][j] = 0
        if tmp > 0:
            for i in range(N):
                for j in range(N):
                    graph[i][j] += temp_list[i][j]

    elif dir == 2:
        delta = [[-1, -1], [-1, 0], [-2, 0], [-1, 1], [0, 2], [1, 1], [1, 0], [2, 0], [1, -1]]
        lst = deque([int(0.01 * graph[i][j]), int(0.07 * graph[i][j]), int(0.02 * graph[i][j]), int(0.1 * graph[i][j]),
                     int(0.05 * graph[i][j]), int(0.1 * graph[i][j]), int(0.07 * graph[i][j]), int(0.02 * graph[i][j]),
                     int(0.01 * graph[i][j])])
        d = 0
        while d < 9:
            di, dj = delta[d][0],delta[d][1]
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                temp_list[ni][nj] = lst[d]
            tmp += lst[d]
            d += 1
        if 0<=i<N and 0<=j+1<N :
            graph[i][j+1] += (graph[i][j] - tmp)
        graph[i][j] = 0
        if tmp > 0:
            for i in range(N):
                for j in range(N):
                    graph[i][j] += temp_list[i][j]

    elif dir == 3:
        delta = [[1, -1], [0, -1], [0, -2], [-1, -1], [-2, 0], [-1, 1], [0, 1], [0, 2], [1, 1]]
        lst = deque([int(0.01 * graph[i][j]), int(0.07 * graph[i][j]), int(0.02 * graph[i][j]), int(0.1 * graph[i][j]),
                     int(0.05 * graph[i][j]), int(0.1 * graph[i][j]), int(0.07 * graph[i][j]), int(0.02 * graph[i][j]),
                     int(0.01 * graph[i][j])])
        d = 0
        while d < 9:
            di, dj = delta[d][0],delta[d][1]
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                temp_list[ni][nj] = lst[d]
            tmp += lst[d]
            d += 1
        if 0 <= i-1 < N and 0 <= j < N:
            graph[i-1][j] += (graph[i][j] - tmp)
        graph[i][j] = 0
        if tmp > 0:
            for i in range(N):
                for j in range(N):
                    graph[i][j] += temp_list[i][j]

SUM = 0
for i in range(N):
    SUM += sum(graph[i])
n = 0
while True:
    n%=4
    if n == 0 or n == 2 :
        k += 1

    for i in range(1,k+1):
        ki = si + point[n%4][0]*i
        kj = sj + point[n%4][1]*i
        move(ki,kj,n)

        if ki == 0 and kj == 0 :
            break

    si,sj = ki,kj
    if si == 0 and sj == 0:
        break

    n += 1

ans = 0
for i in range(N):
    ans += sum(graph[i])

print(SUM-ans)