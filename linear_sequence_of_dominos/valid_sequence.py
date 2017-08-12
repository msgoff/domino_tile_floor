# http://www.domino-games.com/domino-rules/double-six.html
import itertools

'''
list_of_dominos = [ (0,0), (1,0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
                           (1,1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1),
                                  (2, 2), (3, 2), (4, 2), (5, 2), (6, 2),
                                          (3, 3), (4, 3), (5, 3), (6, 3),
                                                  (4, 4), (5, 4), (6, 4),
                                                          (5, 5), (6, 5),
                                                                  (6, 6)]
'''

list_of_dominos = [(0,0),(1,0),(2,0),(3,0),
                         (1,1),(2,1),(3,1),
                               (2,2),(3,2),
                                     (3,3)]


print(len(list_of_dominos))
# 28! = 3*10^29
#print(list_of_dominos)

broke_on={}
for indx in range(11):
    broke_on[indx+1]=0
print(broke_on)

for this_perm in itertools.permutations(list_of_dominos):
    if(this_perm[0][1] != this_perm[1][0]):
        #print("broke on first pair")
        broke_on[1] += 1
    elif(this_perm[1][1] != this_perm[2][0]):    
        #print("broke on second pair")
        broke_on[2] += 1
    elif(this_perm[2][1] != this_perm[3][0]):    
        broke_on[3] += 1
    elif(this_perm[3][1] != this_perm[4][0]):    
        broke_on[4] += 1
    elif(this_perm[4][1] != this_perm[5][0]):    
        broke_on[5] += 1
    elif(this_perm[5][1] != this_perm[6][0]):    
        broke_on[6] += 1
    elif(this_perm[6][1] != this_perm[7][0]):    
        broke_on[7] += 1
    elif(this_perm[7][1] != this_perm[8][0]):    
        broke_on[8] += 1
    elif(this_perm[8][1] != this_perm[9][0]):    
        broke_on[9] += 1
#    elif(this_perm[9][1] != this_perm[10][0]):    
#        broke_on[10] += 1
    else:
        print("made it to another pair")
        print(this_perm)
        break

print(broke_on)