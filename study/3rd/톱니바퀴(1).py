from collections import deque

lst = [0] + list(deque(map(int, input())) for _ in range(4))
K = int(input())
for _ in range(K):
    idx, rotation = map(int, input().split())

    if idx == 1:
        if lst[1][2] != lst[2][6] and lst[2][2] != lst[3][6] and lst[3][2] != lst[4][6] :
            if rotation == 1:
                lst[1].appendleft(lst[1].pop()) #시계
                lst[2].append(lst[2].popleft()) #반시계
                lst[3].appendleft(lst[3].pop())
                lst[4].append(lst[4].popleft())
            else :
                lst[1].append(lst[1].popleft()) #반시계
                lst[2].appendleft(lst[2].pop()) #시계
                lst[3].append(lst[3].popleft())
                lst[4].appendleft(lst[4].pop())

        elif lst[1][2] != lst[2][6] and lst[2][2] != lst[3][6] :
            if rotation == 1:
                lst[1].appendleft(lst[1].pop()) #시계
                lst[2].append(lst[2].popleft()) #반시계
                lst[3].appendleft(lst[3].pop())
            else :
                lst[1].append(lst[1].popleft()) #반시계
                lst[2].appendleft(lst[2].pop()) #시계
                lst[3].append(lst[3].popleft())

        elif lst[1][2] != lst[2][6] :
            if rotation == 1:
                lst[1].appendleft(lst[1].pop()) #시계
                lst[2].append(lst[2].popleft()) #반시계
            else :
                lst[1].append(lst[1].popleft()) #반시계
                lst[2].appendleft(lst[2].pop()) #시계

        elif lst[1][2] == lst[2][6] :
            if rotation == 1:
                lst[1].appendleft(lst[1].pop()) #시계
            else :
                lst[1].append(lst[1].popleft()) #반시계

    elif idx == 2:
        if lst[2][6] != lst[1][2] and lst[2][2] != lst[3][6] and lst[3][2] != lst[4][6]:
            if rotation == 1:
                lst[1].append(lst[1].popleft()) #반시계
                lst[2].appendleft(lst[2].pop()) #시계
                lst[3].append(lst[3].popleft())
                lst[4].appendleft(lst[4].pop())
            else :
                lst[1].appendleft(lst[1].pop()) #시계
                lst[2].append(lst[2].popleft()) #반시계
                lst[3].appendleft(lst[3].pop())
                lst[4].append(lst[4].popleft())

        elif lst[2][2] != lst[3][6] and lst[3][2] != lst[4][6]:
            if rotation == 1:
                lst[2].appendleft(lst[2].pop()) #시계
                lst[3].append(lst[3].popleft())
                lst[4].appendleft(lst[4].pop())
            else :
                lst[2].append(lst[2].popleft()) #반시계
                lst[3].appendleft(lst[3].pop())
                lst[4].append(lst[4].popleft())

        elif lst[2][2] != lst[3][6] and lst[2][6] != lst[1][2] :
            if rotation == 1:
                lst[2].appendleft(lst[2].pop()) #시계
                lst[3].append(lst[3].popleft())
                lst[1].append(lst[1].popleft())
            else :
                lst[2].append(lst[2].popleft()) #반시계
                lst[3].appendleft(lst[3].pop())
                lst[1].appendleft(lst[1].pop())

        elif lst[2][2] != lst[3][6] :
            if rotation == 1:
                lst[2].appendleft(lst[2].pop()) #시계
                lst[3].append(lst[3].popleft())
            else :
                lst[2].append(lst[2].popleft()) #반시계
                lst[3].appendleft(lst[3].pop())

        elif lst[2][6] != lst[1][2] :
            if rotation == 1:
                lst[2].appendleft(lst[2].pop()) #시계
                lst[1].append(lst[1].popleft())
            else :
                lst[2].append(lst[2].popleft()) #반시계
                lst[1].appendleft(lst[1].pop())

        elif lst[2][2] == lst[3][6] and lst[2][6] == lst[1][2] :
            if rotation == 1:
                lst[2].appendleft(lst[2].pop()) #시계
            else :
                lst[2].append(lst[2].popleft()) #반시계

    elif idx == 3:
        if lst[3][2] != lst[4][6] and lst[3][6] != lst[2][2] and lst[2][6] != lst[1][2] :
            if rotation == 1:
                lst[1].appendleft(lst[1].pop()) #시계
                lst[2].append(lst[2].popleft()) #반시계
                lst[3].appendleft(lst[3].pop())
                lst[4].append(lst[4].popleft())
            else :
                lst[1].append(lst[1].popleft()) #반시계
                lst[2].appendleft(lst[2].pop()) #시계
                lst[3].append(lst[3].popleft())
                lst[4].appendleft(lst[4].pop())

        elif lst[3][6] != lst[2][2] and lst[2][6] != lst[1][2] :
            if rotation == 1:
                lst[1].appendleft(lst[1].pop()) #시계
                lst[2].append(lst[2].popleft()) #반시계
                lst[3].appendleft(lst[3].pop())
            else :
                lst[1].append(lst[1].popleft()) #반시계
                lst[2].appendleft(lst[2].pop()) #시계
                lst[3].append(lst[3].popleft())

        elif lst[3][6] != lst[2][2] and lst[3][2] != lst[4][6] :
            if rotation == 1:
                lst[2].append(lst[2].popleft()) #반시계
                lst[3].appendleft(lst[3].pop())
                lst[4].append(lst[4].popleft())
            else :
                lst[2].appendleft(lst[2].pop()) #시계
                lst[3].append(lst[3].popleft())
                lst[4].appendleft(lst[4].pop())

        elif lst[3][6] != lst[2][2]:
            if rotation == 1:
                lst[2].append(lst[2].popleft()) #반시계
                lst[3].appendleft(lst[3].pop())
            else :
                lst[2].appendleft(lst[2].pop()) #시계
                lst[3].append(lst[3].popleft())

        elif lst[3][2] != lst[4][6] :
            if rotation == 1:
                lst[3].appendleft(lst[3].pop())
                lst[4].append(lst[4].popleft())
            else :
                lst[3].append(lst[3].popleft())
                lst[4].appendleft(lst[4].pop())

        elif lst[3][2] == lst[4][6] and lst[3][6] == lst[2][2] :
            if rotation == 1:
                lst[3].appendleft(lst[3].pop())
            else :
                lst[3].append(lst[3].popleft())

    elif idx == 4:
        if lst[4][6] != lst[3][2] and lst[3][6] != lst[2][2] and lst[2][6] != lst[1][2]:
            if rotation == 1:
                lst[1].append(lst[1].popleft())
                lst[2].appendleft(lst[2].pop())  # 시계
                lst[3].append(lst[3].popleft())  # 반시계
                lst[4].appendleft(lst[4].pop())
            else:
                lst[1].appendleft(lst[1].pop())
                lst[2].append(lst[2].popleft())  # 반시계
                lst[3].appendleft(lst[3].pop())  # 시계
                lst[4].append(lst[4].popleft())

        elif lst[4][6] != lst[3][2] and lst[3][6] != lst[2][2]:
            if rotation == 1:
                lst[2].appendleft(lst[2].pop())  # 시계
                lst[3].append(lst[3].popleft())  # 반시계
                lst[4].appendleft(lst[4].pop())
            else:
                lst[2].append(lst[2].popleft())  # 반시계
                lst[3].appendleft(lst[3].pop())  # 시계
                lst[4].append(lst[4].popleft())

        elif lst[4][6] != lst[3][2]:
            if rotation == 1:
                lst[4].appendleft(lst[4].pop())  # 시계
                lst[3].append(lst[3].popleft())  # 반시계
            else:
                lst[4].append(lst[4].popleft())  # 반시계
                lst[3].appendleft(lst[3].pop())  # 시계

        elif lst[4][6] == lst[3][2] :
            if rotation == 1:
                lst[4].appendleft(lst[4].pop())  # 시계
            else:
                lst[4].append(lst[4].popleft())  # 반시계
score = 0
k = 1
for i in range(1,5):
    if lst[i][0] == 1 :
        score += k
    k*=2
print(score)