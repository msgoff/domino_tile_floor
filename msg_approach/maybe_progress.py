from itertools import product
from sys import argv
from collections import deque

width = int(argv[1])
"""
The search space can be reduced by stopping when there is only one solution.
in the 3x3 case 

the solutions are 
(1, 2, 3, 6, 5, 4, 7, 8, 9) (['R', 'R', 'D', 'L', 'L', 'D', 'R', 'R'], ['X', 'Y', 'X', 'Y', 'Z', 'Y', 'X', 'Y', 'X'])
(1, 2, 3, 6, 9, 8, 5, 4, 7) (['R', 'R', 'D', 'D', 'L', 'U', 'L', 'D'], ['X', 'Y', 'X', 'Y', 'X', 'Y', 'Z', 'Y', 'X'])
(1, 2, 3, 6, 9, 8, 7, 4, 5) (['R', 'R', 'D', 'D', 'L', 'L', 'U', 'R'], ['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'Z'])
(1, 2, 5, 4, 7, 8, 9, 6, 3) (['R', 'D', 'L', 'D', 'R', 'R', 'U', 'U'], ['X', 'Y', 'Z', 'Y', 'X', 'Y', 'X', 'Y', 'X'])
(1, 4, 5, 2, 3, 6, 9, 8, 7) (['D', 'R', 'U', 'R', 'D', 'D', 'L', 'L'], ['X', 'Y', 'Z', 'Y', 'X', 'Y', 'X', 'Y', 'X'])
(1, 4, 7, 8, 5, 2, 3, 6, 9) (['D', 'D', 'R', 'U', 'U', 'R', 'D', 'D'], ['X', 'Y', 'X', 'Y', 'Z', 'Y', 'X', 'Y', 'X'])
(1, 4, 7, 8, 9, 6, 3, 2, 5) (['D', 'D', 'R', 'R', 'U', 'U', 'L', 'D'], ['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'Z'])
(1, 4, 7, 8, 9, 6, 5, 2, 3) (['D', 'D', 'R', 'R', 'U', 'L', 'U', 'R'], ['X', 'Y', 'X', 'Y', 'X', 'Y', 'Z', 'Y', 'X'])

initially we can start by only exploring the case where 1 -> 2
the case where 1->4 can be derived from all of the solutions from 1 -> 2... by substituing R -> D, L -> U
so the search space is reduced by 50%

only considering the 4 cases
(1, 2, 3, 6, 5, 4, 7, 8, 9) (['R', 'R', 'D', 'L', 'L', 'D', 'R', 'R'], ['X', 'Y', 'X', 'Y', 'Z', 'Y', 'X', 'Y', 'X'])
(1, 2, 3, 6, 9, 8, 5, 4, 7) (['R', 'R', 'D', 'D', 'L', 'U', 'L', 'D'], ['X', 'Y', 'X', 'Y', 'X', 'Y', 'Z', 'Y', 'X'])
(1, 2, 3, 6, 9, 8, 7, 4, 5) (['R', 'R', 'D', 'D', 'L', 'L', 'U', 'R'], ['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'Z'])
(1, 2, 5, 4, 7, 8, 9, 6, 3) (['R', 'D', 'L', 'D', 'R', 'R', 'U', 'U'], ['X', 'Y', 'Z', 'Y', 'X', 'Y', 'X', 'Y', 'X'])

can stop after 2 choices since there is only 1 possible solution remaining
RD .
(1, 2, 5) 0.125

... after 4
RRDL 
(1, 2, 3, 6, 5) 0.125

after 6
RRDDLU
(1, 2, 3, 6, 9, 8, 5) 0.125

after 6
RRDDLL
(1, 2, 3, 6, 9, 8, 7) 0.125

(1, 2) 0.5
(1, 2, 3) 0.375
(1, 2, 5) 0.125
(1, 2, 3, 6) 0.375
(1, 2, 5, 4) 0.125
(1, 2, 3, 6, 5) 0.125
(1, 2, 3, 6, 9) 0.25
(1, 2, 5, 4, 7) 0.125
(1, 2, 3, 6, 5, 4) 0.125
(1, 2, 3, 6, 9, 8) 0.25
(1, 2, 5, 4, 7, 8) 0.125
(1, 2, 3, 6, 5, 4, 7) 0.125
(1, 2, 3, 6, 9, 8, 5) 0.125
(1, 2, 3, 6, 9, 8, 7) 0.125
(1, 2, 5, 4, 7, 8, 9) 0.125
(1, 2, 3, 6, 5, 4, 7, 8) 0.125
(1, 2, 3, 6, 9, 8, 5, 4) 0.125
(1, 2, 3, 6, 9, 8, 7, 4) 0.125
(1, 2, 5, 4, 7, 8, 9, 6) 0.125
(1, 2, 3, 6, 5, 4, 7, 8, 9) 0.125
(1, 2, 3, 6, 9, 8, 5, 4, 7) 0.125
(1, 2, 3, 6, 9, 8, 7, 4, 5) 0.125
(1, 2, 5, 4, 7, 8, 9, 6, 3) 0.125

"""


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
    if len(tpl) == width**2:
        solutions.add(tpl)
    else:
        product_gen(list(tpl))

for tpl in sorted(solutions):
    if len(tpl) == width**2:
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
for ix, xs in enumerate(df.columns.tolist()):
    lst = list(range(ix + 1))
    for k, v in df.loc[:, lst].groupby(lst).size().to_dict().items():
        print(k, round(1.0 * v / number_of_solutions, ndigits=5))
