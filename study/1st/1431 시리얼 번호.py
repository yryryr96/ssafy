# 선택 정렬 사용해서 풀이
import sys
input = sys.stdin.readline

N = int(input())
lst = []
ans = []
for _ in range(N):
    lst.append(input().rstrip())

lst.sort(key=len)

for i in range(len(lst) - 1):
    minIdx = i
    for j in range(i + 1, len(lst)):
        if len(lst[i]) == len(lst[j]):
            front = 0;
            back = 0

            for n in lst[minIdx]:
                if n.isdigit():
                    front += int(n)
            for n in lst[j]:
                if n.isdigit():
                    back += int(n)

            if front == back:
                if lst[minIdx] > lst[j]:
                    minIdx = j

            if back < front:
                minIdx = j

    lst[i], lst[minIdx] = lst[minIdx], lst[i]

for i in range(N):
    print(''.join(lst[i]))