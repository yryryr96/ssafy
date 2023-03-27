T = int(input())

def check(p):
    for i in range(8):
        if p[i] and p[i+1] and p[i+2] :
            return True
    return False

for tc in range(1,T+1):
    p1 = [0]*10
    p2 = [0]*10
    lst = list(map(int,input().split()))
    temp = 0
    for i in range(12):
        if i%2 == 0 :
            p1[lst[i]] += 1
            if p1[lst[i]] == 3 or check(p1) :
                print(f'#{tc} 1')
                temp = 1
                break
        else :
            p2[lst[i]] += 1
            if p2[lst[i]] == 3 or check(p2):
                print(f'#{tc} 2')
                temp = 1
                break

    if temp == 0 :
        print(f'#{tc} 0')
