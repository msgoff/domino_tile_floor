from itertools import product
from sys import argv

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


dct = create_transition_dic(width,width)
#keep = set()
#seen = set()

src = [1]
#https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque


d = deque()
def product_gen(src):
    #if tuple(src) in seen:
    #    return 
    #seen.add(tuple(src))
    l = src[:-1]
    for ix in product([src[-1]],dct[src[-1]]):
        try:
            l.extend(list(ix))
            if len(set(l)) == len(l):
                d.append(tuple(l))
            l = src[:-1]
        except Exception as e:
            print(e)
            pass

solutions = set()
product_gen(src)
neighbors = {2:'X',3:'Y',4:'Z'}
while d:
    tpl = d.popleft()
    if len(tpl) == width**2:
        solutions.add(tpl)
    else:
        product_gen(list(tpl))

moves = {}
square_type = []
for tpl in sorted(solutions):
    if len(tpl) == width**2:
        tmp_lst = []
    
        for ix in list(zip(tpl,tpl[1:])):
            if ix[1] - 1 == ix[0]:
                tmp_lst.append('R')

            if ix[1] + 1 == ix[0]:
                tmp_lst.append('L')

            if ix[1] - width == ix[0]:
                tmp_lst.append('D')

            if ix[1] + width == ix[0]:
                tmp_lst.append('U')
    
        moves[tpl] = (tmp_lst,[neighbors[len(dct[x])] for x in tpl])

counter = 0
for k,v in moves.items():
    #if counter < 5 :
    counter += 1
    print(k,v)
