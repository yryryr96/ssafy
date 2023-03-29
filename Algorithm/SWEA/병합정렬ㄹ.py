def msort(LIST):
    global cnt
    if len(LIST) == 1:
        return LIST

    middle = len(LIST) // 2
    left = LIST[:middle]
    right = LIST[middle:]

    left = msort(left)
    right = msort(right)
    if left[-1] > right[-1] :
        cnt += 1

    temp = []
    l = h = 0
    while l< len(left) and h<len(right):
        if left[l] < right[h] :
            temp.append(left[l])
            l+=1
        else:
            temp.append(right[h])
            h+=1
    temp += left[l:]
    temp += right[h:]
    return temp

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    lst = list(map(int,input().split()))
    temp = []
    cnt = 0
    print(f'#{tc} {msort(lst)[n//2]} {cnt}')
