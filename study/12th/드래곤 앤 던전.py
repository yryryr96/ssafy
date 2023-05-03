import sys
input = sys.stdin.readline

n,attack = map(int,input().split()) # 방 개수, 용사 공격력
room = []
for _ in range(n):
    t,a,h = map(int,input().split())
    # t == 1 공격력 a, 생명력 h 인 몬스터가 존재
    # t == 2 용사 공격력 a증가 생명력 h 만큼 회복
    room.append((t,a,h))
