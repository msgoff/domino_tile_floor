# z3 output.cnf provides solutions
# ignore the -int in the soluiton
# the transitions can be found in the transition_dic_inverse.
# for example 1:(1,2) means move from square labeled 1 to the squared labeled 2 and 1 is the integer in the solution.
# a sample solution for the 2x2 square
# {(1, 2): 1, (1, 3): 2, (2, 1): 3, (2, 4): 4, (3, 4): 5, (3, 1): 6, (4, 3): 7, (4, 2): 8}
# s SATISFIABLE
# v -1 2 3 -4 5 -6 -7 8 0
# (1,3), (2,1), (3,4), (4,2)
#  1->3          3->4   4->2    2->1

# The 200 x 200 case runs in less than 1 second
# to get additional solutions you can invert the output from z3 add it to the cnf and re-run z3 on the cnf file
# to get all solutions, repeat until UNSAT


from itertools import product

id_transition = {}
transition_dic_inverse = {}
output = []
seen = set()
width = 2


def create_transition_dic(width, height):
    counter = 1
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
        for ix, tpl in enumerate(list(product([n], adjacent_edges_list))):
            id_transition[counter] = tpl
            transition_dic_inverse[tpl] = counter
            counter += 1
    return transition_dic


dct = create_transition_dic(width, width)
for k, v in dct.items():
    lst = list(product([k], v))
    resp = [transition_dic_inverse.get(tpl) for tpl in lst]
    resp.append(0)
    output.append(tuple(resp))
    output.append(tuple([-1 * x for x in resp]))
    for item in lst:
        q1 = transition_dic_inverse.get(item)
        q2 = transition_dic_inverse.get(tuple([item[1], item[0]]))
        if (q1, q2) not in seen:
            seen.add((q1, q2))
            seen.add((q2, q1))
            output.append((-1 * q1, -1 * q2, 0))

print(transition_dic_inverse)
variable_count = len(transition_dic_inverse.keys())
clause_count = len(output)
f = open("output.cnf", "w")
f.write(f"p cnf {variable_count} {clause_count}")
f.write("\n")
for line in output:
    line = str(line).replace("(", "").replace(")", "").replace(",", "")
    f.write(line)
    f.write("\n")
f.close()
