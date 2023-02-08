N = list(input())
n = int(input())
s = -1
cnt = 0
for i in range(n):
    a = input()

    if a == 'L':
        if s == -len(N):

            pass

        else:
            s -= 1

        print(s)

    elif a == 'B':
        if s == -len(N):
            pass
        else:
            N.remove(N.index[s])

    elif a == 'D':
        if s == -1:
            pass
        else:
            s += 1

    elif a[:1] == 'P' :

        if s == -len(N):
            N.insert(s,a[-1])

        else :
            N.insert(4, a[-1])
        print(s,a[-1],N)


