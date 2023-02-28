from collections import deque
import sys
input = sys.stdin.readline

gears = [0] + list(deque(map(int,input().rstrip())) for _ in range(4))

def check_right(start,dirs): # 해당 톱니 왼쪽 검사
    if start > 4 or gears[start-1][2] == gears[start][6] :
        # 오른쪽 검사하면서 톱니 번호가 4가 넘어가거나 그 다음 톱니와 상태가 같아지면 종료
        return

    if gears[start-1][2] != gears[start][6] :
        check_right(start + 1, -dirs) # 반대방향으로 돌아야하므로 돌수 있을 때 - 붙여서 검사
        gears[start].rotate(dirs)

def check_left(start,dirs): # 해당 톱니 오른쪽 검사
    if start<1 or gears[start][2] == gears[start+1][6] :
        # 왼쪽 검사하면서 톱니 번호가 4가 넘어가거나 그 다음 톱니와 상태가 같아지면 종료
        return

    if gears[start][2] != gears[start+1][6] :
        check_left(start - 1, -dirs)
        gears[start].rotate(dirs)

K = int(input().rstrip())
for _ in range(K):
    num, dirs = map(int,input().split())
    check_right(num+1,-dirs)    # 오른쪽 검사
    check_left(num-1,-dirs)     # 왼쪽 검사
    gears[num].rotate(dirs)     # 자기 자신 회전
    # 검사해서 옆에 아무것도 못돌려도 자신은 회전해야함
ans = 0
k = 1
for i in range(1,5):
    if gears[i][0] == 1:
        ans += k
    k*=2
print(ans)