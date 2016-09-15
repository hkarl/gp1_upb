import sys
from itertools import tee

numvl = int(sys.argv[1])

lines = sys.stdin.readlines()
numlines = len(lines)
slidespervl = int(numlines/numvl)+1

print(slidespervl)

for vl in range(numvl):
    print("=======================")
    print("VL: ", vl+1)
    print("".join(lines[vl*slidespervl:(vl+1)*slidespervl]))
    

