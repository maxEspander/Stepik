classes_e = dict()
parents = list()
double_e = list()
exp_list = list()


def get_all_parents(child):
    if classes_e[child] == '':
        return ''
    for ch in classes_e[child]:
        get_all_parents(ch)
    parents.extend(classes_e[child])
    return ''


def is_e_in_list(list_e, list_p):
    for e in list_e:
        if e in list_p:
            return True
    return False


for _ in range(int(input())):
    cur_e = input().split()
    classes_e[cur_e[0]] = cur_e[2:] if len(cur_e) > 2 else ''

for _ in range(int(input())):
    cur_e = input()
    exp_list.append(cur_e)
    if cur_e in double_e:
        continue
    parents = []
    get_all_parents(cur_e)
    is_double = is_e_in_list(exp_list, parents)
    if is_double:
        double_e.append(cur_e)

for d in double_e:
    print(d)
