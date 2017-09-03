# coding: utf-8
from tqdm import tqdm 
from sys import argv
from itertools import product
from itertools import takewhile
from itertools import takewhile
from random import choice
from random import randint 

def write_ary_to_CSV(filename,ary,width):
    with open(filename, 'w') as file:
        for row in range(0,width*width,width):
            for col in range(width):
                file.write(str(this_ary[row+col]))
                if (col<width-1):
                    file.write(',')
            file.write('\n')


def create_transition_dic(width,height):
    transition_dic={}
    num_tiles=width*height
    for n in range(1,num_tiles+1):
        adjacent_edges_list=[]
        if ((n-1)%width != 0): 
            adjacent_edges_list.append(n-1) # left
        if (n%width     != 0): 
            adjacent_edges_list.append(n+1) # right
        if (n > width):
            adjacent_edges_list.append(n-width) # top
        if (n<=((width*height)-width)):
            adjacent_edges_list.append(n+width) # bottom
        transition_dic[n]=adjacent_edges_list
    return transition_dic

boolean_display_max_length=False
boolean_display_width_x_width=False

if (len(argv) != 3):
    print("ERROR: need (only) two arguments, width of squary array and number of solutions")
    exit()

width=int(argv[1])
dct=create_transition_dic(width,width)

lst=[]
for key in dct.keys():
    for tupl in list(product([key],dct[key])):
        lst.append(tupl)


src=choice(lst)


#move list of length of 3
moves_3=[]
moves_gte_3=[]
for tupl in tqdm(lst):
    src=tupl
    for mvs in list(product([src],[x for x in lst if src[1] == x[0] and src[0] != x[1]])):
            x=list(mvs[0])
            y=mvs[1][1]
            x.append(y)
            if x not in moves_3:
                moves_3.append(x)
                
is_growing=len(moves_3)
while is_growing:
    for tupl in tqdm(moves_3):
        src=tupl
        for mvs in list(product([src],[x for x in lst if src[1] == x[0] and src[0] != x[1]])):
                x=list(mvs[0])
                y=mvs[1][1]
                x.append(y)
                if x not in moves_3 and len(x) ==3:
                    moves_3.append(x)
    is_growing -= len(moves_3)
    print is_growing

moves_6=[]
#moves list of greater than 3
counter=0
#moves_gte_3=[]
for i in tqdm(moves_3):
    for j in moves_3:
        if i[-1] == j[0]:
            resp=list(takewhile(lambda x: x not in i,j[1:]))
            if resp:
                for value in resp:
                    i.append(value)
            if j not in moves_gte_3 and len(j) <=6:
                moves_gte_3.append(j)


moves_6=moves_gte_3+moves_3

solutions=[]
max_len=0
#iterate over the moves list of greater than 3
while len(solutions)<int(argv[2]): 
     #moves_gte_3=sorted(moves_gte_3,key=lambda x:len(x))[-1000:]
     #print "len m 3",len(moves_gte_3)
     for i in moves_gte_3:
        for j in moves_gte_3:
            if i[-1] == j[0]:
                resp=list(takewhile(lambda x: x not in i,j[1:]))
                if resp:
                    for value in resp:
                        i.append(value)
                if len(j) > max_len:
                        max_len = len(i)
                        if boolean_display_max_length: print "max len",max_len
                
                if len(j)== width*width:
                    solutions.append(j)
#                    print("length = width*width")
                    if boolean_display_width_x_width: print j


print len(solutions)

for this_ary in solutions:
    print(this_ary)
    
print("and now as squares")
for this_ary in solutions:
    write_ary_to_CSV('filename.csv',this_ary,width)
    for row in range(0,width*width,width):
        print(this_ary[row:row+width])
    print(" ")
