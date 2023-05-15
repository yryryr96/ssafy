import sys,copy
input = sys.stdin.readline

dice = list(map(int,input().split()))
graph = [list(range(0,41,2)),[10,13,16,19,25,30,35,40],[20,22,24,25,30,35,40],[30,28,27,26,25,30,35,40]]
visit = [0]*41
# print(graph)
horse = []
for _ in range(4):
    horse.append([0,0])
ans = 0
def dfs(horse,depth,SUM,visited):
    global ans
    # print(horse,depth,SUM)
    if depth == 10 :
        ans = max(ans,SUM)
        return
    for i in range(4) :
        if horse[i][0] == -1 : continue
        a = horse[i][0]
        b = horse[i][1]
        temp = 0
        if not horse[i][0] :
            if horse[i][1] + dice[depth] >= len(graph[horse[i][0]]):
                horse[i][0] = -1
                dfs(horse,depth+1,SUM,visited)
                horse[i][0] = a
            else :
                if horse[i][1] + dice[depth] == 5 :
                    if [1,0] in horse : continue
                    horse[i][0] = 1
                    horse[i][1] = 0
                elif horse[i][1] + dice[depth] == 10 :
                    if [2, 0] in horse: continue
                    horse[i][0] = 2
                    horse[i][1] = 0
                elif horse[i][1] + dice[depth] == 15 :
                    if [3, 0] in horse: continue
                    horse[i][0] = 3
                    horse[i][1] = 0
                else :
                    if [horse[i][0], horse[i][1]+dice[depth]] in horse: continue
                    if graph[horse[i][0]][horse[i][1]+dice[depth]] == 40 :
                        if visited[40] : continue
                        visited[40] = 1
                        temp = 1
                    horse[i][1] += dice[depth]

                SUM += graph[horse[i][0]][horse[i][1]]
                dfs(horse,depth+1,SUM,visited)
                SUM -= graph[horse[i][0]][horse[i][1]]
                horse[i][0] = a; horse[i][1] = b
                if temp :
                    visited[40] = 0

        else :
            if horse[i][1] + dice[depth] >= len(graph[horse[i][0]]):
                horse[i][0] = -1
                dfs(horse,depth+1,SUM,visited)
                horse[i][0] = a
            else :
                if [horse[i][0],horse[i][1] + dice[depth]] in horse : continue
                if graph[horse[i][0]][horse[i][1]+dice[depth]] in [25,30,35,40] :
                    if visited[graph[horse[i][0]][horse[i][1]+dice[depth]]] : continue
                    visited[graph[horse[i][0]][horse[i][1]+dice[depth]]] = 1
                    temp = 1

                horse[i][1] += dice[depth]
                SUM += graph[horse[i][0]][horse[i][1]]
                dfs(horse, depth + 1, SUM,visited)
                SUM -= graph[horse[i][0]][horse[i][1]]
                horse[i][1] = b
                if temp :
                    visited[graph[horse[i][0]][horse[i][1]+dice[depth]]] = 0

dfs(horse,0,0,visit)
print(ans)