import sys
import pandas as pd 
import numpy as np
from itertools import product

def create_transition_dic(width,height):
    transition_dic={}
    num_tiles=width*height
#    print("width= "+str(width))
#    print("height= "+str(height))
    for n in range(1,num_tiles+1):
#        print("\nn = "+str(n))
        adjacent_edges_list=[]
#        print("if (n-1)%width !=0, then left exists; value is "+str((n-1)%width))
        if ((n-1)%width != 0): 
#            print("left = "+str(n-1))
            adjacent_edges_list.append(n-1) # left
#        print("if n%width !=0, then right exists; value is "+str(n%width))    
        if (n%width     != 0): 
#            print("right = "+str(n+1))
            adjacent_edges_list.append(n+1) # right
#        print("if n > width, then top exists")
        if (n > width):
#            print("top = "+str(n-width))
            adjacent_edges_list.append(n-width) # top
#        print("if n<=((width*height)-width), then bottom exists; value is "+str(    ((width*height)-width)))
        if (n<=((width*height)-width)):
#            print("bottom = "+str(n+width))
            adjacent_edges_list.append(n+width) # bottom
        transition_dic[n]=adjacent_edges_list
    return transition_dic

#for arg in sys.argv:
#    print arg

if len(sys.argv) != 4: 
    print("  WARNING: incorrect number of arguments passed")
    print("  defaulting to 3x3 and egrep")
    width=3
    height=3
    search="egrep"
    print("  use: grep_filters.py <width> <height> <search command>\n")
else:
    width=int(sys.argv[1])
    height=int(sys.argv[2])
    search=sys.argv[3]
    
dct=create_transition_dic(width,height)

Filter=[]
for ix in dct.keys():
    query=search+" "+'"{} ({})'.format(ix,'|'.join([str(x) for x in dct[ix]]))+'"'
    Filter.append(query)

print '|'.join(Filter)

