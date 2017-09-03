import csv

def read_csv_into_ary(filename):
    ary=[]
    with open(filename, 'r') as csvfile:
        input_data = csv.reader(csvfile)
        for row_of_strings in input_data:
            this_row=[]
            for this_str in row_of_strings:
                this_row.append(int(this_str))
            ary.append(this_row)
    return ary

def display_ary(ary,width):
    for row in ary:
        print(row)

def coord_of_indx(ary,indx):
    row_indx=0
    for this_row in ary:
        row_indx+=1
        col_indx=0
        for this_col in this_row:
            col_indx+=1
            if (this_col==indx):
                return row_indx,col_indx

input_file='filename.csv'

input_ary=read_csv_into_ary(input_file)

width = len(input_ary[0])

display_ary(input_ary,width)

#             row-1,col
# row,col-1   row,  col   row,col+1
#             row+1,col

dic_of_next_indx={}
dic_of_next_indx['next is on left']=0
dic_of_next_indx['next is on right']=0
dic_of_next_indx['next is up']=0
dic_of_next_indx['next is down']=0

for indx in range(1,width*width):
    row_this_indx, col_this_indx = coord_of_indx(input_ary,indx)
    #print(str(indx)+': '+str(row)+' '+str(col))
    row_next_indx, col_next_indx = coord_of_indx(input_ary,indx+1)
    
    if (col_this_indx == col_next_indx):
        if (row_this_indx == row_next_indx-1):
            dic_of_next_indx['next is down']+=1
        elif  (row_this_indx == row_next_indx+1):
            dic_of_next_indx['next is up']+=1
        else:
            print("ERROR: this=next for row, indx= "+str(indx))
    if (col_this_indx == col_next_indx-1):
        dic_of_next_indx['next is on left']+=1
    elif (col_this_indx == col_next_indx+1):
        dic_of_next_indx['next is on right']+=1
#    else:
#        print("ERROR: indx= "+str(indx))

print("\ncounts: ")
print("up: "+    str(dic_of_next_indx['next is up'])+
      ", down: "+str(dic_of_next_indx['next is down'])+
      ", left: "+str(dic_of_next_indx['next is on left'])+
      ", right: "+str(dic_of_next_indx['next is on right']))
      
total = (dic_of_next_indx['next is up']+ dic_of_next_indx['next is down']+
        dic_of_next_indx['next is on left']+dic_of_next_indx['next is on right'])

print("total = "+str(total))

print("\n as a percentage: ")
print("up: "+    str(dic_of_next_indx['next is up']*1.0/total)+
      ", down: "+str(dic_of_next_indx['next is down']*1.0/total)+
      ", left: "+str(dic_of_next_indx['next is on left']*1.0/total)+
      ", right: "+str(dic_of_next_indx['next is on right']*1.0/total))

print("\n distance from uniform: ")
print("up: "+    str(0.25-(dic_of_next_indx['next is up']*1.0/total))+
      ", down: "+str(0.25-(dic_of_next_indx['next is down']*1.0/total))+
      ", left: "+str(0.25-(dic_of_next_indx['next is on left']*1.0/total))+
      ", right: "+str(0.25-(dic_of_next_indx['next is on right']*1.0/total)))
