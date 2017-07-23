
def create_transition_dic(width,height):
    transition_dic={}
    transition_dic[1]=[2,4]
    transition_dic[2]=[1,5,3]
    transition_dic[3]=[2,6]
    transition_dic[4]=[1,5]
    transition_dic[5]=[4,2,6]
    transition_dic[6]=[3,5]
    return transition_dic


def print_list_of_transitions(list_of_transitions):
    for this_list in list_of_transitions:
        print(this_list)
    return

    for next_val in transition_dic[5]:
        new_list=[]
        new_list.append(starting_value)
        new_list.append(next_val)
        list_of_transitions.append(new_list)
    return list_of_transitions
    
def append_next_value(transition_dic,list_of_transitions,number_of_tiles_to_fill,print_status):
    new_transition_list=[]
    for this_list in list_of_transitions:
        if print_status: print("\nthis list = ")
        if print_status: print(this_list)
        if (len(this_list)<(number_of_tiles_to_fill)): # if this list isn't "done"
            last_value=this_list[len(this_list)-1]
            if print_status: print("last value = " + str(last_value))
            for next_value in transition_dic[last_value]:
                if print_status: print("next value = "+str(next_value))
                if next_value not in this_list:
                    if print_status: print("adding next value to list")
                    new_list=list(this_list) # https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list
                    new_list.append(next_value)
                    if print_status: print(new_list)
                    new_transition_list.append(new_list)
    list_of_transitions=new_transition_list
    return list_of_transitions

width=3
height=2
number_of_tiles_to_fill=width*height

transition_dic = create_transition_dic(width,height)

starting_value=5

list_of_transitions=[]

print_status=False

if print_status: print("\nseed")
this_transition=[5]
list_of_transitions.append(this_transition)
if print_status: 
    print("list of transitions:")
    print_list_of_transitions(list_of_transitions)

for loop_indx in range(number_of_tiles_to_fill-1):
    print("\nstep "+str(loop_indx))
    list_of_transitions = append_next_value(transition_dic,list_of_transitions,number_of_tiles_to_fill,print_status)
    print("list of transitions:")
    print_list_of_transitions(list_of_transitions)

