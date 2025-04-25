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

from time import sleep
from itertools import product
from itertools import combinations
import pandas as pd
from collections import defaultdict
from pudb import set_trace

id_transition = {}
transition_dict_inverse = {}
output = []
seen = set()
width = 4
square_to_pairs = defaultdict(list)
rules = []


def create_transition_dict(width, height):
    counter = 1
    transition_dict = {}
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
        transition_dict[n] = adjacent_edges_list
        for ix, tpl in enumerate(list(product([n], adjacent_edges_list))):
            square_to_pairs[n].append(tpl)
            id_transition[counter] = tpl
            transition_dict_inverse[tpl] = counter
            counter += 1
    return transition_dict


transition_dict = create_transition_dict(width, width)
rows = []
rule_count = 0
for k, v in square_to_pairs.items():
    # print(k,v)
    lst = list(product([k], v))
    for l in lst:
        l_temp = list(l)
        l_temp.append(f"r{rule_count}")
        l_temp.append(transition_dict_inverse.get(l[1]))
        rows.append(l_temp)
        rule_count += 1
df = pd.DataFrame(rows)
df.columns = ["square", "transition", "rule", "rule_id"]
df["q0"] = df.transition.apply(lambda x: x[0])
df["q1"] = df.transition.apply(lambda x: x[1])
zf0 = df.groupby("q0").apply(lambda x: x["rule_id"])
zf1 = df.groupby("q1").apply(lambda x: x["rule_id"])
output = []
for ix in range(1, width * width + 1):
    lst = zf0[ix].tolist()
    output.append(lst)
    lst1 = zf1[ix].tolist()
    output.append(lst1)
    # neg
    for l in list(combinations(lst, 2)):
        output.append([-1 * x for x in l])
    for l in list(combinations(lst1, 2)):
        output.append([-1 * x for x in l])

for tpl in df["transition"].tolist():
    lst = df[
        (df["transition"] == tpl) | (df["transition"] == (tpl[1], tpl[0]))
    ].rule_id.tolist()
    output.append([-1 * x for x in lst])


print(df)
rules = []
for rule in output:
    rules.append(str(rule).replace("[", "").replace("]", "").replace(",", "") + " 0")
# print(transition_dic_inverse)
variable_count = len(transition_dict_inverse.keys())
clause_count = len(rules)
f = open("output.cnf", "w")
f.write(f"p cnf {variable_count} {clause_count}")
f.write("\n")
for line in rules:
    line = str(line).replace("(", "").replace(")", "").replace(",", "")
    f.write(line)
    f.write("\n")
f.close()

import pickle

with open("transitions.pickle", "wb") as f:
    pickle.dump(transition_dict_inverse, f)
