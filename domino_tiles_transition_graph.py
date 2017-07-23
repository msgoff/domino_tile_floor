
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
    
def append_next_value(transition_dic,list_of_transitions):
    for this_list in list_of_transitions:
        if (len(this_list)<(number_of_tiles_to_fill)): # if this list isn't "done"
            last_value=this_list[len(this_list)-1]
            new_transition_list=[]
            for next_value in transition_dic[last_value]:
                if next_value not in this_list:
                    new_list=list(this_list) # https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list
                    new_list.append(next_value)
                    new_transition_list.append(new_list)
#                    print(new_list)
    list_of_transitions=new_transition_list
    return list_of_transitions

width=3
height=2
number_of_tiles_to_fill=width*height

transition_dic = create_transition_dic(width,height)

starting_value=5

list_of_transitions=[]

print("seed")
this_transition=[5]
list_of_transitions.append(this_transition)
print_list_of_transitions(list_of_transitions)

print("step 1")
list_of_transitions = append_next_value(transition_dic,list_of_transitions)
print_list_of_transitions(list_of_transitions)

print("step 2")
list_of_transitions = append_next_value(transition_dic,list_of_transitions)
print_list_of_transitions(list_of_transitions)

