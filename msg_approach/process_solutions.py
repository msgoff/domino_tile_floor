# z3 output.cnf  > z3_solutions
import pickle
import re

with open("transitions.pickle", "rb") as f:
    dct = pickle.load(f)
    dct = {v: k for k, v in dct.items()}
with open("z3_solutions", "r") as f:
    data = f.readlines()

solution = [int(x.strip()) for x in data[-1].split(" ") if not re.findall("v|\-", x)]
solution = solution[:-1]
print(solution)
for key in solution:
    print(str(dct.get(key)).replace(",", " ->").replace("(", "").replace(")", ""))
