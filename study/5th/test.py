import sys
<<<<<<< HEAD

=======
>>>>>>> 7d2fc15e418825431d35e76edf911ae593e8b81a
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    word = input().strip()
    start = 0
    end = len(word) - 1
<<<<<<< HEAD
    temp = temp_s = temp_e = 0
    cnt = 0
    while start <= end:
        if word[start] == word[end]:
            start += 1
            end -= 1

        else:
            if len(word) == 2:
                temp = 2
                break

            temp = 1
            temp_s = start + 1
            temp_e = end - 1
            break

    if temp_s and temp_e :
        while temp_s <= end:
            if word[temp_s] == word[end]:
                temp_s += 1
                end -= 1
            else:
                print(temp_s,end,word[temp_s],word[end])
                temp = 2
                break

        while start <= temp_e:
            if word[start] == word[temp_e]:
                start += 1
                temp_e -= 1
            else:
                temp = 2
                break

    print(temp)
=======
    temp = 0
    cnt = 0
    while start <= end :
        if word[start] == word[end] :
            start += 1
            end -= 1

        else :
            temp = 1
            cnt += 1
            if cnt > 1 or len(word) == 2 :
                temp = 2
                break
            if word[start+1] == word[end]  :
                start += 1
            elif word[start] == word[end-1] :
                end -= 1
            else :
                temp = 2
                break

    print(temp)
>>>>>>> 7d2fc15e418825431d35e76edf911ae593e8b81a
