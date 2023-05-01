import sys
input = sys.stdin.readline

dice = list(map(int,input().split()))
MAX = 0
map = [list(range(2,41,2)),[10,13,16,19,25,30,35,40],[20,22,24,25,30,35,40],[30,28,27,26,25,30,35,40]]
visited = [0,0,0,0]

def dfs(visited,point,SUM,n) :
    global MAX
    print(visited, point, SUM, f'#{n}')
    if n == 10 :
        if SUM > MAX :
            MAX = SUM

        return

    for i in range(4):
        P = point[i]
        if P == -1 : continue
        if visited[i] :
            idx = map[visited[i]].index(P)

            print(P,idx)
            if idx + dice[n] >= len(map[visited[i]]):
                point[i] = -1
                dfs(visited, point, SUM, n + 1)
                point[i] = P
            else:
                for k in range(4):
                    if visited[k] and point[k] == map[visited[i]][idx + dice[n]] :
                        break
                else:
                    point[i] = map[visited[i]][idx + dice[n]]
                    dfs(visited, point, SUM + map[visited[i]][idx + dice[n]], n + 1)
                    point[i] = P

        else :
            point[i] += 2 * dice[n]
            if point[i] > 40:
                point[i] = -1
                dfs(visited, point, SUM, n + 1)

            elif point[i] == 10 or point[i] == 20 or point[i] == 30:
                for k in range(4):
                    if visited[k] and point[k] == point[i] :
                        break
                else:
                    visited[i] = point[i] // 10
                    dfs(visited, point, SUM + point[i], n + 1)
                    visited[i] = 0
            else:
                for k in range(4):
                    if not visited and point[k] == point[i] :
                        break
                else:
                    dfs(visited, point, SUM + point[i], n + 1)
            point[i] = P

    return

dfs([0,0,0,0],[0,0,0,0],0,0)

print(MAX)