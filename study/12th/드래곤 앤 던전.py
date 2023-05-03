import sys
input = sys.stdin.readline

n, attack = map(int,input().split())
my_hp = 0
max_hp = 0
room = []

for _ in range(n):
    t,a,h = map(int,input().split())
    room.append((t,a,h))

monster = room[-1][2]

for info in room :
    if info[0] == 2 :
        attack += info[1]
        my_hp += info[2]
    else :
        monster_a = info[1]
        monster_hp = info[2]
        k = monster_hp%attack
        if k != 0 :
            damage = monster_a * (monster_hp//attack)
        else:
            damage = monster_a * (monster_hp//attack - 1)

        my_hp -= damage
    if my_hp > 0 :
        my_hp = 0
    max_hp = max(max_hp,abs(my_hp))

print(max_hp+1)

