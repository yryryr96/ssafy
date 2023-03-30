def get_two(num):
    n = len(num)
    SUM = 0
    for i in range(n):
        SUM += int(num[i])*(2**(n-(i+1)))

    return SUM

def get_three(num):
    n = len(num)
    SUM = 0
    for i in range(n):
        SUM += int(num[i])*(3**(n-(i+1)))
    return SUM

T = int(input())
for tc in range(1,T+1):
    ans_two = []
    ans_three = []

    two = input()
    three = input()

    for i in range(len(two)):
        check = list(two)
        if two[i] == '0' :
            check[i] = '1'
            ans_two.append(get_two(''.join(check)))
            check[i] = '0'
        else :
            check[i] = '0'
            ans_two.append(get_two(''.join(check)))
            check[i] = '1'

    for i in range(len(three)):
        check = list(three)
        if three[i] == '0' :
            check[i] = '1'
            ans_three.append(get_three(''.join(check)))
            check[i] = '2'
            ans_three.append(get_three(''.join(check)))
            check[i] = '0'

        elif three[i] == '1' :
            check[i] = '0'
            ans_three.append(get_three(''.join(check)))
            check[i] = '2'
            ans_three.append(get_three(''.join(check)))
            check[i] = '1'

        elif three[i] == '2' :
            check[i] = '0'
            ans_three.append(get_three(''.join(check)))
            check[i] = '1'
            ans_three.append(get_three(''.join(check)))
            check[i] = '2'


    for i in ans_two :
        for j in ans_three :
            if i == j :
                ans = i
                break

    print(f'#{tc} {ans}')

