import pandas as pd
import numpy as np
from random import choice
from itertools import product
from tqdm import tqdm
from redis import Redis
from sys import argv
r=Redis()

bndry=int(argv[1])
seen=set()
move_history=[]
df=pd.DataFrame(np.array(range(bndry**2)).reshape(bndry,bndry))




def possible_moves(ix,iy):
            test_lst=[(ix-1,iy),(ix+1,iy),(ix,iy+1),(ix,iy-1)]
            #filter invalid values
            resp=[(ix,iy) for (ix,iy) in test_lst                   if ix>=0 and ix < bndry and  iy >= 0 and iy < bndry and (ix,iy) not in seen]
            return resp
        
        



#initial dict setup
def dct_setup():
    seen=set()
    move_history=[]
    lst=df.columns.tolist()
    #print lst
    dct={}
    seen=set()
    points=list(product(lst,lst))
   

    for tupl in points:
        dct[tupl]=possible_moves(tupl[0],tupl[1])
        
    return dct
            
            

dct=dct_setup()




solutions=[]
failed=[]

f=Redis(db=1)


for ix in tqdm(range(int(argv[2]))):
    pieces=[]
    for k,v in dct.items():
        for g in product([k],v):
            pieces.append(g)

    node_list=[]
    def query(tupl):
        global pieces
        node_list.append(tupl)
        #print node_list
        resp=[x for x in pieces if x[0]==tupl]
        pieces=[x for x in pieces if x[0] not in node_list and x[1] not in node_list]
        return resp

    resp=query((0,0))
    while True:
        try:
            resp=query(choice([x[1] for x in resp]))
        except:
            if len(node_list)==bndry**2:
                #print "solution",node_list

                r.set(ix,node_list)
                print r.keys()
		break
            else:
                #print "failed"
                f.set(ix,node_list)
                break


    seen=set()
    move_history=[]
    df=pd.DataFrame(np.array(range(bndry**2)).reshape(bndry,bndry))






"""
print len(solutions)




print len(failed)




df=pd.DataFrame(solutions)




print len(df.drop_duplicates())




df.drop_duplicates().to_csv('solutions.csv')



zf=pd.DataFrame(failed)




print len(zf)




print len(zf.drop_duplicates())




print zf.drop_duplicates().fillna('')



zf.drop_duplicates().fillna('').to_csv('failed.csv')


"""



