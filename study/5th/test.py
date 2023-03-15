import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    word = input().strip()
    start = 0
    end = len(word) - 1
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