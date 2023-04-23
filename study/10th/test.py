import sys
input = sys.stdin.readline

A,B = map(int,input().split()) # 가로, 세로
n,m = map(int,input().split()) # 로봇 개수, 명령 수
graph = [[0]*A for _ in range(B)]
point = [[1,0],[0,-1],[-1,0],[0,1]] # 북 동 남 서
robot = []
for k in range(n):
    a,b,d = map(str,input().split())
    if d == 'N' :
        d = 0
    elif d == 'E' :
        d = 3
    elif d == 'S' :
        d = 2
    elif d == 'W' :
        d = 1

    robot.append([int(b)-1,int(a)-1,d])
    graph[int(b)-1][int(a)-1] = k+1
# print(robot)
# for i in range(B):
#     print(*graph[i])
for _ in range(m):
    num,command,cnt = map(str,input().split())
    num = int(num) - 1
    cnt = int(cnt)
    if command == 'L' :
        for _ in range(cnt) :
            robot[num][2] = (robot[num][2] + 1) % 4
    elif command == 'R' :
        for _ in range(cnt):
            robot[num][2] = (robot[num][2] + 3) % 4

    elif command == 'F' :
        temp = 1
        i,j = robot[num][0], robot[num][1]
        graph[i][j] = 0
        di = point[robot[num][2]][0]
        dj = point[robot[num][2]][1]
        for _ in range(cnt):
            i += di
            j += dj
            if i >= B or i<0 or j>=A or j< 0 :
                print(f'Robot {num+1} crashes into the wall')
                temp = 0
                exit()

            elif graph[i][j] != 0 and graph[i][j] != num+1 :
                print(f'Robot {num+1} crashes into robot {graph[i][j]}')
                temp = 0
                exit()

        robot[num][0] = i
        robot[num][1] = j
        graph[i][j] = num + 1

print('OK')