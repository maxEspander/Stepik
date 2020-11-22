number_e = int(input())
classes_e = dict()
for _ in range(number_e):
    cur_e = input().split()
    classes_e[cur_e[0]] = cur_e[2:] if len(cur_e) > 2 else ''

number_c = int(input())

for _ in range(number_e):
    cur_e = input()
