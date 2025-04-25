from itertools import product
from sys import argv
from collections import defaultdict
from random import choice


def create_transition_dic(width, height):
    transition_dic = {}
    num_tiles = width * height
    for n in range(1, num_tiles + 1):
        adjacent_edges_list = []
        if (n - 1) % width != 0:
            adjacent_edges_list.append(n - 1)  # left
        if n % width != 0:
            adjacent_edges_list.append(n + 1)  # right
        if n > width:
            adjacent_edges_list.append(n - width)  # top
        if n <= ((width * height) - width):
            adjacent_edges_list.append(n + width)  # bottom
        transition_dic[n] = adjacent_edges_list
    return transition_dic


width = int(argv[1])
dct = create_transition_dic(width, width)
seen = set()
start_vertex = 1

for ix in list(product([start_vertex], dct[start_vertex])):
    seen.add(ix)

solutions = set()

type_dct = defaultdict(list)
keep = set()
while seen:
    c = seen.copy()
    for ix in c:
        resp = [list(ix[:-1]) + list(x) for x in product([ix[-1]], dct[ix[-1]])]
        for lst in resp:
            if len(set(lst)) == len(lst):
                seen.add(tuple(lst))
    for ix in c:
        seen.discard(ix)
        if len(ix) >= width**2:
            print("solution:", ix, "\n")
            solutions.add(ix)
            # print(solutions)

    for tupl in seen:
        lst = []
        for ix in tupl:
            lst.append(len(dct[ix]))
        type_dct[tuple(lst)].append(tupl)

    for k, v in type_dct.items():
        keep.add(choice(v))
    seen = seen.intersection(keep)
    type_dct = defaultdict(list)
    keep = set()

print(solutions)
