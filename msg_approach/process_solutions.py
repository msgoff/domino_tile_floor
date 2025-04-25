# z3 output.cnf  > z3_solutions
import pickle
import re
import subprocess

solution_seen = set()
z3_path = "/mnt/x/z3/build/z3"
with open("transitions.pickle", "rb") as f:
    dct = pickle.load(f)
    dct = {v: k for k, v in dct.items()}


def run_z3():
    cmd = [z3_path, "output.cnf"]
    stdout = subprocess.check_output(cmd)
    data = stdout.decode("utf-8").splitlines()
    print(data)
    inp = input()
    data = [x for x in data if re.findall("v", x)]
    solution = [int(x.strip()) for x in data[-1].split(" ") if not re.findall("v", x)]
    # print(solution)
    solution_inverse = [
        -1 * int(x.strip()) for x in data[-1].split(" ") if not re.findall("v", x)
    ]
    solution_remove_not = [
        int(x.strip()) for x in data[-1].split(" ") if not re.findall("v|\-", x)
    ]
    solution_remove_not = solution_remove_not[:-1]
    for key in solution_remove_not:
        print(str(dct.get(key)).replace(",", " ->").replace("(", "").replace(")", ""))

    solution_inverse_cleaned = (
        str(solution_inverse).replace(",", "").replace("[", "").replace("]", "")
    )
    return solution_inverse_cleaned


def update_cnf(solution_inverse_cleaned):
    with open("output.cnf", "r") as f:
        clauses = f.readlines()
        clauses = [x.strip() for x in clauses]
        header = [x.strip() for x in clauses[0].split(" ") if x.strip()]
        header = str(header[:-1] + [str(int(header[-1]) + 1)])
        header = header.replace(",", "").replace("[", "").replace("]", "")
        header = header.replace("'", "")
        print(clauses, header)

    with open("output.cnf", "w") as f:
        f.write(header)
        f.write("\n")
        for line in clauses[1:]:
            f.write(line)
            f.write("\n")
        f.write(solution_inverse_cleaned)
        f.write("\n")


solution_inverse_cleaned = run_z3()
update_cnf(solution_inverse_cleaned)
seen = set()
while 1 == 1:
    try:
        solution_inverse_cleaned = run_z3()
        update_cnf(solution_inverse_cleaned)
    except Exception as e:
        print(e)
        exit()
