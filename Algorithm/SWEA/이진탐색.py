T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0
    for num in B:
        if num in A:
            s = 0
            e = len(A) - 1
            temp = ''
            while s <= e:
                m = (s + e) // 2
                if num == A[m]:
                    break

                elif num > A[m]:
                    if temp == 'r':
                        temp = 'False'
                        break
                    temp = 'r'
                    s = m + 1

                elif num < A[m]:
                    if temp == 'l':
                        temp = 'False'
                        break
                    e = m - 1
                    temp = 'l'

            if temp == 'False':
                continue
            else:
                cnt += 1

    print(f'#{tc} {cnt}')
