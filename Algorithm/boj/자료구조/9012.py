import sys
input = sys.stdin.readline
T = int(input())
for tc in range(1,T+1):
    lst = input()
    cnt = 0
    n = 0
    for i in range(len(lst)):
        if lst[i] == '(' :
            cnt += 1
        elif lst[i] == ')' :
            cnt -= 1

        if cnt == -1 :
           n += 1


    if cnt == 0 :
        if n > 0 :
            print('NO')
        else:
            print('YES')

    else :
        print('NO')