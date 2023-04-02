T = int(input())

for tc in range(1,T+1):
    n, number = input().split()
    number = bin(int(number,16))[2:]
    if len(number)%4 != 0 :
        number = '0'*(4-len(number)%4) + number
    print(f'#{tc} {number}')
