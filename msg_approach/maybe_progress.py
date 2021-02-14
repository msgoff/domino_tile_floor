from itertools import product
from sys import argv
from collections import deque

width = int(argv[1])


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

# useage python maybe_progress.py 3 for 3X3 starting at 1
# choose starting point of 1
# estimated number of valid paths
# https://oeis.org/A145157
"""
n=1,1 
n=2,2 
8, 
52, 
824, 
22144, 
1510446, 
180160012, 
54986690944, 
29805993260994, 
41433610713353366, 
103271401574007978038, 
660340630211753942588170, 
7618229614763015717175450784, 
n=15, 225419381425094248494363948728158
"""


dct = create_transition_dic(width, width)
solutions = set()
neighbors = {2: "X", 3: "Y", 4: "Z"}
moves = {}
# https://docs.python.org/3/library/collections.html#collections.deque
d = deque()


def product_gen(src):
    l = src[:-1]
    for ix in product([src[-1]], dct[src[-1]]):
        try:
            l.extend(list(ix))
            if len(set(l)) == len(l):
                d.append(tuple(l))
            l = src[:-1]
        except Exception as e:
            print(e)

src = [1]
product_gen(src)
while d:
    tpl = d.popleft()
    if len(tpl) == width ** 2:
        solutions.add(tpl)
    else:
        product_gen(list(tpl))

for tpl in sorted(solutions):
    if len(tpl) == width ** 2:
        tmp_lst = []

        for ix in list(zip(tpl, tpl[1:])):
            if ix[1] - 1 == ix[0]:
                tmp_lst.append("R")

            if ix[1] + 1 == ix[0]:
                tmp_lst.append("L")

            if ix[1] - width == ix[0]:
                tmp_lst.append("D")

            if ix[1] + width == ix[0]:
                tmp_lst.append("U")

        moves[tpl] = (tmp_lst, [neighbors[len(dct[x])] for x in tpl])

for k, v in moves.items():
    print(k, v)


import pandas as pd 
df = pd.DataFrame(sorted(solutions))
number_of_solutions = len(df.index.tolist())
for ix,xs in enumerate(df.columns.tolist()):
    if ix:
        lst = list(range(ix))
        for k,v in df.loc[:,lst].groupby(lst).size().to_dict().items():
            print(k,round(1.0*v/number_of_solutions,ndigits=5))
